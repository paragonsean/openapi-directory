from typing import List, Dict
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.article_project_create import ArticleProjectCreate
from openapi_server.models.create_project_response import CreateProjectResponse
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.location import Location
from openapi_server.models.location_warnings import LocationWarnings
from openapi_server.models.private_file import PrivateFile
from openapi_server.models.project import Project
from openapi_server.models.project_article import ProjectArticle
from openapi_server.models.project_collaborator import ProjectCollaborator
from openapi_server.models.project_collaborator_invite import ProjectCollaboratorInvite
from openapi_server.models.project_complete import ProjectComplete
from openapi_server.models.project_complete_private import ProjectCompletePrivate
from openapi_server.models.project_create import ProjectCreate
from openapi_server.models.project_note import ProjectNote
from openapi_server.models.project_note_create import ProjectNoteCreate
from openapi_server.models.project_note_private import ProjectNotePrivate
from openapi_server.models.project_private import ProjectPrivate
from openapi_server.models.project_update import ProjectUpdate
from openapi_server.models.projects_search import ProjectsSearch
from openapi_server.models.response_message import ResponseMessage
from openapi_server import util


async def private_project_article_delete(request: web.Request, project_id, article_id) -> web.Response:
    """Delete project article

    Delete project article

    :param project_id: Project unique identifier
    :type project_id: int
    :param article_id: Project Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_project_article_details(request: web.Request, project_id, article_id) -> web.Response:
    """Project article details

    Project article details

    :param project_id: Project unique identifier
    :type project_id: int
    :param article_id: Project Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_project_article_file(request: web.Request, project_id, article_id, file_id) -> web.Response:
    """Project article file details

    Project article file details

    :param project_id: Project unique identifier
    :type project_id: int
    :param article_id: Project Article unique identifier
    :type article_id: int
    :param file_id: File unique identifier
    :type file_id: int

    """
    return web.Response(status=200)


async def private_project_article_files(request: web.Request, project_id, article_id) -> web.Response:
    """Project article list files

    List article files

    :param project_id: Project unique identifier
    :type project_id: int
    :param article_id: Project Article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_project_articles_create(request: web.Request, project_id, body, page=None, page_size=None, limit=None, offset=None) -> web.Response:
    """Create project article

    Create a new Article and associate it with this project

    :param project_id: Project unique identifier
    :type project_id: int
    :param body: Article description
    :type body: dict | bytes
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    body = ArticleProjectCreate.from_dict(body)
    return web.Response(status=200)


async def private_project_articles_list(request: web.Request, project_id, page=None, page_size=None, limit=None, offset=None) -> web.Response:
    """List project articles

    List project articles

    :param project_id: Project unique identifier
    :type project_id: int
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    return web.Response(status=200)


async def private_project_collaborator_delete(request: web.Request, project_id, user_id) -> web.Response:
    """Remove project collaborator

    Remove project collaborator

    :param project_id: Project unique identifier
    :type project_id: int
    :param user_id: User unique identifier
    :type user_id: int

    """
    return web.Response(status=200)


async def private_project_collaborators_invite(request: web.Request, project_id, body) -> web.Response:
    """Invite project collaborators

    Invite users to collaborate on project or view the project

    :param project_id: Project unique identifier
    :type project_id: int
    :param body: viewer or collaborator role. User user_id or email of user
    :type body: dict | bytes

    """
    body = ProjectCollaboratorInvite.from_dict(body)
    return web.Response(status=200)


async def private_project_collaborators_list(request: web.Request, project_id) -> web.Response:
    """List project collaborators

    List Project collaborators and invited users

    :param project_id: Project unique identifier
    :type project_id: int

    """
    return web.Response(status=200)


async def private_project_create(request: web.Request, body) -> web.Response:
    """Create project

    Create a new project

    :param body: Project  description
    :type body: dict | bytes

    """
    body = ProjectCreate.from_dict(body)
    return web.Response(status=200)


async def private_project_delete(request: web.Request, project_id) -> web.Response:
    """Delete project

    A project can be deleted only if: - it is not public - it does not have public articles.  When an individual project is deleted, all the articles are moved to my data of each owner.  When a group project is deleted, all the articles and files are deleted as well. Only project owner, group admin and above can delete a project. 

    :param project_id: Project unique identifier
    :type project_id: int

    """
    return web.Response(status=200)


async def private_project_details(request: web.Request, project_id) -> web.Response:
    """View project details

    View a private project

    :param project_id: Project unique identifier
    :type project_id: int

    """
    return web.Response(status=200)


async def private_project_leave(request: web.Request, project_id) -> web.Response:
    """Private Project Leave

    Please note: project&#39;s owner cannot leave the project.

    :param project_id: Project unique identifier
    :type project_id: int

    """
    return web.Response(status=200)


async def private_project_note(request: web.Request, project_id, note_id) -> web.Response:
    """Project note details

    

    :param project_id: Project unique identifier
    :type project_id: int
    :param note_id: Note unique identifier
    :type note_id: int

    """
    return web.Response(status=200)


async def private_project_note_delete(request: web.Request, project_id, note_id) -> web.Response:
    """Delete project note

    

    :param project_id: Project unique identifier
    :type project_id: int
    :param note_id: Note unique identifier
    :type note_id: int

    """
    return web.Response(status=200)


async def private_project_note_update(request: web.Request, project_id, note_id, body) -> web.Response:
    """Update project note

    

    :param project_id: Project unique identifier
    :type project_id: int
    :param note_id: Note unique identifier
    :type note_id: int
    :param body: Note message
    :type body: dict | bytes

    """
    body = ProjectNoteCreate.from_dict(body)
    return web.Response(status=200)


async def private_project_notes_create(request: web.Request, project_id, body) -> web.Response:
    """Create project note

    Create a new project note

    :param project_id: Project unique identifier
    :type project_id: int
    :param body: Note message
    :type body: dict | bytes

    """
    body = ProjectNoteCreate.from_dict(body)
    return web.Response(status=200)


async def private_project_notes_list(request: web.Request, project_id, page=None, page_size=None, limit=None, offset=None) -> web.Response:
    """List project notes

    List project notes

    :param project_id: Project unique identifier
    :type project_id: int
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    return web.Response(status=200)


async def private_project_publish(request: web.Request, project_id) -> web.Response:
    """Private Project Publish

    Publish a project. Possible after all items inside it are public

    :param project_id: Project unique identifier
    :type project_id: int

    """
    return web.Response(status=200)


async def private_project_update(request: web.Request, project_id, body) -> web.Response:
    """Update project

    Updating an project by passing body parameters; request can also be made with the PATCH method.

    :param project_id: Project unique identifier
    :type project_id: int
    :param body: Project description
    :type body: dict | bytes

    """
    body = ProjectUpdate.from_dict(body)
    return web.Response(status=200)


async def private_projects_list(request: web.Request, page=None, page_size=None, limit=None, offset=None, order=None, order_direction=None, storage=None, roles=None) -> web.Response:
    """Private Projects

    List private projects

    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int
    :param order: The field by which to order.
    :type order: str
    :param order_direction: 
    :type order_direction: str
    :param storage: only return collections from this institution
    :type storage: str
    :param roles: Any combination of owner, collaborator, viewer separated by comma. Examples: \&quot;owner\&quot; or \&quot;owner,collaborator\&quot;.
    :type roles: str

    """
    return web.Response(status=200)


async def private_projects_search(request: web.Request, body=None) -> web.Response:
    """Private Projects search

    Search inside the private projects

    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = ProjectsSearch.from_dict(body)
    return web.Response(status=200)


async def project_articles(request: web.Request, project_id) -> web.Response:
    """Public Project Articles

    List articles in project

    :param project_id: Project Unique identifier
    :type project_id: int

    """
    return web.Response(status=200)


async def project_details(request: web.Request, project_id) -> web.Response:
    """Public Project

    View a project

    :param project_id: Project Unique identifier
    :type project_id: int

    """
    return web.Response(status=200)


async def projects_list(request: web.Request, x_cursor=None, page=None, page_size=None, limit=None, offset=None, order=None, order_direction=None, institution=None, published_since=None, group=None) -> web.Response:
    """Public Projects

    Returns a list of public projects

    :param x_cursor: Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    :type x_cursor: str
    :type x_cursor: str
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int
    :param order: The field by which to order. Default varies by endpoint/resource.
    :type order: str
    :param order_direction: 
    :type order_direction: str
    :param institution: only return collections from this institution
    :type institution: int
    :param published_since: Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    :type published_since: str
    :param group: only return collections from this group
    :type group: int

    """
    return web.Response(status=200)


async def projects_search(request: web.Request, x_cursor=None, body=None) -> web.Response:
    """Public Projects Search

    Returns a list of public articles

    :param x_cursor: Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    :type x_cursor: str
    :type x_cursor: str
    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = ProjectsSearch.from_dict(body)
    return web.Response(status=200)
