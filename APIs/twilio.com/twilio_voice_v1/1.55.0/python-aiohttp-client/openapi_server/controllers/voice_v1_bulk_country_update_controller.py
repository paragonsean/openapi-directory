from typing import List, Dict
from aiohttp import web

from openapi_server.models.voice_v1_dialing_permissions_dialing_permissions_country_bulk_update import VoiceV1DialingPermissionsDialingPermissionsCountryBulkUpdate
from openapi_server import util


async def create_dialing_permissions_country_bulk_update(request: web.Request, update_request) -> web.Response:
    """create_dialing_permissions_country_bulk_update

    Create a bulk update request to change voice dialing country permissions of one or more countries identified by the corresponding [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

    :param update_request: URL encoded JSON array of update objects. example : &#x60;[ { \\\&quot;iso_code\\\&quot;: \\\&quot;GB\\\&quot;, \\\&quot;low_risk_numbers_enabled\\\&quot;: \\\&quot;true\\\&quot;, \\\&quot;high_risk_special_numbers_enabled\\\&quot;:\\\&quot;true\\\&quot;, \\\&quot;high_risk_tollfraud_numbers_enabled\\\&quot;: \\\&quot;false\\\&quot; } ]&#x60;
    :type update_request: str

    """
    return web.Response(status=200)
