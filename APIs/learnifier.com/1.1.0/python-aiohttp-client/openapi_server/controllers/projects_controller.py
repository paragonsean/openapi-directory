from typing import List, Dict
from aiohttp import web

from openapi_server.models.activation_error import ActivationError
from openapi_server.models.add_participant import AddParticipant
from openapi_server.models.add_project import AddProject
from openapi_server.models.error import Error
from openapi_server.models.login_link import LoginLink
from openapi_server.models.participation import Participation
from openapi_server.models.project import Project
from openapi_server.models.project_team_member import ProjectTeamMember
from openapi_server.models.update_project import UpdateProject
from openapi_server import util


async def extproject_get(request: web.Request, extid) -> web.Response:
    """Gets Organization Unit by external id

    Gets an Organization Unit by external id

    :param extid: The external id of the organization unit
    :type extid: str

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_get(request: web.Request, orgid) -> web.Response:
    """Organization Unit Projects

    Returns the available projects for the organization unit 

    :param orgid: Id of the organization unit
    :type orgid: 

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_post(request: web.Request, orgid, body) -> web.Response:
    """Create project

    Creates a new project 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddProject.from_dict(body)
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_delete(request: web.Request, orgid, projectid) -> web.Response:
    """Deletes the project

    Deletes the project. The project can only be deleted if the project do not contain any participants. 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_get(request: web.Request, orgid, projectid) -> web.Response:
    """Project information

    Returns project information 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_participants_get(request: web.Request, orgid, projectid) -> web.Response:
    """Project participants

    Returns project participants 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_participants_participant_id_activate_post(request: web.Request, orgid, projectid, participant_id) -> web.Response:
    """Activate participant

    Activates a participant so that it can be used 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int
    :param participant_id: Id of the participant
    :type participant_id: int

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_participants_participant_id_delete(request: web.Request, orgid, projectid, participant_id) -> web.Response:
    """Deletes a participant

    Deletes a participant. The user itself will still remain but any state related to the project will be deleted. It might not be possible due to constraints from the products in the project to delete the participant. However this can only be determined at the time of the delete. If a delete fails the participant will have their inError flag set. 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int
    :param participant_id: Participant id
    :type participant_id: int

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_participants_participant_id_loginlink_post(request: web.Request, orgid, projectid, participant_id) -> web.Response:
    """Participant login link

    Returns a single sign on link for the participant. The link is only usable once and should be used directly. The link expires after a few minutes.  This operation requires the *login link* permission. 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int
    :param participant_id: Id of the participant
    :type participant_id: int

    """
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_participants_post(request: web.Request, orgid, projectid, body) -> web.Response:
    """Add participant

    Add a user to the project. Participant information is created for the user. In the body object, only one of either email or userid must be specified. The participant needs to be activated before it the user can access it. 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddParticipant.from_dict(body)
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_patch(request: web.Request, orgid, projectid, body) -> web.Response:
    """Update project information

    Updates information about a project. Values are only updated if the fields are specified in the input 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateProject.from_dict(body)
    return web.Response(status=200)


async def orgunits_orgid_projects_projectid_teammembers_get(request: web.Request, orgid, projectid) -> web.Response:
    """Project team members

    Returns the project team members. A team member is a .... 

    :param orgid: Id of the organization unit
    :type orgid: int
    :param projectid: Id of the project
    :type projectid: int

    """
    return web.Response(status=200)
