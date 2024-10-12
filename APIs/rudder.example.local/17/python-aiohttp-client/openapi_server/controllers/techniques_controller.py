from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_technique200_response import CreateTechnique200Response
from openapi_server.models.delete_technique200_response import DeleteTechnique200Response
from openapi_server.models.editor_technique import EditorTechnique
from openapi_server.models.get_technique_all_version200_response import GetTechniqueAllVersion200Response
from openapi_server.models.get_techniques_resources200_response import GetTechniquesResources200Response
from openapi_server.models.list_technique_version_directives200_response import ListTechniqueVersionDirectives200Response
from openapi_server.models.list_techniques200_response import ListTechniques200Response
from openapi_server.models.list_techniques_directives200_response import ListTechniquesDirectives200Response
from openapi_server.models.list_techniques_versions200_response import ListTechniquesVersions200Response
from openapi_server.models.methods200_response import Methods200Response
from openapi_server.models.technique_categories200_response import TechniqueCategories200Response
from openapi_server.models.technique_revisions200_response import TechniqueRevisions200Response
from openapi_server import util


async def create_technique(request: web.Request, body) -> web.Response:
    """Create technique

    Create a new technique in Rudder from a technique in the technique editor

    :param body: 
    :type body: list | bytes

    """
    body = [EditorTechnique.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_technique(request: web.Request, technique_id, technique_version) -> web.Response:
    """Delete technique

    Delete a technique from technique editor

    :param technique_id: Technique ID
    :type technique_id: str
    :param technique_version: Technique version
    :type technique_version: str

    """
    return web.Response(status=200)


async def get_technique_all_version(request: web.Request, technique_id) -> web.Response:
    """Technique metadata by ID

    Get each Technique&#39;s versions with their metadata by ID

    :param technique_id: Technique ID
    :type technique_id: str

    """
    return web.Response(status=200)


async def get_technique_all_version_id(request: web.Request, technique_id, technique_version) -> web.Response:
    """Technique metadata by version and ID

    Get Technique metadata

    :param technique_id: Technique ID
    :type technique_id: str
    :param technique_version: Technique version
    :type technique_version: str

    """
    return web.Response(status=200)


async def get_techniques_resources(request: web.Request, technique_id, technique_version) -> web.Response:
    """Technique&#39;s resources

    Get currently deployed resources of a technique

    :param technique_id: Technique ID
    :type technique_id: str
    :param technique_version: Technique version
    :type technique_version: str

    """
    return web.Response(status=200)


async def list_technique_version_directives(request: web.Request, technique_id, technique_version) -> web.Response:
    """List all directives based on a version of a technique

    List all directives based on a version of a technique

    :param technique_id: Technique ID
    :type technique_id: str
    :param technique_version: Technique version
    :type technique_version: str

    """
    return web.Response(status=200)


async def list_techniques(request: web.Request, ) -> web.Response:
    """List all techniques

    List all technique with their versions


    """
    return web.Response(status=200)


async def list_techniques_directives(request: web.Request, technique_id) -> web.Response:
    """List all directives based on a technique

    List all directives based on all version of a technique

    :param technique_id: Technique ID
    :type technique_id: str

    """
    return web.Response(status=200)


async def list_techniques_versions(request: web.Request, ) -> web.Response:
    """List versions

    List all techniques version


    """
    return web.Response(status=200)


async def methods(request: web.Request, ) -> web.Response:
    """List methods

    Get all generic methods metadata


    """
    return web.Response(status=200)


async def reload_methods(request: web.Request, ) -> web.Response:
    """Reload methods

    Reload methods metadata from file system


    """
    return web.Response(status=200)


async def technique_categories(request: web.Request, ) -> web.Response:
    """List categories

    Get all technique categories


    """
    return web.Response(status=200)


async def technique_revisions(request: web.Request, technique_id, technique_version) -> web.Response:
    """Technique&#39;s revisions

    Get revisions for given technique

    :param technique_id: Technique ID
    :type technique_id: str
    :param technique_version: Technique version
    :type technique_version: str

    """
    return web.Response(status=200)


async def techniques(request: web.Request, ) -> web.Response:
    """Reload techniques

    Reload all techniques metadata from file system


    """
    return web.Response(status=200)


async def update_technique(request: web.Request, technique_id, technique_version, body) -> web.Response:
    """Update technique

    Update technique created with technique editor

    :param technique_id: Technique ID
    :type technique_id: str
    :param technique_version: Technique version
    :type technique_version: str
    :param body: 
    :type body: list | bytes

    """
    body = [EditorTechnique.from_dict(d) for d in body]
    return web.Response(status=200)
