from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.api_v1_accounts_id_follow_post_request import ApiV1AccountsIdFollowPostRequest
from openapi_server.models.api_v1_accounts_id_mute_post_request import ApiV1AccountsIdMutePostRequest
from openapi_server.models.api_v1_accounts_id_note_post_request import ApiV1AccountsIdNotePostRequest
from openapi_server.models.api_v1_accounts_post_request import ApiV1AccountsPostRequest
from openapi_server.models.api_v1_accounts_update_credentials_patch_request import ApiV1AccountsUpdateCredentialsPatchRequest
from openapi_server.models.error import Error
from openapi_server.models.featured_tag import FeaturedTag
from openapi_server.models.identity_proof import IdentityProof
from openapi_server.models.relationship import Relationship
from openapi_server.models.status import Status
from openapi_server import util


async def api_v1_accounts_id_block_post(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_block_post

    Block the given account. Clients should filter statuses from this account if received (e.g. due to a boost in the Home timeline).

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_featured_tags_get(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_featured_tags_get

    Tags featured by this account.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_follow_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_accounts_id_follow_post

    Follow the given account. Can also be used to update whether to show reblogs or enable notifications.

    :param id: The id of the account in the database
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AccountsIdFollowPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_accounts_id_followers_get(request: web.Request, id, max_id=None, since_id=None, limit=None) -> web.Response:
    """api_v1_accounts_id_followers_get

    Accounts which follow the given account, if network is not hidden by the account owner.

    :param id: The id of the account in the database
    :type id: str
    :param max_id: Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination.
    :type max_id: str
    :param since_id: Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination.
    :type since_id: str
    :param limit: Maximum number of results to return. Defaults to 40.
    :type limit: int

    """
    return web.Response(status=200)


async def api_v1_accounts_id_following_get(request: web.Request, id, max_id=None, since_id=None, limit=None) -> web.Response:
    """api_v1_accounts_id_following_get

    Accounts which the given account is following, if network is not hidden by the account owner.

    :param id: The id of the account in the database
    :type id: str
    :param max_id: Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination.
    :type max_id: str
    :param since_id: Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination.
    :type since_id: str
    :param limit: Maximum number of results to return. Defaults to 40.
    :type limit: int

    """
    return web.Response(status=200)


async def api_v1_accounts_id_get(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_get

    

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_identity_proofs_get(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_identity_proofs_get

    Array of IdentityProof

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_lists_get(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_lists_get

    User lists that you have added this account to.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_mute_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_accounts_id_mute_post

    Mute the given account. Clients should filter statuses and notifications from this account, if received (e.g. due to a boost in the Home timeline).

    :param id: The id of the account in the database
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AccountsIdMutePostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_accounts_id_note_post(request: web.Request, id, body=None) -> web.Response:
    """api_v1_accounts_id_note_post

    Sets a private note on a user.

    :param id: The id of the account in the database
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AccountsIdNotePostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_accounts_id_pin_post(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_pin_post

    Add the given account to the user&#39;s featured profiles. (Featured profiles are currently shown on the user&#39;s own public profile.)

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_statuses_get(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_statuses_get

    Statuses posted to the given account.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_unblock_post(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_unblock_post

    Block the given account. Clients should filter statuses from this account if received (e.g. due to a boost in the Home timeline).

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_unfollow_post(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_unfollow_post

    Unfollow the given account.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_unmute_post(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_unmute_post

    Unmute the given account.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_id_unpin_post(request: web.Request, id) -> web.Response:
    """api_v1_accounts_id_unpin_post

    Remove the given account from the user&#39;s featured profiles.

    :param id: The id of the account in the database
    :type id: str

    """
    return web.Response(status=200)


async def api_v1_accounts_post_0(request: web.Request, body=None) -> web.Response:
    """api_v1_accounts_post_0

    Creates a user and account records. Returns an account access token for the app that initiated the request. The app should save this token for later, and should wait for the user to confirm their account by clicking a link in their email inbox.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AccountsPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_accounts_relationships_get(request: web.Request, id) -> web.Response:
    """api_v1_accounts_relationships_get

    Sets a private note on a user.

    :param id: Array of account IDs to check
    :type id: List[str]

    """
    return web.Response(status=200)


async def api_v1_accounts_search_get(request: web.Request, q, limit=None, resolve=None, following=None) -> web.Response:
    """api_v1_accounts_search_get

    Search for matching accounts by username or display name.

    :param q: What to search for
    :type q: str
    :param limit: Maximum number of results. Defaults to 40.
    :type limit: int
    :param resolve: Attempt WebFinger lookup. Defaults to false. Use this when &#x60;q&#x60; is an exact address.
    :type resolve: str
    :param following: Only who the user is following. Defaults to false.
    :type following: bool

    """
    return web.Response(status=200)


async def api_v1_accounts_update_credentials_patch(request: web.Request, body=None) -> web.Response:
    """api_v1_accounts_update_credentials_patch

    Update the user&#39;s display and preferences.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AccountsUpdateCredentialsPatchRequest.from_dict(body)
    return web.Response(status=200)


async def api_v1_accounts_verify_credentials_get(request: web.Request, ) -> web.Response:
    """api_v1_accounts_verify_credentials_get

    Test to make sure that the user token works.


    """
    return web.Response(status=200)
