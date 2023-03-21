from diagrams.aws.compute import Lambda
from mdutils import MdUtils

from lib.documentation.md import add_lambda_section


def create_lambda(module: str, lambda_name: str, md_file: MdUtils, open_search_section: bool, documentation: str = "",
                  open_search_success="Success",
                  open_search_failure="Failed") -> Lambda:
    aws_lambda = Lambda(lambda_name)

    add_lambda_section(md_file, module, lambda_name, documentation, open_search_section, open_search_success,
                       open_search_failure)

    return aws_lambda
