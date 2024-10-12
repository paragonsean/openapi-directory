from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_entry import AccessEntry
from openapi_server import util


async def access_add(request: web.Request, user, agents, mask) -> web.Response:
    """Adds/Overwrites the user entry in the access control database.

    Adds/Overwrites the user entry in the access control database.

    :param user: Username of the simulator hosting system
    :type user: str
    :param agents: Agent range in minimal range representation
    :type agents: str
    :param mask: Currently not used
    :type mask: str

    """
    return web.Response(status=200)


async def access_del(request: web.Request, user) -> web.Response:
    """Clears a users entry from access control database.

    Using &#39;*&#39; for user clears all the users.

    :param user: username of the simulator hosting system
    :type user: str

    """
    return web.Response(status=200)


async def access_get_acldb(request: web.Request, ) -> web.Response:
    """Returns the current access control database in use.

    If nothing is specified then this returns \&quot;\&quot;.


    """
    return web.Response(status=200)


async def access_get_admindir(request: web.Request, ) -> web.Response:
    """Returns the current admin directory.

    If nothing is specified in admin/settings.cfg then returns \&quot;\&quot;. If no admin directory is specified then the shared area will be used where needed (e.g. for persistent info, access control data files etc. )


    """
    return web.Response(status=200)


async def access_get_adminuser(request: web.Request, ) -> web.Response:
    """Returns the current administrator.

    If nothing is specified in admin/settings.cfg then returns \&quot;\&quot;.


    """
    return web.Response(status=200)


async def access_get_enabled(request: web.Request, ) -> web.Response:
    """Returns the state of access control checking.

    0 indicates that it is disabled, 1 indicates it is enabled.


    """
    return web.Response(status=200)


async def access_list(request: web.Request, ) -> web.Response:
    """Returns an array of entries.

    Each entry consists of user, agents (in minimal range representation) and access mask (not used currently).


    """
    return web.Response(status=200)


async def access_load(request: web.Request, filename) -> web.Response:
    """Loads the specified file for access control data.

    If filename is not specified then the currently set &#39;acldb&#39; parameter is used.

    :param filename: Filename to load
    :type filename: str

    """
    return web.Response(status=200)


async def access_save(request: web.Request, filename) -> web.Response:
    """Saves current access control data in specified file.

    If filename is not specified then the currently set &#39;acldb&#39; parameter is used.

    :param filename: Filename to save
    :type filename: str

    """
    return web.Response(status=200)


async def access_set_acldb(request: web.Request, database_name) -> web.Response:
    """Allows setting the name of the current access control database.

    This will be used for subsequent load and save operations.

    :param database_name: Database name to use
    :type database_name: str

    """
    return web.Response(status=200)


async def access_set_enabled(request: web.Request, enabled_or_not) -> web.Response:
    """Allows the user to enable/disable the access control check.

    0 indicates disabled, 1 indicates enabled.

    :param enabled_or_not: indicator
    :type enabled_or_not: str

    """
    return web.Response(status=200)
