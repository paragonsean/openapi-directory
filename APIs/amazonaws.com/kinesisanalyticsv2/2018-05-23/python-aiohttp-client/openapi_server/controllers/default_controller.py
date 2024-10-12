from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_application_cloud_watch_logging_option_request import AddApplicationCloudWatchLoggingOptionRequest
from openapi_server.models.add_application_cloud_watch_logging_option_response import AddApplicationCloudWatchLoggingOptionResponse
from openapi_server.models.add_application_input_processing_configuration_request import AddApplicationInputProcessingConfigurationRequest
from openapi_server.models.add_application_input_processing_configuration_response import AddApplicationInputProcessingConfigurationResponse
from openapi_server.models.add_application_input_request import AddApplicationInputRequest
from openapi_server.models.add_application_input_response import AddApplicationInputResponse
from openapi_server.models.add_application_output_request import AddApplicationOutputRequest
from openapi_server.models.add_application_output_response import AddApplicationOutputResponse
from openapi_server.models.add_application_reference_data_source_request import AddApplicationReferenceDataSourceRequest
from openapi_server.models.add_application_reference_data_source_response import AddApplicationReferenceDataSourceResponse
from openapi_server.models.add_application_vpc_configuration_request import AddApplicationVpcConfigurationRequest
from openapi_server.models.add_application_vpc_configuration_response import AddApplicationVpcConfigurationResponse
from openapi_server.models.create_application_presigned_url_request import CreateApplicationPresignedUrlRequest
from openapi_server.models.create_application_presigned_url_response import CreateApplicationPresignedUrlResponse
from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.create_application_response import CreateApplicationResponse
from openapi_server.models.create_application_snapshot_request import CreateApplicationSnapshotRequest
from openapi_server.models.delete_application_cloud_watch_logging_option_request import DeleteApplicationCloudWatchLoggingOptionRequest
from openapi_server.models.delete_application_cloud_watch_logging_option_response import DeleteApplicationCloudWatchLoggingOptionResponse
from openapi_server.models.delete_application_input_processing_configuration_request import DeleteApplicationInputProcessingConfigurationRequest
from openapi_server.models.delete_application_input_processing_configuration_response import DeleteApplicationInputProcessingConfigurationResponse
from openapi_server.models.delete_application_output_request import DeleteApplicationOutputRequest
from openapi_server.models.delete_application_output_response import DeleteApplicationOutputResponse
from openapi_server.models.delete_application_reference_data_source_request import DeleteApplicationReferenceDataSourceRequest
from openapi_server.models.delete_application_reference_data_source_response import DeleteApplicationReferenceDataSourceResponse
from openapi_server.models.delete_application_request import DeleteApplicationRequest
from openapi_server.models.delete_application_snapshot_request import DeleteApplicationSnapshotRequest
from openapi_server.models.delete_application_vpc_configuration_request import DeleteApplicationVpcConfigurationRequest
from openapi_server.models.delete_application_vpc_configuration_response import DeleteApplicationVpcConfigurationResponse
from openapi_server.models.describe_application_request import DescribeApplicationRequest
from openapi_server.models.describe_application_response import DescribeApplicationResponse
from openapi_server.models.describe_application_snapshot_request import DescribeApplicationSnapshotRequest
from openapi_server.models.describe_application_snapshot_response import DescribeApplicationSnapshotResponse
from openapi_server.models.describe_application_version_request import DescribeApplicationVersionRequest
from openapi_server.models.describe_application_version_response import DescribeApplicationVersionResponse
from openapi_server.models.discover_input_schema_request import DiscoverInputSchemaRequest
from openapi_server.models.discover_input_schema_response import DiscoverInputSchemaResponse
from openapi_server.models.list_application_snapshots_request import ListApplicationSnapshotsRequest
from openapi_server.models.list_application_snapshots_response import ListApplicationSnapshotsResponse
from openapi_server.models.list_application_versions_request import ListApplicationVersionsRequest
from openapi_server.models.list_application_versions_response import ListApplicationVersionsResponse
from openapi_server.models.list_applications_request import ListApplicationsRequest
from openapi_server.models.list_applications_response import ListApplicationsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.rollback_application_request import RollbackApplicationRequest
from openapi_server.models.rollback_application_response import RollbackApplicationResponse
from openapi_server.models.start_application_request import StartApplicationRequest
from openapi_server.models.stop_application_request import StopApplicationRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_application_maintenance_configuration_request import UpdateApplicationMaintenanceConfigurationRequest
from openapi_server.models.update_application_maintenance_configuration_response import UpdateApplicationMaintenanceConfigurationResponse
from openapi_server.models.update_application_request import UpdateApplicationRequest
from openapi_server.models.update_application_response import UpdateApplicationResponse
from openapi_server import util


async def add_application_cloud_watch_logging_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_application_cloud_watch_logging_option

    Adds an Amazon CloudWatch log stream to monitor application configuration errors.

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
    body = AddApplicationCloudWatchLoggingOptionRequest.from_dict(body)
    return web.Response(status=200)


async def add_application_input(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_application_input

    &lt;p&gt; Adds a streaming source to your SQL-based Kinesis Data Analytics application. &lt;/p&gt; &lt;p&gt;You can add a streaming source when you create an application, or you can use this operation to add a streaming source after you create an application. For more information, see &lt;a&gt;CreateApplication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a&gt;DescribeApplication&lt;/a&gt; operation to find the current application version. &lt;/p&gt;

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
    body = AddApplicationInputRequest.from_dict(body)
    return web.Response(status=200)


async def add_application_input_processing_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_application_input_processing_configuration

    Adds an &lt;a&gt;InputProcessingConfiguration&lt;/a&gt; to a SQL-based Kinesis Data Analytics application. An input processor pre-processes records on the input stream before the application&#39;s SQL code executes. Currently, the only input processor available is &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lambda/\&quot;&gt;Amazon Lambda&lt;/a&gt;.

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
    body = AddApplicationInputProcessingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def add_application_output(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_application_output

    &lt;p&gt;Adds an external destination to your SQL-based Kinesis Data Analytics application.&lt;/p&gt; &lt;p&gt;If you want Kinesis Data Analytics to deliver data from an in-application stream within your application to an external destination (such as an Kinesis data stream, a Kinesis Data Firehose delivery stream, or an Amazon Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.&lt;/p&gt; &lt;p&gt; You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. &lt;/p&gt; &lt;p&gt; Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a&gt;DescribeApplication&lt;/a&gt; operation to find the current application version.&lt;/p&gt;

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
    body = AddApplicationOutputRequest.from_dict(body)
    return web.Response(status=200)


async def add_application_reference_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_application_reference_data_source

    &lt;p&gt;Adds a reference data source to an existing SQL-based Kinesis Data Analytics application.&lt;/p&gt; &lt;p&gt;Kinesis Data Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in an Amazon S3 object maps to columns in the resulting in-application table.&lt;/p&gt;

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
    body = AddApplicationReferenceDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def add_application_vpc_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_application_vpc_configuration

    &lt;p&gt;Adds a Virtual Private Cloud (VPC) configuration to the application. Applications can use VPCs to store and access resources securely.&lt;/p&gt; &lt;p&gt;Note the following about VPC configurations for Kinesis Data Analytics applications:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;VPC configurations are not supported for SQL applications.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When a VPC is added to a Kinesis Data Analytics application, the application can no longer be accessed from the Internet directly. To enable Internet access to the application, add an Internet gateway to your VPC.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = AddApplicationVpcConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def create_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application

    Creates a Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html\&quot;&gt;Creating an Application&lt;/a&gt;.

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


async def create_application_presigned_url(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application_presigned_url

    &lt;p&gt;Creates and returns a URL that you can use to connect to an application&#39;s extension.&lt;/p&gt; &lt;p&gt;The IAM role or user used to call this API defines the permissions to access the extension. After the presigned URL is created, no additional permission is required to access this URL. IAM authorization policies for this API are also enforced for every HTTP request that attempts to connect to the extension. &lt;/p&gt; &lt;p&gt;You control the amount of time that the URL will be valid using the &lt;code&gt;SessionExpirationDurationInSeconds&lt;/code&gt; parameter. If you do not provide this parameter, the returned URL is valid for twelve hours.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The URL that you get from a call to CreateApplicationPresignedUrl must be used within 3 minutes to be valid. If you first try to use the URL after the 3-minute limit expires, the service returns an HTTP 403 Forbidden error.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateApplicationPresignedUrlRequest.from_dict(body)
    return web.Response(status=200)


async def create_application_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application_snapshot

    Creates a snapshot of the application&#39;s state data.

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
    body = CreateApplicationSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application

    Deletes the specified application. Kinesis Data Analytics halts application execution and deletes the application.

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
    body = DeleteApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application_cloud_watch_logging_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application_cloud_watch_logging_option

    Deletes an Amazon CloudWatch log stream from an Kinesis Data Analytics application. 

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
    body = DeleteApplicationCloudWatchLoggingOptionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application_input_processing_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application_input_processing_configuration

    Deletes an &lt;a&gt;InputProcessingConfiguration&lt;/a&gt; from an input.

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
    body = DeleteApplicationInputProcessingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application_output(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application_output

    Deletes the output destination configuration from your SQL-based Kinesis Data Analytics application&#39;s configuration. Kinesis Data Analytics will no longer write data from the corresponding in-application stream to the external output destination.

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
    body = DeleteApplicationOutputRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application_reference_data_source(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application_reference_data_source

    &lt;p&gt;Deletes a reference data source configuration from the specified SQL-based Kinesis Data Analytics application&#39;s configuration.&lt;/p&gt; &lt;p&gt;If the application is running, Kinesis Data Analytics immediately removes the in-application table that you created using the &lt;a&gt;AddApplicationReferenceDataSource&lt;/a&gt; operation. &lt;/p&gt;

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
    body = DeleteApplicationReferenceDataSourceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application_snapshot

    Deletes a snapshot of application state.

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
    body = DeleteApplicationSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def delete_application_vpc_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application_vpc_configuration

    Removes a VPC configuration from a Kinesis Data Analytics application.

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
    body = DeleteApplicationVpcConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_application

    &lt;p&gt;Returns information about a specific Kinesis Data Analytics application.&lt;/p&gt; &lt;p&gt;If you want to retrieve a list of all applications in your account, use the &lt;a&gt;ListApplications&lt;/a&gt; operation.&lt;/p&gt;

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
    body = DescribeApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_application_snapshot(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_application_snapshot

    Returns information about a snapshot of application state data.

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
    body = DescribeApplicationSnapshotRequest.from_dict(body)
    return web.Response(status=200)


async def describe_application_version(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_application_version

    &lt;p&gt;Provides a detailed description of a specified version of the application. To see a list of all the versions of an application, invoke the &lt;a&gt;ListApplicationVersions&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is supported only for Amazon Kinesis Data Analytics for Apache Flink.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeApplicationVersionRequest.from_dict(body)
    return web.Response(status=200)


async def discover_input_schema(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """discover_input_schema

    &lt;p&gt;Infers a schema for a SQL-based Kinesis Data Analytics application by evaluating sample records on the specified streaming source (Kinesis data stream or Kinesis Data Firehose delivery stream) or Amazon S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.&lt;/p&gt; &lt;p&gt; You can use the inferred schema when configuring a streaming source for your application. When you create an application using the Kinesis Data Analytics console, the console uses this operation to infer a schema and show it in the console user interface. &lt;/p&gt;

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
    body = DiscoverInputSchemaRequest.from_dict(body)
    return web.Response(status=200)


async def list_application_snapshots(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_application_snapshots

    Lists information about the current application snapshots.

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
    body = ListApplicationSnapshotsRequest.from_dict(body)
    return web.Response(status=200)


async def list_application_versions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_application_versions

    &lt;p&gt;Lists all the versions for the specified application, including versions that were rolled back. The response also includes a summary of the configuration associated with each version.&lt;/p&gt; &lt;p&gt;To get the complete description of a specific application version, invoke the &lt;a&gt;DescribeApplicationVersion&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is supported only for Amazon Kinesis Data Analytics for Apache Flink.&lt;/p&gt; &lt;/note&gt;

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
    body = ListApplicationVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_applications(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_applications

    &lt;p&gt;Returns a list of Kinesis Data Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. &lt;/p&gt; &lt;p&gt;If you want detailed information about a specific application, use &lt;a&gt;DescribeApplication&lt;/a&gt;.&lt;/p&gt;

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
    body = ListApplicationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Retrieves the list of key-value tags assigned to the application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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


async def rollback_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """rollback_application

    &lt;p&gt;Reverts the application to the previous running version. You can roll back an application if you suspect it is stuck in a transient status. &lt;/p&gt; &lt;p&gt;You can roll back an application only if it is in the &lt;code&gt;UPDATING&lt;/code&gt; or &lt;code&gt;AUTOSCALING&lt;/code&gt; status.&lt;/p&gt; &lt;p&gt;When you rollback an application, it loads state data from the last successful snapshot. If the application has no snapshots, Kinesis Data Analytics rejects the rollback request.&lt;/p&gt; &lt;p&gt;This action is not supported for Kinesis Data Analytics for SQL applications.&lt;/p&gt;

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
    body = RollbackApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def start_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_application

    Starts the specified Kinesis Data Analytics application. After creating an application, you must exclusively call this operation to start your application.

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
    body = StartApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def stop_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """stop_application

    &lt;p&gt;Stops the application from processing data. You can stop an application only if it is in the running status, unless you set the &lt;code&gt;Force&lt;/code&gt; parameter to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can use the &lt;a&gt;DescribeApplication&lt;/a&gt; operation to find the application status. &lt;/p&gt; &lt;p&gt;Kinesis Data Analytics takes a snapshot when the application is stopped, unless &lt;code&gt;Force&lt;/code&gt; is set to &lt;code&gt;true&lt;/code&gt;.&lt;/p&gt;

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
    body = StopApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds one or more key-value tags to a Kinesis Data Analytics application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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

    Removes one or more tags from a Kinesis Data Analytics application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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


async def update_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_application

    &lt;p&gt;Updates an existing Kinesis Data Analytics application. Using this operation, you can update application code, input configuration, and output configuration. &lt;/p&gt; &lt;p&gt;Kinesis Data Analytics updates the &lt;code&gt;ApplicationVersionId&lt;/code&gt; each time you update your application. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You cannot update the &lt;code&gt;RuntimeEnvironment&lt;/code&gt; of an existing application. If you need to update an application&#39;s &lt;code&gt;RuntimeEnvironment&lt;/code&gt;, you must delete the application and create it again.&lt;/p&gt; &lt;/note&gt;

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


async def update_application_maintenance_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_application_maintenance_configuration

    &lt;p&gt;Updates the maintenance configuration of the Kinesis Data Analytics application. &lt;/p&gt; &lt;p&gt;You can invoke this operation on an application that is in one of the two following states: &lt;code&gt;READY&lt;/code&gt; or &lt;code&gt;RUNNING&lt;/code&gt;. If you invoke it when the application is in a state other than these two states, it throws a &lt;code&gt;ResourceInUseException&lt;/code&gt;. The service makes use of the updated configuration the next time it schedules maintenance for the application. If you invoke this operation after the service schedules maintenance, the service will apply the configuration update the next time it schedules maintenance for the application. This means that you might not see the maintenance configuration update applied to the maintenance process that follows a successful invocation of this operation, but to the following maintenance process instead.&lt;/p&gt; &lt;p&gt;To see the current maintenance configuration of your application, invoke the &lt;a&gt;DescribeApplication&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;For information about application maintenance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/java/maintenance.html\&quot;&gt;Kinesis Data Analytics for Apache Flink Maintenance&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is supported only for Amazon Kinesis Data Analytics for Apache Flink.&lt;/p&gt; &lt;/note&gt;

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
    body = UpdateApplicationMaintenanceConfigurationRequest.from_dict(body)
    return web.Response(status=200)
