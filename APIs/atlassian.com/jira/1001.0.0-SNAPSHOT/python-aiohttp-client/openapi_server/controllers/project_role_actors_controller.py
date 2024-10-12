from typing import List, Dict
from aiohttp import web

from openapi_server.models.actor_input_bean import ActorInputBean
from openapi_server.models.actors_map import ActorsMap
from openapi_server.models.project_role import ProjectRole
from openapi_server.models.project_role_actors_update_bean import ProjectRoleActorsUpdateBean
from openapi_server import util


async def add_actor_users(request: web.Request, project_id_or_key, id, body) -> web.Response:
    """Add actors to project role

    Adds actors to a project role for the project.  To replace all actors for the project, use [Set actors for project role](#api-rest-api-3-project-projectIdOrKey-role-id-put).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param id: The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.
    :type id: int
    :param body: The groups or users to associate with the project role for this project. Provide the user account ID, group name, or group ID. As a group&#39;s name can change, use of group ID is recommended.
    :type body: dict | bytes

    """
    body = ActorsMap.from_dict(body)
    return web.Response(status=200)


async def add_project_role_actors_to_role(request: web.Request, id, body) -> web.Response:
    """Add default actors to project role

    Adds [default actors](#api-rest-api-3-resolution-get) to a role. You may add groups or users, but you cannot add groups and users in the same request.  Changing a project role&#39;s default actors does not affect project role members for projects already created.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ActorInputBean.from_dict(body)
    return web.Response(status=200)


async def delete_actor(request: web.Request, project_id_or_key, id, user=None, group=None, group_id=None) -> web.Response:
    """Delete actors from project role

    Deletes actors from a project role for the project.  To remove default actors from the project role, use [Delete default actors from project role](#api-rest-api-3-role-id-actors-delete).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param id: The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.
    :type id: int
    :param user: The user account ID of the user to remove from the project role.
    :type user: str
    :param group: The name of the group to remove from the project role. This parameter cannot be used with the &#x60;groupId&#x60; parameter. As a group&#39;s name can change, use of &#x60;groupId&#x60; is recommended.
    :type group: str
    :param group_id: The ID of the group to remove from the project role. This parameter cannot be used with the &#x60;group&#x60; parameter.
    :type group_id: str

    """
    return web.Response(status=200)


async def delete_project_role_actors_from_role(request: web.Request, id, user=None, group_id=None, group=None) -> web.Response:
    """Delete default actors from project role

    Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a group or user, but you cannot delete a group and a user in the same request.  Changing a project role&#39;s default actors does not affect project role members for projects already created.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.
    :type id: int
    :param user: The user account ID of the user to remove as a default actor.
    :type user: str
    :param group_id: The group ID of the group to be removed as a default actor. This parameter cannot be used with the &#x60;group&#x60; parameter.
    :type group_id: str
    :param group: The group name of the group to be removed as a default actor.This parameter cannot be used with the &#x60;groupId&#x60; parameter. As a group&#39;s name can change, use of &#x60;groupId&#x60; is recommended.
    :type group: str

    """
    return web.Response(status=200)


async def get_project_role_actors_for_role(request: web.Request, id) -> web.Response:
    """Get default actors for project role

    Returns the [default actors](#api-rest-api-3-resolution-get) for the project role.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.
    :type id: int

    """
    return web.Response(status=200)


async def set_actors(request: web.Request, project_id_or_key, id, body) -> web.Response:
    """Set actors for project role

    Sets the actors for a project role for a project, replacing all existing actors.  To add actors to the project without overwriting the existing list, use [Add actors to project role](#api-rest-api-3-project-projectIdOrKey-role-id-post).  **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param project_id_or_key: The project ID or project key (case sensitive).
    :type project_id_or_key: str
    :param id: The ID of the project role. Use [Get all project roles](#api-rest-api-3-role-get) to get a list of project role IDs.
    :type id: int
    :param body: The groups or users to associate with the project role for this project. Provide the user account ID, group name, or group ID. As a group&#39;s name can change, use of group ID is recommended.
    :type body: dict | bytes

    """
    body = ProjectRoleActorsUpdateBean.from_dict(body)
    return web.Response(status=200)
