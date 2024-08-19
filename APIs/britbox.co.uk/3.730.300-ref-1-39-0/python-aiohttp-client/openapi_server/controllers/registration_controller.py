from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.registration_request import RegistrationRequest
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def register(request: web.Request, body, ff=None, lang=None) -> web.Response:
    """register

    Register a new user, creating them an account.  Registration, when successful, will return an array of access tokens so the user is immediately signed in.  It returns Catalog and Commerce scoped tokens for both Account and Profile. The Commerce ones are intended to allow the purchase of a subscription plan in the step after registration, without the user being prompted to enter their username and password again.  An email will also be sent with a link they need to click to confirm their email address. This confirmation is done via the /verify-email endpoint. 

    :param body: Registration details.
    :type body: dict | bytes
    :param ff: The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details. 
    :type ff: List[str]
    :param lang: Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    :type lang: str

    """
    body = RegistrationRequest.from_dict(body)
    return web.Response(status=200)
