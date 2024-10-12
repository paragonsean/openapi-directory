from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_cli_token_response import CreateCliTokenResponse
from openapi_server.models.create_environment_output import CreateEnvironmentOutput
from openapi_server.models.create_environment_request import CreateEnvironmentRequest
from openapi_server.models.create_web_login_token_response import CreateWebLoginTokenResponse
from openapi_server.models.get_environment_output import GetEnvironmentOutput
from openapi_server.models.list_environments_output import ListEnvironmentsOutput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.publish_metrics_request import PublishMetricsRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_environment_output import UpdateEnvironmentOutput
from openapi_server.models.update_environment_request import UpdateEnvironmentRequest
from openapi_server import util


async def create_cli_token(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cli_token

    Creates a CLI token for the Airflow CLI. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-cli.html\&quot;&gt;Creating an Apache Airflow CLI token&lt;/a&gt;.

    :param name: The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;.
    :type name: str
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


async def create_environment(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_environment

    Creates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

    :param name: The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;.
    :type name: str
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
    body = CreateEnvironmentRequest.from_dict(body)
    return web.Response(status=200)


async def create_web_login_token(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_web_login_token

    Creates a web login token for the Airflow Web UI. To learn more, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mwaa/latest/userguide/call-mwaa-apis-web.html\&quot;&gt;Creating an Apache Airflow web login token&lt;/a&gt;.

    :param name: The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;.
    :type name: str
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


async def delete_environment(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_environment

    Deletes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

    :param name: The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;.
    :type name: str
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


async def get_environment(request: web.Request, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_environment

    Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

    :param name: The name of the Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;.
    :type name: str
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


async def list_environments(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_environments

    Lists the Amazon Managed Workflows for Apache Airflow (MWAA) environments.

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
    :param max_results: The maximum number of results to retrieve per page. For example, &lt;code&gt;5&lt;/code&gt; environments per page.
    :type max_results: int
    :param next_token: Retrieves the next page of the results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the key-value tag pairs associated to the Amazon Managed Workflows for Apache Airflow (MWAA) environment. For example, &lt;code&gt;\&quot;Environment\&quot;: \&quot;Staging\&quot;&lt;/code&gt;. 

    :param resource_arn: The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, &lt;code&gt;arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment&lt;/code&gt;.
    :type resource_arn: str
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


async def publish_metrics(request: web.Request, environment_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """publish_metrics

     &lt;b&gt;Internal only&lt;/b&gt;. Publishes environment health metrics to Amazon CloudWatch.

    :param environment_name:  &lt;b&gt;Internal only&lt;/b&gt;. The name of the environment.
    :type environment_name: str
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
    body = PublishMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Associates key-value tag pairs to your Amazon Managed Workflows for Apache Airflow (MWAA) environment. 

    :param resource_arn: The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, &lt;code&gt;arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment&lt;/code&gt;.
    :type resource_arn: str
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


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes key-value tag pairs associated to your Amazon Managed Workflows for Apache Airflow (MWAA) environment. For example, &lt;code&gt;\&quot;Environment\&quot;: \&quot;Staging\&quot;&lt;/code&gt;.

    :param resource_arn: The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, &lt;code&gt;arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment&lt;/code&gt;.
    :type resource_arn: str
    :param tag_keys: The key-value tag pair you want to remove. For example, &lt;code&gt;\&quot;Environment\&quot;: \&quot;Staging\&quot;&lt;/code&gt;. 
    :type tag_keys: List[str]
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


async def update_environment(request: web.Request, name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_environment

    Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

    :param name: The name of your Amazon MWAA environment. For example, &lt;code&gt;MyMWAAEnvironment&lt;/code&gt;.
    :type name: str
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
    body = UpdateEnvironmentRequest.from_dict(body)
    return web.Response(status=200)
