from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_configuration_items_to_application_request import AssociateConfigurationItemsToApplicationRequest
from openapi_server.models.batch_delete_import_data_request import BatchDeleteImportDataRequest
from openapi_server.models.batch_delete_import_data_response import BatchDeleteImportDataResponse
from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.create_application_response import CreateApplicationResponse
from openapi_server.models.create_tags_request import CreateTagsRequest
from openapi_server.models.delete_applications_request import DeleteApplicationsRequest
from openapi_server.models.delete_tags_request import DeleteTagsRequest
from openapi_server.models.describe_agents_request import DescribeAgentsRequest
from openapi_server.models.describe_agents_response import DescribeAgentsResponse
from openapi_server.models.describe_configurations_request import DescribeConfigurationsRequest
from openapi_server.models.describe_configurations_response import DescribeConfigurationsResponse
from openapi_server.models.describe_continuous_exports_request import DescribeContinuousExportsRequest
from openapi_server.models.describe_continuous_exports_response import DescribeContinuousExportsResponse
from openapi_server.models.describe_export_configurations_request import DescribeExportConfigurationsRequest
from openapi_server.models.describe_export_configurations_response import DescribeExportConfigurationsResponse
from openapi_server.models.describe_export_tasks_request import DescribeExportTasksRequest
from openapi_server.models.describe_export_tasks_response import DescribeExportTasksResponse
from openapi_server.models.describe_import_tasks_request import DescribeImportTasksRequest
from openapi_server.models.describe_import_tasks_response import DescribeImportTasksResponse
from openapi_server.models.describe_tags_request import DescribeTagsRequest
from openapi_server.models.describe_tags_response import DescribeTagsResponse
from openapi_server.models.disassociate_configuration_items_from_application_request import DisassociateConfigurationItemsFromApplicationRequest
from openapi_server.models.export_configurations_response import ExportConfigurationsResponse
from openapi_server.models.get_discovery_summary_response import GetDiscoverySummaryResponse
from openapi_server.models.list_configurations_request import ListConfigurationsRequest
from openapi_server.models.list_configurations_response import ListConfigurationsResponse
from openapi_server.models.list_server_neighbors_request import ListServerNeighborsRequest
from openapi_server.models.list_server_neighbors_response import ListServerNeighborsResponse
from openapi_server.models.start_continuous_export_response import StartContinuousExportResponse
from openapi_server.models.start_data_collection_by_agent_ids_request import StartDataCollectionByAgentIdsRequest
from openapi_server.models.start_data_collection_by_agent_ids_response import StartDataCollectionByAgentIdsResponse
from openapi_server.models.start_export_task_request import StartExportTaskRequest
from openapi_server.models.start_export_task_response import StartExportTaskResponse
from openapi_server.models.start_import_task_request import StartImportTaskRequest
from openapi_server.models.start_import_task_response import StartImportTaskResponse
from openapi_server.models.stop_continuous_export_request import StopContinuousExportRequest
from openapi_server.models.stop_continuous_export_response import StopContinuousExportResponse
from openapi_server.models.stop_data_collection_by_agent_ids_request import StopDataCollectionByAgentIdsRequest
from openapi_server.models.stop_data_collection_by_agent_ids_response import StopDataCollectionByAgentIdsResponse
from openapi_server.models.update_application_request import UpdateApplicationRequest
from openapi_server import util


async def associate_configuration_items_to_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_configuration_items_to_application

    Associates one or more configuration items with an application.

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
    body = AssociateConfigurationItemsToApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def batch_delete_import_data(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_delete_import_data

    &lt;p&gt;Deletes one or more import tasks, each identified by their import ID. Each import task has a number of records that can identify servers or applications. &lt;/p&gt; &lt;p&gt;Amazon Web Services Application Discovery Service has built-in matching logic that will identify when discovered servers match existing entries that you&#39;ve previously discovered, the information for the already-existing discovered server is updated. When you delete an import task that contains records that were used to match, the information in those matched records that comes from the deleted records will also be deleted.&lt;/p&gt;

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
    body = BatchDeleteImportDataRequest.from_dict(body)
    return web.Response(status=200)


async def create_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application

    Creates an application with the given name and description.

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
    body = CreateApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def create_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tags

    &lt;p&gt;Creates one or more tags for configuration items. Tags are metadata that help you categorize IT assets. This API accepts a list of multiple configuration items.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Do not store sensitive information (like personal data) in tags.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateTagsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_applications(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_applications

    Deletes a list of applications and their associations with configuration items.

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
    body = DeleteApplicationsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tags

    Deletes the association between configuration items and one or more tags. This API accepts a list of multiple configuration items.

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
    body = DeleteTagsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_agents(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_agents

    Lists agents or collectors as specified by ID or other filters. All agents/collectors associated with your user can be listed if you call &lt;code&gt;DescribeAgents&lt;/code&gt; as is without passing any parameters.

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
    body = DescribeAgentsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_configurations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_configurations

    &lt;p&gt;Retrieves attributes for a list of configuration item IDs.&lt;/p&gt; &lt;note&gt; &lt;p&gt;All of the supplied IDs must be for the same asset type from one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;server&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;application&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;process&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;connection&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Output fields are specific to the asset type specified. For example, the output for a &lt;i&gt;server&lt;/i&gt; configuration item includes a list of attributes about the server, such as host name, operating system, number of network cards, etc.&lt;/p&gt; &lt;p&gt;For a complete list of outputs for each asset type, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#DescribeConfigurations\&quot;&gt;Using the DescribeConfigurations Action&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_continuous_exports(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_continuous_exports

    Lists exports as specified by ID. All continuous exports associated with your user can be listed if you call &lt;code&gt;DescribeContinuousExports&lt;/code&gt; as is without passing any parameters.

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
    body = DescribeContinuousExportsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_export_configurations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_export_configurations

     &lt;code&gt;DescribeExportConfigurations&lt;/code&gt; is deprecated. Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_DescribeExportTasks.html\&quot;&gt;DescribeExportTasks&lt;/a&gt;, instead.

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
    body = DescribeExportConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_export_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_export_tasks

    Retrieve status of one or more export tasks. You can retrieve the status of up to 100 export tasks.

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
    body = DescribeExportTasksRequest.from_dict(body)
    return web.Response(status=200)


async def describe_import_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_import_tasks

    Returns an array of import tasks for your account, including status information, times, IDs, the Amazon S3 Object URL for the import file, and more.

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
    body = DescribeImportTasksRequest.from_dict(body)
    return web.Response(status=200)


async def describe_tags(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_tags

    &lt;p&gt;Retrieves a list of configuration items that have tags as specified by the key-value pairs, name and value, passed to the optional parameter &lt;code&gt;filters&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;There are three valid tag filter names:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;tagKey&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;tagValue&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;configurationId&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Also, all configuration items associated with your user that have tags can be listed if you call &lt;code&gt;DescribeTags&lt;/code&gt; as is without passing any parameters.&lt;/p&gt;

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
    body = DescribeTagsRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_configuration_items_from_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_configuration_items_from_application

    Disassociates one or more configuration items from an application.

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
    body = DisassociateConfigurationItemsFromApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def export_configurations(request: web.Request, x_amz_target, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """export_configurations

    &lt;p&gt;Deprecated. Use &lt;code&gt;StartExportTask&lt;/code&gt; instead.&lt;/p&gt; &lt;p&gt;Exports all discovered configuration data to an Amazon S3 bucket or an application that enables you to view and evaluate the data. Data includes tags and tag associations, processes, connections, servers, and system performance. This API returns an export ID that you can query using the &lt;i&gt;DescribeExportConfigurations&lt;/i&gt; API. The system imposes a limit of two configuration exports in six hours.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
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
    return web.Response(status=200)


async def get_discovery_summary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_discovery_summary

    &lt;p&gt;Retrieves a short summary of discovered assets.&lt;/p&gt; &lt;p&gt;This API operation takes no request parameters and is called as is at the command prompt as shown in the example.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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
    return web.Response(status=200)


async def list_configurations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_configurations

    Retrieves a list of configuration items as specified by the value passed to the required parameter &lt;code&gt;configurationType&lt;/code&gt;. Optional filtering may be applied to refine search results.

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
    body = ListConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_server_neighbors(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_server_neighbors

    Retrieves a list of servers that are one network hop away from a specified server.

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
    body = ListServerNeighborsRequest.from_dict(body)
    return web.Response(status=200)


async def start_continuous_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_continuous_export

    Start the continuous flow of agent&#39;s discovered data into Amazon Athena.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
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
    return web.Response(status=200)


async def start_data_collection_by_agent_ids(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_data_collection_by_agent_ids

    Instructs the specified agents to start collecting data.

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
    body = StartDataCollectionByAgentIdsRequest.from_dict(body)
    return web.Response(status=200)


async def start_export_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_export_task

    &lt;p&gt;Begins the export of a discovered data report to an Amazon S3 bucket managed by Amazon Web Services.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Exports might provide an estimate of fees and savings based on certain information that you provide. Fee estimates do not include any taxes that might apply. Your actual fees and savings depend on a variety of factors, including your actual usage of Amazon Web Services services, which might vary from the estimates provided in this report.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you do not specify &lt;code&gt;preferences&lt;/code&gt; or &lt;code&gt;agentIds&lt;/code&gt; in the filter, a summary of all servers, applications, tags, and performance is generated. This data is an aggregation of all server data collected through on-premises tooling, file import, application grouping and applying tags.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;agentIds&lt;/code&gt; in a filter, the task exports up to 72 hours of detailed data collected by the identified Application Discovery Agent, including network, process, and performance details. A time range for exported agent data may be set by using &lt;code&gt;startTime&lt;/code&gt; and &lt;code&gt;endTime&lt;/code&gt;. Export of detailed agent data is limited to five concurrently running exports. Export of detailed agent data is limited to two exports per day.&lt;/p&gt; &lt;p&gt;If you enable &lt;code&gt;ec2RecommendationsPreferences&lt;/code&gt; in &lt;code&gt;preferences&lt;/code&gt; , an Amazon EC2 instance matching the characteristics of each server in Application Discovery Service is generated. Changing the attributes of the &lt;code&gt;ec2RecommendationsPreferences&lt;/code&gt; changes the criteria of the recommendation.&lt;/p&gt;

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
    body = StartExportTaskRequest.from_dict(body)
    return web.Response(status=200)


async def start_import_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_import_task

    &lt;p&gt;Starts an import task, which allows you to import details of your on-premises environment directly into Amazon Web Services Migration Hub without having to use the Amazon Web Services Application Discovery Service (Application Discovery Service) tools such as the Amazon Web Services Application Discovery Service Agentless Collector or Application Discovery Agent. This gives you the option to perform migration assessment and planning directly from your imported data, including the ability to group your devices as applications and track their migration status.&lt;/p&gt; &lt;p&gt;To start an import request, do this:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Download the specially formatted comma separated value (CSV) import template, which you can find here: &lt;a href&#x3D;\&quot;https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv\&quot;&gt;https://s3.us-west-2.amazonaws.com/templates-7cffcf56-bd96-4b1c-b45b-a5b42f282e46/import_template.csv&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Fill out the template with your server and application data.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Upload your import file to an Amazon S3 bucket, and make a note of it&#39;s Object URL. Your import file must be in the CSV format.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the console or the &lt;code&gt;StartImportTask&lt;/code&gt; command with the Amazon Web Services CLI or one of the Amazon Web Services SDKs to import the records from your file.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information, including step-by-step procedures, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-import.html\&quot;&gt;Migration Hub Import&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;There are limits to the number of import tasks you can create (and delete) in an Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/ads_service_limits.html\&quot;&gt;Amazon Web Services Application Discovery Service Limits&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Application Discovery Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = StartImportTaskRequest.from_dict(body)
    return web.Response(status=200)


async def stop_continuous_export(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_continuous_export

    Stop the continuous flow of agent&#39;s discovered data into Amazon Athena.

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
    body = StopContinuousExportRequest.from_dict(body)
    return web.Response(status=200)


async def stop_data_collection_by_agent_ids(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_data_collection_by_agent_ids

    Instructs the specified agents to stop collecting data.

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
    body = StopDataCollectionByAgentIdsRequest.from_dict(body)
    return web.Response(status=200)


async def update_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_application

    Updates metadata about an application.

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
    body = UpdateApplicationRequest.from_dict(body)
    return web.Response(status=200)
