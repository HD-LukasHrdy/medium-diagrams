
DIAGRAM_NAME = "molecule-upload-flow"

MOLLIB_UPLOAD_DOCUMENTATION = """ 
Molecule upload api takes care of : 
1. Check
2. Validate
"""

MOLLIB_UPLOAD_OPEN_SEARCH_SUCCESS = "Molecules for molecule library id: {request.mol_lib_id} sucesffuly uploaded."
MOLLIB_UPLOAD_OPEN_SEARCH_FAILURE = "Error occurred during molecule upload for molecule library id: {request.mol_lib_id}."


CALCULATE_RDKIT_DOCUMENTATION = """ 
Calculate rdkit properties and store them to DB.
"""

CALCULATE_RDKIT_OPEN_SEARCH_SUCCESS = "RDKit properties for a batch of molecule library id: {request.mol_lib_id} sucesffuly calculated."
CALCULATE_RDKIT_OPEN_SEARCH_FAILURE = "RDKit properties for a batch of molecule library id: {request.mol_lib_id} failed."

CALCULATE_ML_DOCUMENTATION = """ 
Calculate ML properties and store them to DB.
"""

CALCULATE_MPO_DOCUMENTATION = """ 
Calculate both system and company mpo properties and store them to DB. MPO properties are calculated as an standardization of other RDKit or ML properties standardized values which are calculated in their specific calculation functions.
"""

CALCULATE_MPO_OPEN_SEARCH_SUCCESS = "MPO properties for a batch of molecule library id: {request.mol_lib_id} sucesffuly calculated."
CALCULATE_MPO_OPEN_SEARCH_FAILURE = "MPO properties for a batch of molecule library id: {request.mol_lib_id} failed."

CLUSTERING_PREPARE_INPUT_DOCUMENTATION = """ 
Prepare clustering input.
"""

CLUSTERING_PREPARE_INPUT_OPEN_SEARCH_SUCCESS = "Clustering input preparation for molecule library id: {request.mol_lib_id} sucesful."
CLUSTERING_PREPARE_INPUT_OPEN_SEARCH_FAILURE = "Clustering input preparation for molecule library id: {request.mol_lib_id} failed."

CLUSTERING_AGENTS_DOCUMENTATION = """ 
Actual clustering
"""

CLUSTERING_AGENTS_OPEN_SEARCH_SUCCESS = "Clustering for molecule library id: {request.mol_lib_id} sucesful."
CLUSTERING_AGENTS_OPEN_SEARCH_FAILURE = "Clustering for molecule library id: {request.mol_lib_id} failed."

CLUSTERING_STORE_RESULTS_DOCUMENTATION = """ 
Store clustering results.
"""

CLUSTERING_STORE_RESULTS_OPEN_SEARCH_SUCCESS = "Store clustering results for molecule library id: {request.mol_lib_id} sucesful."
CLUSTERING_STORE_RESULTS_OPEN_SEARCH_FAILURE = "Store clustering results for molecule library id: {request.mol_lib_id} failed."

ADD_FINGERPRINTS_DOCUMENTATION = """During the molecule upload only molecule structure is stored. After all molecules 
and properties are successfully stored, we add fingerprints to all molecules in the library in order to enable to 
neighbour search."""

ADD_FINGERPRINTS_OPEN_SEARCH_SUCCESS = "Add fingerprints for molecules in molecule library id: {request.mol_lib_id} sucesffuly executed."
ADD_FINGERPRINTS_OPEN_SEARCH_FAILURE = "Add fingerprints for molecules in molecule library id: {request.mol_lib_id} failed."