from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_authorization_contact_information import APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_authorization_contact_information import AuthorizationCodesSharedModelsAuthorizationContactInformation
from openapi_server import util


async def authorization_contact_information_get(request: web.Request, limit=None, offset=None, authorization_code=None, after_date=None, before_date=None, dealer_code=None) -> web.Response:
    """Get contact information for authorization codes.

    No Documentation Found.

    :param limit: Optional. The page limit.  If not specified, the default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset.  If not specified, the default page offset is 0.
    :type offset: int
    :param authorization_code: Optional. Search by authorization code.
    :type authorization_code: str
    :param after_date: Optional. Include only data for authorization codes created after a provided date.
    :type after_date: str
    :param before_date: Optional. Include only data for authorization codes created before a provided date.
    :type before_date: str
    :param dealer_code: Optional. Search by dealer code.
    :type dealer_code: str

    """
    after_date = util.deserialize_datetime(after_date)
    before_date = util.deserialize_datetime(before_date)
    return web.Response(status=200)


async def authorization_contact_information_post(request: web.Request, body) -> web.Response:
    """Add contact information for authorization code.

    No Documentation Found.

    :param body: A contact information.
    :type body: dict | bytes

    """
    body = AuthorizationCodesSharedModelsAuthorizationContactInformation.from_dict(body)
    return web.Response(status=200)
