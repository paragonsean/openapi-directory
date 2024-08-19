from typing import List, Dict
from aiohttp import web

from openapi_server.models.ee_bt_eligibility import EeBtEligibility
from openapi_server.models.ee_create_pin_request import EeCreatePinRequest
from openapi_server.models.ee_create_pin_response import EeCreatePinResponse
from openapi_server.models.ee_create_token_response import EeCreateTokenResponse
from openapi_server.models.ee_offers_request import EeOffersRequest
from openapi_server.models.ee_offers_response import EeOffersResponse
from openapi_server.models.ee_plan_list_item import EePlanListItem
from openapi_server.models.ee_plans import EePlans
from openapi_server.models.ee_validate_pin_request import EeValidatePinRequest
from openapi_server.models.ee_validate_pin_response import EeValidatePinResponse
from openapi_server.models.itv_assign_msisdn_request import ItvAssignMsisdnRequest
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def assign_msisdn(request: web.Request, body, lang=None) -> web.Response:
    """assign_msisdn

    Assigns a msisdn to a profile on ITV side.

    :param body: Details of an assign request.
    :type body: dict | bytes
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = ItvAssignMsisdnRequest.from_dict(body)
    return web.Response(status=200)


async def check_ee_bt_eligibility(request: web.Request, lang=None) -> web.Response:
    """check_ee_bt_eligibility

    Check whether or not a user is eligible for switching to Bt or EE offers.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def create_pin_request(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """create_pin_request

    Creates a PIN request that will send an SMS to the given msisdn. This call is to validate MSISDN entered by a user not comming through EE network. This call should be followed by POST ee/pin. 

    :param body: Data for creating the PIN request.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = EeCreatePinRequest.from_dict(body)
    return web.Response(status=200)


async def create_token(request: web.Request, ) -> web.Response:
    """create_token

    Returns a token for later calls to EE API. TTL is one hour. Recommended is FE refreshes this token before each call.


    """
    return web.Response(status=200)


async def ee_plans_get(request: web.Request, lang=None) -> web.Response:
    """ee_plans_get

    Returns all the plans available for EE flow including additional description data.

    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def get_eligible_offers(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """get_eligible_offers

    Returns eligible partner specific offers for the querying partner for an EE MSISDN. This call is supposed to be called after we have MSISDN accired. This call should be followed by POST /ee/msisdn. 

    :param body: Data for getting the eligible offers.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = EeOffersRequest.from_dict(body)
    return web.Response(status=200)


async def get_plan(request: web.Request, id, lang=None) -> web.Response:
    """get_plan

    Returns the plan description for EE flow including additional description data.

    :param id: The identifier of the plan received from ee/offers.
    :type id: str
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    return web.Response(status=200)


async def validate_pin_request(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """validate_pin_request

    Validate PIN request created by calling POST /ee/pin This call is to validate MSISDN entered by a user not comming through EE network. This call should be called after PUT /ee/pin. This call should be followed by POST /ee/offers.

    :param body: Data for validating PIN.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = EeValidatePinRequest.from_dict(body)
    return web.Response(status=200)
