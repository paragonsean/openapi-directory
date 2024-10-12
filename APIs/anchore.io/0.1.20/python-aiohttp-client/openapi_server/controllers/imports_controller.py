from typing import List, Dict
from aiohttp import web

from openapi_server.models.image_import_content_response import ImageImportContentResponse
from openapi_server.models.image_import_operation import ImageImportOperation
from openapi_server.models.image_package_manifest import ImagePackageManifest
from openapi_server import util


async def create_operation(request: web.Request, ) -> web.Response:
    """Begin the import of an image analyzed by Syft into the system

    


    """
    return web.Response(status=200)


async def get_operation(request: web.Request, operation_id) -> web.Response:
    """Get detail on a single import

    

    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)


async def import_image_config(request: web.Request, operation_id, body) -> web.Response:
    """Import a docker or OCI image config to associate with the image

    

    :param operation_id: 
    :type operation_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def import_image_dockerfile(request: web.Request, operation_id, body) -> web.Response:
    """Begin the import of an image analyzed by Syft into the system

    

    :param operation_id: 
    :type operation_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def import_image_manifest(request: web.Request, operation_id, body) -> web.Response:
    """Import a docker or OCI distribution manifest to associate with the image

    

    :param operation_id: 
    :type operation_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def import_image_packages(request: web.Request, operation_id, body) -> web.Response:
    """Begin the import of an image analyzed by Syft into the system

    

    :param operation_id: 
    :type operation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ImagePackageManifest.from_dict(body)
    return web.Response(status=200)


async def import_image_parent_manifest(request: web.Request, operation_id, body) -> web.Response:
    """Import a docker or OCI distribution manifest list to associate with the image

    

    :param operation_id: 
    :type operation_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def invalidate_operation(request: web.Request, operation_id) -> web.Response:
    """Invalidate operation ID so it can be garbage collected

    

    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)


async def list_import_dockerfiles(request: web.Request, operation_id) -> web.Response:
    """List uploaded dockerfiles

    

    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)


async def list_import_image_configs(request: web.Request, operation_id) -> web.Response:
    """List uploaded image configs

    

    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)


async def list_import_image_manifests(request: web.Request, operation_id) -> web.Response:
    """List uploaded image manifests

    

    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)


async def list_import_packages(request: web.Request, operation_id) -> web.Response:
    """List uploaded package manifests

    

    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)


async def list_import_parent_manifests(request: web.Request, operation_id) -> web.Response:
    """List uploaded parent manifests (manifest lists for a tag)

    

    :param operation_id: 
    :type operation_id: str

    """
    return web.Response(status=200)


async def list_operations(request: web.Request, ) -> web.Response:
    """Lists in-progress imports

    


    """
    return web.Response(status=200)
