from typing import List, Dict
from aiohttp import web

from openapi_server.models.pricing_v2_trunking_number import PricingV2TrunkingNumber
from openapi_server.models.pricing_v2_voice_voice_number import PricingV2VoiceVoiceNumber
from openapi_server import util


async def fetch_trunking_number(request: web.Request, destination_number, origination_number=None) -> web.Response:
    """fetch_trunking_number

    Fetch pricing information for a specific destination and, optionally, origination phone number.

    :param destination_number: The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    :type destination_number: str
    :param origination_number: The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    :type origination_number: str

    """
    return web.Response(status=200)


async def fetch_voice_number(request: web.Request, destination_number, origination_number=None) -> web.Response:
    """fetch_voice_number

    Fetch pricing information for a specific destination and, optionally, origination phone number.

    :param destination_number: The destination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    :type destination_number: str
    :param origination_number: The origination phone number, in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, for which to fetch the origin-based voice pricing information. E.164 format consists of a + followed by the country code and subscriber number.
    :type origination_number: str

    """
    return web.Response(status=200)
