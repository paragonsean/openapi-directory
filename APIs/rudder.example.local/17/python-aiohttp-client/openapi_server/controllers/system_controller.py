from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_archive200_response import CreateArchive200Response
from openapi_server.models.get_healthcheck_result200_response import GetHealthcheckResult200Response
from openapi_server.models.get_status200_response import GetStatus200Response
from openapi_server.models.get_system_info200_response import GetSystemInfo200Response
from openapi_server.models.list_archives200_response import ListArchives200Response
from openapi_server.models.purge_software200_response import PurgeSoftware200Response
from openapi_server.models.regenerate_policies200_response import RegeneratePolicies200Response
from openapi_server.models.reload_all200_response import ReloadAll200Response
from openapi_server.models.reload_groups200_response import ReloadGroups200Response
from openapi_server.models.reload_techniques200_response import ReloadTechniques200Response
from openapi_server.models.restore_archive200_response import RestoreArchive200Response
from openapi_server.models.update_policies200_response import UpdatePolicies200Response
from openapi_server import util


async def create_archive(request: web.Request, archive_kind) -> web.Response:
    """Create an archive

    Create new archive of the given kind

    :param archive_kind: Type of archive to make
    :type archive_kind: str

    """
    return web.Response(status=200)


async def get_healthcheck_result(request: web.Request, ) -> web.Response:
    """Get healthcheck

    Run and get the result of all checks


    """
    return web.Response(status=200)


async def get_status(request: web.Request, ) -> web.Response:
    """Get server status

    Get information about current server status


    """
    return web.Response(status=200)


async def get_system_info(request: web.Request, ) -> web.Response:
    """Get server information

    Get information about the server version


    """
    return web.Response(status=200)


async def get_zip_archive(request: web.Request, archive_kind, commit_id) -> web.Response:
    """Get an archive as a ZIP

    Get an archive of the given kind as a zip

    :param archive_kind: Type of archive to make
    :type archive_kind: str
    :param commit_id: commit ID of the archive to get as a ZIP file
    :type commit_id: str

    """
    return web.Response(status=200)


async def list_archives(request: web.Request, archive_kind) -> web.Response:
    """List archives

    List configuration archives

    :param archive_kind: Type of archive to make
    :type archive_kind: str

    """
    return web.Response(status=200)


async def purge_software(request: web.Request, ) -> web.Response:
    """Trigger batch for cleaning unreferenced software

    Start the software cleaning batch asynchronously.


    """
    return web.Response(status=200)


async def regenerate_policies(request: web.Request, ) -> web.Response:
    """Trigger a new policy generation

    Trigger a full policy generation


    """
    return web.Response(status=200)


async def reload_all(request: web.Request, ) -> web.Response:
    """Reload both techniques and dynamic groups

    Reload both techniques and dynamic groups


    """
    return web.Response(status=200)


async def reload_groups(request: web.Request, ) -> web.Response:
    """Reload dynamic groups

    Reload dynamic groups


    """
    return web.Response(status=200)


async def reload_techniques(request: web.Request, ) -> web.Response:
    """Reload techniques

    Reload techniques from local technique library


    """
    return web.Response(status=200)


async def restore_archive(request: web.Request, archive_kind, archive_restore_kind) -> web.Response:
    """Restore an archive

    Restore an archive of the given kind for the given moment

    :param archive_kind: Type of archive to make
    :type archive_kind: str
    :param archive_restore_kind: 
    :type archive_restore_kind: str

    """
    return web.Response(status=200)


async def update_policies(request: web.Request, ) -> web.Response:
    """Trigger update of policies

    Update configuration policies if needed


    """
    return web.Response(status=200)
