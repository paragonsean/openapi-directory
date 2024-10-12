from typing import List, Dict
from aiohttp import web

from openapi_server.models.pricing_v1_voice_voice_number import PricingV1VoiceVoiceNumber
from openapi_server import util


async def fetch_voice_number(request: web.Request, number) -> web.Response:
    """fetch_voice_number

    

    :param number: The phone number to fetch.
    :type number: str

    """
    return web.Response(status=200)
