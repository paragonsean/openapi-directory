from typing import List, Dict
from aiohttp import web

from openapi_server.models.apis_json import ApisJson
from openapi_server.models.closable_comment import ClosableComment
from openapi_server.models.comments_batch import CommentsBatch
from openapi_server.models.fork_version import ForkVersion
from openapi_server.models.lifecycle_settings import LifecycleSettings
from openapi_server.models.template_wrapper import TemplateWrapper
from openapi_server.models.visibility_settings import VisibilitySettings
from openapi_server import util


async def delete_template(request: web.Request, owner, template_id) -> web.Response:
    """Delete a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str

    """
    return web.Response(status=200)


async def delete_template_version(request: web.Request, owner, template_id, version) -> web.Response:
    """Delete a particular version of a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def fork_template(request: web.Request, owner, template_id, version, body) -> web.Response:
    """Create a fork for a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str
    :param body: Fork version information
    :type body: dict | bytes

    """
    body = ForkVersion.from_dict(body)
    return web.Response(status=200)


async def get_template_comments(request: web.Request, owner, template_id, version) -> web.Response:
    """Return the list of comments for a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_template_definition(request: web.Request, owner, template_id, version, flatten=None) -> web.Response:
    """Retrieve a template definition

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str
    :param flatten: If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    :type flatten: bool

    """
    return web.Response(status=200)


async def get_template_lifecycle_settings(request: web.Request, owner, template_id, version) -> web.Response:
    """Retrieve lifecycle settings for a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_template_private_settings(request: web.Request, owner, template_id, version) -> web.Response:
    """Retrieve visibility settings for a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_template_versions(request: web.Request, owner, template_id) -> web.Response:
    """Retrieve an APIs.json listing for all template versions for an owner and template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str

    """
    return web.Response(status=200)


async def get_templates(request: web.Request, owner=None) -> web.Response:
    """Retrieve a list of templates for an owner

    

    :param owner: Owner name
    :type owner: str

    """
    return web.Response(status=200)


async def rename_template(request: web.Request, owner, template_id, new_name) -> web.Response:
    """Rename a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param new_name: New name
    :type new_name: str

    """
    return web.Response(status=200)


async def save_template_definition(request: web.Request, owner, template_id, body, is_private=None, version=None, force=None, project_name=None) -> web.Response:
    """Create or update a template

    Saves the provided template definition; the owner must match the token owner. The version will be extracted from the template definitions itself.

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param body: The template definition
    :type body: str
    :param is_private: Defines whether the API or template has to be private
    :type is_private: bool
    :param version: Template version to create or update. If omitted, the version will be taken from the &#x60;info.version&#x60; field in the definition.
    :type version: str
    :param force: Force update
    :type force: bool
    :param project_name: The project to add the API, domain, or template to
    :type project_name: str

    """
    return web.Response(status=200)


async def search_apis_and_domains_1(request: web.Request, spec_type=None, visibility=None, state=None, owner=None, query=None, page=None, limit=None, sort=None, order=None) -> web.Response:
    """Retrieve a list of currently defined APIs, domains, and templates in APIs.json format

    

    :param spec_type: Type of definitions to search: * API - APIs only * DOMAIN - domains only * TEMPLATE - templates only * ANY - APIs, domains, and templates 
    :type spec_type: str
    :param visibility: The visibility of a definition in SwaggerHub: * PUBLIC - can be viewed by anyone * PRIVATE - can only be viewed by you or your organization and those that you are collaborating with or have shared it with * ANY - either PUBLIC or PRIVATE 
    :type visibility: str
    :param state: Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
    :type state: str
    :param owner: API or domain owner. Can be username or organization name. Case-sensitive.
    :type owner: str
    :param query: Free text query to match
    :type query: str
    :param page: Page to return
    :type page: int
    :param limit: Number of results per page (1 .. 100)
    :type limit: int
    :param sort: Sort criteria of result set: * NAME * UPDATED * CREATED * OWNER * BEST_MATCH - by relevance * TITLE - by &#x60;info.title&#x60; 
    :type sort: str
    :param order: Sort order
    :type order: str

    """
    return web.Response(status=200)


async def set_template_lifecycle_settings(request: web.Request, owner, template_id, version, body, force=None) -> web.Response:
    """Update lifecycle settings for a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str
    :param body: Fork version information
    :type body: dict | bytes
    :param force: Force update
    :type force: bool

    """
    body = LifecycleSettings.from_dict(body)
    return web.Response(status=200)


async def set_template_private_settings(request: web.Request, owner, template_id, version, body) -> web.Response:
    """Update visibility settings for a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str
    :param body: Private settings
    :type body: dict | bytes

    """
    body = VisibilitySettings.from_dict(body)
    return web.Response(status=200)


async def update_template_comments(request: web.Request, owner, template_id, version, body) -> web.Response:
    """Update the list of comments for a template

    

    :param owner: API, domain, or template owner identifier (case-sensitive)
    :type owner: str
    :param template_id: Template identifier
    :type template_id: str
    :param version: Version identifier
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = CommentsBatch.from_dict(body)
    return web.Response(status=200)
