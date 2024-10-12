from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_change_password import AuthChangePassword
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.place_created import PlaceCreated
from openapi_server.models.place_item import PlaceItem
from openapi_server.models.place_new import PlaceNew
from openapi_server.models.user import User
from openapi_server.models.user_created import UserCreated
from openapi_server.models.user_item import UserItem
from openapi_server.models.user_new import UserNew
from openapi_server.models.user_patch import UserPatch
from openapi_server.models.user_token_item import UserTokenItem
from openapi_server import util


async def account_change_password(request: web.Request, change_password_info) -> web.Response:
    """Change the password

    Set a new password for the account.  **Note**: requires full access to the *Account*. 

    :param change_password_info: Old and new password
    :type change_password_info: dict | bytes

    """
    change_password_info = AuthChangePassword.from_dict(change_password_info)
    return web.Response(status=200)


async def account_delete_user(request: web.Request, user_id) -> web.Response:
    """Delete a User

    Delete a *User* from this *Account*, and revoke all his/her *Tokens*.  **Note**: requires full access to the *Account*. 

    :param user_id: Unique identifier of a *User*.
    :type user_id: str

    """
    return web.Response(status=200)


async def account_get_user(request: web.Request, user_id) -> web.Response:
    """Information about a User

    Get information about a *User* in the same *Account*.

    :param user_id: Unique identifier of a *User*.
    :type user_id: str

    """
    return web.Response(status=200)


async def account_new_place(request: web.Request, place=None) -> web.Response:
    """Create a Place

    Create a new *Place*.  A *Device* (&#x60;class&#x60;: &#x60;MINT&#x60;, &#x60;address&#x60;: &#x60;0&#x60;) is automatically created and attached to the new *Place*.  **Note:** requires full access to the *Account*. 

    :param place: 
    :type place: dict | bytes

    """
    place = PlaceNew.from_dict(place)
    return web.Response(status=200)


async def account_new_user(request: web.Request, user_info) -> web.Response:
    """New User

    Add a *User*.  **Note**: requires full access to the *Account*. 

    :param user_info: 
    :type user_info: dict | bytes

    """
    user_info = UserNew.from_dict(user_info)
    return web.Response(status=200)


async def account_patch_user(request: web.Request, user_id, user_patch) -> web.Response:
    """Modify a User

    Modify a *User*.  **Note**: requires full access to the *Account*. 

    :param user_id: Unique identifier of a *User*.
    :type user_id: str
    :param user_patch: 
    :type user_patch: dict | bytes

    """
    user_patch = UserPatch.from_dict(user_patch)
    return web.Response(status=200)


async def account_places(request: web.Request, ) -> web.Response:
    """List Places of the Account

    List the *Places* of the account.  **Note:** requires full access to the *Account*. 


    """
    return web.Response(status=200)


async def account_revoke_token(request: web.Request, token_id) -> web.Response:
    """Revoke a Token

    Revoke the given *Token*.  **Note:** requires full access to the *Account*. 

    :param token_id: Identifier of the token
    :type token_id: str

    """
    return web.Response(status=200)


async def account_tokens(request: web.Request, ) -> web.Response:
    """List active Tokens of the Account

    List the active *Tokens* on the account.  **Note:** requires full access to the *Account*. 


    """
    return web.Response(status=200)


async def account_users(request: web.Request, embed_metadata=None) -> web.Response:
    """List Users of the Account

    Get the list of *Users* of this *Account*.

    :param embed_metadata: Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    :type embed_metadata: List[str]

    """
    return web.Response(status=200)


async def user_get_metadata(request: web.Request, user_id) -> web.Response:
    """List metadata

    Get the metadata.

    :param user_id: Unique identifier of a *User*.
    :type user_id: str

    """
    return web.Response(status=200)


async def user_patch_metadata(request: web.Request, user_id, metadata_patch) -> web.Response:
    """Modify metadata

    Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

    :param user_id: Unique identifier of a *User*.
    :type user_id: str
    :param metadata_patch: Modifications to apply to the metadata of the resource. 
    :type metadata_patch: dict | bytes

    """
    metadata_patch = MetadataPatch.from_dict(metadata_patch)
    return web.Response(status=200)
