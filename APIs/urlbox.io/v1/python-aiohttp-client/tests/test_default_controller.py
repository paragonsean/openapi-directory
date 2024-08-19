# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.redirect_response import RedirectResponse
from openapi_server.models.render_request import RenderRequest
from openapi_server.models.render_response import RenderResponse


pytestmark = pytest.mark.asyncio

async def test_render_sync(client):
    """Test case for render_sync

    Render a URL as an image or video
    """
    body = {"metadata":True,"click_accept":True,"hide_cookie_banners":True,"thumb_width":1,"thumb_height":6,"format":"png","gpu":True,"url":"url","delay":"delay","wait_until":"requestsfinished","retina":True,"full_page":True,"wait_to_leave":"wait_to_leave","width":5,"html":"html","selector":"selector","block_ads":True,"wait_for":"wait_for","height":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/render/sync',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

