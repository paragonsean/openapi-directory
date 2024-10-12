from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_room_patch_request import OperationRoomPatchRequest
from openapi_server.models.room import Room
from openapi_server.models.room_list_response import RoomListResponse
from openapi_server.models.total_count_response import TotalCountResponse
from openapi_server import util


async def rooms_get_available_rooms(request: web.Request, app_id, app_key, hotel_id, _from, to, adults=None, include_out_of_service=None, room_types=None, amenities=None, views=None, locations=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Request available rooms using a given criteria.

    

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel you are looking for available rooms.
    :type hotel_id: int
    :param _from: Rooms returned will not be assigned to a reservation or be under maintenance between this date              and the specified to date. Still there could be departing reservations or ending maintenances              for this date.
    :type _from: str
    :param to: Rooms returned will not be assigned to a reservation or be under maintenance between the specified              from date and this date. Still there could be arriving reservations or beginning maintenances              for this date.
    :type to: str
    :param adults: Specifies number of adults the returned rooms will have to be able to house. The default value is 1.
    :type adults: str
    :param include_out_of_service: Should rooms that are set OutOfService in the defined time period be returned as available. By default              they are not.
    :type include_out_of_service: bool
    :param room_types: Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
    :type room_types: List[str]
    :param amenities: Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
    :type amenities: List[str]
    :param views: Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
    :type views: List[str]
    :param locations: Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
    :type locations: List[str]
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def rooms_get_room(request: web.Request, app_id, app_key, hotel_id, room_number) -> web.Response:
    """Get all the details for a specific room in the hotel.

    With this call you can load the details about a specific room in the hotel. It will show you the current status of the room.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the room belongs to.
    :type hotel_id: int
    :param room_number: The room number you want to see details for.
    :type room_number: str

    """
    return web.Response(status=200)


async def rooms_get_rooms(request: web.Request, app_id, app_key, hotel_id, occupancy=None, conditions=None, maintenances=None, room_types=None, amenities=None, views=None, locations=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Get a list of rooms using the provided filtering and pagination criteria.

    Find all rooms for the hotel that match the specified filter criteria. The filtering will be done based on the current state of              the rooms.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel you are trying to find rooms for.
    :type hotel_id: int
    :param occupancy: Return results only for rooms that have the given frontdesk ocuppancy status.
    :type occupancy: str
    :param conditions: Return results only for rooms that have the given room condition status.
    :type conditions: List[str]
    :param maintenances: Return results only for rooms that have the given maintenance status.
    :type maintenances: List[str]
    :param room_types: Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
    :type room_types: List[str]
    :param amenities: Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
    :type amenities: List[str]
    :param views: Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
    :type views: List[str]
    :param locations: Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
    :type locations: List[str]
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    return web.Response(status=200)


async def rooms_get_rooms_count(request: web.Request, app_id, app_key, hotel_id, occupancy=None, conditions=None, maintenances=None, room_types=None, amenities=None, views=None, locations=None) -> web.Response:
    """Get the count of all rooms in the hotel matching the given filter criteria.

    

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel you are counting the rooms for.
    :type hotel_id: int
    :param occupancy: Return results only for rooms that have the given frontdesk ocuppancy status.
    :type occupancy: str
    :param conditions: Return results only for rooms that have the given room condition status.
    :type conditions: List[str]
    :param maintenances: Return results only for rooms that have the given maintenance status.
    :type maintenances: List[str]
    :param room_types: Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
    :type room_types: List[str]
    :param amenities: Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
    :type amenities: List[str]
    :param views: Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
    :type views: List[str]
    :param locations: Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
    :type locations: List[str]

    """
    return web.Response(status=200)


async def rooms_patch_room(request: web.Request, app_id, app_key, hotel_id, room_number, patch_request) -> web.Response:
    """Partially updates a room.

    The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to modify condition and housekeeping occupancy status of the room.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/status/condition\&quot;, \&quot;value\&quot;: \&quot;CleanNotInspected\&quot;                }, {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/status/housekeeping_occupancy\&quot;, \&quot;value\&quot;: \&quot;Vacant\&quot;                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the room belongs to.
    :type hotel_id: int
    :param room_number: The room number of the room you would like to update.
    :type room_number: str
    :param patch_request: A set of JSON Patch operations.
    :type patch_request: list | bytes

    """
    patch_request = [OperationRoomPatchRequest.from_dict(d) for d in patch_request]
    return web.Response(status=200)
