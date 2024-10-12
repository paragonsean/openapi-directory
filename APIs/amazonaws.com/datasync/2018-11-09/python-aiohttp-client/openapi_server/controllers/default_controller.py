from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_storage_system_request import AddStorageSystemRequest
from openapi_server.models.add_storage_system_response import AddStorageSystemResponse
from openapi_server.models.cancel_task_execution_request import CancelTaskExecutionRequest
from openapi_server.models.create_agent_request import CreateAgentRequest
from openapi_server.models.create_agent_response import CreateAgentResponse
from openapi_server.models.create_location_azure_blob_request import CreateLocationAzureBlobRequest
from openapi_server.models.create_location_azure_blob_response import CreateLocationAzureBlobResponse
from openapi_server.models.create_location_efs_request import CreateLocationEfsRequest
from openapi_server.models.create_location_efs_response import CreateLocationEfsResponse
from openapi_server.models.create_location_fsx_lustre_request import CreateLocationFsxLustreRequest
from openapi_server.models.create_location_fsx_lustre_response import CreateLocationFsxLustreResponse
from openapi_server.models.create_location_fsx_ontap_request import CreateLocationFsxOntapRequest
from openapi_server.models.create_location_fsx_ontap_response import CreateLocationFsxOntapResponse
from openapi_server.models.create_location_fsx_open_zfs_request import CreateLocationFsxOpenZfsRequest
from openapi_server.models.create_location_fsx_open_zfs_response import CreateLocationFsxOpenZfsResponse
from openapi_server.models.create_location_fsx_windows_request import CreateLocationFsxWindowsRequest
from openapi_server.models.create_location_fsx_windows_response import CreateLocationFsxWindowsResponse
from openapi_server.models.create_location_hdfs_request import CreateLocationHdfsRequest
from openapi_server.models.create_location_hdfs_response import CreateLocationHdfsResponse
from openapi_server.models.create_location_nfs_request import CreateLocationNfsRequest
from openapi_server.models.create_location_nfs_response import CreateLocationNfsResponse
from openapi_server.models.create_location_object_storage_request import CreateLocationObjectStorageRequest
from openapi_server.models.create_location_object_storage_response import CreateLocationObjectStorageResponse
from openapi_server.models.create_location_s3_request import CreateLocationS3Request
from openapi_server.models.create_location_s3_response import CreateLocationS3Response
from openapi_server.models.create_location_smb_request import CreateLocationSmbRequest
from openapi_server.models.create_location_smb_response import CreateLocationSmbResponse
from openapi_server.models.create_task_request import CreateTaskRequest
from openapi_server.models.create_task_response import CreateTaskResponse
from openapi_server.models.delete_agent_request import DeleteAgentRequest
from openapi_server.models.delete_location_request import DeleteLocationRequest
from openapi_server.models.delete_task_request import DeleteTaskRequest
from openapi_server.models.describe_agent_request import DescribeAgentRequest
from openapi_server.models.describe_agent_response import DescribeAgentResponse
from openapi_server.models.describe_discovery_job_request import DescribeDiscoveryJobRequest
from openapi_server.models.describe_discovery_job_response import DescribeDiscoveryJobResponse
from openapi_server.models.describe_location_azure_blob_request import DescribeLocationAzureBlobRequest
from openapi_server.models.describe_location_azure_blob_response import DescribeLocationAzureBlobResponse
from openapi_server.models.describe_location_efs_request import DescribeLocationEfsRequest
from openapi_server.models.describe_location_efs_response import DescribeLocationEfsResponse
from openapi_server.models.describe_location_fsx_lustre_request import DescribeLocationFsxLustreRequest
from openapi_server.models.describe_location_fsx_lustre_response import DescribeLocationFsxLustreResponse
from openapi_server.models.describe_location_fsx_ontap_request import DescribeLocationFsxOntapRequest
from openapi_server.models.describe_location_fsx_ontap_response import DescribeLocationFsxOntapResponse
from openapi_server.models.describe_location_fsx_open_zfs_request import DescribeLocationFsxOpenZfsRequest
from openapi_server.models.describe_location_fsx_open_zfs_response import DescribeLocationFsxOpenZfsResponse
from openapi_server.models.describe_location_fsx_windows_request import DescribeLocationFsxWindowsRequest
from openapi_server.models.describe_location_fsx_windows_response import DescribeLocationFsxWindowsResponse
from openapi_server.models.describe_location_hdfs_request import DescribeLocationHdfsRequest
from openapi_server.models.describe_location_hdfs_response import DescribeLocationHdfsResponse
from openapi_server.models.describe_location_nfs_request import DescribeLocationNfsRequest
from openapi_server.models.describe_location_nfs_response import DescribeLocationNfsResponse
from openapi_server.models.describe_location_object_storage_request import DescribeLocationObjectStorageRequest
from openapi_server.models.describe_location_object_storage_response import DescribeLocationObjectStorageResponse
from openapi_server.models.describe_location_s3_request import DescribeLocationS3Request
from openapi_server.models.describe_location_s3_response import DescribeLocationS3Response
from openapi_server.models.describe_location_smb_request import DescribeLocationSmbRequest
from openapi_server.models.describe_location_smb_response import DescribeLocationSmbResponse
from openapi_server.models.describe_storage_system_request import DescribeStorageSystemRequest
from openapi_server.models.describe_storage_system_resource_metrics_request import DescribeStorageSystemResourceMetricsRequest
from openapi_server.models.describe_storage_system_resource_metrics_response import DescribeStorageSystemResourceMetricsResponse
from openapi_server.models.describe_storage_system_resources_request import DescribeStorageSystemResourcesRequest
from openapi_server.models.describe_storage_system_resources_response import DescribeStorageSystemResourcesResponse
from openapi_server.models.describe_storage_system_response import DescribeStorageSystemResponse
from openapi_server.models.describe_task_execution_request import DescribeTaskExecutionRequest
from openapi_server.models.describe_task_execution_response import DescribeTaskExecutionResponse
from openapi_server.models.describe_task_request import DescribeTaskRequest
from openapi_server.models.describe_task_response import DescribeTaskResponse
from openapi_server.models.generate_recommendations_request import GenerateRecommendationsRequest
from openapi_server.models.list_agents_request import ListAgentsRequest
from openapi_server.models.list_agents_response import ListAgentsResponse
from openapi_server.models.list_discovery_jobs_request import ListDiscoveryJobsRequest
from openapi_server.models.list_discovery_jobs_response import ListDiscoveryJobsResponse
from openapi_server.models.list_locations_request import ListLocationsRequest
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_storage_systems_request import ListStorageSystemsRequest
from openapi_server.models.list_storage_systems_response import ListStorageSystemsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_task_executions_request import ListTaskExecutionsRequest
from openapi_server.models.list_task_executions_response import ListTaskExecutionsResponse
from openapi_server.models.list_tasks_request import ListTasksRequest
from openapi_server.models.list_tasks_response import ListTasksResponse
from openapi_server.models.remove_storage_system_request import RemoveStorageSystemRequest
from openapi_server.models.start_discovery_job_request import StartDiscoveryJobRequest
from openapi_server.models.start_discovery_job_response import StartDiscoveryJobResponse
from openapi_server.models.start_task_execution_request import StartTaskExecutionRequest
from openapi_server.models.start_task_execution_response import StartTaskExecutionResponse
from openapi_server.models.stop_discovery_job_request import StopDiscoveryJobRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_agent_request import UpdateAgentRequest
from openapi_server.models.update_discovery_job_request import UpdateDiscoveryJobRequest
from openapi_server.models.update_location_azure_blob_request import UpdateLocationAzureBlobRequest
from openapi_server.models.update_location_hdfs_request import UpdateLocationHdfsRequest
from openapi_server.models.update_location_nfs_request import UpdateLocationNfsRequest
from openapi_server.models.update_location_object_storage_request import UpdateLocationObjectStorageRequest
from openapi_server.models.update_location_smb_request import UpdateLocationSmbRequest
from openapi_server.models.update_storage_system_request import UpdateStorageSystemRequest
from openapi_server.models.update_task_execution_request import UpdateTaskExecutionRequest
from openapi_server.models.update_task_request import UpdateTaskRequest
from openapi_server import util


async def add_storage_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_storage_system

    Creates an Amazon Web Services resource for an on-premises storage system that you want DataSync Discovery to collect information about.

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
    body = AddStorageSystemRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_task_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_task_execution

    &lt;p&gt;Stops an DataSync task execution that&#39;s in progress. The transfer of some files are abruptly interrupted. File contents that&#39;re transferred to the destination might be incomplete or inconsistent with the source files.&lt;/p&gt; &lt;p&gt;However, if you start a new task execution using the same task and allow it to finish, file content on the destination will be complete and consistent. This applies to other unexpected failures that interrupt a task execution. In all of these cases, DataSync successfully completes the transfer when you start the next task execution.&lt;/p&gt;

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
    body = CancelTaskExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def create_agent(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_agent

    &lt;p&gt;Activates an DataSync agent that you&#39;ve deployed in your storage environment. The activation process associates the agent with your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;If you haven&#39;t deployed an agent yet, see the following topics to learn more:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/agent-requirements.html\&quot;&gt;Agent requirements&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/configure-agent.html\&quot;&gt;Create an agent&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;If you&#39;re transferring between Amazon Web Services storage services, you don&#39;t need a DataSync agent. &lt;/p&gt; &lt;/note&gt;

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
    body = CreateAgentRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_azure_blob(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_azure_blob

    &lt;p&gt;Creates an endpoint for a Microsoft Azure Blob Storage container that DataSync can use as a transfer source or destination.&lt;/p&gt; &lt;p&gt;Before you begin, make sure you know &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access\&quot;&gt;how DataSync accesses Azure Blob Storage&lt;/a&gt; and works with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-access-tiers\&quot;&gt;access tiers&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#blob-types\&quot;&gt;blob types&lt;/a&gt;. You also need a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html#azure-blob-creating-agent\&quot;&gt;DataSync agent&lt;/a&gt; that can connect to your container.&lt;/p&gt;

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
    body = CreateLocationAzureBlobRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_efs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_efs

    Creates an endpoint for an Amazon EFS file system that DataSync can access for a transfer. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html\&quot;&gt;Creating a location for Amazon EFS&lt;/a&gt;.

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
    body = CreateLocationEfsRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_fsx_lustre(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_fsx_lustre

    Creates an endpoint for an Amazon FSx for Lustre file system.

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
    body = CreateLocationFsxLustreRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_fsx_ontap(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_fsx_ontap

    Creates an endpoint for an Amazon FSx for NetApp ONTAP file system that DataSync can access for a transfer. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html\&quot;&gt;Creating a location for FSx for ONTAP&lt;/a&gt;.

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
    body = CreateLocationFsxOntapRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_fsx_open_zfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_fsx_open_zfs

    &lt;p&gt;Creates an endpoint for an Amazon FSx for OpenZFS file system that DataSync can access for a transfer. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-openzfs-location.html\&quot;&gt;Creating a location for FSx for OpenZFS&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Request parameters related to &lt;code&gt;SMB&lt;/code&gt; aren&#39;t supported with the &lt;code&gt;CreateLocationFsxOpenZfs&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateLocationFsxOpenZfsRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_fsx_windows(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_fsx_windows

    Creates an endpoint for an Amazon FSx for Windows File Server file system.

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
    body = CreateLocationFsxWindowsRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_hdfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_hdfs

    Creates an endpoint for a Hadoop Distributed File System (HDFS). 

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
    body = CreateLocationHdfsRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_nfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_nfs

    &lt;p&gt;Creates an endpoint for a Network File System (NFS) file server that DataSync can use for a data transfer.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html\&quot;&gt;Configuring transfers to or from an NFS file server&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you&#39;re copying data to or from an Snowcone device, you can also use &lt;code&gt;CreateLocationNfs&lt;/code&gt; to create your transfer location. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/nfs-on-snowcone.html\&quot;&gt;Configuring transfers with Snowcone&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateLocationNfsRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_object_storage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_object_storage

    Creates an endpoint for an object storage system that DataSync can access for a transfer. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-object-location.html\&quot;&gt;Creating a location for object storage&lt;/a&gt;.

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
    body = CreateLocationObjectStorageRequest.from_dict(body)
    return web.Response(status=200)


async def create_location_s3(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_s3

    &lt;p&gt;A &lt;i&gt;location&lt;/i&gt; is an endpoint for an Amazon S3 bucket. DataSync can use the location as a source or destination for copying data.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Before you create your location, make sure that you read the following sections:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes\&quot;&gt;Storage class considerations with Amazon S3 locations&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests\&quot;&gt;Evaluating S3 request costs when using DataSync&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/important&gt; &lt;p&gt; For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-locations-cli.html#create-location-s3-cli\&quot;&gt;Creating an Amazon S3 location&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateLocationS3Request.from_dict(body)
    return web.Response(status=200)


async def create_location_smb(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_location_smb

    &lt;p&gt;Creates an endpoint for a Server Message Block (SMB) file server that DataSync can use for a data transfer.&lt;/p&gt; &lt;p&gt;Before you begin, make sure that you understand how DataSync &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html\&quot;&gt;accesses an SMB file server&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateLocationSmbRequest.from_dict(body)
    return web.Response(status=200)


async def create_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_task

    &lt;p&gt;Configures a task, which defines where and how DataSync transfers your data.&lt;/p&gt; &lt;p&gt;A task includes a source location, a destination location, and the preferences for how and when you want to transfer your data (such as bandwidth limits, scheduling, among other options).&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you&#39;re planning to transfer data to or from an Amazon S3 location, review &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests\&quot;&gt;how DataSync can affect your S3 request charges&lt;/a&gt; and the &lt;a href&#x3D;\&quot;http://aws.amazon.com/datasync/pricing/\&quot;&gt;DataSync pricing page&lt;/a&gt; before you begin.&lt;/p&gt; &lt;/important&gt;

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
    body = CreateTaskRequest.from_dict(body)
    return web.Response(status=200)


async def delete_agent(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_agent

    Deletes an agent. To specify which agent to delete, use the Amazon Resource Name (ARN) of the agent in your request. The operation disassociates the agent from your Amazon Web Services account. However, it doesn&#39;t delete the agent virtual machine (VM) from your on-premises environment.

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
    body = DeleteAgentRequest.from_dict(body)
    return web.Response(status=200)


async def delete_location(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_location

    Deletes the configuration of a location used by DataSync. 

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
    body = DeleteLocationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_task

    Deletes an DataSync task.

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
    body = DeleteTaskRequest.from_dict(body)
    return web.Response(status=200)


async def describe_agent(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_agent

    Returns metadata about an DataSync agent, such as its name, endpoint type, and status.

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
    body = DescribeAgentRequest.from_dict(body)
    return web.Response(status=200)


async def describe_discovery_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_discovery_job

    Returns information about a DataSync discovery job.

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
    body = DescribeDiscoveryJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_azure_blob(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_azure_blob

    Provides details about how an DataSync transfer location for Microsoft Azure Blob Storage is configured.

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
    body = DescribeLocationAzureBlobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_efs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_efs

    Returns metadata about your DataSync location for an Amazon EFS file system.

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
    body = DescribeLocationEfsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_fsx_lustre(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_fsx_lustre

    Provides details about how an DataSync location for an Amazon FSx for Lustre file system is configured.

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
    body = DescribeLocationFsxLustreRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_fsx_ontap(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_fsx_ontap

    &lt;p&gt;Provides details about how an DataSync location for an Amazon FSx for NetApp ONTAP file system is configured.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your location uses SMB, the &lt;code&gt;DescribeLocationFsxOntap&lt;/code&gt; operation doesn&#39;t actually return a &lt;code&gt;Password&lt;/code&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeLocationFsxOntapRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_fsx_open_zfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_fsx_open_zfs

    &lt;p&gt;Provides details about how an DataSync location for an Amazon FSx for OpenZFS file system is configured.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Response elements related to &lt;code&gt;SMB&lt;/code&gt; aren&#39;t supported with the &lt;code&gt;DescribeLocationFsxOpenZfs&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeLocationFsxOpenZfsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_fsx_windows(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_fsx_windows

    Returns metadata about an Amazon FSx for Windows File Server location, such as information about its path.

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
    body = DescribeLocationFsxWindowsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_hdfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_hdfs

    Returns metadata, such as the authentication information about the Hadoop Distributed File System (HDFS) location. 

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
    body = DescribeLocationHdfsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_nfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_nfs

    Provides details about how an DataSync transfer location for a Network File System (NFS) file server is configured.

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
    body = DescribeLocationNfsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_object_storage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_object_storage

    Returns metadata about your DataSync location for an object storage system.

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
    body = DescribeLocationObjectStorageRequest.from_dict(body)
    return web.Response(status=200)


async def describe_location_s3(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_s3

    Returns metadata, such as bucket name, about an Amazon S3 bucket location.

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
    body = DescribeLocationS3Request.from_dict(body)
    return web.Response(status=200)


async def describe_location_smb(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_location_smb

    Returns metadata, such as the path and user information about an SMB location.

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
    body = DescribeLocationSmbRequest.from_dict(body)
    return web.Response(status=200)


async def describe_storage_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_storage_system

    Returns information about an on-premises storage system that you&#39;re using with DataSync Discovery.

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
    body = DescribeStorageSystemRequest.from_dict(body)
    return web.Response(status=200)


async def describe_storage_system_resource_metrics(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_storage_system_resource_metrics

    Returns information, including performance data and capacity usage, which DataSync Discovery collects about a specific resource in your-premises storage system.

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
    body = DescribeStorageSystemResourceMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_storage_system_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_storage_system_resources

    Returns information that DataSync Discovery collects about resources in your on-premises storage system.

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
    body = DescribeStorageSystemResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_task

    Provides information about an DataSync transfer task.

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
    body = DescribeTaskRequest.from_dict(body)
    return web.Response(status=200)


async def describe_task_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_task_execution

    Provides information about an DataSync transfer task that&#39;s running.

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
    body = DescribeTaskExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def generate_recommendations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """generate_recommendations

    &lt;p&gt;Creates recommendations about where to migrate your data to in Amazon Web Services. Recommendations are generated based on information that DataSync Discovery collects about your on-premises storage system&#39;s resources. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/discovery-understand-recommendations.html\&quot;&gt;Recommendations provided by DataSync Discovery&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Once generated, you can view your recommendations by using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResources.html\&quot;&gt;DescribeStorageSystemResources&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If your &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/discovery-job-statuses.html#discovery-job-statuses-table\&quot;&gt;discovery job completes successfully&lt;/a&gt;, you don&#39;t need to use this operation. DataSync Discovery generates the recommendations for you automatically.&lt;/p&gt; &lt;/note&gt;

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
    body = GenerateRecommendationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_agents(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_agents

    &lt;p&gt;Returns a list of DataSync agents that belong to an Amazon Web Services account in the Amazon Web Services Region specified in the request.&lt;/p&gt; &lt;p&gt;With pagination, you can reduce the number of agents returned in a response. If you get a truncated list of agents in a response, the response contains a marker that you can specify in your next request to fetch the next page of agents.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListAgents&lt;/code&gt; is eventually consistent. This means the result of running the operation might not reflect that you just created or deleted an agent. For example, if you create an agent with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateAgent.html\&quot;&gt;CreateAgent&lt;/a&gt; and then immediately run &lt;code&gt;ListAgents&lt;/code&gt;, that agent might not show up in the list right away. In situations like this, you can always confirm whether an agent has been created (or deleted) by using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeAgent.html\&quot;&gt;DescribeAgent&lt;/a&gt;.&lt;/p&gt;

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
    body = ListAgentsRequest.from_dict(body)
    return web.Response(status=200)


async def list_discovery_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_discovery_jobs

    Provides a list of the existing discovery jobs in the Amazon Web Services Region and Amazon Web Services account where you&#39;re using DataSync Discovery.

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
    body = ListDiscoveryJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_locations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_locations

    &lt;p&gt;Returns a list of source and destination locations.&lt;/p&gt; &lt;p&gt;If you have more locations than are returned in a response (that is, the response returns only a truncated list of your agents), the response contains a token that you can specify in your next request to fetch the next page of locations.&lt;/p&gt;

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
    body = ListLocationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_storage_systems(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_storage_systems

    Lists the on-premises storage systems that you&#39;re using with DataSync Discovery.

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
    body = ListStorageSystemsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    Returns all the tags associated with an Amazon Web Services resource.

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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_task_executions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_task_executions

    Returns a list of executed tasks.

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
    body = ListTaskExecutionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tasks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tasks

    Returns a list of the DataSync tasks you created.

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


async def remove_storage_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """remove_storage_system

    Permanently removes a storage system resource from DataSync Discovery, including the associated discovery jobs, collected data, and recommendations.

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
    body = RemoveStorageSystemRequest.from_dict(body)
    return web.Response(status=200)


async def start_discovery_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_discovery_job

    Runs a DataSync discovery job on your on-premises storage system. If you haven&#39;t added the storage system to DataSync Discovery yet, do this first by using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/API_AddStorageSystem.html\&quot;&gt;AddStorageSystem&lt;/a&gt; operation.

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
    body = StartDiscoveryJobRequest.from_dict(body)
    return web.Response(status=200)


async def start_task_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_task_execution

    &lt;p&gt;Starts an DataSync task. For each task, you can only run one task execution at a time.&lt;/p&gt; &lt;p&gt;There are several phases to a task execution. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/working-with-task-executions.html#understand-task-execution-statuses\&quot;&gt;Task execution statuses&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you&#39;re planning to transfer data to or from an Amazon S3 location, review &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#create-s3-location-s3-requests\&quot;&gt;how DataSync can affect your S3 request charges&lt;/a&gt; and the &lt;a href&#x3D;\&quot;http://aws.amazon.com/datasync/pricing/\&quot;&gt;DataSync pricing page&lt;/a&gt; before you begin.&lt;/p&gt; &lt;/important&gt;

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
    body = StartTaskExecutionRequest.from_dict(body)
    return web.Response(status=200)


async def stop_discovery_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_discovery_job

    &lt;p&gt;Stops a running DataSync discovery job.&lt;/p&gt; &lt;p&gt;You can stop a discovery job anytime. A job that&#39;s stopped before it&#39;s scheduled to end likely will provide you some information about your on-premises storage system resources. To get recommendations for a stopped job, you must use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/API_GenerateRecommendations.html\&quot;&gt;GenerateRecommendations&lt;/a&gt; operation.&lt;/p&gt;

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
    body = StopDiscoveryJobRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Applies a &lt;i&gt;tag&lt;/i&gt; to an Amazon Web Services resource. Tags are key-value pairs that can help you manage, filter, and search for your resources.&lt;/p&gt; &lt;p&gt;These include DataSync resources, such as locations, tasks, and task executions.&lt;/p&gt;

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

    Removes tags from an Amazon Web Services resource.

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


async def update_agent(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_agent

    Updates the name of an agent.

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
    body = UpdateAgentRequest.from_dict(body)
    return web.Response(status=200)


async def update_discovery_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_discovery_job

    Edits a DataSync discovery job configuration.

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
    body = UpdateDiscoveryJobRequest.from_dict(body)
    return web.Response(status=200)


async def update_location_azure_blob(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_location_azure_blob

    Modifies some configurations of the Microsoft Azure Blob Storage transfer location that you&#39;re using with DataSync.

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
    body = UpdateLocationAzureBlobRequest.from_dict(body)
    return web.Response(status=200)


async def update_location_hdfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_location_hdfs

    Updates some parameters of a previously created location for a Hadoop Distributed File System cluster.

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
    body = UpdateLocationHdfsRequest.from_dict(body)
    return web.Response(status=200)


async def update_location_nfs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_location_nfs

    &lt;p&gt;Modifies some configurations of the Network File System (NFS) transfer location that you&#39;re using with DataSync.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html\&quot;&gt;Configuring transfers to or from an NFS file server&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateLocationNfsRequest.from_dict(body)
    return web.Response(status=200)


async def update_location_object_storage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_location_object_storage

    Updates some parameters of an existing object storage location that DataSync accesses for a transfer. For information about creating a self-managed object storage location, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-object-location.html\&quot;&gt;Creating a location for object storage&lt;/a&gt;.

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
    body = UpdateLocationObjectStorageRequest.from_dict(body)
    return web.Response(status=200)


async def update_location_smb(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_location_smb

    Updates some of the parameters of a previously created location for Server Message Block (SMB) file system access. For information about creating an SMB location, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html\&quot;&gt;Creating a location for SMB&lt;/a&gt;.

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
    body = UpdateLocationSmbRequest.from_dict(body)
    return web.Response(status=200)


async def update_storage_system(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_storage_system

    Modifies some configurations of an on-premises storage system resource that you&#39;re using with DataSync Discovery.

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
    body = UpdateStorageSystemRequest.from_dict(body)
    return web.Response(status=200)


async def update_task(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_task

    Updates the metadata associated with a task.

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
    body = UpdateTaskRequest.from_dict(body)
    return web.Response(status=200)


async def update_task_execution(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_task_execution

    &lt;p&gt;Modifies a running DataSync task.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Currently, the only &lt;code&gt;Option&lt;/code&gt; that you can modify with &lt;code&gt;UpdateTaskExecution&lt;/code&gt; is &lt;code&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-BytesPerSecond\&quot;&gt;BytesPerSecond&lt;/a&gt; &lt;/code&gt;, which throttles bandwidth for a running or queued task.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateTaskExecutionRequest.from_dict(body)
    return web.Response(status=200)
