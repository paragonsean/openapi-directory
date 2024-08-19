# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request import Request
from openapi_server.models.response import Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_batch_execute(client):
    """Test case for batch_execute

    Execute a batch of requests against the service. As shown in the Sample Request, the input is a dictionary with IDs as keys and request objects as values. Each request object specifies the HTTP method and the resource and, optionally, the content and a list of parent IDs. The list of parent IDs specifies which other requests must complete before the given request will be executed. The example first creates an element, then gets the element by the response's Location header, then creates an attribute for the element. Note that the resource can be an absolute URL or a JsonPath that references the response to the parent request. The batch's response is a dictionary uses keys corresponding those provided in the request, with response objects containing a status code, response headers, and the response body. A request can alternatively specify a request template in place of a resource. In this case, a single JsonPath may select multiple tokens, and a separate subrequest will be made from the template for each token. The responses of these subrequests will returned as the content of a single outer response.
    """
    batch = {"Parameters":["Parameters","Parameters"],"Content":"Content","Headers":{"key":"Headers"},"ParentIds":["ParentIds","ParentIds"],"RequestTemplate":{"Resource":"Resource"},"Resource":"Resource","Method":"GET"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/piwebapi/batch',
        headers=headers,
        json=batch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

