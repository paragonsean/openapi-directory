from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.activity import Activity
from openapi_server.models.create_access_token_option import CreateAccessTokenOption
from openapi_server.models.create_email_option import CreateEmailOption
from openapi_server.models.create_gpg_key_option import CreateGPGKeyOption
from openapi_server.models.create_hook_option import CreateHookOption
from openapi_server.models.create_key_option import CreateKeyOption
from openapi_server.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from openapi_server.models.create_repo_option import CreateRepoOption
from openapi_server.models.delete_email_option import DeleteEmailOption
from openapi_server.models.edit_hook_option import EditHookOption
from openapi_server.models.email import Email
from openapi_server.models.gpg_key import GPGKey
from openapi_server.models.hook import Hook
from openapi_server.models.o_auth2_application import OAuth2Application
from openapi_server.models.public_key import PublicKey
from openapi_server.models.repository import Repository
from openapi_server.models.stop_watch import StopWatch
from openapi_server.models.team import Team
from openapi_server.models.tracked_time import TrackedTime
from openapi_server.models.user import User
from openapi_server.models.user_heatmap_data import UserHeatmapData
from openapi_server.models.user_search200_response import UserSearch200Response
from openapi_server.models.user_settings import UserSettings
from openapi_server.models.user_settings_options import UserSettingsOptions
from openapi_server import util


async def create_current_user_repo_0(request: web.Request, body=None) -> web.Response:
    """Create a repository

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateRepoOption.from_dict(body)
    return web.Response(status=200)


async def get_user_settings(request: web.Request, ) -> web.Response:
    """Get user settings

    


    """
    return web.Response(status=200)


async def get_verification_token(request: web.Request, ) -> web.Response:
    """Get a Token to verify

    


    """
    return web.Response(status=200)


async def update_user_settings(request: web.Request, body=None) -> web.Response:
    """Update user settings

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserSettingsOptions.from_dict(body)
    return web.Response(status=200)


async def user_add_email(request: web.Request, body=None) -> web.Response:
    """Add email addresses

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateEmailOption.from_dict(body)
    return web.Response(status=200)


async def user_check_following(request: web.Request, username, target) -> web.Response:
    """Check if one user is following another user

    

    :param username: username of following user
    :type username: str
    :param target: username of followed user
    :type target: str

    """
    return web.Response(status=200)


async def user_create_hook(request: web.Request, body) -> web.Response:
    """Create a hook

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateHookOption.from_dict(body)
    return web.Response(status=200)


async def user_create_o_auth2_application(request: web.Request, body) -> web.Response:
    """creates a new OAuth2 application

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateOAuth2ApplicationOptions.from_dict(body)
    return web.Response(status=200)


async def user_create_token(request: web.Request, username, body=None) -> web.Response:
    """Create an access token

    

    :param username: username of user
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateAccessTokenOption.from_dict(body)
    return web.Response(status=200)


async def user_current_check_following(request: web.Request, username) -> web.Response:
    """Check whether a user is followed by the authenticated user

    

    :param username: username of followed user
    :type username: str

    """
    return web.Response(status=200)


async def user_current_check_starring(request: web.Request, owner, repo) -> web.Response:
    """Whether the authenticated is starring the repo

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def user_current_delete_follow(request: web.Request, username) -> web.Response:
    """Unfollow a user

    

    :param username: username of user to unfollow
    :type username: str

    """
    return web.Response(status=200)


async def user_current_delete_gpg_key(request: web.Request, id) -> web.Response:
    """Remove a GPG key

    

    :param id: id of key to delete
    :type id: int

    """
    return web.Response(status=200)


async def user_current_delete_key(request: web.Request, id) -> web.Response:
    """Delete a public key

    

    :param id: id of key to delete
    :type id: int

    """
    return web.Response(status=200)


async def user_current_delete_star(request: web.Request, owner, repo) -> web.Response:
    """Unstar the given repo

    

    :param owner: owner of the repo to unstar
    :type owner: str
    :param repo: name of the repo to unstar
    :type repo: str

    """
    return web.Response(status=200)


async def user_current_get_gpg_key(request: web.Request, id) -> web.Response:
    """Get a GPG key

    

    :param id: id of key to get
    :type id: int

    """
    return web.Response(status=200)


async def user_current_get_key(request: web.Request, id) -> web.Response:
    """Get a public key

    

    :param id: id of key to get
    :type id: int

    """
    return web.Response(status=200)


async def user_current_list_followers(request: web.Request, page=None, limit=None) -> web.Response:
    """List the authenticated user&#39;s followers

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_list_following(request: web.Request, page=None, limit=None) -> web.Response:
    """List the users that the authenticated user is following

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_list_gpg_keys(request: web.Request, page=None, limit=None) -> web.Response:
    """List the authenticated user&#39;s GPG keys

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_list_keys(request: web.Request, fingerprint=None, page=None, limit=None) -> web.Response:
    """List the authenticated user&#39;s public keys

    

    :param fingerprint: fingerprint of the key
    :type fingerprint: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_list_repos(request: web.Request, page=None, limit=None) -> web.Response:
    """List the repos that the authenticated user owns

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_list_starred(request: web.Request, page=None, limit=None) -> web.Response:
    """The repos that the authenticated user has starred

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_list_subscriptions(request: web.Request, page=None, limit=None) -> web.Response:
    """List repositories watched by the authenticated user

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_current_post_gpg_key(request: web.Request, body=None) -> web.Response:
    """Create a GPG key

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateGPGKeyOption.from_dict(body)
    return web.Response(status=200)


async def user_current_post_key(request: web.Request, body=None) -> web.Response:
    """Create a public key

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateKeyOption.from_dict(body)
    return web.Response(status=200)


async def user_current_put_follow(request: web.Request, username) -> web.Response:
    """Follow a user

    

    :param username: username of user to follow
    :type username: str

    """
    return web.Response(status=200)


async def user_current_put_star(request: web.Request, owner, repo) -> web.Response:
    """Star the given repo

    

    :param owner: owner of the repo to star
    :type owner: str
    :param repo: name of the repo to star
    :type repo: str

    """
    return web.Response(status=200)


async def user_current_tracked_times(request: web.Request, page=None, limit=None, since=None, before=None) -> web.Response:
    """List the current user&#39;s tracked times

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int
    :param since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
    :type since: str
    :param before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
    :type before: str

    """
    since = util.deserialize_datetime(since)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def user_delete_access_token(request: web.Request, username, token) -> web.Response:
    """delete an access token

    

    :param username: username of user
    :type username: str
    :param token: token to be deleted, identified by ID and if not available by name
    :type token: str

    """
    return web.Response(status=200)


async def user_delete_email(request: web.Request, body=None) -> web.Response:
    """Delete email addresses

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteEmailOption.from_dict(body)
    return web.Response(status=200)


async def user_delete_hook(request: web.Request, id) -> web.Response:
    """Delete a hook

    

    :param id: id of the hook to delete
    :type id: int

    """
    return web.Response(status=200)


async def user_delete_o_auth2_application(request: web.Request, id) -> web.Response:
    """delete an OAuth2 Application

    

    :param id: token to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def user_edit_hook(request: web.Request, id, body=None) -> web.Response:
    """Update a hook

    

    :param id: id of the hook to update
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditHookOption.from_dict(body)
    return web.Response(status=200)


async def user_get(request: web.Request, username) -> web.Response:
    """Get a user

    

    :param username: username of user to get
    :type username: str

    """
    return web.Response(status=200)


async def user_get_current(request: web.Request, ) -> web.Response:
    """Get the authenticated user

    


    """
    return web.Response(status=200)


async def user_get_heatmap_data(request: web.Request, username) -> web.Response:
    """Get a user&#39;s heatmap

    

    :param username: username of user to get
    :type username: str

    """
    return web.Response(status=200)


async def user_get_hook(request: web.Request, id) -> web.Response:
    """Get a hook

    

    :param id: id of the hook to get
    :type id: int

    """
    return web.Response(status=200)


async def user_get_o_auth2_application(request: web.Request, id) -> web.Response:
    """get an OAuth2 Application

    

    :param id: Application ID to be found
    :type id: int

    """
    return web.Response(status=200)


async def user_get_oauth2_application(request: web.Request, page=None, limit=None) -> web.Response:
    """List the authenticated user&#39;s oauth2 applications

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_get_stop_watches(request: web.Request, page=None, limit=None) -> web.Response:
    """Get list of all existing stopwatches

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_get_tokens(request: web.Request, username, page=None, limit=None) -> web.Response:
    """List the authenticated user&#39;s access tokens

    

    :param username: username of user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_activity_feeds(request: web.Request, username, only_performed_by=None, _date=None, page=None, limit=None) -> web.Response:
    """List a user&#39;s activity feeds

    

    :param username: username of user
    :type username: str
    :param only_performed_by: if true, only show actions performed by the requested user
    :type only_performed_by: bool
    :param _date: the date of the activities to be found
    :type _date: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def user_list_emails(request: web.Request, ) -> web.Response:
    """List the authenticated user&#39;s email addresses

    


    """
    return web.Response(status=200)


async def user_list_followers(request: web.Request, username, page=None, limit=None) -> web.Response:
    """List the given user&#39;s followers

    

    :param username: username of user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_following(request: web.Request, username, page=None, limit=None) -> web.Response:
    """List the users that the given user is following

    

    :param username: username of user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_gpg_keys(request: web.Request, username, page=None, limit=None) -> web.Response:
    """List the given user&#39;s GPG keys

    

    :param username: username of user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_hooks(request: web.Request, page=None, limit=None) -> web.Response:
    """List the authenticated user&#39;s webhooks

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_keys(request: web.Request, username, fingerprint=None, page=None, limit=None) -> web.Response:
    """List the given user&#39;s public keys

    

    :param username: username of user
    :type username: str
    :param fingerprint: fingerprint of the key
    :type fingerprint: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_repos(request: web.Request, username, page=None, limit=None) -> web.Response:
    """List the repos owned by the given user

    

    :param username: username of user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_starred(request: web.Request, username, page=None, limit=None) -> web.Response:
    """The repos that the given user has starred

    

    :param username: username of user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_subscriptions(request: web.Request, username, page=None, limit=None) -> web.Response:
    """List the repositories watched by a user

    

    :param username: username of the user
    :type username: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_list_teams(request: web.Request, page=None, limit=None) -> web.Response:
    """List all the teams a user belongs to

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_search(request: web.Request, q=None, uid=None, page=None, limit=None) -> web.Response:
    """Search for users

    

    :param q: keyword
    :type q: str
    :param uid: ID of the user to search for
    :type uid: int
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def user_update_o_auth2_application(request: web.Request, id, body) -> web.Response:
    """update an OAuth2 Application, this includes regenerating the client secret

    

    :param id: application to be updated
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOAuth2ApplicationOptions.from_dict(body)
    return web.Response(status=200)


async def user_verify_gpg_key(request: web.Request, ) -> web.Response:
    """Verify a GPG key

    


    """
    return web.Response(status=200)
