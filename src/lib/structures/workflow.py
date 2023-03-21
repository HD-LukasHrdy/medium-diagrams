from diagrams import Diagram, Node, Cluster
from diagrams.aws.network import Route53, CloudMap
from diagrams.aws.compute import Lambda
from diagrams.aws.network import APIGateway
from diagrams.aws.integration import SQS
from diagrams.aws.management import SSM
from diagrams.aws.integration import SF
from mdutils import MdUtils


def api_service_discovery_integration(next_node: Node, mdfile: MdUtils):
    python_gateway = APIGateway("Proxy route: /py/* ")

    with Cluster("Service Discovery Module"):
        private_route = Route53("Private DNS")

        cloud_map = CloudMap("CloudMap Namespace")

        sd_lambda = Lambda("service-adapter")

        sd_lambda >> private_route
        private_route << sd_lambda
        private_route >> cloud_map
        private_route << cloud_map

        sd_lambda >> next_node
        python_gateway >> sd_lambda

        mdfile.new_header(level=2, title=sd_lambda.label)


def step_function_workflow_handle(initiating_node: Node, workflow_node: SF):
    with Cluster("Workflow handle"):
        workflow_queue = SQS("workflow-queue")
        workflow_handle_lambda = Lambda("workflow-handle")
        app_config = SSM("AppConfig")

    initiating_node >> workflow_queue
    workflow_queue >> workflow_handle_lambda
    workflow_handle_lambda >> app_config
    workflow_handle_lambda << app_config
    workflow_handle_lambda >> workflow_node
