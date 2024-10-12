from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_endpoint_request import CreateEndpointRequest
from openapi_server.models.create_endpoint_result import CreateEndpointResult
from openapi_server.models.list_endpoints_result import ListEndpointsResult
from openapi_server.models.list_outposts_with_s3_result import ListOutpostsWithS3Result
from openapi_server.models.list_shared_endpoints_result import ListSharedEndpointsResult
from openapi_server import util


async def create_endpoint(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_endpoint

    &lt;p&gt;Creates an endpoint and associates it with the specified Outpost.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It can take up to 5 minutes for this action to finish.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html\&quot;&gt;DeleteEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html\&quot;&gt;ListEndpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def delete_endpoint(request: web.Request, endpoint_id, outpost_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_endpoint

    &lt;p&gt;Deletes an endpoint.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It can take up to 5 minutes for this action to finish.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html\&quot;&gt;ListEndpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param endpoint_id: The ID of the endpoint.
    :type endpoint_id: str
    :param outpost_id: The ID of the Outposts. 
    :type outpost_id: str
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


async def list_endpoints(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_endpoints

    &lt;p&gt;Lists endpoints associated with the specified Outpost. &lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html\&quot;&gt;DeleteEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    :param next_token: If a previous response from this operation included a &lt;code&gt;NextToken&lt;/code&gt; value, provide that value here to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of endpoints that will be returned in the response.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_outposts_with_s3(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_outposts_with_s3

    Lists the Outposts with S3 on Outposts capacity for your Amazon Web Services account. Includes S3 on Outposts that you have access to as the Outposts owner, or as a shared user from Resource Access Manager (RAM). 

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
    :param next_token: When you can get additional results from the &lt;code&gt;ListOutpostsWithS3&lt;/code&gt; call, a &lt;code&gt;NextToken&lt;/code&gt; parameter is returned in the output. You can then pass in a subsequent command to the &lt;code&gt;NextToken&lt;/code&gt; parameter to continue listing additional Outposts.
    :type next_token: str
    :param max_results: The maximum number of Outposts to return. The limit is 100.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_shared_endpoints(request: web.Request, outpost_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, max_results2=None, next_token2=None) -> web.Response:
    """list_shared_endpoints

    &lt;p&gt;Lists all endpoints associated with an Outpost that has been shared by Amazon Web Services Resource Access Manager (RAM).&lt;/p&gt; &lt;p&gt;Related actions include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html\&quot;&gt;CreateEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html\&quot;&gt;DeleteEndpoint&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param outpost_id: The ID of the Amazon Web Services Outpost.
    :type outpost_id: str
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
    :param next_token: If a previous response from this operation included a &lt;code&gt;NextToken&lt;/code&gt; value, you can provide that value here to retrieve the next page of results.
    :type next_token: str
    :param max_results: The maximum number of endpoints that will be returned in the response.
    :type max_results: int
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)
