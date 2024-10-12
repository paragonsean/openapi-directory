from typing import List, Dict
from aiohttp import web

from openapi_server.models.child_objects import ChildObjects
from openapi_server.models.ooxml_dto import OoxmlDTO
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.shared_pictures import SharedPictures
from openapi_server.models.shared_pictures_details import SharedPicturesDetails
from openapi_server import util


async def shared_images_childobjects_get_id(request: web.Request, id) -> web.Response:
    """Shared: Get Dependent Objects Tree

    This endpoint is helpful for helping users and bots identify dependent objects to this Shared and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def shared_images_details_get_id(request: web.Request, id) -> web.Response:
    """Shared: Get Details

    Returns object metadata and information about relative dependent objects 

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def shared_images_get_id(request: web.Request, id) -> web.Response:
    """Images: Get by Id

    Get by Id: Use this method to retrieve a Images object by its primary key (id)

    :param id: An Id of the respository DTO elemennt
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def shared_images_getimage_put_id(request: web.Request, id) -> web.Response:
    """Image: Download Image

    Download Images extracted from Ooxml Documents

    :param id: The Image Id
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def shared_images_openofficexml_get_id_updated(request: web.Request, id, updated=None) -> web.Response:
    """Shared: Get Underlying Xml

    Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Shared object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Shared objects.

    :param id: 
    :type id: str
    :type id: str
    :param updated: Indicates whether API should return the orginal uploaded xml (false) or the actively updated version (true, default)
    :type updated: bool

    """
    return web.Response(status=200)


async def shared_images_openofficexml_put_id(request: web.Request, id, body=None) -> web.Response:
    """Shared: Modify Underlying Xml

    Directly eidt the underlying xml of a Shared object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Shared objects.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OoxmlDTO.from_dict(body)
    return web.Response(status=200)


async def shared_images_svg_get_id_use_cache(request: web.Request, id, use_cache=None) -> web.Response:
    """Shared: Get Svg file

    This endpoint is helpful for rending this Shared as an svg or image object that can then be rendered in a story, dashboard or website.

    :param id: 
    :type id: str
    :type id: str
    :param use_cache: Indicates whether API should retrieve content from a cache if aviable (true, default), or force an update (false)
    :type use_cache: bool

    """
    return web.Response(status=200)
