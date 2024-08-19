from typing import List, Dict
from aiohttp import web

from openapi_server.models.ownership import Ownership
from openapi_server.models.ownership_pages import OwnershipPages
from openapi_server import util


async def ownership_get(request: web.Request, query=None, sort=None, page_number=None, limit=None) -> web.Response:
    """Returns a paginated list of app licenses

     - Results are returned for the market provided within the basic authentication credentials 

    :param query: A query document. Example: {&#39;userId&#39;:&#39;12&#39;} matches all the ownership records that have the userId &#39;12&#39;.
    :type query: str
    :param sort: A sort document. Example: {&#39;date&#39;:1} sorts the results by date in ascending order
    :type sort: str
    :param page_number: The result set page number to be returned
    :type page_number: int
    :param limit: The maximum number of results to return per page
    :type limit: int

    """
    return web.Response(status=200)


async def ownership_install_post(request: web.Request, app_id, user_id, model_id=None, model=None, custom_data=None) -> web.Response:
    """Aquires an app license for a user (installs app)

     - This method is called on behalf of a user - This method requires either a modelId from the app or a custom model - User data and statistics are recorded when this method is called 

    :param app_id: The id of the App being owned
    :type app_id: str
    :param user_id: The id of the User requesting to own the App
    :type user_id: str
    :param model_id: The id of the model associated with this ownership request
    :type model_id: str
    :param model: A custom model that will override the app&#39;s default model for this install
    :type model: str
    :param custom_data: A custom JSON object to attach to this ownership record
    :type custom_data: str

    """
    return web.Response(status=200)


async def ownership_ownership_id_get(request: web.Request, ownership_id) -> web.Response:
    """Returns an ownership record

     - Results are returned for the market provided within the basic authentication credentials 

    :param ownership_id: The id belonging to the ownership record
    :type ownership_id: str

    """
    return web.Response(status=200)


async def ownership_ownership_id_patch(request: web.Request, ownership_id, custom_data=None, expires=None) -> web.Response:
    """Updates ownership fields

     - Results are returned for the market provided within the basic authentication credentials 

    :param ownership_id: The id of the ownership to be updated
    :type ownership_id: str
    :param custom_data: Custom JSON object that will be attached to this ownership record
    :type custom_data: str
    :param expires: The date (in millis) of when this app ownership expires
    :type expires: int

    """
    return web.Response(status=200)


async def ownership_ownership_id_post(request: web.Request, ownership_id, custom_data=None, expires=None) -> web.Response:
    """Updates an ownership record

     - Results are returned for the market provided within the basic authentication credentials 

    :param ownership_id: The id of the ownership to be updated
    :type ownership_id: str
    :param custom_data: Custom JSON object that will be attached to this ownership record
    :type custom_data: str
    :param expires: The date (in millis) of when this app ownership expires
    :type expires: int

    """
    return web.Response(status=200)


async def ownership_uninstall_ownership_id_post(request: web.Request, ownership_id, user_id, cancel_ownership=None, custom_data=None) -> web.Response:
    """Uninstalls a license for a particular user and app (uninstalls app)

     - This method is called on behalf of a user - User data and statistics are recorded when this method is called 

    :param ownership_id: The id of the ownership to be unintalled
    :type ownership_id: str
    :param user_id: The id of the User requesting to uninstall the App
    :type user_id: str
    :param cancel_ownership: True if this app will require payment to be re-installed. Default is false
    :type cancel_ownership: bool
    :param custom_data: A custom JSON object to attach to this ownership record
    :type custom_data: str

    """
    return web.Response(status=200)
