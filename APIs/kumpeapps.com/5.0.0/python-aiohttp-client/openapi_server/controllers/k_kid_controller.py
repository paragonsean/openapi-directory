from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user_response import AddUserResponse
from openapi_server.models.allowance import Allowance
from openapi_server.models.chorelist import Chorelist
from openapi_server.models.model201_share import Model201Share
from openapi_server.models.model405 import Model405
from openapi_server.models.model412 import Model412
from openapi_server.models.nodata import Nodata
from openapi_server.models.success import Success
from openapi_server.models.userlist import Userlist
from openapi_server.models.wishlist import Wishlist
from openapi_server import util


async def kkid_allowance_get(request: web.Request, kid_user_id, transaction_days=None) -> web.Response:
    """returns allowance balance and allowance transactions

    By passing in the appropriate options, you can view allowance balance and allowance transactions for a given user provided that they are within the masterID account of the authenticated user. 

    :param kid_user_id: userID of the kid
    :type kid_user_id: int
    :param transaction_days: number of days you wish to search allowance transactions (default is 90 days)
    :type transaction_days: int

    """
    return web.Response(status=200)


async def kkid_allowance_post(request: web.Request, kid_user_id, amount, description, transaction_type) -> web.Response:
    """adds new allowance transaction to kidUserID

    By passing in the appropriate options, you can add an allowance transaction to a given user. 

    :param kid_user_id: userID of the kid
    :type kid_user_id: int
    :param amount: amount you wish to Add/Subtract (subtract value should be a negative value)
    :type amount: 
    :param description: Description (reason) of allowance transaction
    :type description: str
    :param transaction_type: Transaction Type (Add/Subtract)
    :type transaction_type: str

    """
    return web.Response(status=200)


async def kkid_apns_post(request: web.Request, kid_user_id, tool, token=None, devicename=None, title=None, message=None, badge=None, sound=None, section=None, priority=None) -> web.Response:
    """subscribes/unsubscribes/registers for apns push notifications

    

    :param kid_user_id: userID of the kid
    :type kid_user_id: int
    :param tool: tool you wish to talk to
    :type tool: str
    :param token: device APNS token (required for register)
    :type token: str
    :param devicename: Name of device to associate to token (required for register)
    :type devicename: str
    :param title: title of APNS message (required for send)
    :type title: str
    :param message: APNS message body (required for send)
    :type message: str
    :param badge: Number for badge icon (optional for send)
    :type badge: int
    :param sound: Name of sound file to play for send notification (optional for send)
    :type sound: str
    :param section: Notification section name (required for send/subscribe/unsubscribe)
    :type section: str
    :param priority: Notification section name (optional for send, default is active)
    :type priority: str

    """
    return web.Response(status=200)


async def kkid_chorelist_delete(request: web.Request, id_chore_list) -> web.Response:
    """deletes chore for given chore id

    By passing in the appropriate options, you can delete a chore for the given chore id under authenticated user&#39;s master account 

    :param id_chore_list: id of the chore you wish to delete
    :type id_chore_list: int

    """
    return web.Response(status=200)


async def kkid_chorelist_get(request: web.Request, kid_username=None, day=None, status=None, block_dash=None, optional=None, can_steal=None, include_calendar=None) -> web.Response:
    """returns list of chores for given user

    By passing in the appropriate options, you can search for chores assigned to a given user within the authenticated user&#39;s master account 

    :param kid_username: Username of kid you wish to search
    :type kid_username: str
    :param day: Day of week for chores (Weekly for weekly chores)
    :type day: str
    :param status: Status of Chore to search
    :type status: str
    :param block_dash: Filter results by blockDash parameter
    :type block_dash: bool
    :param optional: Filter results by optional parameter
    :type optional: bool
    :param can_steal: Filter results by canSteal parameter
    :type can_steal: bool
    :param include_calendar: include calendar notations (default is false)
    :type include_calendar: bool

    """
    return web.Response(status=200)


async def kkid_chorelist_post(request: web.Request, kid_username, chore_name, day=None, nfc_tag=None, status=None, chore_description=None, chore_number=None, block_dash=None, one_time=None, extra_allowance=None, optional=None, reassignable=None, can_steal=None, start_date=None, notes=None, require_object_detection=None, object_detection_tag=None, updated_by_automation=None, ai_icon=None, is_calendar=None) -> web.Response:
    """adds chore for given user

    By passing in the appropriate options, you can add a chore to given kid username under authenticated user&#39;s master account 

    :param kid_username: username of kid to assign the chore to.
    :type kid_username: str
    :param chore_name: name of chore
    :type chore_name: str
    :param day: day of week (Monday, Tuesday....) for the chore. For weekly chores put Weekly or leave blank
    :type day: str
    :param nfc_tag: text field of nfc tag required to check off chore
    :type nfc_tag: str
    :param status: status of chore (default is todo)
    :type status: str
    :param chore_description: optional chore description
    :type chore_description: str
    :param chore_number: number priority of chore (default is 5)
    :type chore_number: int
    :param block_dash: block dash option on this chore
    :type block_dash: bool
    :param one_time: mark as one time chore (does not repeat each week)
    :type one_time: bool
    :param extra_allowance: ammount of allowance added at end of week for completing this chore
    :type extra_allowance: int
    :param optional: mark as optional chore
    :type optional: bool
    :param reassignable: mark as reassignable (default is true)
    :type reassignable: bool
    :param can_steal: mark as sibling can steal chore
    :type can_steal: bool
    :param start_date: date (yyyy-mm-dd) that you wish the chore to start showing up. (default is today)
    :type start_date: str
    :param notes: notes added to chore (visable only on reports, kids do not see this note, this is mostly just for the developer)
    :type notes: str
    :param require_object_detection: require use of camera to detect object detection tag order to check off chore
    :type require_object_detection: bool
    :param object_detection_tag: tag for object detection to search for (required if requireObjectDetection is true)
    :type object_detection_tag: str
    :param updated_by_automation: true if chore updated via API from an Automation System
    :type updated_by_automation: bool
    :param ai_icon: Notes if AI Icons should be used (n for no, y for yes, e for yes- error)
    :type ai_icon: str
    :param is_calendar: True if this is a calendar note instead of a chore.
    :type is_calendar: bool

    """
    return web.Response(status=200)


async def kkid_chorelist_put(request: web.Request, id_chore_list, status=None, stolen=None, stolen_by=None, nfc_tag=None, notes=None, latitude=None, longitude=None, altitude=None, updated_by_automation=None, where_day=None, where_status=None, where_name=None) -> web.Response:
    """updates chore for given chore id

    By passing in the appropriate options, you can update the fields of a specific core within the authenticated user&#39;s master account 

    :param id_chore_list: id number of chore you wish to update
    :type id_chore_list: int
    :param status: new status of chore
    :type status: str
    :param stolen: mark chore as stolen by sibling
    :type stolen: bool
    :param stolen_by: username of sibling that stole the chore (required if stolen is true)
    :type stolen_by: str
    :param nfc_tag: text field of NFC tag that is required to be scanned to check off this chore (normally null)
    :type nfc_tag: str
    :param notes: notes field for chore
    :type notes: str
    :param latitude: GPS latitude of where the chore was marked
    :type latitude: int
    :param longitude: GPS longitude of where the chore was marked
    :type longitude: int
    :param altitude: GPS altitude of where the chore was marked
    :type altitude: int
    :param updated_by_automation: true if updated via API by automation system
    :type updated_by_automation: bool
    :param where_day: Where day equals...
    :type where_day: str
    :param where_status: Where status equals...
    :type where_status: str
    :param where_name: Where chore name equals...
    :type where_name: str

    """
    return web.Response(status=200)


async def kkid_masteruser_post(request: web.Request, username, password, email, first_name, last_name) -> web.Response:
    """adds new master user account

    By passing in the appropriate variables this method creates a new user with master account access. (The use of this method is restricted to Superusers ONLY) 

    :param username: username of user to create
    :type username: str
    :param password: password of user to create
    :type password: str
    :param email: email address of user to create
    :type email: str
    :param first_name: First Name of user to create
    :type first_name: str
    :param last_name: Last Name of user to create
    :type last_name: str

    """
    return web.Response(status=200)


async def kkid_share_get(request: web.Request, link_user_id, link, scope, scope2=None, scope3=None, scope4=None) -> web.Response:
    """Create Share Link

    Create share link

    :param link_user_id: User ID that the link should be authenticated to
    :type link_user_id: str
    :param link: Link to share
    :type link: str
    :param scope: Authentication scope for link
    :type scope: str
    :param scope2: Authentication scope for link
    :type scope2: str
    :param scope3: Authentication scope for link
    :type scope3: str
    :param scope4: Authentication scope for link
    :type scope4: str

    """
    return web.Response(status=200)


async def kkid_user_get(request: web.Request, enable_bool=None) -> web.Response:
    """Gets user info

    Gets user info for authenticated user

    :param enable_bool: Use bool values instead of Int 0/1
    :type enable_bool: bool

    """
    return web.Response(status=200)


async def kkid_userlist_delete(request: web.Request, user_id) -> web.Response:
    """deletes user

    By passing in the appropriate variables this method deletes the specified user. (This function is restricted to Superusers ONLY) 

    :param user_id: userID of the user you wish to delete
    :type user_id: int

    """
    return web.Response(status=200)


async def kkid_userlist_get(request: web.Request, is_child=None, is_active=None, is_admin=None, enable_allowance=None, enable_chores=None, user_id=None, username=None, email=None) -> web.Response:
    """returns list of users

    By passing in the appropriate options, you can search for users within the authenticated user&#39;s master account 

    :param is_child: Filter Search by isChild flag
    :type is_child: bool
    :param is_active: Filter Search by isActive flag
    :type is_active: bool
    :param is_admin: Filter Search by isAdmin flag
    :type is_admin: bool
    :param enable_allowance: Filter Search by enableAllowance flag
    :type enable_allowance: bool
    :param enable_chores: Filter Search by enableChores flag
    :type enable_chores: bool
    :param user_id: userID of user to search
    :type user_id: int
    :param username: Username of user to search
    :type username: str
    :param email: Email address of user to search
    :type email: str

    """
    return web.Response(status=200)


async def kkid_userlist_post(request: web.Request, username, password, email, first_name, last_name) -> web.Response:
    """adds new child user

    By passing in the appropriate variables this method creates a new user and assigns it to the master account of the authenticated user. By default this user will have chores and allowance access. 

    :param username: username of user to create
    :type username: str
    :param password: password of user to create
    :type password: str
    :param email: email address of user to create
    :type email: str
    :param first_name: First Name of user to create
    :type first_name: str
    :param last_name: Last Name of user to create
    :type last_name: str

    """
    return web.Response(status=200)


async def kkid_userlist_put(request: web.Request, user_id, username, email, first_name, last_name, emoji=None, tmdb_key=None, enable_wish_list=None, enable_chores=None, enable_allowance=None, enable_admin=None, enable_tmdb=None, enable_object_detection=None) -> web.Response:
    """updates user

    By passing in the appropriate variables this method updates the user&#39;s profile 

    :param user_id: userID of the user you wish to update
    :type user_id: int
    :param username: username of user to create
    :type username: str
    :param email: email address of user to create
    :type email: str
    :param first_name: First Name of user to create
    :type first_name: str
    :param last_name: Last Name of user to create
    :type last_name: str
    :param emoji: emoji character for user
    :type emoji: str
    :param tmdb_key: User&#39;s TMdB Session Key
    :type tmdb_key: str
    :param enable_wish_list: set status of Wish List module enabled
    :type enable_wish_list: bool
    :param enable_chores: set status of chores module enabled
    :type enable_chores: bool
    :param enable_allowance: set status of allowance module enabled
    :type enable_allowance: bool
    :param enable_admin: set status of isAdmin
    :type enable_admin: bool
    :param enable_tmdb: set status of enableTmdb (movie and tv search)
    :type enable_tmdb: bool
    :param enable_object_detection: set status of enableObjectDetection
    :type enable_object_detection: bool

    """
    return web.Response(status=200)


async def kkid_wishlist_delete(request: web.Request, wish_id) -> web.Response:
    """Delete item from wishlist

    

    :param wish_id: ID of wishlist item to delete
    :type wish_id: int

    """
    return web.Response(status=200)


async def kkid_wishlist_get(request: web.Request, kid_user_id=None) -> web.Response:
    """Get list of wishlist items

    

    :param kid_user_id: userID of the kid
    :type kid_user_id: int

    """
    return web.Response(status=200)


async def kkid_wishlist_post(request: web.Request, kid_user_id, title, description=None, priority=None, link=None) -> web.Response:
    """Add item to kid&#39;s wishlist

    

    :param kid_user_id: userID of the kid
    :type kid_user_id: int
    :param title: Item title
    :type title: str
    :param description: Item Description
    :type description: str
    :param priority: Item Priority
    :type priority: int
    :param link: URL Link to item
    :type link: str

    """
    return web.Response(status=200)


async def kkid_wishlist_put(request: web.Request, wish_id, title=None, description=None, priority=None, link=None) -> web.Response:
    """Update item on kid&#39;s wishlist

    

    :param wish_id: Wish list item ID to update
    :type wish_id: int
    :param title: Item title
    :type title: str
    :param description: Item Description
    :type description: str
    :param priority: Item Priority
    :type priority: int
    :param link: URL Link to item
    :type link: str

    """
    return web.Response(status=200)
