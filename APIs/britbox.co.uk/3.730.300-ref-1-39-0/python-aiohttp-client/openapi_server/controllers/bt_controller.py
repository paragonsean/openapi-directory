from typing import List, Dict
from aiohttp import web

from openapi_server.models.bt_plan_list_item import BtPlanListItem
from openapi_server.models.bt_plans import BtPlans
from openapi_server.models.ee_bt_eligibility import EeBtEligibility
from openapi_server.models.itv_assign_bt_token_request import ItvAssignBtTokenRequest
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def assign_token(request: web.Request, body, lang=None) -> web.Response:
    """assign_token

    Assigns an UserToken to a profile on the ITV side. Currently throws an exception.

    :param body: Details of an assign request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvAssignBtTokenRequest.from_dict(body)
    return web.Response(status=200)


async def check_ee_bt_eligibility_0(request: web.Request, lang=None) -> web.Response:
    """check_ee_bt_eligibility_0

    Check whether or not a user is eligible for switching to Bt or EE offers.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def check_user_token(request: web.Request, id, ff=None, lang=None) -> web.Response:
    """check_user_token

    Checks a provided token for BT eligible user. 

    :param id: User token provided by BT.
    :type id: str
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_plan_by_token(request: web.Request, token, lang=None) -> web.Response:
    """get_plan_by_token

    Returns all the plans available for BT flow including additional description data.

    :param token: The identifier of the user provided by BT in an initial URL.
    :type token: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_plans(request: web.Request, lang=None) -> web.Response:
    """get_plans

    Returns all the plans available for BT flow including additional description data.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)
