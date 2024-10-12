from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_application_cloud_watch_logging_option_request import AddApplicationCloudWatchLoggingOptionRequest
from openapi_server.models.add_application_input_processing_configuration_request import AddApplicationInputProcessingConfigurationRequest
from openapi_server.models.add_application_input_request import AddApplicationInputRequest
from openapi_server.models.add_application_output_request import AddApplicationOutputRequest
from openapi_server.models.add_application_reference_data_source_request import AddApplicationReferenceDataSourceRequest
from openapi_server.models.create_application_request import CreateApplicationRequest
from openapi_server.models.create_application_response import CreateApplicationResponse
from openapi_server.models.delete_application_cloud_watch_logging_option_request import DeleteApplicationCloudWatchLoggingOptionRequest
from openapi_server.models.delete_application_input_processing_configuration_request import DeleteApplicationInputProcessingConfigurationRequest
from openapi_server.models.delete_application_output_request import DeleteApplicationOutputRequest
from openapi_server.models.delete_application_reference_data_source_request import DeleteApplicationReferenceDataSourceRequest
from openapi_server.models.delete_application_request import DeleteApplicationRequest
from openapi_server.models.describe_application_request import DescribeApplicationRequest
from openapi_server.models.describe_application_response import DescribeApplicationResponse
from openapi_server.models.discover_input_schema_request import DiscoverInputSchemaRequest
from openapi_server.models.discover_input_schema_response import DiscoverInputSchemaResponse
from openapi_server.models.list_applications_request import ListApplicationsRequest
from openapi_server.models.list_applications_response import ListApplicationsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.start_application_request import StartApplicationRequest
from openapi_server.models.stop_application_request import StopApplicationRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_application_request import UpdateApplicationRequest
from openapi_server import util


async def add_application_cloud_watch_logging_option(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_application_cloud_watch_logging_option

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds a CloudWatch log stream to monitor application configuration errors. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html\&quot;&gt;Working with Amazon CloudWatch Logs&lt;/a&gt;.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; Adds a streaming source to your Amazon Kinesis application. For conceptual information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\&quot;&gt;Configuring Application Input&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;You can add a streaming source either when you create an application or you can use this operation to add a streaming source after you create an application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_CreateApplication.html\&quot;&gt;CreateApplication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation to find the current application version. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:AddApplicationInput&lt;/code&gt; action.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html\&quot;&gt;InputProcessingConfiguration&lt;/a&gt; to an application. An input processor preprocesses records on the input stream before the application&#39;s SQL code executes. Currently, the only input processor available is &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lambda/\&quot;&gt;AWS Lambda&lt;/a&gt;.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds an external destination to your Amazon Kinesis Analytics application.&lt;/p&gt; &lt;p&gt;If you want Amazon Kinesis Analytics to deliver data from an in-application stream within your application to an external destination (such as an Amazon Kinesis stream, an Amazon Kinesis Firehose delivery stream, or an AWS Lambda function), you add the relevant configuration to your application using this operation. You can configure one or more outputs for your application. Each output configuration maps an in-application stream and an external destination.&lt;/p&gt; &lt;p&gt; You can use one of the output configurations to deliver data from your in-application error stream to an external destination so that you can analyze the errors. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-output.html\&quot;&gt;Understanding Application Output (Destination)&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; Any configuration update, including adding a streaming source using this operation, results in a new version of the application. You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation to find the current application version.&lt;/p&gt; &lt;p&gt;For the limits on the number of application inputs and outputs you can configure, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html\&quot;&gt;Limits&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:AddApplicationOutput&lt;/code&gt; action.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Adds a reference data source to an existing application.&lt;/p&gt; &lt;p&gt;Amazon Kinesis Analytics reads reference data (that is, an Amazon S3 object) and creates an in-application table within your application. In the request, you provide the source (S3 bucket name and object key name), name of the in-application table to create, and the necessary mapping information that describes how data in Amazon S3 object maps to columns in the resulting in-application table.&lt;/p&gt; &lt;p&gt; For conceptual information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\&quot;&gt;Configuring Application Input&lt;/a&gt;. For the limits on data sources you can add to your application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/limits.html\&quot;&gt;Limits&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:AddApplicationOutput&lt;/code&gt; action. &lt;/p&gt;

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


async def create_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_application

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; Creates an Amazon Kinesis Analytics application. You can configure each application with one streaming source as input, application code to process the input, and up to three destinations where you want Amazon Kinesis Analytics to write the output data from your application. For an overview, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works.html\&quot;&gt;How it Works&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;In the input configuration, you map the streaming source to an in-application stream, which you can think of as a constantly updating table. In the mapping, you must provide a schema for the in-application stream and map each data column in the in-application stream to a data element in the streaming source.&lt;/p&gt; &lt;p&gt;Your application code is one or more SQL statements that read input data, transform it, and generate output. Your application code can create one or more SQL artifacts like SQL streams or pumps.&lt;/p&gt; &lt;p&gt;In the output configuration, you can configure the application to write data from in-application streams created in your applications to up to three destinations.&lt;/p&gt; &lt;p&gt; To read data from your source stream or write data to destination streams, Amazon Kinesis Analytics needs your permissions. You grant these permissions by creating IAM roles. This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:CreateApplication&lt;/code&gt; action. &lt;/p&gt; &lt;p&gt; For introductory exercises to create an Amazon Kinesis Analytics application, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/getting-started.html\&quot;&gt;Getting Started&lt;/a&gt;. &lt;/p&gt;

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


async def delete_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_application

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes the specified application. Amazon Kinesis Analytics halts application execution and deletes the application, including any application artifacts (such as in-application streams, reference table, and application code).&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DeleteApplication&lt;/code&gt; action.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes a CloudWatch log stream from an application. For more information about using CloudWatch log streams with Amazon Kinesis Analytics applications, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/cloudwatch-logs.html\&quot;&gt;Working with Amazon CloudWatch Logs&lt;/a&gt;.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes an &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_InputProcessingConfiguration.html\&quot;&gt;InputProcessingConfiguration&lt;/a&gt; from an input.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes output destination configuration from your application configuration. Amazon Kinesis Analytics will no longer write data from the corresponding in-application stream to the external output destination.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DeleteApplicationOutput&lt;/code&gt; action.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Deletes a reference data source configuration from the specified application configuration.&lt;/p&gt; &lt;p&gt;If the application is running, Amazon Kinesis Analytics immediately removes the in-application table that you created using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_AddApplicationReferenceDataSource.html\&quot;&gt;AddApplicationReferenceDataSource&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics.DeleteApplicationReferenceDataSource&lt;/code&gt; action.&lt;/p&gt;

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


async def describe_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_application

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns information about a specific Amazon Kinesis Analytics application.&lt;/p&gt; &lt;p&gt;If you want to retrieve a list of all applications in your account, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_ListApplications.html\&quot;&gt;ListApplications&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DescribeApplication&lt;/code&gt; action. You can use &lt;code&gt;DescribeApplication&lt;/code&gt; to get the current application versionId, which you need to call other operations such as &lt;code&gt;Update&lt;/code&gt;. &lt;/p&gt;

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


async def discover_input_schema(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """discover_input_schema

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Infers a schema by evaluating sample records on the specified streaming source (Amazon Kinesis stream or Amazon Kinesis Firehose delivery stream) or S3 object. In the response, the operation returns the inferred schema and also the sample records that the operation used to infer the schema.&lt;/p&gt; &lt;p&gt; You can use the inferred schema when configuring a streaming source for your application. For conceptual information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-it-works-input.html\&quot;&gt;Configuring Application Input&lt;/a&gt;. Note that when you create an application using the Amazon Kinesis Analytics console, the console uses this operation to infer a schema and show it in the console user interface. &lt;/p&gt; &lt;p&gt; This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:DiscoverInputSchema&lt;/code&gt; action. &lt;/p&gt;

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


async def list_applications(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_applications

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns a list of Amazon Kinesis Analytics applications in your account. For each application, the response includes the application name, Amazon Resource Name (ARN), and status. If the response returns the &lt;code&gt;HasMoreApplications&lt;/code&gt; value as true, you can send another request by adding the &lt;code&gt;ExclusiveStartApplicationName&lt;/code&gt; in the request body, and set the value of this to the last application name from the previous response. &lt;/p&gt; &lt;p&gt;If you want detailed information about a specific application, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:ListApplications&lt;/code&gt; action.&lt;/p&gt;

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

    Retrieves the list of key-value tags assigned to the application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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


async def start_application(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_application

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Starts the specified Amazon Kinesis Analytics application. After creating an application, you must exclusively call this operation to start your application.&lt;/p&gt; &lt;p&gt;After the application starts, it begins consuming the input data, processes it, and writes the output to the configured destination.&lt;/p&gt; &lt;p&gt; The application status must be &lt;code&gt;READY&lt;/code&gt; for you to start an application. You can get the application status in the console or using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;After you start the application, you can stop the application from processing the input by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_StopApplication.html\&quot;&gt;StopApplication&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:StartApplication&lt;/code&gt; action.&lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Stops the application from processing input data. You can stop an application only if it is in the running state. You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_DescribeApplication.html\&quot;&gt;DescribeApplication&lt;/a&gt; operation to find the application state. After the application is stopped, Amazon Kinesis Analytics stops reading data from the input, the application stops processing data, and there is no output written to the destination. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;kinesisanalytics:StopApplication&lt;/code&gt; action.&lt;/p&gt;

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

    Adds one or more key-value tags to a Kinesis Analytics application. Note that the maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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

    Removes one or more tags from a Kinesis Analytics application. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kinesisanalytics/latest/dev/how-tagging.html\&quot;&gt;Using Tagging&lt;/a&gt;.

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

    &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Updates an existing Amazon Kinesis Analytics application. Using this API, you can update application code, input configuration, and output configuration. &lt;/p&gt; &lt;p&gt;Note that Amazon Kinesis Analytics updates the &lt;code&gt;CurrentApplicationVersionId&lt;/code&gt; each time you update your application. &lt;/p&gt; &lt;p&gt;This operation requires permission for the &lt;code&gt;kinesisanalytics:UpdateApplication&lt;/code&gt; action.&lt;/p&gt;

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
