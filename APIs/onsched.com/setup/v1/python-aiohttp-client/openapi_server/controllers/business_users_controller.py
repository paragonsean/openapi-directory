from typing import List, Dict
from aiohttp import web

from openapi_server.models.authorized_company_list_view_model import AuthorizedCompanyListViewModel
from openapi_server.models.business_permission_list_view_model import BusinessPermissionListViewModel
from openapi_server.models.business_user_input_model import BusinessUserInputModel
from openapi_server.models.business_user_list_view_model import BusinessUserListViewModel
from openapi_server.models.business_user_update_model import BusinessUserUpdateModel
from openapi_server.models.business_user_view_model import BusinessUserViewModel
from openapi_server import util


async def setup_v1_businessusers_email_companies_get(request: web.Request, email, search_text=None, offset=None, limit=None) -> web.Response:
    """List User Companies

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Companies&lt;/b&gt; associated with the business users email requested. A business user &lt;b&gt;email&lt;/b&gt; address is required. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param email: Email of business user
    :type email: str
    :param search_text: All or partial company name
    :type search_text: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_businessusers_get(request: web.Request, location_id=None, email=None, role=None, offset=None, limit=None) -> web.Response:
    """List Users

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business Users and their Roles&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param email: Filter by email address
    :type email: str
    :param role: Filter user role
    :type role: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_businessusers_id_delete(request: web.Request, id) -> web.Response:
    """Delete User

    &lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Business User. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_businessusers_id_get(request: web.Request, id) -> web.Response:
    """Get User

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Business User&lt;/b&gt; object. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required. Find businessUser id&#39;s using the &lt;i&gt;GET /setup/v1/businessusers&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of businessUser object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_businessusers_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update User

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Business User. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Business Roles Include: bizowner&lt;/b&gt; (Business Owner), &lt;b&gt;bizadmin&lt;/b&gt; (Business Administrator), &lt;b&gt;bizresource&lt;/b&gt; (Business User - Bookable Resource).&lt;/p&gt;

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BusinessUserUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_businessusers_permissions_get(request: web.Request, role=None, offset=None, limit=None) -> web.Response:
    """List User Permissions

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business User Permissions by Role&lt;/b&gt;. Results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param role: Filter permissions by role
    :type role: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_businessusers_post(request: web.Request, body=None) -> web.Response:
    """Create User

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Business User. If not specified, the business location defaults to the primary business location. &lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;Name&lt;/b&gt;, &lt;b&gt;Email&lt;/b&gt; and &lt;b&gt;Role&lt;/b&gt;&lt;b&gt;Note:&lt;/b&gt; If the businessUser is a bookable resource (bizresource) then a resourceId is required.&lt;/p&gt;  &lt;p&gt;For role, use one of the values listed. &lt;b&gt;Business Roles Include: bizowner&lt;/b&gt; (Business Owner), &lt;b&gt;bizadmin&lt;/b&gt; (Business Administrator), &lt;b&gt;bizresource&lt;/b&gt; (Business User - Bookable Resource).&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;sendRegistrationInvite&lt;/b&gt; parameter is available to API consumers for their own use. It provides no added functionality in OnSched.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = BusinessUserInputModel.from_dict(body)
    return web.Response(status=200)
