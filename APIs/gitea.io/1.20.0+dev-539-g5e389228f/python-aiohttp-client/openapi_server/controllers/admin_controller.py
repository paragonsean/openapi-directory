from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_hook_option import CreateHookOption
from openapi_server.models.create_key_option import CreateKeyOption
from openapi_server.models.create_org_option import CreateOrgOption
from openapi_server.models.create_repo_option import CreateRepoOption
from openapi_server.models.create_user_option import CreateUserOption
from openapi_server.models.cron import Cron
from openapi_server.models.edit_hook_option import EditHookOption
from openapi_server.models.edit_user_option import EditUserOption
from openapi_server.models.email import Email
from openapi_server.models.hook import Hook
from openapi_server.models.organization import Organization
from openapi_server.models.public_key import PublicKey
from openapi_server.models.rename_user_option import RenameUserOption
from openapi_server.models.repository import Repository
from openapi_server.models.user import User
from openapi_server import util


async def admin_adopt_repository(request: web.Request, owner, repo) -> web.Response:
    """Adopt unadopted files as a repository

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def admin_create_hook(request: web.Request, body) -> web.Response:
    """Create a hook

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateHookOption.from_dict(body)
    return web.Response(status=200)


async def admin_create_org(request: web.Request, username, body) -> web.Response:
    """Create an organization

    

    :param username: username of the user that will own the created organization
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrgOption.from_dict(body)
    return web.Response(status=200)


async def admin_create_public_key(request: web.Request, username, body=None) -> web.Response:
    """Add a public key on behalf of a user

    

    :param username: username of the user
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateKeyOption.from_dict(body)
    return web.Response(status=200)


async def admin_create_repo(request: web.Request, username, body) -> web.Response:
    """Create a repository on behalf of a user

    

    :param username: username of the user. This user will own the created repository
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateRepoOption.from_dict(body)
    return web.Response(status=200)


async def admin_create_user(request: web.Request, body=None) -> web.Response:
    """Create a user

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateUserOption.from_dict(body)
    return web.Response(status=200)


async def admin_cron_list(request: web.Request, page=None, limit=None) -> web.Response:
    """List cron tasks

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def admin_cron_run(request: web.Request, task) -> web.Response:
    """Run cron task

    

    :param task: task to run
    :type task: str

    """
    return web.Response(status=200)


async def admin_delete_hook(request: web.Request, id) -> web.Response:
    """Delete a hook

    

    :param id: id of the hook to delete
    :type id: int

    """
    return web.Response(status=200)


async def admin_delete_unadopted_repository(request: web.Request, owner, repo) -> web.Response:
    """Delete unadopted files

    

    :param owner: owner of the repo
    :type owner: str
    :param repo: name of the repo
    :type repo: str

    """
    return web.Response(status=200)


async def admin_delete_user(request: web.Request, username, purge=None) -> web.Response:
    """Delete a user

    

    :param username: username of user to delete
    :type username: str
    :param purge: purge the user from the system completely
    :type purge: bool

    """
    return web.Response(status=200)


async def admin_delete_user_public_key(request: web.Request, username, id) -> web.Response:
    """Delete a user&#39;s public key

    

    :param username: username of user
    :type username: str
    :param id: id of the key to delete
    :type id: int

    """
    return web.Response(status=200)


async def admin_edit_hook(request: web.Request, id, body=None) -> web.Response:
    """Update a hook

    

    :param id: id of the hook to update
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EditHookOption.from_dict(body)
    return web.Response(status=200)


async def admin_edit_user(request: web.Request, username, body=None) -> web.Response:
    """Edit an existing user

    

    :param username: username of user to edit
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditUserOption.from_dict(body)
    return web.Response(status=200)


async def admin_get_all_emails(request: web.Request, page=None, limit=None) -> web.Response:
    """List all emails

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def admin_get_all_orgs(request: web.Request, page=None, limit=None) -> web.Response:
    """List all organizations

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def admin_get_hook(request: web.Request, id) -> web.Response:
    """Get a hook

    

    :param id: id of the hook to get
    :type id: int

    """
    return web.Response(status=200)


async def admin_list_hooks(request: web.Request, page=None, limit=None) -> web.Response:
    """List system&#39;s webhooks

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def admin_rename_user(request: web.Request, username, body) -> web.Response:
    """Rename a user

    

    :param username: existing username of user
    :type username: str
    :param body: 
    :type body: dict | bytes

    """
    body = RenameUserOption.from_dict(body)
    return web.Response(status=200)


async def admin_search_emails(request: web.Request, q=None, page=None, limit=None) -> web.Response:
    """Search all emails

    

    :param q: keyword
    :type q: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def admin_search_users(request: web.Request, source_id=None, login_name=None, page=None, limit=None) -> web.Response:
    """Search users according filter conditions

    

    :param source_id: ID of the user&#39;s login source to search for
    :type source_id: int
    :param login_name: user&#39;s login name to search for
    :type login_name: str
    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int

    """
    return web.Response(status=200)


async def admin_unadopted_list(request: web.Request, page=None, limit=None, pattern=None) -> web.Response:
    """List unadopted repositories

    

    :param page: page number of results to return (1-based)
    :type page: int
    :param limit: page size of results
    :type limit: int
    :param pattern: pattern of repositories to search for
    :type pattern: str

    """
    return web.Response(status=200)
