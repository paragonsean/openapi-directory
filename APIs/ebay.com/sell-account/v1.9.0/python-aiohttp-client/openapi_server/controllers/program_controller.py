from typing import List, Dict
from aiohttp import web

from openapi_server.models.program import Program
from openapi_server.models.programs import Programs
from openapi_server import util


async def get_opted_in_programs(request: web.Request, ) -> web.Response:
    """get_opted_in_programs

    This method gets a list of the seller programs that the seller has opted-in to.


    """
    return web.Response(status=200)


async def opt_in_to_program(request: web.Request, body) -> web.Response:
    """opt_in_to_program

    This method opts the seller in to an eBay seller program. Refer to the &lt;a href&#x3D;\&quot;/api-docs/sell/account/overview.html#opt-in\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Account API overview&lt;/a&gt; for information about available eBay seller programs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; It can take up to 24-hours for eBay to process your request to opt-in to a Seller Program. Use the &lt;a href&#x3D;\&quot;/api-docs/sell/account/resources/program/methods/getOptedInPrograms\&quot; target&#x3D;\&quot;_blank\&quot;&gt;getOptedInPrograms&lt;/a&gt; call to check the status of your request after the processing period has passed.&lt;/span&gt;

    :param body: Program being opted-in to.
    :type body: dict | bytes

    """
    body = Program.from_dict(body)
    return web.Response(status=200)


async def opt_out_of_program(request: web.Request, body) -> web.Response:
    """opt_out_of_program

    This method opts the seller out of a seller program to which you have previously opted-in to. Get a list of the seller programs you have opted-in to using the &lt;b&gt;getOptedInPrograms&lt;/b&gt; call.

    :param body: Program being opted-out of.
    :type body: dict | bytes

    """
    body = Program.from_dict(body)
    return web.Response(status=200)
