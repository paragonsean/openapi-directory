from typing import List, Dict
from aiohttp import web

from openapi_server.models.bus_item import BusItem
from openapi_server.models.bus_pairing import BusPairing
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.error_sub_entity import ErrorSubEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.place import Place
from openapi_server.models.place_patch import PlacePatch
from openapi_server import util


async def place_buses(request: web.Request, place_id, with_pairing=None) -> web.Response:
    """List Buses

    Get the list of *Buses* available on the gateway of this *Place*. If &#x60;withPairing&#x60; is &#x60;true&#x60;, return only buses that allow device pairing (see &#x60;/places/{placeId}/buses/{busId}/pairing&#x60;).

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param with_pairing: Filter out buses that have no pairing window
    :type with_pairing: bool

    """
    return web.Response(status=200)


async def place_get_metadata(request: web.Request, place_id) -> web.Response:
    """List metadata

    Get the metadata.

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str

    """
    return web.Response(status=200)


async def place_open_pairing(request: web.Request, place_id, bus_id, pairing) -> web.Response:
    """Open/Close the pairing window

    Open/Close the pairing window.  **Note**: requires full access to the *Account*. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param bus_id: Unique identifier of a *Bus*.
    :type bus_id: str
    :param pairing: 
    :type pairing: dict | bytes

    """
    pairing = BusPairing.from_dict(pairing)
    return web.Response(status=200)


async def place_pairing(request: web.Request, place_id, bus_id) -> web.Response:
    """State of the pairing window

    Get the state of the pairing window of the *Bus*.  **Note**: requires full access to the *Account*. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param bus_id: Unique identifier of a *Bus*.
    :type bus_id: str

    """
    return web.Response(status=200)


async def place_patch(request: web.Request, place_id, place_patch) -> web.Response:
    """Update a Place

    Change information about a *Place*.  **Note**: requires full access to the *Account*. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param place_patch: 
    :type place_patch: dict | bytes

    """
    place_patch = PlacePatch.from_dict(place_patch)
    return web.Response(status=200)


async def place_patch_metadata(request: web.Request, place_id, metadata_patch) -> web.Response:
    """Modify metadata

    Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param metadata_patch: Modifications to apply to the metadata of the resource. 
    :type metadata_patch: dict | bytes

    """
    metadata_patch = MetadataPatch.from_dict(metadata_patch)
    return web.Response(status=200)


async def places_get(request: web.Request, place_id) -> web.Response:
    """Information about a Place

    Get information about a *Place*.

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str

    """
    return web.Response(status=200)
