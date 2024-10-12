from typing import List, Dict
from aiohttp import web

from openapi_server.models.kyc_response import KycResponse
from openapi_server import util


async def get_kyc(request: web.Request, ) -> web.Response:
    """get_kyc

    &lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;This method was originally created to see which onboarding requirements were still pending for sellers being onboarded for eBay managed payments, but now that all seller accounts are onboarded globally, this method should now just returne an empty payload with a &lt;code&gt;204 No Content&lt;/code&gt; HTTP status code. &lt;/span&gt;


    """
    return web.Response(status=200)
