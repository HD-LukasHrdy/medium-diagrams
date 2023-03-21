from diagrams.programming.framework import Fastapi
from mdutils import MdUtils
from lib.documentation.md import add_rest_api_section


def create_python_rest_api(module: str, path, md_file: MdUtils, documentation: str = "", open_search_success="Success",
                           open_search_failure="Failed"):
    api = _create_rest_api("py", module, path, md_file, documentation, open_search_success,
                           open_search_failure)

    return api


def create_ds_rest_api(module: str, path, md_file: MdUtils, documentation: str = "", open_search_success="Success",
                       open_search_failure="Failed"):
    api = _create_rest_api("ds", module, path, md_file, documentation, open_search_success,
                           open_search_failure)

    return api


def _create_rest_api(prefix, module: str, path, md_file: MdUtils, documentation: str = "",
                     open_search_success="Success",
                     open_search_failure="Failed"):
    full_path = prefix + path
    api = Fastapi(prefix + path)
    add_rest_api_section(md_file, module, full_path, documentation, True, open_search_success, open_search_failure)

    return api
