from typing import List, Dict
from aiohttp import web

from openapi_server.models.identity import Identity
from openapi_server.models.member import Member
from openapi_server.models.member_and_identity import MemberAndIdentity
from openapi_server import util


async def workspace_slug_members_find_get(request: web.Request, workspace_slug, source=None, source_host=None, uid=None, username=None, email=None, github=None) -> web.Response:
    """Find a member by an identity

    Provide a source and one of username/uid/email params to return a member with that identity, if one exists. Common values for source include github, twitter, and email.

    :param workspace_slug: 
    :type workspace_slug: str
    :param source: 
    :type source: str
    :param source_host: 
    :type source_host: str
    :param uid: 
    :type uid: str
    :param username: 
    :type username: str
    :param email: 
    :type email: str
    :param github: Deprecated, please use source&#x3D;github and username&#x3D;&lt;username&gt; instead
    :type github: str

    """
    return web.Response(status=200)


async def workspace_slug_members_get(request: web.Request, workspace_slug, affiliation=None, member_tags=None, orbit=None, activity_type=None, identity=None, company=None, title=None, regions=None, countries=None, cities=None, start_date=None, end_date=None, relative=None, query=None, page=None, direction=None, items=None, activities_count_min=None, activities_count_max=None, sort=None, type=None) -> web.Response:
    """List members in a workspace

    

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
    :param query: 
    :type query: str
    :param page: 
    :type page: str
    :param direction: 
    :type direction: str
    :param items: 
    :type items: str
    :param activities_count_min: 
    :type activities_count_min: str
    :param activities_count_max: 
    :type activities_count_max: str
    :param sort: 
    :type sort: str
    :param type: Deprecated in favor of the activity_type parameter.
    :type type: str

    """
    return web.Response(status=200)


async def workspace_slug_members_member_slug_delete(request: web.Request, workspace_slug, member_slug) -> web.Response:
    """Delete a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str

    """
    return web.Response(status=200)


async def workspace_slug_members_member_slug_get(request: web.Request, workspace_slug, member_slug) -> web.Response:
    """Get a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str

    """
    return web.Response(status=200)


async def workspace_slug_members_member_slug_identities_delete(request: web.Request, workspace_slug, member_slug, body=None) -> web.Response:
    """Remove identity from a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = Identity.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_members_member_slug_identities_post(request: web.Request, workspace_slug, member_slug, body=None) -> web.Response:
    """Add identity to a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = Identity.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_members_member_slug_put(request: web.Request, workspace_slug, member_slug, body=None) -> web.Response:
    """Update a member

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param member_slug: 
    :type member_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = Member.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_members_post(request: web.Request, workspace_slug, body=None) -> web.Response:
    """Create or update a member

    This method is useful when you know a member&#39;s identity in another system and want to create or update the corresponding Orbit member. Identities can be specified in the identity object or member attributes like member.github. If no member exists, a new member will be created and linked to any provided identities.

    :param workspace_slug: 
    :type workspace_slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = MemberAndIdentity.from_dict(body)
    return web.Response(status=200)


async def workspace_slug_organizations_organization_id_members_get(request: web.Request, workspace_slug, organization_id, page=None, items=None) -> web.Response:
    """List members in an organization

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param organization_id: 
    :type organization_id: str
    :param page: 
    :type page: str
    :param items: 
    :type items: str

    """
    return web.Response(status=200)
