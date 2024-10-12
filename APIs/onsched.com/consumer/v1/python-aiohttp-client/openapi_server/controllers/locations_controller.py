from typing import List, Dict
from aiohttp import web

from openapi_server.models.location_list_view_model import LocationListViewModel
from openapi_server.models.location_view_model import LocationViewModel
from openapi_server import util


async def consumer_v1_locations_get(request: web.Request, name=None, nearest_to=None, proximity=None, units=None, service_id=None, friendly_id=None, region_id=None, ignore_primary=None, offset=None, limit=None) -> web.Response:
    """List Locations

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business Locations&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and size. Default offset is 0, and limit is 20 and maximum is 100. Use the other query parameters to filter the results further. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

    :param name: Location name (full or partial)
    :type name: str
    :param nearest_to: Search by distance nearest Geocoords, City, Postal/Zip Code
    :type nearest_to: str
    :param proximity: Maximum distance to display
    :type proximity: int
    :param units: Distance either imperial(miles), metric(kilometers)
    :type units: str
    :param service_id: Locations that offer this service
    :type service_id: str
    :param friendly_id: Frienldy Id of location
    :type friendly_id: str
    :param region_id: Locations within a specific region
    :type region_id: str
    :param ignore_primary: Don&#39;t include the Primary Location
    :type ignore_primary: bool
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit, default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def consumer_v1_locations_id_get(request: web.Request, id) -> web.Response:
    """Get Location

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Location&lt;/b&gt; object. A valid business &lt;b&gt;location id&lt;/b&gt; is required. Find all location id&#39;s by using the &lt;i&gt;GET /consumer/v1/locations&lt;/i&gt; endpoint.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;IMPORTANT DEPRECATION NOTICE&lt;/b&gt;: The following online settings parameters were intended for internal use in our Portal application only. They will be deprecated on &lt;b&gt;OCTOBER 15, 2022&lt;/b&gt;. These fields are currently part of the &lt;b&gt;SETTINGS&lt;/b&gt; object in all location endpoints: &lt;b&gt;businessId, enabled, familyMembersEnabled, serviceLabel, resourceLabel, resourceAnyLabel, resourceSelection, liveMode, formFlow, availabilityForm, showServiceGroups, showOnSchedLogo, showBusinessLogo, disableAuthorization, hideNavBar, hideLocationNav, hideServiceGroupsNav, hideServicesNav, hideContinueBooking, returnToService, returnToAvailability, hideBreadCrumbNav.&lt;/b&gt; If you are using these fields, please adjust your code to handle the deprecation or let us know by submitting a ticket to: &lt;b&gt;&lt;i&gt;support@onsched.com&lt;/i&gt;&lt;/b&gt; as we do not want to interrupt your existing workflows.&lt;/p&gt;

    :param id: id of business location
    :type id: str

    """
    return web.Response(status=200)
