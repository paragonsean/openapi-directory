from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.program import Program
from openapi_server.models.program_created import ProgramCreated
from openapi_server.models.program_item import ProgramItem
from openapi_server.models.program_log import ProgramLog
from openapi_server.models.program_new import ProgramNew
from openapi_server.models.program_patch import ProgramPatch
from openapi_server import util


async def place_new_program(request: web.Request, place_id, program_info) -> web.Response:
    """Create a Program

    Create a new *Program*.  **Note**: requires full access to the *Account*. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param program_info: 
    :type program_info: dict | bytes

    """
    program_info = ProgramNew.from_dict(program_info)
    return web.Response(status=200)


async def place_programs(request: web.Request, place_id, embed_metadata=None) -> web.Response:
    """List Programs

    Get the list of *Programs* available in this *Place*.

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param embed_metadata: Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    :type embed_metadata: List[str]

    """
    return web.Response(status=200)


async def program_delete(request: web.Request, program_id) -> web.Response:
    """Delete a Program

    Delete a *Program*.  **Note**: requires full access to the *Account*. 

    :param program_id: Unique identifier of a *Program*.
    :type program_id: str

    """
    return web.Response(status=200)


async def program_get_metadata(request: web.Request, program_id) -> web.Response:
    """List metadata

    Get the metadata of the *Program*.

    :param program_id: Unique identifier of a *Program*.
    :type program_id: str

    """
    return web.Response(status=200)


async def program_log(request: web.Request, program_id, _from, to=None) -> web.Response:
    """History of executions of a Program

    Get the execution history list of this *Program*.

    :param program_id: Unique identifier of a *Program*.
    :type program_id: str
    :param _from: Beginning of the time interval.
    :type _from: str
    :param to: End of the interval. Default: now. 
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def program_patch(request: web.Request, program_id, program_patch) -> web.Response:
    """Modify a Program

    Modify a *Program*: - name - status (enabled/disabled) - code  **Note**: requires full access to the *Account*. 

    :param program_id: Unique identifier of a *Program*.
    :type program_id: str
    :param program_patch: 
    :type program_patch: dict | bytes

    """
    program_patch = ProgramPatch.from_dict(program_patch)
    return web.Response(status=200)


async def program_patch_metadata(request: web.Request, program_id, metadata_patch) -> web.Response:
    """Modify metadata of a Program

    Modify the metadata of a *Program*. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

    :param program_id: Unique identifier of a *Program*.
    :type program_id: str
    :param metadata_patch: Modifications to apply to the metadata of the resource. 
    :type metadata_patch: dict | bytes

    """
    metadata_patch = MetadataPatch.from_dict(metadata_patch)
    return web.Response(status=200)


async def program_run(request: web.Request, program_id) -> web.Response:
    """Run the Program

    Launch the *Program*. The result will be available later in the run history.

    :param program_id: Unique identifier of a *Program*.
    :type program_id: str

    """
    return web.Response(status=200)


async def programs_get(request: web.Request, program_id) -> web.Response:
    """Information about a Program

    Get information about a *Program*. 

    :param program_id: Unique identifier of a *Program*.
    :type program_id: str

    """
    return web.Response(status=200)
