from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_and_identity import ActivityAndIdentity
from openapi_server.models.custom_or_post_activity import CustomOrPostActivity
from openapi_server import util


async def workspace_slug_activities_get(request: web.Request, workspace_slug, affiliation=None, member_tags=None, orbit=None, activity_type=None, identity=None, company=None, title=None, regions=None, countries=None, cities=None, start_date=None, end_date=None, relative=None, page=None, direction=None, items=None, sort=None, type=None) -> web.Response:
    """List activities for a workspace

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param affiliation: 
    :type affiliation: str
    :param member_tags: The list of tags to filter against. Separate tags with &#x60;,&#x60; to do an intersection (AND), or with &#x60;|&#x60; to do a union (OR)
    :type member_tags: str
    :param orbit: The list of orbit levels to filter against. Accepted values are 1, 2, 3, 4, n. In the request, a format like &#x60;23&#x60; would include levels 2 and 3. &#x60;n&#x60; is for members with no orbit level.
    :type orbit: str
    :param activity_type: Comma separated list of activity types
    :type activity_type: str
    :param identity: 
    :type identity: str
    :param company: Comma separated list of companies. The union (OR) of companies is applied.
    :type company: str
    :param title: Comma separated list of job titles. The union (OR) of job titles is applied.
    :type title: str
    :param regions: Comma separated list of regions. The union (OR) of regions is applied.
    :type regions: str
    :param countries: Comma separated list of countries. The union (OR) of countries is applied.
    :type countries: str
    :param cities: Comma separated list of cities. The union (OR) of cities is applied.
    :type cities: str
    :param start_date: Filter activities after this date. Format: YYYY-MM-DD.
    :type start_date: str
    :param end_date: Filter activities before this date. Format: YYYY-MM-DD.
    :type end_date: str
    :param relative: Relative timeframes. Format: this_&lt;integer&gt;_&lt;period&gt;, with period in [days, weeks, months, years]. For example, this_30_days.
    :type relative: str
    :param page: 
    :type page: str
    :param direction: 
    :type direction: str
    :param items: 
    :type items: str
    :param sort: 
    :type sort: str
    :param type: Deprecated in favor of the activity_type parameter.
    :type type: str

    """
    return web.Response(status=200)


async def workspace_slug_activities_id_get(request: web.Request, workspace_slug, id) -> web.Response:
    """Get an activity in the workspace

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def workspace_slug_activities_post(request: web.Request, workspace_slug, body=None) -> web.Response:
    """Create a Custom or a Content activity for a new or existing member

    Use this method when you know an identity of the member (github, email, twitter, etc.) but not their Orbit ID. Pass fields in the member object to update the member in addition to creating the activity.

    :param workspace_slug: 
    :type workspace_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActivityAndIdentity.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_members_member_slug_activities_get(request: web.Request, workspace_slug, member_slug, page=None, direction=None, items=None, sort=None, activity_type=None, type=None) -> web.Response:
    """List activities for a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param page: 
    :type page: str
    :param direction: 
    :type direction: str
    :param items: 
    :type items: str
    :param sort: 
    :type sort: str
    :param activity_type: 
    :type activity_type: str
    :param type: Deprecated in favor of the activity_type parameter.
    :type type: str

    """
    return web.Response(status=200)


async def workspace_slug_members_member_slug_activities_id_delete(request: web.Request, workspace_slug, member_slug, id) -> web.Response:
    """Delete a post activity

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def workspace_slug_members_member_slug_activities_id_put(request: web.Request, workspace_slug, member_slug, id, body=None) -> web.Response:
    """Update a custom activity for a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Activity.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_members_member_slug_activities_post(request: web.Request, workspace_slug, member_slug, body=None) -> web.Response:
    """Create a Custom or a Content activity for a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomOrPostActivity.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_organizations_organization_id_activities_get(request: web.Request, workspace_slug, organization_id, page=None, direction=None, items=None, sort=None, activity_type=None) -> web.Response:
    """List member activities in an organization

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param organization_id: 
    :type organization_id: str
    :param page: 
    :type page: str
    :param direction: 
    :type direction: str
    :param items: 
    :type items: str
    :param sort: 
    :type sort: str
    :param activity_type: 
    :type activity_type: str

    """
    return web.Response(status=200)
