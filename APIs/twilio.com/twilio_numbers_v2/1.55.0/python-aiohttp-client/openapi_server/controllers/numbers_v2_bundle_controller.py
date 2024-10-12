from typing import List, Dict
from aiohttp import web

from openapi_server.models.bundle_enum_end_user_type import BundleEnumEndUserType
from openapi_server.models.bundle_enum_sort_by import BundleEnumSortBy
from openapi_server.models.bundle_enum_sort_direction import BundleEnumSortDirection
from openapi_server.models.bundle_enum_status import BundleEnumStatus
from openapi_server.models.list_bundle_response import ListBundleResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle import NumbersV2RegulatoryComplianceBundle
from openapi_server import util


async def create_bundle(request: web.Request, email, friendly_name, end_user_type=None, iso_country=None, number_type=None, regulation_sid=None, status_callback=None) -> web.Response:
    """create_bundle

    Create a new Bundle.

    :param email: The email address that will receive updates when the Bundle resource changes status.
    :type email: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param end_user_type: 
    :type end_user_type: str
    :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle&#39;s phone number country ownership request.
    :type iso_country: str
    :param number_type: The type of phone number of the Bundle&#39;s ownership request. Can be &#x60;local&#x60;, &#x60;mobile&#x60;, &#x60;national&#x60;, or &#x60;toll free&#x60;.
    :type number_type: str
    :param regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
    :type regulation_sid: str
    :param status_callback: The URL we call to inform your application of status changes.
    :type status_callback: str

    """
    return web.Response(status=200)


async def delete_bundle(request: web.Request, sid) -> web.Response:
    """delete_bundle

    Delete a specific Bundle.

    :param sid: The unique string that we created to identify the Bundle resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_bundle(request: web.Request, sid) -> web.Response:
    """fetch_bundle

    Fetch a specific Bundle instance.

    :param sid: The unique string that we created to identify the Bundle resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_bundle(request: web.Request, status=None, friendly_name=None, regulation_sid=None, iso_country=None, number_type=None, has_valid_until_date=None, sort_by=None, sort_direction=None, valid_until_date=None, valid_until_date2=None, valid_until_date3=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_bundle

    Retrieve a list of all Bundles for an account.

    :param status: The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details.
    :type status: str
    :param friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable characters.
    :type friendly_name: str
    :param regulation_sid: The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource.
    :type regulation_sid: str
    :param iso_country: The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle&#39;s phone number country ownership request.
    :type iso_country: str
    :param number_type: The type of phone number of the Bundle&#39;s ownership request. Can be &#x60;local&#x60;, &#x60;mobile&#x60;, &#x60;national&#x60;, or &#x60;tollfree&#x60;.
    :type number_type: str
    :param has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
    :type has_valid_until_date: bool
    :param sort_by: Can be &#x60;valid-until&#x60; or &#x60;date-updated&#x60;. Defaults to &#x60;date-created&#x60;.
    :type sort_by: str
    :param sort_direction: Default is &#x60;DESC&#x60;. Can be &#x60;ASC&#x60; or &#x60;DESC&#x60;.
    :type sort_direction: str
    :param valid_until_date: Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
    :type valid_until_date: str
    :param valid_until_date2: Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
    :type valid_until_date2: str
    :param valid_until_date3: Date to filter Bundles having their &#x60;valid_until_date&#x60; before or after the specified date. Can be &#x60;ValidUntilDate&gt;&#x3D;&#x60; or &#x60;ValidUntilDate&lt;&#x3D;&#x60;. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
    :type valid_until_date3: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    valid_until_date = util.deserialize_datetime(valid_until_date)
    valid_until_date2 = util.deserialize_datetime(valid_until_date2)
    valid_until_date3 = util.deserialize_datetime(valid_until_date3)
    return web.Response(status=200)


async def update_bundle(request: web.Request, sid, email=None, friendly_name=None, status=None, status_callback=None) -> web.Response:
    """update_bundle

    Updates a Bundle in an account.

    :param sid: The unique string that we created to identify the Bundle resource.
    :type sid: str
    :param email: The email address that will receive updates when the Bundle resource changes status.
    :type email: str
    :param friendly_name: The string that you assigned to describe the resource.
    :type friendly_name: str
    :param status: 
    :type status: str
    :param status_callback: The URL we call to inform your application of status changes.
    :type status_callback: str

    """
    return web.Response(status=200)
