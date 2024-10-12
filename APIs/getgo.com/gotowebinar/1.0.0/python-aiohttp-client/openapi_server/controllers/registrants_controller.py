from typing import List, Dict
from aiohttp import web

from openapi_server.models.registrant import Registrant
from openapi_server.models.registrant_created import RegistrantCreated
from openapi_server.models.registrant_detailed import RegistrantDetailed
from openapi_server.models.registrant_fields import RegistrantFields
from openapi_server.models.registration_fields import RegistrationFields
from openapi_server import util


async def create_registrant(request: web.Request, authorization, organizer_key, webinar_key, body, accept=None, resend_confirmation=None) -> web.Response:
    """Create registrant

    Register an attendee for a scheduled webinar. The response contains the registrantKey and join URL for the registrant. An email will be sent to the registrant unless the organizer turns off the confirmation email setting from the GoToWebinar website. Please note that you must provide all required fields including custom fields defined during the webinar creation. Use the API call &#39;Get registration fields&#39; to get a list of all fields, if they are required, and their possible values. At this time there are two versions of the &#39;Create Registrant&#39; call. The first version only accepts firstName, lastName, and email and ignores all other fields. If you have custom fields or want to capture additional information this version won&#39;t work for you. The second version allows you to pass all required and optional fields, including custom fields defined when creating the webinar. To use the second version you must pass the header value &#39;Accept: application/vnd.citrix.g2wapi-v1.1+json&#39; instead of &#39;Accept: application/json&#39;. Leaving this header out results in the first version of the API call.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param body: The registrant details. To get all possible values run the API call &#39;Get registration fields&#39; which is also part of this documentation.
    :type body: dict | bytes
    :param accept: Set to &#39;application/vnd.citrix.g2wapi-v1.1+json&#39; to make a registration using fields (custom or default) additional to the basic ones.
    :type accept: str
    :param resend_confirmation: Indicates whether the confirmation email should be resent when a registrant is re-registered. The default value is false.
    :type resend_confirmation: bool

    """
    body = RegistrantFields.from_dict(body)
    return web.Response(status=200)


async def delete_registrant(request: web.Request, authorization, organizer_key, webinar_key, registrant_key) -> web.Response:
    """Delete registrant

    Removes a webinar registrant from current registrations for the specified webinar. The webinar must be a scheduled, future webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_all_registrants_for_webinar(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get registrants

    Retrieve registration details for all registrants of a specific webinar. Registrant details will not include all fields captured when creating the registrant. To see all data, use the API call &#39;Get Registrant&#39;. Registrants can have one of the following states; &lt;br&gt;WAITING - registrant registered and is awaiting approval (where organizer has required approval), &lt;br&gt;APPROVED - registrant registered and is approved, and &lt;br&gt;DENIED - registrant registered and was denied.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def get_registrant(request: web.Request, authorization, organizer_key, webinar_key, registrant_key) -> web.Response:
    """Get registrant

    Retrieve registration details for a specific registrant.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param registrant_key: The key of the registrant
    :type registrant_key: int

    """
    return web.Response(status=200)


async def get_registration_fields(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get registration fields

    Retrieve required, optional registration, and custom questions for a specified webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)
