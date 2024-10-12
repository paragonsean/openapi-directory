from typing import List, Dict
from aiohttp import web

from openapi_server.models.apis_json import ApisJson
from openapi_server.models.closable_comment import ClosableComment
from openapi_server.models.closable_comment_patch import ClosableCommentPatch
from openapi_server.models.comment import Comment
from openapi_server.models.comment_patch import CommentPatch
from openapi_server.models.comments_batch import CommentsBatch
from openapi_server.models.default_version import DefaultVersion
from openapi_server.models.fork_version import ForkVersion
from openapi_server.models.lifecycle_settings import LifecycleSettings
from openapi_server.models.new_comment import NewComment
from openapi_server.models.new_reply import NewReply
from openapi_server.models.new_version import NewVersion
from openapi_server.models.visibility_settings import VisibilitySettings
from openapi_server import util


async def add_domain_comment_reply_v2(request: web.Request, owner, domain, version, comment, body) -> web.Response:
    """Reply to a comment

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewReply.from_dict(body)
    return web.Response(status=200)


async def add_domain_comment_v2(request: web.Request, owner, domain, version, body) -> web.Response:
    """Add a new comment

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewComment.from_dict(body)
    return web.Response(status=200)


async def clone_domain(request: web.Request, owner, domain, version, new_version) -> web.Response:
    """Create a new domain version

    Use this operation to clone an existing domain version as a new version.  Note that the new version is not automatically set as the default version.

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: The version to clone (case-sensitive)
    :type version: str
    :param new_version: An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format).
    :type new_version: dict | bytes

    """
    new_version = NewVersion.from_dict(new_version)
    return web.Response(status=200)


async def delete_domain(request: web.Request, owner, domain, force=None) -> web.Response:
    """Delete a domain

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param force: If this domain is referenced from other APIs and domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424.
    :type force: bool

    """
    return web.Response(status=200)


async def delete_domain_comment_reply_v2(request: web.Request, owner, domain, version, comment, reply) -> web.Response:
    """Delete a comment reply

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param reply: Reply identifier
    :type reply: str

    """
    return web.Response(status=200)


async def delete_domain_comment_v2(request: web.Request, owner, domain, version, comment) -> web.Response:
    """Delete a comment

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str

    """
    return web.Response(status=200)


async def delete_domain_version(request: web.Request, owner, domain, version, force=None) -> web.Response:
    """Delete a domain version

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param force: If this domain version is referenced from other APIs and domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424.
    :type force: bool

    """
    return web.Response(status=200)


async def fork_domain(request: web.Request, owner, domain, version, fork_version) -> web.Response:
    """Fork a domain

    Creates a [fork](https://support.smartbear.com/swaggerhub/docs/apis/forking-api.html) of the specified domain definition and version. The fork can be created as a new domain, or as a new version in another existing domain.

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param fork_version: Fork parameters
    :type fork_version: dict | bytes

    """
    fork_version = ForkVersion.from_dict(fork_version)
    return web.Response(status=200)


async def get_domain_comments_v2(request: web.Request, owner, domain, version) -> web.Response:
    """Get comments for the specified domain version

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_domain_default_version(request: web.Request, owner, domain) -> web.Response:
    """Get the default version of a domain

    This operation returns the version identifier, such as &#x60;1.0.0&#x60;. To get the definition itself, use &#x60;GET /domains/{owner}/{domain}/{version}&#x60;.

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str

    """
    return web.Response(status=200)


async def get_domain_definition(request: web.Request, owner, domain, version) -> web.Response:
    """Get the OpenAPI definition of the specified domain version

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_domain_json_definition(request: web.Request, owner, domain, version) -> web.Response:
    """Get the OpenAPI definition for the specified domain version in JSON format

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_domain_lifecycle_settings(request: web.Request, owner, domain, version) -> web.Response:
    """Get the published status for the specified domain and version

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_domain_private_settings(request: web.Request, owner, domain, version) -> web.Response:
    """Get the visibility (public or private) of a domain version

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_domain_versions(request: web.Request, owner, domain) -> web.Response:
    """Get a list of domain versions

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str

    """
    return web.Response(status=200)


async def get_domain_yaml_definition(request: web.Request, owner, domain, version) -> web.Response:
    """Get the OpenAPI definition for the specified domain version in YAML format

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_owner_domains(request: web.Request, owner, page=None, limit=None, sort=None, order=None) -> web.Response:
    """Get a list of domains of the specified owner

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
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


async def rename_domain(request: web.Request, owner, domain, new_name, force=None) -> web.Response:
    """Rename a domain

    The new name must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html).

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param new_name: New name
    :type new_name: str
    :param force: If this domain is referenced from other APIs and domains, this parameter must be true. Otherwise, the request will be rejected with status code 424.
    :type force: bool

    """
    return web.Response(status=200)


async def save_domain_definition(request: web.Request, owner, domain, is_private=None, version=None, force=None, definition=None) -> web.Response:
    """Create or update a domain

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param is_private: Specifies whether the domain has to be private
    :type is_private: bool
    :param version: Domain version. If omitted, will be taken from the &#x60;info.version&#x60; field in the definition.
    :type version: str
    :param force: Force update
    :type force: bool
    :param definition: OpenAPI definition of this domain
    :type definition: str

    """
    return web.Response(status=200)


async def search_apis_and_domains_0(request: web.Request, spec_type=None, visibility=None, state=None, owner=None, query=None, page=None, limit=None, sort=None, order=None) -> web.Response:
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


async def search_domains(request: web.Request, query=None, state=None, page=None, limit=None, sort=None, order=None) -> web.Response:
    """Search domains

    This is a convenience alias for &#x60;GET /specs?specType&#x3D;DOMAIN&#x60;.

    :param query: Free text query to match
    :type query: str
    :param state: Matches against published state of the spec: * UNPUBLISHED - spec is a draft, a work in progress * PUBLISHED - spec is a stable version ready for consuming from client applications * ANY - either PUBLISHED or UNPUBLISHED 
    :type state: str
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


async def set_domain_comment_status_v2(request: web.Request, owner, domain, version, comment, status) -> web.Response:
    """Resolve or reopen a comment

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param status: Comment status
    :type status: str

    """
    return web.Response(status=200)


async def set_domain_default_version(request: web.Request, owner, domain, default_version) -> web.Response:
    """Set the default version for a domain

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param default_version: An object that specifies the default version for this domain
    :type default_version: dict | bytes

    """
    default_version = DefaultVersion.from_dict(default_version)
    return web.Response(status=200)


async def set_domain_lifecycle_settings(request: web.Request, owner, domain, version, settings, force=None) -> web.Response:
    """Publish or unpublish a domain version

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param settings: An object that specifies the new &#x60;published&#x60; state: &#x60;true&#x60; means published, &#x60;false&#x60; - unpublished
    :type settings: dict | bytes
    :param force: To publish a domain that references other _unpublished_ domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424.
    :type force: bool

    """
    settings = LifecycleSettings.from_dict(settings)
    return web.Response(status=200)


async def set_domain_private_settings(request: web.Request, owner, domain, version, settings, force=None) -> web.Response:
    """Set the visibility (public or private) of a domain version

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param settings: An object that specifies the new visibility level: &#x60;true&#x60; means private, &#x60;false&#x60; - public
    :type settings: dict | bytes
    :param force: To change the visibility from _public_ to _private_ in case this domain is referenced from other _public_ definitions, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424.
    :type force: bool

    """
    settings = VisibilitySettings.from_dict(settings)
    return web.Response(status=200)


async def update_domain_comment_reply_v2(request: web.Request, owner, domain, version, comment, reply, body=None) -> web.Response:
    """Update a comment reply

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param reply: Reply identifier
    :type reply: str
    :param body: 
    :type body: dict | bytes

    """
    body = CommentPatch.from_dict(body)
    return web.Response(status=200)


async def update_domain_comment_v2(request: web.Request, owner, domain, version, comment, body=None) -> web.Response:
    """Update a comment

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClosableCommentPatch.from_dict(body)
    return web.Response(status=200)


async def update_domain_comments_v2(request: web.Request, owner, domain, version, body) -> web.Response:
    """Bulk update comments

    

    :param owner: Domain owner (organization or user, case-sensitive)
    :type owner: str
    :param domain: Domain name (case-sensitive)
    :type domain: str
    :param version: Version identifier
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = CommentsBatch.from_dict(body)
    return web.Response(status=200)
