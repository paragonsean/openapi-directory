from typing import List, Dict
from aiohttp import web

from openapi_server.models.personalised_radio_batch_request import PersonalisedRadioBatchRequest
from openapi_server.models.personalised_radio_error_response import PersonalisedRadioErrorResponse
from openapi_server.models.personalised_radio_request import PersonalisedRadioRequest
from openapi_server.models.personalised_radio_response import PersonalisedRadioResponse
from openapi_server.models.personalised_radio_success_response import PersonalisedRadioSuccessResponse
from openapi_server import util


async def delete_personalised_radio_by_activity_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid) -> web.Response:
    """Favourite Episode or Clip

    Remove User favourite 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio favourite types: Clips or Episodes
    :type type: str
    :param pid: pid
    :type pid: str

    """
    return web.Response(status=200)


async def delete_personalised_radio_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid) -> web.Response:
    """Followed Brand or Series

    Remove &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio follows types: Brands or Series
    :type type: str
    :param pid: pid
    :type pid: str

    """
    return web.Response(status=200)


async def get_personalised_radio_by_activity_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid, show_all_activity=None) -> web.Response:
    """Favourite Episode or Clip

    Check to see if a single clip or episode entity is in a users favourites - determines UX of add button.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio favourite types: Clips or Episodes
    :type type: str
    :param pid: pid
    :type pid: str
    :param show_all_activity: Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39;
    :type show_all_activity: bool

    """
    return web.Response(status=200)


async def get_personalised_radio_favourites(request: web.Request, authorization, x_authentication_provider, x_api_key, offset=None, limit=None, sort=None, show_all_activity=None) -> web.Response:
    """Favourite Episodes and Clips

    List of favourited episodes and clips for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param sort: Sort order for Personalised Radio results
    :type sort: str
    :param show_all_activity: Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39;
    :type show_all_activity: bool

    """
    return web.Response(status=200)


async def get_personalised_radio_favourites_by_type(request: web.Request, authorization, x_authentication_provider, x_api_key, type, sort=None, show_all_activity=None, offset=None, limit=None) -> web.Response:
    """Favourite Episodes and Clips by Type

    List of followed &#39;clips&#39; or &#39;episode&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio favourite types: Clips or Episodes
    :type type: str
    :param sort: Sort order for Personalised Radio results
    :type sort: str
    :param show_all_activity: Include items which have been &#39;soft&#39; unfavourited in response. I.e items with UAS type of &#39;unfavourited&#39;
    :type show_all_activity: bool
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)


async def get_personalised_radio_follows(request: web.Request, authorization, x_authentication_provider, x_api_key, offset=None, limit=None, sort=None, show_all_activity=None) -> web.Response:
    """Followed Brands and Series

    List of favourited brands and series for a given user for iPlayer Radio.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param sort: Sort order for Personalised Radio results
    :type sort: str
    :param show_all_activity: Include items which have been &#39;soft&#39; unfollowed in response. I.e items with UAS type of &#39;unfollowed&#39;
    :type show_all_activity: bool

    """
    return web.Response(status=200)


async def get_personalised_radio_follows_by_type(request: web.Request, authorization, x_authentication_provider, x_api_key, type, sort=None, offset=None, limit=None, show_all_activity=None) -> web.Response:
    """Followed Brands or Series by Type

    List of followed &#39;brand&#39; or &#39;series&#39; items for a given iPlayer Radio user  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio follows types: Brands or Series
    :type type: str
    :param sort: Sort order for Personalised Radio results
    :type sort: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param show_all_activity: Include items which have been &#39;soft&#39; unfollowed in response. I.e items with UAS type of &#39;unfollowed&#39;
    :type show_all_activity: bool

    """
    return web.Response(status=200)


async def get_personalised_radio_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid) -> web.Response:
    """Followed Brand or Series

    Check to see if a single brand or series entity is in a users follows - determines UX of add button. 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio follows types: Brands or Series
    :type type: str
    :param pid: pid
    :type pid: str

    """
    return web.Response(status=200)


async def get_personalised_radio_plays(request: web.Request, authorization, x_authentication_provider, x_api_key, offset=None, limit=None, sort=None, show_all_activity=None) -> web.Response:
    """Played Episode or Clip

    Returns mixed episode and clip plays for a given BBC iPlayer radio user.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining data as a Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int
    :param sort: Sort order for Personalised Radio results
    :type sort: str
    :param show_all_activity: Include expired/unavailable items
    :type show_all_activity: bool

    """
    return web.Response(status=200)


async def post_personalised_radio_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body) -> web.Response:
    """Favourite Episodes and Clips

    Add User favourites  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action favourited or unfavourited
    :type body: list | bytes

    """
    body = [PersonalisedRadioBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def post_personalised_radio_by_activity_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid, body) -> web.Response:
    """Favourite Episode or Clip

    Add User favourite  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio favourite types: Clips or Episodes
    :type type: str
    :param pid: pid
    :type pid: str
    :param body: Action favourited or unfavourited
    :type body: dict | bytes

    """
    body = PersonalisedRadioRequest.from_dict(body)
    return web.Response(status=200)


async def post_personalised_radio_follows_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body) -> web.Response:
    """Followed Brands and Series

    Add &#39;brand&#39; or &#39;series&#39; items to a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action followed or unfollowed
    :type body: list | bytes

    """
    body = [PersonalisedRadioBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def post_personalised_radio_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid, body) -> web.Response:
    """Followed Brand or Series

    Add &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio follows types: Brands or Series
    :type type: str
    :param pid: pid
    :type pid: str
    :param body: Action followed or unfollowed
    :type body: dict | bytes

    """
    body = PersonalisedRadioRequest.from_dict(body)
    return web.Response(status=200)


async def put_personalised_radio_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body) -> web.Response:
    """Favourite Episodes and Clips

    Update user favourites  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action favourited or unfavourited
    :type body: list | bytes

    """
    body = [PersonalisedRadioBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def put_personalised_radio_by_activity_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid, body) -> web.Response:
    """Favourite Episode or Clip

    Update user favourite  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio favourite types: Clips or Episodes
    :type type: str
    :param pid: pid
    :type pid: str
    :param body: Action favourited or unfavourited
    :type body: dict | bytes

    """
    body = PersonalisedRadioRequest.from_dict(body)
    return web.Response(status=200)


async def put_personalised_radio_follows_batch(request: web.Request, authorization, x_authentication_provider, x_api_key, body) -> web.Response:
    """Followed Brands and Series

    Update &#39;brands&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param body: Action followed or unfollowed
    :type body: list | bytes

    """
    body = [PersonalisedRadioBatchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def put_personalised_radio_follows_by_type_by_id(request: web.Request, authorization, x_authentication_provider, x_api_key, type, pid, body) -> web.Response:
    """Followed Brand or Series

    Update &#39;brand&#39; or &#39;series&#39; items from a users iPlayer Radio follows  N.B. Any HTML tags submitted in metadata will be removed 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_authentication_provider: Authentication type
    :type x_authentication_provider: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param type: Supported Radio follows types: Brands or Series
    :type type: str
    :param pid: pid
    :type pid: str
    :param body: Action followed or unfollowed
    :type body: dict | bytes

    """
    body = PersonalisedRadioRequest.from_dict(body)
    return web.Response(status=200)
