from typing import List, Dict
from aiohttp import web

from openapi_server.models.block_user_mutation_response import BlockUserMutationResponse
from openapi_server.models.block_user_request import BlockUserRequest
from openapi_server.models.error import Error
from openapi_server.models.get2_lists_id_followers_response import Get2ListsIdFollowersResponse
from openapi_server.models.get2_lists_id_members_response import Get2ListsIdMembersResponse
from openapi_server.models.get2_tweets_id_liking_users_response import Get2TweetsIdLikingUsersResponse
from openapi_server.models.get2_tweets_id_retweeted_by_response import Get2TweetsIdRetweetedByResponse
from openapi_server.models.get2_users_by_response import Get2UsersByResponse
from openapi_server.models.get2_users_by_username_username_response import Get2UsersByUsernameUsernameResponse
from openapi_server.models.get2_users_id_blocking_response import Get2UsersIdBlockingResponse
from openapi_server.models.get2_users_id_followers_response import Get2UsersIdFollowersResponse
from openapi_server.models.get2_users_id_following_response import Get2UsersIdFollowingResponse
from openapi_server.models.get2_users_id_muting_response import Get2UsersIdMutingResponse
from openapi_server.models.get2_users_id_response import Get2UsersIdResponse
from openapi_server.models.get2_users_me_response import Get2UsersMeResponse
from openapi_server.models.get2_users_response import Get2UsersResponse
from openapi_server.models.mute_user_mutation_response import MuteUserMutationResponse
from openapi_server.models.mute_user_request import MuteUserRequest
from openapi_server.models.problem import Problem
from openapi_server.models.users_following_create_request import UsersFollowingCreateRequest
from openapi_server.models.users_following_create_response import UsersFollowingCreateResponse
from openapi_server.models.users_following_delete_response import UsersFollowingDeleteResponse
from openapi_server import util


async def find_my_user(request: web.Request, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """User lookup me

    This endpoint returns information about the requesting User.

    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def find_user_by_id(request: web.Request, id, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """User lookup by ID

    This endpoint returns information about a User. Specify User by ID.

    :param id: The ID of the User to lookup.
    :type id: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def find_user_by_username(request: web.Request, username, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """User lookup by username

    This endpoint returns information about a User. Specify User by username.

    :param username: A username.
    :type username: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def find_users_by_id(request: web.Request, ids, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """User lookup by IDs

    This endpoint returns information about Users. Specify Users by their ID.

    :param ids: A list of User IDs, comma-separated. You can specify up to 100 IDs.
    :type ids: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def find_users_by_username(request: web.Request, usernames, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """User lookup by usernames

    This endpoint returns information about Users. Specify Users by their username.

    :param usernames: A list of usernames, comma-separated.
    :type usernames: List[str]
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def list_get_followers(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Returns User objects that follow a List by the provided List ID

    Returns a list of Users that follow a List by the provided List ID

    :param id: The ID of the List.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def list_get_members(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Returns User objects that are members of a List by the provided List ID.

    Returns a list of Users that are members of a List by the provided List ID.

    :param id: The ID of the List.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def tweets_id_liking_users(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Returns User objects that have liked the provided Tweet ID

    Returns a list of Users that have liked the provided Tweet ID

    :param id: A single Tweet ID.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def tweets_id_retweeting_users(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Returns User objects that have retweeted the provided Tweet ID

    Returns a list of Users that have retweeted the provided Tweet ID

    :param id: A single Tweet ID.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def users_id_block(request: web.Request, id, body) -> web.Response:
    """Block User by User ID

    Causes the User (in the path) to block the target User. The User (in the path) must match the User context authorizing the request

    :param id: The ID of the authenticated source User that is requesting to block the target User.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BlockUserRequest.from_dict(body)
    return web.Response(status=200)


async def users_id_blocking(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Returns User objects that are blocked by provided User ID

    Returns a list of Users that are blocked by the provided User ID

    :param id: The ID of the authenticated source User for whom to return results.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def users_id_follow(request: web.Request, id, body=None) -> web.Response:
    """Follow User

    Causes the User(in the path) to follow, or “request to follow” for protected Users, the target User. The User(in the path) must match the User context authorizing the request

    :param id: The ID of the authenticated source User that is requesting to follow the target User.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UsersFollowingCreateRequest.from_dict(body)
    return web.Response(status=200)


async def users_id_followers(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Followers by User ID

    Returns a list of Users who are followers of the specified User ID.

    :param id: The ID of the User to lookup.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def users_id_following(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Following by User ID

    Returns a list of Users that are being followed by the provided User ID

    :param id: The ID of the User to lookup.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get a specified &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def users_id_mute(request: web.Request, id, body=None) -> web.Response:
    """Mute User by User ID.

    Causes the User (in the path) to mute the target User. The User (in the path) must match the User context authorizing the request.

    :param id: The ID of the authenticated source User that is requesting to mute the target User.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MuteUserRequest.from_dict(body)
    return web.Response(status=200)


async def users_id_muting(request: web.Request, id, max_results=None, pagination_token=None, user_fields=None, expansions=None, tweet_fields=None) -> web.Response:
    """Returns User objects that are muted by the provided User ID

    Returns a list of Users that are muted by the provided User ID

    :param id: The ID of the authenticated source User for whom to return results.
    :type id: str
    :param max_results: The maximum number of results.
    :type max_results: int
    :param pagination_token: This parameter is used to get the next &#39;page&#39; of results.
    :type pagination_token: str
    :param user_fields: A comma separated list of User fields to display.
    :type user_fields: List[str]
    :param expansions: A comma separated list of fields to expand.
    :type expansions: List[str]
    :param tweet_fields: A comma separated list of Tweet fields to display.
    :type tweet_fields: List[str]

    """
    return web.Response(status=200)


async def users_id_unblock(request: web.Request, source_user_id, target_user_id) -> web.Response:
    """Unblock User by User ID

    Causes the source User to unblock the target User. The source User must match the User context authorizing the request

    :param source_user_id: The ID of the authenticated source User that is requesting to unblock the target User.
    :type source_user_id: str
    :param target_user_id: The ID of the User that the source User is requesting to unblock.
    :type target_user_id: str

    """
    return web.Response(status=200)


async def users_id_unfollow(request: web.Request, source_user_id, target_user_id) -> web.Response:
    """Unfollow User

    Causes the source User to unfollow the target User. The source User must match the User context authorizing the request

    :param source_user_id: The ID of the authenticated source User that is requesting to unfollow the target User.
    :type source_user_id: str
    :param target_user_id: The ID of the User that the source User is requesting to unfollow.
    :type target_user_id: str

    """
    return web.Response(status=200)


async def users_id_unmute(request: web.Request, source_user_id, target_user_id) -> web.Response:
    """Unmute User by User ID

    Causes the source User to unmute the target User. The source User must match the User context authorizing the request

    :param source_user_id: The ID of the authenticated source User that is requesting to unmute the target User.
    :type source_user_id: str
    :param target_user_id: The ID of the User that the source User is requesting to unmute.
    :type target_user_id: str

    """
    return web.Response(status=200)
