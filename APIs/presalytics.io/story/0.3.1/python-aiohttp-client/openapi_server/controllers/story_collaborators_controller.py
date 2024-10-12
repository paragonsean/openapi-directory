from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_new_collaborator_request import AddNewCollaboratorRequest
from openapi_server.models.modify_inactive_collaborator import ModifyInactiveCollaborator
from openapi_server.models.problem_detail import ProblemDetail
from openapi_server.models.story_collaborator import StoryCollaborator
from openapi_server import util


async def story_id_collaborators_get(request: web.Request, id) -> web.Response:
    """Story Collaborators: List

    Gets a list users that can read or edit this story

    :param id: the id from the story object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def story_id_collaborators_inactive_post(request: web.Request, id, body) -> web.Response:
    """Story Collaborators: Edit Inactive User Permission

    Edit story permissions for inactive users.  Requires admin rights.

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param body: Collaborator user id and permission type
    :type body: dict | bytes

    """
    body = ModifyInactiveCollaborator.from_dict(body)
    return web.Response(status=200)


async def story_id_collaborators_post(request: web.Request, id, body) -> web.Response:
    """Story Collaborators: Add New User

    Add a colloborator to this story

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param body: Collaborator user id and permission type
    :type body: dict | bytes

    """
    body = AddNewCollaboratorRequest.from_dict(body)
    return web.Response(status=200)


async def story_id_collaborators_userid_delete(request: web.Request, id, story_collaborator_userid) -> web.Response:
    """Story Collaborators: Remove User

    Remove a collaborator from this story

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param story_collaborator_userid: The presalytics userid (NOT the Id of the story_collaborator object)
    :type story_collaborator_userid: str
    :type story_collaborator_userid: str

    """
    return web.Response(status=200)


async def story_id_collaborators_userid_get(request: web.Request, id, story_collaborator_userid) -> web.Response:
    """Story Collaborators: Access Permissions

    Data to help you understand the access rights of a particular collaborator on this story

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param story_collaborator_userid: The presalytics userid (NOT the Id of the story_collaborator object)
    :type story_collaborator_userid: str
    :type story_collaborator_userid: str

    """
    return web.Response(status=200)


async def story_id_collaborators_userid_put(request: web.Request, id, story_collaborator_userid, body) -> web.Response:
    """Story Collaborators: Edit Access Rights

    Modify a user&#39;s access right to this story (e.g., grant edit permissions)

    :param id: the id from the story object
    :type id: str
    :type id: str
    :param story_collaborator_userid: The presalytics userid (NOT the Id of the story_collaborator object)
    :type story_collaborator_userid: str
    :type story_collaborator_userid: str
    :param body: Collaborator user id (presalytics userid) and permission type
    :type body: dict | bytes

    """
    body = StoryCollaborator.from_dict(body)
    return web.Response(status=200)
