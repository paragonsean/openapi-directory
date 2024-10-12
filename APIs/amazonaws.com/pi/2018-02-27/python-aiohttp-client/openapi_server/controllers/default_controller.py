from typing import List, Dict
from aiohttp import web

from openapi_server.models.describe_dimension_keys_request import DescribeDimensionKeysRequest
from openapi_server.models.describe_dimension_keys_response import DescribeDimensionKeysResponse
from openapi_server.models.get_dimension_key_details_request import GetDimensionKeyDetailsRequest
from openapi_server.models.get_dimension_key_details_response import GetDimensionKeyDetailsResponse
from openapi_server.models.get_resource_metadata_request import GetResourceMetadataRequest
from openapi_server.models.get_resource_metadata_response import GetResourceMetadataResponse
from openapi_server.models.get_resource_metrics_request import GetResourceMetricsRequest
from openapi_server.models.get_resource_metrics_response import GetResourceMetricsResponse
from openapi_server.models.list_available_resource_dimensions_request import ListAvailableResourceDimensionsRequest
from openapi_server.models.list_available_resource_dimensions_response import ListAvailableResourceDimensionsResponse
from openapi_server.models.list_available_resource_metrics_request import ListAvailableResourceMetricsRequest
from openapi_server.models.list_available_resource_metrics_response import ListAvailableResourceMetricsResponse
from openapi_server import util


async def describe_dimension_keys(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_dimension_keys

    &lt;p&gt;For a specific time period, retrieve the top &lt;code&gt;N&lt;/code&gt; dimension keys for a metric. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.&lt;/p&gt; &lt;/note&gt;

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
    body = DescribeDimensionKeysRequest.from_dict(body)
    return web.Response(status=200)


async def get_dimension_key_details(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dimension_key_details

    Get the attributes of the specified dimension group for a DB instance or data source. For example, if you specify a SQL ID, &lt;code&gt;GetDimensionKeyDetails&lt;/code&gt; retrieves the full text of the dimension &lt;code&gt;db.sql.statement&lt;/code&gt; associated with this ID. This operation is useful because &lt;code&gt;GetResourceMetrics&lt;/code&gt; and &lt;code&gt;DescribeDimensionKeys&lt;/code&gt; don&#39;t support retrieval of large SQL statement text.

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
    body = GetDimensionKeyDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_resource_metadata

    Retrieve the metadata for different features. For example, the metadata might indicate that a feature is turned on or off on a specific DB instance. 

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
    body = GetResourceMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def get_resource_metrics(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """get_resource_metrics

    &lt;p&gt;Retrieve Performance Insights metrics for a set of data sources over a time period. You can provide specific dimension groups and dimensions, and provide aggregation and filtering criteria for each group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Each response element returns a maximum of 500 bytes. For larger elements, such as SQL statements, only the first 500 bytes are returned.&lt;/p&gt; &lt;/note&gt;

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
    body = GetResourceMetricsRequest.from_dict(body)
    return web.Response(status=200)


async def list_available_resource_dimensions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_available_resource_dimensions

    Retrieve the dimensions that can be queried for each specified metric type on a specified DB instance.

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
    body = ListAvailableResourceDimensionsRequest.from_dict(body)
    return web.Response(status=200)


async def list_available_resource_metrics(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_available_resource_metrics

    Retrieve metrics of the specified types that can be queried for a specified DB instance. 

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
    body = ListAvailableResourceMetricsRequest.from_dict(body)
    return web.Response(status=200)
