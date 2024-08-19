from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_capacity_provider_request import CreateCapacityProviderRequest
from openapi_server.models.create_capacity_provider_response import CreateCapacityProviderResponse
from openapi_server.models.create_cluster_request import CreateClusterRequest
from openapi_server.models.create_cluster_response import CreateClusterResponse
from openapi_server.models.create_service_request import CreateServiceRequest
from openapi_server.models.create_service_response import CreateServiceResponse
from openapi_server.models.create_task_set_request import CreateTaskSetRequest
from openapi_server.models.create_task_set_response import CreateTaskSetResponse
from openapi_server.models.delete_account_setting_request import DeleteAccountSettingRequest
from openapi_server.models.delete_account_setting_response import DeleteAccountSettingResponse
from openapi_server.models.delete_attributes_request import DeleteAttributesRequest
from openapi_server.models.delete_attributes_response import DeleteAttributesResponse
from openapi_server.models.delete_capacity_provider_request import DeleteCapacityProviderRequest
from openapi_server.models.delete_capacity_provider_response import DeleteCapacityProviderResponse
from openapi_server.models.delete_cluster_request import DeleteClusterRequest
from openapi_server.models.delete_cluster_response import DeleteClusterResponse
from openapi_server.models.delete_service_request import DeleteServiceRequest
from openapi_server.models.delete_service_response import DeleteServiceResponse
from openapi_server.models.delete_task_definitions_request import DeleteTaskDefinitionsRequest
from openapi_server.models.delete_task_definitions_response import DeleteTaskDefinitionsResponse
from openapi_server.models.delete_task_set_request import DeleteTaskSetRequest
from openapi_server.models.delete_task_set_response import DeleteTaskSetResponse
from openapi_server.models.deregister_container_instance_request import DeregisterContainerInstanceRequest
from openapi_server.models.deregister_container_instance_response import DeregisterContainerInstanceResponse
from openapi_server.models.deregister_task_definition_request import DeregisterTaskDefinitionRequest
from openapi_server.models.deregister_task_definition_response import DeregisterTaskDefinitionResponse
from openapi_server.models.describe_capacity_providers_request import DescribeCapacityProvidersRequest
from openapi_server.models.describe_capacity_providers_response import DescribeCapacityProvidersResponse
from openapi_server.models.describe_clusters_request import DescribeClustersRequest
from openapi_server.models.describe_clusters_response import DescribeClustersResponse
from openapi_server.models.describe_container_instances_request import DescribeContainerInstancesRequest
from openapi_server.models.describe_container_instances_response import DescribeContainerInstancesResponse
from openapi_server.models.describe_services_request import DescribeServicesRequest
from openapi_server.models.describe_services_response import DescribeServicesResponse
from openapi_server.models.describe_task_definition_request import DescribeTaskDefinitionRequest
from openapi_server.models.describe_task_definition_response import DescribeTaskDefinitionResponse
from openapi_server.models.describe_task_sets_request import DescribeTaskSetsRequest
from openapi_server.models.describe_task_sets_response import DescribeTaskSetsResponse
from openapi_server.models.describe_tasks_request import DescribeTasksRequest
from openapi_server.models.describe_tasks_response import DescribeTasksResponse
from openapi_server.models.discover_poll_endpoint_request import DiscoverPollEndpointRequest
from openapi_server.models.discover_poll_endpoint_response import DiscoverPollEndpointResponse
from openapi_server.models.execute_command_request import ExecuteCommandRequest
from openapi_server.models.execute_command_response import ExecuteCommandResponse
from openapi_server.models.get_task_protection_request import GetTaskProtectionRequest
from openapi_server.models.get_task_protection_response import GetTaskProtectionResponse
from openapi_server.models.list_account_settings_request import ListAccountSettingsRequest
from openapi_server.models.list_account_settings_response import ListAccountSettingsResponse
from openapi_server.models.list_attributes_request import ListAttributesRequest
from openapi_server.models.list_attributes_response import ListAttributesResponse
from openapi_server.models.list_clusters_request import ListClustersRequest
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_container_instances_request import ListContainerInstancesRequest
from openapi_server.models.list_container_instances_response import ListContainerInstancesResponse
from openapi_server.models.list_services_by_namespace_request import ListServicesByNamespaceRequest
from openapi_server.models.list_services_by_namespace_response import ListServicesByNamespaceResponse
from openapi_server.models.list_services_request import ListServicesRequest
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_task_definition_families_request import ListTaskDefinitionFamiliesRequest
from openapi_server.models.list_task_definition_families_response import ListTaskDefinitionFamiliesResponse
from openapi_server.models.list_task_definitions_request import ListTaskDefinitionsRequest
from openapi_server.models.list_task_definitions_response import ListTaskDefinitionsResponse
from openapi_server.models.list_tasks_request import ListTasksRequest
from openapi_server.models.list_tasks_response import ListTasksResponse
from openapi_server.models.put_account_setting_default_request import PutAccountSettingDefaultRequest
from openapi_server.models.put_account_setting_default_response import PutAccountSettingDefaultResponse
from openapi_server.models.put_account_setting_request import PutAccountSettingRequest
from openapi_server.models.put_account_setting_response import PutAccountSettingResponse
from openapi_server.models.put_attributes_request import PutAttributesRequest
from openapi_server.models.put_attributes_response import PutAttributesResponse
from openapi_server.models.put_cluster_capacity_providers_request import PutClusterCapacityProvidersRequest
from openapi_server.models.put_cluster_capacity_providers_response import PutClusterCapacityProvidersResponse
from openapi_server.models.register_container_instance_request import RegisterContainerInstanceRequest
from openapi_server.models.register_container_instance_response import RegisterContainerInstanceResponse
from openapi_server.models.register_task_definition_request import RegisterTaskDefinitionRequest
from openapi_server.models.register_task_definition_response import RegisterTaskDefinitionResponse
from openapi_server.models.run_task_request import RunTaskRequest
from openapi_server.models.run_task_response import RunTaskResponse
from openapi_server.models.start_task_request import StartTaskRequest
from openapi_server.models.start_task_response import StartTaskResponse
from openapi_server.models.stop_task_request import StopTaskRequest
from openapi_server.models.stop_task_response import StopTaskResponse
from openapi_server.models.submit_attachment_state_changes_request import SubmitAttachmentStateChangesRequest
from openapi_server.models.submit_attachment_state_changes_response import SubmitAttachmentStateChangesResponse
from openapi_server.models.submit_container_state_change_request import SubmitContainerStateChangeRequest
from openapi_server.models.submit_container_state_change_response import SubmitContainerStateChangeResponse
from openapi_server.models.submit_task_state_change_request import SubmitTaskStateChangeRequest
from openapi_server.models.submit_task_state_change_response import SubmitTaskStateChangeResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_capacity_provider_request import UpdateCapacityProviderRequest
from openapi_server.models.update_capacity_provider_response import UpdateCapacityProviderResponse
from openapi_server.models.update_cluster_request import UpdateClusterRequest
from openapi_server.models.update_cluster_response import UpdateClusterResponse
from openapi_server.models.update_cluster_settings_request import UpdateClusterSettingsRequest
from openapi_server.models.update_cluster_settings_response import UpdateClusterSettingsResponse
from openapi_server.models.update_container_agent_request import UpdateContainerAgentRequest
from openapi_server.models.update_container_agent_response import UpdateContainerAgentResponse
from openapi_server.models.update_container_instances_state_request import UpdateContainerInstancesStateRequest
from openapi_server.models.update_container_instances_state_response import UpdateContainerInstancesStateResponse
from openapi_server.models.update_service_primary_task_set_request import UpdateServicePrimaryTaskSetRequest
from openapi_server.models.update_service_primary_task_set_response import UpdateServicePrimaryTaskSetResponse
from openapi_server.models.update_service_request import UpdateServiceRequest
from openapi_server.models.update_service_response import UpdateServiceResponse
from openapi_server.models.update_task_protection_request import UpdateTaskProtectionRequest
from openapi_server.models.update_task_protection_response import UpdateTaskProtectionResponse
from openapi_server.models.update_task_set_request import UpdateTaskSetRequest
from openapi_server.models.update_task_set_response import UpdateTaskSetResponse
from openapi_server import util


async def create_capacity_provider(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_capacity_provider

    &lt;p&gt;Creates a new capacity provider. Capacity providers are associated with an Amazon ECS cluster and are used in capacity provider strategies to facilitate cluster auto scaling.&lt;/p&gt; &lt;p&gt;Only capacity providers that use an Auto Scaling group can be created. Amazon ECS tasks on Fargate use the &lt;code&gt;FARGATE&lt;/code&gt; and &lt;code&gt;FARGATE_SPOT&lt;/code&gt; capacity providers. These providers are available to all accounts in the Amazon Web Services Regions that Fargate supports.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateCapacityProviderRequest.from_dict(body)
    return web.Response(status=200)


async def create_cluster(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cluster

    &lt;p&gt;Creates a new Amazon ECS cluster. By default, your account receives a &lt;code&gt;default&lt;/code&gt; cluster when you launch your first container instance. However, you can create your own cluster with a unique name with the &lt;code&gt;CreateCluster&lt;/code&gt; action.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you call the &lt;a&gt;CreateCluster&lt;/a&gt; API operation, Amazon ECS attempts to create the Amazon ECS service-linked role for your account. This is so that it can manage required resources in other Amazon Web Services services on your behalf. However, if the user that makes the call doesn&#39;t have permissions to create the service-linked role, it isn&#39;t created. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html\&quot;&gt;Using service-linked roles for Amazon ECS&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateClusterRequest.from_dict(body)
    return web.Response(status=200)


async def create_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service

    &lt;p&gt;Runs and maintains your desired number of tasks from a specified task definition. If the number of tasks running in a service drops below the &lt;code&gt;desiredCount&lt;/code&gt;, Amazon ECS runs another copy of the task in the specified cluster. To update an existing service, see the &lt;a&gt;UpdateService&lt;/a&gt; action.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, Amazon ECS, or Amazon EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;In addition to maintaining the desired count of tasks in your service, you can optionally run your service behind one or more load balancers. The load balancers distribute traffic across the tasks that are associated with the service. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html\&quot;&gt;Service load balancing&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Tasks for services that don&#39;t use a load balancer are considered healthy if they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state. Tasks for services that use a load balancer are considered healthy if they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state and are reported as healthy by the load balancer.&lt;/p&gt; &lt;p&gt;There are two service scheduler strategies available:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;REPLICA&lt;/code&gt; - The replica scheduling strategy places and maintains your desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html\&quot;&gt;Service scheduler concepts&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DAEMON&lt;/code&gt; - The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks. It also stops tasks that don&#39;t meet the placement constraints. When using this strategy, you don&#39;t need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html\&quot;&gt;Service scheduler concepts&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can optionally specify a deployment configuration for your service. The deployment is initiated by changing properties. For example, the deployment might be initiated by the task definition or by your desired count of a service. This is done with an &lt;a&gt;UpdateService&lt;/a&gt; operation. The default value for a replica service for &lt;code&gt;minimumHealthyPercent&lt;/code&gt; is 100%. The default value for a daemon service for &lt;code&gt;minimumHealthyPercent&lt;/code&gt; is 0%.&lt;/p&gt; &lt;p&gt;If a service uses the &lt;code&gt;ECS&lt;/code&gt; deployment controller, the minimum healthy percent represents a lower limit on the number of tasks in a service that must remain in the &lt;code&gt;RUNNING&lt;/code&gt; state during a deployment. Specifically, it represents it as a percentage of your desired number of tasks (rounded up to the nearest integer). This happens when any of your container instances are in the &lt;code&gt;DRAINING&lt;/code&gt; state if the service contains tasks using the EC2 launch type. Using this parameter, you can deploy without using additional cluster capacity. For example, if you set your service to have desired number of four tasks and a minimum healthy percent of 50%, the scheduler might stop two existing tasks to free up cluster capacity before starting two new tasks. If they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state, tasks for services that don&#39;t use a load balancer are considered healthy . If they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state and reported as healthy by the load balancer, tasks for services that &lt;i&gt;do&lt;/i&gt; use a load balancer are considered healthy . The default value for minimum healthy percent is 100%.&lt;/p&gt; &lt;p&gt;If a service uses the &lt;code&gt;ECS&lt;/code&gt; deployment controller, the &lt;b&gt;maximum percent&lt;/b&gt; parameter represents an upper limit on the number of tasks in a service that are allowed in the &lt;code&gt;RUNNING&lt;/code&gt; or &lt;code&gt;PENDING&lt;/code&gt; state during a deployment. Specifically, it represents it as a percentage of the desired number of tasks (rounded down to the nearest integer). This happens when any of your container instances are in the &lt;code&gt;DRAINING&lt;/code&gt; state if the service contains tasks using the EC2 launch type. Using this parameter, you can define the deployment batch size. For example, if your service has a desired number of four tasks and a maximum percent value of 200%, the scheduler may start four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available). The default value for maximum percent is 200%.&lt;/p&gt; &lt;p&gt;If a service uses either the &lt;code&gt;CODE_DEPLOY&lt;/code&gt; or &lt;code&gt;EXTERNAL&lt;/code&gt; deployment controller types and tasks that use the EC2 launch type, the &lt;b&gt;minimum healthy percent&lt;/b&gt; and &lt;b&gt;maximum percent&lt;/b&gt; values are used only to define the lower and upper limit on the number of the tasks in the service that remain in the &lt;code&gt;RUNNING&lt;/code&gt; state. This is while the container instances are in the &lt;code&gt;DRAINING&lt;/code&gt; state. If the tasks in the service use the Fargate launch type, the minimum healthy percent and maximum percent values aren&#39;t used. This is the case even if they&#39;re currently visible when describing your service.&lt;/p&gt; &lt;p&gt;When creating a service that uses the &lt;code&gt;EXTERNAL&lt;/code&gt; deployment controller, you can specify only parameters that aren&#39;t controlled at the task set level. The only required parameter is the service name. You control your services using the &lt;a&gt;CreateTaskSet&lt;/a&gt; operation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\&quot;&gt;Amazon ECS deployment types&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When the service scheduler launches new tasks, it determines task placement. For information about task placement and task placement strategies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html\&quot;&gt;Amazon ECS task placement&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServiceRequest.from_dict(body)
    return web.Response(status=200)


async def create_task_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_task_set

    Create a task set in the specified cluster and service. This is used when a service uses the &lt;code&gt;EXTERNAL&lt;/code&gt; deployment controller type. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\&quot;&gt;Amazon ECS deployment types&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateTaskSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_account_setting(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_account_setting

    Disables an account setting for a specified user, role, or the root user for an account.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAccountSettingRequest.from_dict(body)
    return web.Response(status=200)


async def delete_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_attributes

    Deletes one or more custom attributes from an Amazon ECS resource.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def delete_capacity_provider(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_capacity_provider

    &lt;p&gt;Deletes the specified capacity provider.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;FARGATE&lt;/code&gt; and &lt;code&gt;FARGATE_SPOT&lt;/code&gt; capacity providers are reserved and can&#39;t be deleted. You can disassociate them from a cluster using either the &lt;a&gt;PutClusterCapacityProviders&lt;/a&gt; API or by deleting the cluster.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Prior to a capacity provider being deleted, the capacity provider must be removed from the capacity provider strategy from all services. The &lt;a&gt;UpdateService&lt;/a&gt; API can be used to remove a capacity provider from a service&#39;s capacity provider strategy. When updating a service, the &lt;code&gt;forceNewDeployment&lt;/code&gt; option can be used to ensure that any tasks using the Amazon EC2 instance capacity provided by the capacity provider are transitioned to use the capacity from the remaining capacity providers. Only capacity providers that aren&#39;t associated with a cluster can be deleted. To remove a capacity provider from a cluster, you can either use &lt;a&gt;PutClusterCapacityProviders&lt;/a&gt; or delete the cluster.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteCapacityProviderRequest.from_dict(body)
    return web.Response(status=200)


async def delete_cluster(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_cluster

    &lt;p&gt;Deletes the specified cluster. The cluster transitions to the &lt;code&gt;INACTIVE&lt;/code&gt; state. Clusters with an &lt;code&gt;INACTIVE&lt;/code&gt; status might remain discoverable in your account for a period of time. However, this behavior is subject to change in the future. We don&#39;t recommend that you rely on &lt;code&gt;INACTIVE&lt;/code&gt; clusters persisting.&lt;/p&gt; &lt;p&gt;You must deregister all container instances from this cluster before you may delete it. You can list the container instances in a cluster with &lt;a&gt;ListContainerInstances&lt;/a&gt; and deregister them with &lt;a&gt;DeregisterContainerInstance&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteClusterRequest.from_dict(body)
    return web.Response(status=200)


async def delete_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service

    &lt;p&gt;Deletes a specified service within a cluster. You can delete a service if you have no running tasks in it and the desired task count is zero. If the service is actively maintaining tasks, you can&#39;t delete it, and you must update the service to a desired task count of zero. For more information, see &lt;a&gt;UpdateService&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you delete a service, if there are still running tasks that require cleanup, the service status moves from &lt;code&gt;ACTIVE&lt;/code&gt; to &lt;code&gt;DRAINING&lt;/code&gt;, and the service is no longer visible in the console or in the &lt;a&gt;ListServices&lt;/a&gt; API operation. After all tasks have transitioned to either &lt;code&gt;STOPPING&lt;/code&gt; or &lt;code&gt;STOPPED&lt;/code&gt; status, the service status moves from &lt;code&gt;DRAINING&lt;/code&gt; to &lt;code&gt;INACTIVE&lt;/code&gt;. Services in the &lt;code&gt;DRAINING&lt;/code&gt; or &lt;code&gt;INACTIVE&lt;/code&gt; status can still be viewed with the &lt;a&gt;DescribeServices&lt;/a&gt; API operation. However, in the future, &lt;code&gt;INACTIVE&lt;/code&gt; services may be cleaned up and purged from Amazon ECS record keeping, and &lt;a&gt;DescribeServices&lt;/a&gt; calls on those services return a &lt;code&gt;ServiceNotFoundException&lt;/code&gt; error.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;If you attempt to create a new service with the same name as an existing service in either &lt;code&gt;ACTIVE&lt;/code&gt; or &lt;code&gt;DRAINING&lt;/code&gt; status, you receive an error.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteServiceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_task_definitions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_task_definitions

    &lt;p&gt;Deletes one or more task definitions.&lt;/p&gt; &lt;p&gt;You must deregister a task definition revision before you delete it. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterTaskDefinition.html\&quot;&gt;DeregisterTaskDefinition&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When you delete a task definition revision, it is immediately transitions from the &lt;code&gt;INACTIVE&lt;/code&gt; to &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt;. Existing tasks and services that reference a &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt; task definition revision continue to run without disruption. Existing services that reference a &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt; task definition revision can still scale up or down by modifying the service&#39;s desired count.&lt;/p&gt; &lt;p&gt;You can&#39;t use a &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt; task definition revision to run new tasks or create new services. You also can&#39;t update an existing service to reference a &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt; task definition revision.&lt;/p&gt; &lt;p&gt; A task definition revision will stay in &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt; status until all the associated tasks and services have been terminated.&lt;/p&gt; &lt;p&gt;When you delete all &lt;code&gt;INACTIVE&lt;/code&gt; task definition revisions, the task definition name is not displayed in the console and not returned in the API. If a task definition revisions are in the &lt;code&gt;DELETE_IN_PROGRESS&lt;/code&gt; state, the task definition name is displayed in the console and returned in the API. The task definition name is retained by Amazon ECS and the revision is incremented the next time you create a task definition with that name.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteTaskDefinitionsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_task_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_task_set

    Deletes a specified task set within a service. This is used when a service uses the &lt;code&gt;EXTERNAL&lt;/code&gt; deployment controller type. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\&quot;&gt;Amazon ECS deployment types&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteTaskSetRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_container_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_container_instance

    &lt;p&gt;Deregisters an Amazon ECS container instance from the specified cluster. This instance is no longer available to run tasks.&lt;/p&gt; &lt;p&gt;If you intend to use the container instance for some other purpose after deregistration, we recommend that you stop all of the tasks running on the container instance before deregistration. That prevents any orphaned tasks from consuming resources.&lt;/p&gt; &lt;p&gt;Deregistering a container instance removes the instance from a cluster, but it doesn&#39;t terminate the EC2 instance. If you are finished using the instance, be sure to terminate it in the Amazon EC2 console to stop billing.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you terminate a running container instance, Amazon ECS automatically deregisters the instance from your cluster (stopped container instances or instances with disconnected agents aren&#39;t automatically deregistered when terminated).&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeregisterContainerInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def deregister_task_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_task_definition

    &lt;p&gt;Deregisters the specified task definition by family and revision. Upon deregistration, the task definition is marked as &lt;code&gt;INACTIVE&lt;/code&gt;. Existing tasks and services that reference an &lt;code&gt;INACTIVE&lt;/code&gt; task definition continue to run without disruption. Existing services that reference an &lt;code&gt;INACTIVE&lt;/code&gt; task definition can still scale up or down by modifying the service&#39;s desired count. If you want to delete a task definition revision, you must first deregister the task definition revision.&lt;/p&gt; &lt;p&gt;You can&#39;t use an &lt;code&gt;INACTIVE&lt;/code&gt; task definition to run new tasks or create new services, and you can&#39;t update an existing service to reference an &lt;code&gt;INACTIVE&lt;/code&gt; task definition. However, there may be up to a 10-minute window following deregistration where these restrictions have not yet taken effect.&lt;/p&gt; &lt;note&gt; &lt;p&gt;At this time, &lt;code&gt;INACTIVE&lt;/code&gt; task definitions remain discoverable in your account indefinitely. However, this behavior is subject to change in the future. We don&#39;t recommend that you rely on &lt;code&gt;INACTIVE&lt;/code&gt; task definitions persisting beyond the lifecycle of any associated tasks and services.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You must deregister a task definition revision before you delete it. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteTaskDefinitions.html\&quot;&gt;DeleteTaskDefinitions&lt;/a&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeregisterTaskDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def describe_capacity_providers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_capacity_providers

    Describes one or more of your capacity providers.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeCapacityProvidersRequest.from_dict(body)
    return web.Response(status=200)


async def describe_clusters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_clusters

    Describes one or more of your clusters.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeClustersRequest.from_dict(body)
    return web.Response(status=200)


async def describe_container_instances(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_container_instances

    Describes one or more container instances. Returns metadata about each container instance requested.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeContainerInstancesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_services(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_services

    Describes the specified services running in your cluster.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeServicesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_task_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_task_definition

    &lt;p&gt;Describes a task definition. You can specify a &lt;code&gt;family&lt;/code&gt; and &lt;code&gt;revision&lt;/code&gt; to find information about a specific task definition, or you can simply specify the family to find the latest &lt;code&gt;ACTIVE&lt;/code&gt; revision in that family.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can only describe &lt;code&gt;INACTIVE&lt;/code&gt; task definitions while an active task or service references them.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeTaskDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def describe_task_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_task_sets

    Describes the task sets in the specified cluster and service. This is used when a service uses the &lt;code&gt;EXTERNAL&lt;/code&gt; deployment controller type. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\&quot;&gt;Amazon ECS Deployment Types&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeTaskSetsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_tasks

    &lt;p&gt;Describes a specified task or tasks.&lt;/p&gt; &lt;p&gt;Currently, stopped tasks appear in the returned results for at least one hour.&lt;/p&gt; &lt;p&gt;If you have tasks with tags, and then delete the cluster, the tagged tasks are returned in the response. If you create a new cluster with the same name as the deleted cluster, the tagged tasks are not included in the response.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeTasksRequest.from_dict(body)
    return web.Response(status=200)


async def discover_poll_endpoint(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """discover_poll_endpoint

    &lt;note&gt; &lt;p&gt;This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an endpoint for the Amazon ECS agent to poll for updates.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DiscoverPollEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def execute_command(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """execute_command

    &lt;p&gt;Runs a command remotely on a container within a task.&lt;/p&gt; &lt;p&gt;If you use a condition key in your IAM policy to refine the conditions for the policy statement, for example limit the actions to a specific cluster, you receive an &lt;code&gt;AccessDeniedException&lt;/code&gt; when there is a mismatch between the condition key value and the corresponding parameter value.&lt;/p&gt; &lt;p&gt;For information about required permissions and considerations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html\&quot;&gt;Using Amazon ECS Exec for debugging&lt;/a&gt; in the &lt;i&gt;Amazon ECS Developer Guide&lt;/i&gt;. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ExecuteCommandRequest.from_dict(body)
    return web.Response(status=200)


async def get_task_protection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_task_protection

    Retrieves the protection status of tasks in an Amazon ECS service.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetTaskProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def list_account_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_account_settings

    Lists the account settings for a specified principal.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAccountSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def list_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_attributes

    Lists the attributes for Amazon ECS resources within a specified target type and cluster. When you specify a target type and cluster, &lt;code&gt;ListAttributes&lt;/code&gt; returns a list of attribute objects, one for each attribute on each resource. You can filter the list of results to a single attribute name to only return results that have that name. You can also filter the results by attribute name and value. You can do this, for example, to see which container instances in a cluster are running a Linux AMI (&lt;code&gt;ecs.os-type&#x3D;linux&lt;/code&gt;). 

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def list_clusters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_clusters

    Returns a list of existing clusters.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListClustersRequest.from_dict(body)
    return web.Response(status=200)


async def list_container_instances(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_container_instances

    Returns a list of container instances in a specified cluster. You can filter the results of a &lt;code&gt;ListContainerInstances&lt;/code&gt; operation with cluster query language statements inside the &lt;code&gt;filter&lt;/code&gt; parameter. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html\&quot;&gt;Cluster Query Language&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListContainerInstancesRequest.from_dict(body)
    return web.Response(status=200)


async def list_services(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_services

    Returns a list of services. You can filter the results by cluster, launch type, and scheduling strategy.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServicesRequest.from_dict(body)
    return web.Response(status=200)


async def list_services_by_namespace(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_services_by_namespace

    This operation lists all of the services that are associated with a Cloud Map namespace. This list might include services in different clusters. In contrast, &lt;code&gt;ListServices&lt;/code&gt; can only list services in one cluster at a time. If you need to filter the list of services in a single cluster by various parameters, use &lt;code&gt;ListServices&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\&quot;&gt;Service Connect&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListServicesByNamespaceRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    List the tags for an Amazon ECS resource.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_task_definition_families(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_task_definition_families

    &lt;p&gt;Returns a list of task definition families that are registered to your account. This list includes task definition families that no longer have any &lt;code&gt;ACTIVE&lt;/code&gt; task definition revisions.&lt;/p&gt; &lt;p&gt;You can filter out task definition families that don&#39;t contain any &lt;code&gt;ACTIVE&lt;/code&gt; task definition revisions by setting the &lt;code&gt;status&lt;/code&gt; parameter to &lt;code&gt;ACTIVE&lt;/code&gt;. You can also filter the results with the &lt;code&gt;familyPrefix&lt;/code&gt; parameter.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTaskDefinitionFamiliesRequest.from_dict(body)
    return web.Response(status=200)


async def list_task_definitions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_task_definitions

    Returns a list of task definitions that are registered to your account. You can filter the results by family name with the &lt;code&gt;familyPrefix&lt;/code&gt; parameter or by status with the &lt;code&gt;status&lt;/code&gt; parameter.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTaskDefinitionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tasks

    &lt;p&gt;Returns a list of tasks. You can filter the results by cluster, task definition family, container instance, launch type, what IAM principal started the task, or by the desired status of the task.&lt;/p&gt; &lt;p&gt;Recently stopped tasks might appear in the returned results. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTasksRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_setting(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_setting

    &lt;p&gt;Modifies an account setting. Account settings are set on a per-Region basis.&lt;/p&gt; &lt;p&gt;If you change the root user account setting, the default settings are reset for users and roles that do not have specified individual account settings. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html\&quot;&gt;Account Settings&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When &lt;code&gt;serviceLongArnFormat&lt;/code&gt;, &lt;code&gt;taskLongArnFormat&lt;/code&gt;, or &lt;code&gt;containerInstanceLongArnFormat&lt;/code&gt; are specified, the Amazon Resource Name (ARN) and resource ID format of the resource type for a specified user, role, or the root user for an account is affected. The opt-in and opt-out account setting must be set for each Amazon ECS resource separately. The ARN and resource ID format of a resource is defined by the opt-in status of the user or role that created the resource. You must turn on this setting to use Amazon ECS features such as resource tagging.&lt;/p&gt; &lt;p&gt;When &lt;code&gt;awsvpcTrunking&lt;/code&gt; is specified, the elastic network interface (ENI) limit for any new container instances that support the feature is changed. If &lt;code&gt;awsvpcTrunking&lt;/code&gt; is turned on, any new container instances that support the feature are launched have the increased ENI limits available to them. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-eni.html\&quot;&gt;Elastic Network Interface Trunking&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When &lt;code&gt;containerInsights&lt;/code&gt; is specified, the default setting indicating whether Amazon Web Services CloudWatch Container Insights is turned on for your clusters is changed. If &lt;code&gt;containerInsights&lt;/code&gt; is turned on, any new clusters that are created will have Container Insights turned on unless you disable it during cluster creation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-container-insights.html\&quot;&gt;CloudWatch Container Insights&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Amazon ECS is introducing tagging authorization for resource creation. Users must have permissions for actions that create the resource, such as &lt;code&gt;ecsCreateCluster&lt;/code&gt;. If tags are specified when you create a resource, Amazon Web Services performs additional authorization to verify if users or roles have permissions to create tags. Therefore, you must grant explicit permissions to use the &lt;code&gt;ecs:TagResource&lt;/code&gt; action. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/supported-iam-actions-tagging.html\&quot;&gt;Grant permission to tag resources on creation&lt;/a&gt; in the &lt;i&gt;Amazon ECS Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountSettingRequest.from_dict(body)
    return web.Response(status=200)


async def put_account_setting_default(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_account_setting_default

    Modifies an account setting for all users on an account for whom no individual account setting has been specified. Account settings are set on a per-Region basis.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAccountSettingDefaultRequest.from_dict(body)
    return web.Response(status=200)


async def put_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_attributes

    Create or update an attribute on an Amazon ECS resource. If the attribute doesn&#39;t exist, it&#39;s created. If the attribute exists, its value is replaced with the specified value. To delete an attribute, use &lt;a&gt;DeleteAttributes&lt;/a&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-constraints.html#attributes\&quot;&gt;Attributes&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def put_cluster_capacity_providers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_cluster_capacity_providers

    &lt;p&gt;Modifies the available capacity providers and the default capacity provider strategy for a cluster.&lt;/p&gt; &lt;p&gt;You must specify both the available capacity providers and a default capacity provider strategy for the cluster. If the specified cluster has existing capacity providers associated with it, you must specify all existing capacity providers in addition to any new ones you want to add. Any existing capacity providers that are associated with a cluster that are omitted from a &lt;a&gt;PutClusterCapacityProviders&lt;/a&gt; API call will be disassociated with the cluster. You can only disassociate an existing capacity provider from a cluster if it&#39;s not being used by any existing tasks.&lt;/p&gt; &lt;p&gt;When creating a service or running a task on a cluster, if no capacity provider or launch type is specified, then the cluster&#39;s default capacity provider strategy is used. We recommend that you define a default capacity provider strategy for your cluster. However, you must specify an empty array (&lt;code&gt;[]&lt;/code&gt;) to bypass defining a default strategy.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutClusterCapacityProvidersRequest.from_dict(body)
    return web.Response(status=200)


async def register_container_instance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_container_instance

    &lt;note&gt; &lt;p&gt;This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Registers an EC2 instance into the specified cluster. This instance becomes available to place containers on.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RegisterContainerInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def register_task_definition(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_task_definition

    &lt;p&gt;Registers a new task definition from the supplied &lt;code&gt;family&lt;/code&gt; and &lt;code&gt;containerDefinitions&lt;/code&gt;. Optionally, you can add data volumes to your containers with the &lt;code&gt;volumes&lt;/code&gt; parameter. For more information about task definition parameters and defaults, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html\&quot;&gt;Amazon ECS Task Definitions&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can specify a role for your task with the &lt;code&gt;taskRoleArn&lt;/code&gt; parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the Amazon Web Services services that are specified in the policy that&#39;s associated with the role. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html\&quot;&gt;IAM Roles for Tasks&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can specify a Docker networking mode for the containers in your task definition with the &lt;code&gt;networkMode&lt;/code&gt; parameter. The available network modes correspond to those described in &lt;a href&#x3D;\&quot;https://docs.docker.com/engine/reference/run/#/network-settings\&quot;&gt;Network settings&lt;/a&gt; in the Docker run reference. If you specify the &lt;code&gt;awsvpc&lt;/code&gt; network mode, the task is allocated an elastic network interface, and you must specify a &lt;a&gt;NetworkConfiguration&lt;/a&gt; when you create a service or run a task with the task definition. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html\&quot;&gt;Task Networking&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RegisterTaskDefinitionRequest.from_dict(body)
    return web.Response(status=200)


async def run_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """run_task

    &lt;p&gt;Starts a new task using the specified task definition.&lt;/p&gt; &lt;p&gt;You can allow Amazon ECS to place tasks for you, or you can customize how Amazon ECS places tasks using placement constraints and placement strategies. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html\&quot;&gt;Scheduling Tasks&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Alternatively, you can use &lt;a&gt;StartTask&lt;/a&gt; to use your own scheduler or place tasks manually on specific container instances.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, Amazon ECS, or Amazon EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Amazon ECS API follows an eventual consistency model. This is because of the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your Amazon ECS resources might not be immediately visible to all subsequent commands you run. Keep this in mind when you carry out an API command that immediately follows a previous API command.&lt;/p&gt; &lt;p&gt;To manage eventual consistency, you can do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Confirm the state of the resource before you run a command to modify it. Run the DescribeTasks command using an exponential backoff algorithm to ensure that you allow enough time for the previous command to propagate through the system. To do this, run the DescribeTasks command repeatedly, starting with a couple of seconds of wait time and increasing gradually up to five minutes of wait time.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add wait time between subsequent commands, even if the DescribeTasks command returns an accurate response. Apply an exponential backoff algorithm starting with a couple of seconds of wait time, and increase gradually up to about five minutes of wait time.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RunTaskRequest.from_dict(body)
    return web.Response(status=200)


async def start_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_task

    &lt;p&gt;Starts a new task from the specified task definition on the specified container instance or instances.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, Amazon ECS, or Amazon EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Alternatively, you can use &lt;a&gt;RunTask&lt;/a&gt; to place tasks for you. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html\&quot;&gt;Scheduling Tasks&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartTaskRequest.from_dict(body)
    return web.Response(status=200)


async def stop_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_task

    &lt;p&gt;Stops a running task. Any tags associated with the task will be deleted.&lt;/p&gt; &lt;p&gt;When &lt;a&gt;StopTask&lt;/a&gt; is called on a task, the equivalent of &lt;code&gt;docker stop&lt;/code&gt; is issued to the containers running in the task. This results in a &lt;code&gt;SIGTERM&lt;/code&gt; value and a default 30-second timeout, after which the &lt;code&gt;SIGKILL&lt;/code&gt; value is sent and the containers are forcibly stopped. If the container handles the &lt;code&gt;SIGTERM&lt;/code&gt; value gracefully and exits within 30 seconds from receiving it, no &lt;code&gt;SIGKILL&lt;/code&gt; value is sent.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The default 30-second timeout can be configured on the Amazon ECS container agent with the &lt;code&gt;ECS_CONTAINER_STOP_TIMEOUT&lt;/code&gt; variable. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html\&quot;&gt;Amazon ECS Container Agent Configuration&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StopTaskRequest.from_dict(body)
    return web.Response(status=200)


async def submit_attachment_state_changes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """submit_attachment_state_changes

    &lt;note&gt; &lt;p&gt;This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sent to acknowledge that an attachment changed states.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SubmitAttachmentStateChangesRequest.from_dict(body)
    return web.Response(status=200)


async def submit_container_state_change(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """submit_container_state_change

    &lt;note&gt; &lt;p&gt;This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sent to acknowledge that a container changed states.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SubmitContainerStateChangeRequest.from_dict(body)
    return web.Response(status=200)


async def submit_task_state_change(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """submit_task_state_change

    &lt;note&gt; &lt;p&gt;This action is only used by the Amazon ECS agent, and it is not intended for use outside of the agent.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sent to acknowledge that a task changed states.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = SubmitTaskStateChangeRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Associates the specified tags to a resource with the specified &lt;code&gt;resourceArn&lt;/code&gt;. If existing tags on a resource aren&#39;t specified in the request parameters, they aren&#39;t changed. When a resource is deleted, the tags that are associated with that resource are deleted as well.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Deletes specified tags from a resource.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_capacity_provider(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_capacity_provider

    Modifies the parameters for a capacity provider.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateCapacityProviderRequest.from_dict(body)
    return web.Response(status=200)


async def update_cluster(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cluster

    Updates the cluster.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateClusterRequest.from_dict(body)
    return web.Response(status=200)


async def update_cluster_settings(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cluster_settings

    Modifies the settings to use for a cluster.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateClusterSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def update_container_agent(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_container_agent

    &lt;p&gt;Updates the Amazon ECS container agent on a specified container instance. Updating the Amazon ECS container agent doesn&#39;t interrupt running tasks or services on the container instance. The process for updating the agent differs depending on whether your container instance was launched with the Amazon ECS-optimized AMI or another operating system.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;UpdateContainerAgent&lt;/code&gt; API isn&#39;t supported for container instances using the Amazon ECS-optimized Amazon Linux 2 (arm64) AMI. To update the container agent, you can update the &lt;code&gt;ecs-init&lt;/code&gt; package. This updates the agent. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/agent-update-ecs-ami.html\&quot;&gt;Updating the Amazon ECS container agent&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;Agent updates with the &lt;code&gt;UpdateContainerAgent&lt;/code&gt; API operation do not apply to Windows container instances. We recommend that you launch new container instances to update the agent version in your Windows clusters.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The &lt;code&gt;UpdateContainerAgent&lt;/code&gt; API requires an Amazon ECS-optimized AMI or Amazon Linux AMI with the &lt;code&gt;ecs-init&lt;/code&gt; service installed and running. For help updating the Amazon ECS container agent on other operating systems, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html#manually_update_agent\&quot;&gt;Manually updating the Amazon ECS container agent&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContainerAgentRequest.from_dict(body)
    return web.Response(status=200)


async def update_container_instances_state(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_container_instances_state

    &lt;p&gt;Modifies the status of an Amazon ECS container instance.&lt;/p&gt; &lt;p&gt;Once a container instance has reached an &lt;code&gt;ACTIVE&lt;/code&gt; state, you can change the status of a container instance to &lt;code&gt;DRAINING&lt;/code&gt; to manually remove an instance from a cluster, for example to perform system updates, update the Docker daemon, or scale down the cluster size.&lt;/p&gt; &lt;important&gt; &lt;p&gt;A container instance can&#39;t be changed to &lt;code&gt;DRAINING&lt;/code&gt; until it has reached an &lt;code&gt;ACTIVE&lt;/code&gt; status. If the instance is in any other status, an error will be received.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;When you set a container instance to &lt;code&gt;DRAINING&lt;/code&gt;, Amazon ECS prevents new tasks from being scheduled for placement on the container instance and replacement service tasks are started on other container instances in the cluster if the resources are available. Service tasks on the container instance that are in the &lt;code&gt;PENDING&lt;/code&gt; state are stopped immediately.&lt;/p&gt; &lt;p&gt;Service tasks on the container instance that are in the &lt;code&gt;RUNNING&lt;/code&gt; state are stopped and replaced according to the service&#39;s deployment configuration parameters, &lt;code&gt;minimumHealthyPercent&lt;/code&gt; and &lt;code&gt;maximumPercent&lt;/code&gt;. You can change the deployment configuration of your service using &lt;a&gt;UpdateService&lt;/a&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;minimumHealthyPercent&lt;/code&gt; is below 100%, the scheduler can ignore &lt;code&gt;desiredCount&lt;/code&gt; temporarily during task replacement. For example, &lt;code&gt;desiredCount&lt;/code&gt; is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. If the minimum is 100%, the service scheduler can&#39;t remove existing tasks until the replacement tasks are considered healthy. Tasks for services that do not use a load balancer are considered healthy if they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state. Tasks for services that use a load balancer are considered healthy if they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state and are reported as healthy by the load balancer.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;maximumPercent&lt;/code&gt; parameter represents an upper limit on the number of running tasks during task replacement. You can use this to define the replacement batch size. For example, if &lt;code&gt;desiredCount&lt;/code&gt; is four tasks, a maximum of 200% starts four new tasks before stopping the four tasks to be drained, provided that the cluster resources required to do this are available. If the maximum is 100%, then replacement tasks can&#39;t start until the draining tasks have stopped.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Any &lt;code&gt;PENDING&lt;/code&gt; or &lt;code&gt;RUNNING&lt;/code&gt; tasks that do not belong to a service aren&#39;t affected. You must wait for them to finish or stop them manually.&lt;/p&gt; &lt;p&gt;A container instance has completed draining when it has no more &lt;code&gt;RUNNING&lt;/code&gt; tasks. You can verify this using &lt;a&gt;ListTasks&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When a container instance has been drained, you can set a container instance to &lt;code&gt;ACTIVE&lt;/code&gt; status and once it has reached that status the Amazon ECS scheduler can begin scheduling tasks on the instance again.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateContainerInstancesStateRequest.from_dict(body)
    return web.Response(status=200)


async def update_service(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service

    &lt;p&gt;Modifies the parameters of a service.&lt;/p&gt; &lt;p&gt;For services using the rolling update (&lt;code&gt;ECS&lt;/code&gt;) you can update the desired count, deployment configuration, network configuration, load balancers, service registries, enable ECS managed tags option, propagate tags option, task placement constraints and strategies, and task definition. When you update any of these parameters, Amazon ECS starts new tasks with the new configuration. &lt;/p&gt; &lt;p&gt;For services using the blue/green (&lt;code&gt;CODE_DEPLOY&lt;/code&gt;) deployment controller, only the desired count, deployment configuration, health check grace period, task placement constraints and strategies, enable ECS managed tags option, and propagate tags can be updated using this API. If the network configuration, platform version, task definition, or load balancer need to be updated, create a new CodeDeploy deployment. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html\&quot;&gt;CreateDeployment&lt;/a&gt; in the &lt;i&gt;CodeDeploy API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For services using an external deployment controller, you can update only the desired count, task placement constraints and strategies, health check grace period, enable ECS managed tags option, and propagate tags option, using this API. If the launch type, load balancer, network configuration, platform version, or task definition need to be updated, create a new task set For more information, see &lt;a&gt;CreateTaskSet&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can add to or subtract from the number of instantiations of a task definition in a service by specifying the cluster that the service is running in and a new &lt;code&gt;desiredCount&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you have updated the Docker image of your application, you can create a new task definition with that image and deploy it to your service. The service scheduler uses the minimum healthy percent and maximum percent parameters (in the service&#39;s deployment configuration) to determine the deployment strategy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your updated Docker image uses the same tag as what is in the existing task definition for your service (for example, &lt;code&gt;my_image:latest&lt;/code&gt;), you don&#39;t need to create a new revision of your task definition. You can update the service using the &lt;code&gt;forceNewDeployment&lt;/code&gt; option. The new tasks launched by the deployment pull the current image/tag combination from your repository when they start.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can also update the deployment configuration of a service. When a deployment is triggered by updating the task definition of a service, the service scheduler uses the deployment configuration parameters, &lt;code&gt;minimumHealthyPercent&lt;/code&gt; and &lt;code&gt;maximumPercent&lt;/code&gt;, to determine the deployment strategy.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If &lt;code&gt;minimumHealthyPercent&lt;/code&gt; is below 100%, the scheduler can ignore &lt;code&gt;desiredCount&lt;/code&gt; temporarily during a deployment. For example, if &lt;code&gt;desiredCount&lt;/code&gt; is four tasks, a minimum of 50% allows the scheduler to stop two existing tasks before starting two new tasks. Tasks for services that don&#39;t use a load balancer are considered healthy if they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state. Tasks for services that use a load balancer are considered healthy if they&#39;re in the &lt;code&gt;RUNNING&lt;/code&gt; state and are reported as healthy by the load balancer.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;maximumPercent&lt;/code&gt; parameter represents an upper limit on the number of running tasks during a deployment. You can use it to define the deployment batch size. For example, if &lt;code&gt;desiredCount&lt;/code&gt; is four tasks, a maximum of 200% starts four new tasks before stopping the four older tasks (provided that the cluster resources required to do this are available).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When &lt;a&gt;UpdateService&lt;/a&gt; stops a task during a deployment, the equivalent of &lt;code&gt;docker stop&lt;/code&gt; is issued to the containers running in the task. This results in a &lt;code&gt;SIGTERM&lt;/code&gt; and a 30-second timeout. After this, &lt;code&gt;SIGKILL&lt;/code&gt; is sent and the containers are forcibly stopped. If the container handles the &lt;code&gt;SIGTERM&lt;/code&gt; gracefully and exits within 30 seconds from receiving it, no &lt;code&gt;SIGKILL&lt;/code&gt; is sent.&lt;/p&gt; &lt;p&gt;When the service scheduler launches new tasks, it determines task placement in your cluster with the following logic.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Determine which of the container instances in your cluster can support your service&#39;s task definition. For example, they have the required CPU, memory, ports, and container instance attributes.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;By default, the service scheduler attempts to balance tasks across Availability Zones in this manner even though you can choose a different placement strategy.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Sort the valid container instances by the fewest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have zero, valid container instances in either zone B or C are considered optimal for placement.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Place the new service task on a valid container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the fewest number of running tasks for this service.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When the service scheduler stops running tasks, it attempts to maintain balance across the Availability Zones in your cluster using the following logic: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Sort the container instances by the largest number of running tasks for this service in the same Availability Zone as the instance. For example, if zone A has one running service task and zones B and C each have two, container instances in either zone B or C are considered optimal for termination.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Stop the task on a container instance in an optimal Availability Zone (based on the previous steps), favoring container instances with the largest number of running tasks for this service.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;You must have a service-linked role when you update any of the following service properties:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;loadBalancers&lt;/code&gt;,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;serviceRegistries&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about the role see the &lt;code&gt;CreateService&lt;/code&gt; request parameter &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html#ECS-CreateService-request-role\&quot;&gt; &lt;code&gt;role&lt;/code&gt; &lt;/a&gt;. &lt;/p&gt; &lt;/note&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServiceRequest.from_dict(body)
    return web.Response(status=200)


async def update_service_primary_task_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_primary_task_set

    Modifies which task set in a service is the primary task set. Any parameters that are updated on the primary task set in a service will transition to the service. This is used when a service uses the &lt;code&gt;EXTERNAL&lt;/code&gt; deployment controller type. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\&quot;&gt;Amazon ECS Deployment Types&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServicePrimaryTaskSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_task_protection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_task_protection

    &lt;p&gt;Updates the protection status of a task. You can set &lt;code&gt;protectionEnabled&lt;/code&gt; to &lt;code&gt;true&lt;/code&gt; to protect your task from termination during scale-in events from &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html\&quot;&gt;Service Autoscaling&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\&quot;&gt;deployments&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Task-protection, by default, expires after 2 hours at which point Amazon ECS clears the &lt;code&gt;protectionEnabled&lt;/code&gt; property making the task eligible for termination by a subsequent scale-in event.&lt;/p&gt; &lt;p&gt;You can specify a custom expiration period for task protection from 1 minute to up to 2,880 minutes (48 hours). To specify the custom expiration period, set the &lt;code&gt;expiresInMinutes&lt;/code&gt; property. The &lt;code&gt;expiresInMinutes&lt;/code&gt; property is always reset when you invoke this operation for a task that already has &lt;code&gt;protectionEnabled&lt;/code&gt; set to &lt;code&gt;true&lt;/code&gt;. You can keep extending the protection expiration period of a task by invoking this operation repeatedly.&lt;/p&gt; &lt;p&gt;To learn more about Amazon ECS task protection, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection.html\&quot;&gt;Task scale-in protection&lt;/a&gt; in the &lt;i&gt; &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt; &lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is only supported for tasks belonging to an Amazon ECS service. Invoking this operation for a standalone task will result in an &lt;code&gt;TASK_NOT_VALID&lt;/code&gt; failure. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html\&quot;&gt;API failure reasons&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt;If you prefer to set task protection from within the container, we recommend using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-scale-in-protection-endpoint.html\&quot;&gt;Task scale-in protection endpoint&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTaskProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_task_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_task_set

    Modifies a task set. This is used when a service uses the &lt;code&gt;EXTERNAL&lt;/code&gt; deployment controller type. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html\&quot;&gt;Amazon ECS Deployment Types&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Service Developer Guide&lt;/i&gt;.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateTaskSetRequest.from_dict(body)
    return web.Response(status=200)
