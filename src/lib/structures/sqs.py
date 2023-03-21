from diagrams.aws.integration import SQS
from mdutils import MdUtils

from lib.documentation.md import add_sqs_job_section


def create_sqs_job(module: str, queue_name: str, job_function_name: str, container_name: str, md_file: MdUtils,
                   open_search_section: bool,
                   documentation: str = "",
                   open_search_success="Success",
                   open_search_failure="Failed") -> SQS:
    module_queue = SQS(queue_name)

    add_sqs_job_section(module, md_file, queue_name, container_name
                        , job_function_name, documentation, open_search_section, open_search_success, open_search_failure)

    return module_queue
