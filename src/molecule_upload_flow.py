from diagrams import Cluster, Diagram
from diagrams.aws.integration import SF
from diagrams.programming.flowchart import Merge

from lib.documentation.md import prepare_module_md_file, store_md_file
from lib.structures.api import create_python_rest_api, create_ds_rest_api
from lib.structures.aws_lambda import create_lambda
from lib.structures.sqs import create_sqs_job
from lib.structures.workflow import api_service_discovery_integration, step_function_workflow_handle
from molecule.doc import MOLLIB_UPLOAD_DOCUMENTATION, DIAGRAM_NAME, CALCULATE_RDKIT_DOCUMENTATION, \
    CALCULATE_ML_DOCUMENTATION, MOLLIB_UPLOAD_OPEN_SEARCH_SUCCESS, MOLLIB_UPLOAD_OPEN_SEARCH_FAILURE, \
    CALCULATE_RDKIT_OPEN_SEARCH_SUCCESS, CALCULATE_RDKIT_OPEN_SEARCH_FAILURE, CALCULATE_MPO_DOCUMENTATION, \
    CALCULATE_MPO_OPEN_SEARCH_SUCCESS, CALCULATE_MPO_OPEN_SEARCH_FAILURE, CLUSTERING_PREPARE_INPUT_DOCUMENTATION, \
    CLUSTERING_PREPARE_INPUT_OPEN_SEARCH_SUCCESS, CLUSTERING_PREPARE_INPUT_OPEN_SEARCH_FAILURE, \
    CLUSTERING_AGENTS_DOCUMENTATION, CLUSTERING_AGENTS_OPEN_SEARCH_FAILURE, CLUSTERING_AGENTS_OPEN_SEARCH_SUCCESS, \
    CLUSTERING_STORE_RESULTS_DOCUMENTATION, CLUSTERING_STORE_RESULTS_OPEN_SEARCH_SUCCESS, \
    CLUSTERING_STORE_RESULTS_OPEN_SEARCH_FAILURE, ADD_FINGERPRINTS_DOCUMENTATION, ADD_FINGERPRINTS_OPEN_SEARCH_SUCCESS, \
    ADD_FINGERPRINTS_OPEN_SEARCH_FAILURE

with Diagram(DIAGRAM_NAME, show=False):
    md_file = prepare_module_md_file(DIAGRAM_NAME)

    mollib_upload_api = create_python_rest_api("Python-Molecule", "/molLib/upload", md_file, MOLLIB_UPLOAD_DOCUMENTATION,
                                               MOLLIB_UPLOAD_OPEN_SEARCH_SUCCESS
                                               , MOLLIB_UPLOAD_OPEN_SEARCH_FAILURE
                                               )
    api_service_discovery_integration(mollib_upload_api, md_file)

    with Cluster("Step Function Workflow") as workflow:
        molecule_calculate_step_function = SF("molecule-calculate")
        prepare_batches = create_lambda("Python-Molecule", "prepare-batches", md_file, True, "")

        with Cluster("Calculate RDKit props"):
            calculate_rdkit_api = create_python_rest_api("Python-Molecule", "/molLib/calculaterdkit", md_file,
                                                         CALCULATE_RDKIT_DOCUMENTATION,
                                                         CALCULATE_RDKIT_OPEN_SEARCH_SUCCESS
                                                         , CALCULATE_RDKIT_OPEN_SEARCH_FAILURE)
            calculate_rdkit_sqs = create_sqs_job("Python-Molecule", "molecule",
                                                 "calculate_rdkit_properties",
                                                 "molecule-sqs",
                                                 md_file,
                                                 True,
                                                 CALCULATE_RDKIT_DOCUMENTATION,
                                                 CALCULATE_RDKIT_OPEN_SEARCH_SUCCESS,
                                                 CALCULATE_RDKIT_OPEN_SEARCH_FAILURE)

        with Cluster("Calculate ML properties"):
            calculate_ml_api = create_ds_rest_api("DataScience-ModelInference", "/modelinference/batchpredict", md_file,
                                                  CALCULATE_ML_DOCUMENTATION)
            calculate_ml_sqs = create_sqs_job("DataScience-ModelInference", "batchPrediction", "calculate_and_store_ml_properties", "batchPrediction",
                                              md_file, True, CALCULATE_ML_DOCUMENTATION)

        merge = Merge("end")

        calculate_mpo = create_lambda("Python-Molecule", "calculate-mpo", md_file, True, CALCULATE_MPO_DOCUMENTATION,
                                      CALCULATE_MPO_OPEN_SEARCH_SUCCESS
                                      , CALCULATE_MPO_OPEN_SEARCH_FAILURE)

        with Cluster("Clustering"):
            clustering_step_function = SF("clustering")
            clustering_prepare_input = create_lambda("Python-Infrastructure", "clustering-prepare-input", md_file, True,
                                                     CLUSTERING_PREPARE_INPUT_DOCUMENTATION,
                                                     CLUSTERING_PREPARE_INPUT_OPEN_SEARCH_SUCCESS
                                                     , CLUSTERING_PREPARE_INPUT_OPEN_SEARCH_FAILURE)
            clustering_sqs = create_sqs_job("DataScience-Clustering", "clustering", "clustering_agents", "clustering",
                                            md_file, True, CLUSTERING_AGENTS_DOCUMENTATION,
                                            CLUSTERING_AGENTS_OPEN_SEARCH_SUCCESS
                                            , CLUSTERING_AGENTS_OPEN_SEARCH_FAILURE)
            clustering_store_results = create_lambda("Python-Infrastructure", "clustering-store-results", md_file, True,
                                                     CLUSTERING_STORE_RESULTS_DOCUMENTATION,
                                                     CLUSTERING_STORE_RESULTS_OPEN_SEARCH_SUCCESS
                                                     , CLUSTERING_STORE_RESULTS_OPEN_SEARCH_FAILURE)

            clustering_step_function >> clustering_prepare_input
            clustering_prepare_input >> clustering_sqs
            clustering_sqs >> clustering_store_results

        add_finger_prints_sqs = create_sqs_job("Python-Molecule", "molecule",
                                               "add_finger_prints_to_mollib",
                                               "molecule-sqs",
                                               md_file,
                                               True,
                                               ADD_FINGERPRINTS_DOCUMENTATION,
                                               ADD_FINGERPRINTS_OPEN_SEARCH_SUCCESS,
                                               ADD_FINGERPRINTS_OPEN_SEARCH_FAILURE)

    step_function_workflow_handle(mollib_upload_api, molecule_calculate_step_function)

    molecule_calculate_step_function >> prepare_batches
    prepare_batches >> calculate_rdkit_api
    prepare_batches >> calculate_ml_api
    calculate_rdkit_api >> merge
    calculate_ml_api >> merge
    merge >> calculate_mpo
    calculate_mpo >> clustering_step_function
    clustering_store_results >> add_finger_prints_sqs

    store_md_file(md_file)
