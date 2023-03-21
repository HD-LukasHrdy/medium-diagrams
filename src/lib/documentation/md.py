from mdutils import MdUtils


def prepare_module_md_file(module_name: str):
    md_file = MdUtils(file_name=module_name, title=f"Documentation for {module_name}.")
    return md_file


def store_md_file(md_file: MdUtils):
    md_file.new_table_of_contents(table_title='Contents', depth=2)
    md_file.create_md_file()


def add_rest_api_section(mdfile: MdUtils, module: str, path: str, documentation: str, open_search=False,
                         open_search_success="Success",
                         open_search_failure="Failed"):
    mdfile.new_header(level=1, title=f"Documentation for api {path}")
    mdfile.new_line(text=f"Code location: AIDD-PVC-{module}")
    mdfile.new_line(
        text=f"Contract: https://dfwstp01.sial.com/projects/AID/repos/aidd-pvc-api/browse/src/api/{str(path.split('/')[1]).lower()}")
    mdfile.new_header(level=2, title=f"Functional description")
    mdfile.new_line(text=documentation)
    if open_search:
        _add_open_search_section(mdfile, open_search_success, open_search_failure)


def add_lambda_section(mdfile: MdUtils, module: str, name: str, documentation: str, open_search=False,
                       open_search_success="Success",
                       open_search_failure="Failed"):
    mdfile.new_header(level=1, title=f"Documentation for aidd-pvc-{name} lambda.")
    mdfile.new_line(text=f"Code location: AIDD-PVC-{module}")
    mdfile.new_header(level=2, title=f"Functional description")
    mdfile.new_line(text=documentation)
    if open_search:
        _add_open_search_section(mdfile, open_search_success, open_search_failure)


def add_sqs_job_section(module: str, mdfile: MdUtils, queue_name: str, container_name: str, job_function_name: str,
                        documentation: str, open_search=False,
                        open_search_success="Success",
                        open_search_failure="Failed"):
    mdfile.new_header(level=1, title=f"Documentation for sqs job {job_function_name}.")
    mdfile.new_line(text=f"Code location: AIDD-PVC-{module}")
    mdfile.new_header(level=2, title=f"Functional description")
    mdfile.new_line(
        text=f"This is a job that is behind sqs queue: aidd-pvc-{queue_name} which is consumed by a python function called: {job_function_name} on container {container_name}.")
    mdfile.new_line(text=documentation)
    if open_search:
        _add_open_search_section(mdfile, open_search_success, open_search_failure)


def _add_open_search_section(mdfile: MdUtils, open_search_success, open_search_failure):
    mdfile.new_header(level=2, title="Open search description")
    mdfile.new_line(text=f"FAILED EXECUTIONS NEEDS TO PROVIDE FULL STACK TRACE TO THE ERROR MESSAGE AS WELL.")
    mdfile.new_list(
        [f"Message on success: **{open_search_success}**", f"Message on failure: **{open_search_failure}**"])
