from typing import List, Dict
from aiohttp import web

from openapi_server.models.column_dto import ColumnDTO
from openapi_server.models.filter_dto import FilterDTO
from openapi_server.models.filter_property_dto import FilterPropertyDTO
from openapi_server.models.local_settings_dto import LocalSettingsDTO
from openapi_server.models.order_dto import OrderDTO
from openapi_server.models.permissions_dto import PermissionsDTO
from openapi_server.models.settings_dto import SettingsDTO
from openapi_server.models.view_dto import ViewDTO
from openapi_server.models.view_details_dto import ViewDetailsDTO
from openapi_server.models.view_with_id_dto import ViewWithIdDTO
from openapi_server.models.views_brief_dto import ViewsBriefDTO
from openapi_server import util


async def browse_csv(request: web.Request, view_id=None, separator=None, secondary_separator=None, additional_order=None) -> web.Response:
    """Searches for data (ie. customer, task, etc) and returns it in a CSV form.

    Searches for data (ie. customer, task, etc) and returns it in a CSV form.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param separator: csv field separator
    :type separator: str
    :param secondary_separator: secondary csv field separator
    :type secondary_separator: str
    :param additional_order: 
    :type additional_order: str

    """
    return web.Response(status=200)


async def browse_json(request: web.Request, view_id=None, page=None, additional_order=None, use_deferred_columns=None, max_rows=None) -> web.Response:
    """Searches for data (ie. customer, task, etc) and returns it in a tabular form.

    Searches for data (ie. customer, task, etc) and returns it in a tabular form.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param page: 
    :type page: int
    :param additional_order: 
    :type additional_order: str
    :param use_deferred_columns: 
    :type use_deferred_columns: str
    :param max_rows: overrides view&#39;s default rows limit, supported values 10 to 1000
    :type max_rows: int

    """
    return web.Response(status=200)


async def create(request: web.Request, class_name, body) -> web.Response:
    """Creates view for given class.

    Creates view for given class.

    :param class_name: view&#39;s class name
    :type class_name: str
    :param body: Created view for given class.
    :type body: dict | bytes

    """
    body = ViewDTO.from_dict(body)
    return web.Response(status=200)


async def delete(request: web.Request, view_id) -> web.Response:
    """Removes a view.

    Removes a view. No content is returned upon success (204).

    :param view_id: view&#39;s internal identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def delete_column(request: web.Request, view_id, column_name) -> web.Response:
    """Deletes a single column from view.

    Deletes a single column from view.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param column_name: column&#39;s name
    :type column_name: str

    """
    return web.Response(status=200)


async def get(request: web.Request, view_id) -> web.Response:
    """Returns all view&#39;s information.

    Returns all view&#39;s information (ie. name, columns, filters, etc).

    :param view_id: view&#39;s identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def get_column_settings(request: web.Request, view_id, column_name) -> web.Response:
    """Returns column&#39;s specific settings.

    Returns column&#39;s specific settings. For example when column describes money amount we can decide whether it should display currency or not.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param column_name: column&#39;s name
    :type column_name: str

    """
    return web.Response(status=200)


async def get_columns(request: web.Request, view_id) -> web.Response:
    """Returns columns defined in view.

    Returns columns defined in view.

    :param view_id: view&#39;s identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def get_current_view_details(request: web.Request, class_name, place_name=None) -> web.Response:
    """Returns current view&#39;s detailed information, suitable for browser.

    Returns current view&#39;s detailed information, suitable for browser.

    :param class_name: views&#39; class name
    :type class_name: str
    :param place_name: place name (denotes specific place in system with the table)
    :type place_name: str

    """
    return web.Response(status=200)


async def get_filter(request: web.Request, view_id) -> web.Response:
    """Returns view&#39;s filter.

    Returns view&#39;s filter.

    :param view_id: view&#39;s identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def get_local_settings(request: web.Request, view_id) -> web.Response:
    """Returns view&#39;s local settings (for current user).

    Returns view&#39;s local settings (for current user).

    :param view_id: view&#39;s identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def get_order(request: web.Request, view_id) -> web.Response:
    """Returns view&#39;s order settings.

    Returns view&#39;s order settings.

    :param view_id: view&#39;s identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def get_permissions(request: web.Request, view_id) -> web.Response:
    """Returns view&#39;s permissions.

    Returns view&#39;s permissions.

    :param view_id: view&#39;s identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def get_settings(request: web.Request, view_id) -> web.Response:
    """Returns view&#39;s settings.

    Returns view&#39;s settings (ie. name).

    :param view_id: view&#39;s identifier
    :type view_id: int

    """
    return web.Response(status=200)


async def get_view_details(request: web.Request, class_name, view_id, place_name=None) -> web.Response:
    """Returns view&#39;s detailed information, suitable for browser.

    Returns view&#39;s detailed information, suitable for browser.

    :param class_name: views&#39; class name
    :type class_name: str
    :param view_id: 
    :type view_id: int
    :param place_name: place name (denotes specific place in system with the table)
    :type place_name: str

    """
    return web.Response(status=200)


async def get_views_brief(request: web.Request, class_name, place_name=None) -> web.Response:
    """Returns views&#39; brief.

    Returns views&#39; brief.

    :param class_name: views&#39; class name
    :type class_name: str
    :param place_name: place name (denotes specific place in system with the table)
    :type place_name: str

    """
    return web.Response(status=200)


async def select_view_and_get_its_details(request: web.Request, class_name, view_id, place_name__denotes_specific_place_in_system_with_the_table=None) -> web.Response:
    """Selects given view as current and returns its detailed information, suitable for browser.

    Selects given view as current and returns its detailed information, suitable for browser.

    :param class_name: views&#39; class name
    :type class_name: str
    :param view_id: 
    :type view_id: int
    :param place_name__denotes_specific_place_in_system_with_the_table: 
    :type place_name__denotes_specific_place_in_system_with_the_table: str

    """
    return web.Response(status=200)


async def update(request: web.Request, view_id, body) -> web.Response:
    """Updates all view&#39;s information.

    Updates all view&#39;s information (ie. name, columns, filters, etc).

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param body: Updated all view&#39;s information.
    :type body: dict | bytes

    """
    body = ViewDTO.from_dict(body)
    return web.Response(status=200)


async def update_column_settings(request: web.Request, view_id, column_name, body) -> web.Response:
    """Updates column&#39;s specific settings.

    Updates column&#39;s specific settings. For example when column describes money amount we can decide whether it should display currency or not.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param column_name: column&#39;s name
    :type column_name: str
    :param body: Updated column&#39;s specific settings.
    :type body: 

    """
    return web.Response(status=200)


async def update_columns(request: web.Request, view_id, body) -> web.Response:
    """Updates columns in view.

    Updates columns in view.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param body: Updated columns in view.
    :type body: list | bytes

    """
    body = [ColumnDTO.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_filter(request: web.Request, view_id, body) -> web.Response:
    """Updates view&#39;s filter.

    Updates view&#39;s filter.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param body: Updated view&#39;s filter.
    :type body: list | bytes

    """
    body = [FilterPropertyDTO.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_filter_property(request: web.Request, view_id, filter_property, body) -> web.Response:
    """Updates view&#39;s filter property.

    Updates view&#39;s filter property.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param filter_property: view&#39;s filter property name
    :type filter_property: str
    :param body: Updated view&#39;s filter property.
    :type body: dict | bytes

    """
    body = FilterPropertyDTO.from_dict(body)
    return web.Response(status=200)


async def update_local_settings(request: web.Request, view_id, body) -> web.Response:
    """Updates view&#39;s local settings (for current user).

    Updates view&#39;s local settings (for current user).

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param body: Updated view&#39;s local settings (for current user).
    :type body: dict | bytes

    """
    body = LocalSettingsDTO.from_dict(body)
    return web.Response(status=200)


async def update_order(request: web.Request, view_id, body) -> web.Response:
    """Updates view&#39;s order settings.

    Updates view&#39;s order settings.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param body: Updated view&#39;s order settings.
    :type body: dict | bytes

    """
    body = OrderDTO.from_dict(body)
    return web.Response(status=200)


async def update_permissions(request: web.Request, view_id, body) -> web.Response:
    """Updates view&#39;s permissions.

    Updates view&#39;s permissions.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param body: Updated view&#39;s permissions.
    :type body: dict | bytes

    """
    body = PermissionsDTO.from_dict(body)
    return web.Response(status=200)


async def update_settings(request: web.Request, view_id, body) -> web.Response:
    """Updates view&#39;s settings.

    Updates view&#39;s settings.

    :param view_id: view&#39;s identifier
    :type view_id: int
    :param body: Updated view&#39;s settings.
    :type body: dict | bytes

    """
    body = SettingsDTO.from_dict(body)
    return web.Response(status=200)
