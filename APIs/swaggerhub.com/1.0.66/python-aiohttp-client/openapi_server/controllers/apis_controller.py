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
from openapi_server.models.standardization_result import StandardizationResult
from openapi_server.models.validation_result import ValidationResult
from openapi_server.models.visibility_settings import VisibilitySettings
from openapi_server import util


async def add_api_comment_reply_v2(request: web.Request, owner, api, version, comment, body) -> web.Response:
    """Reply to a comment

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewReply.from_dict(body)
    return web.Response(status=200)


async def add_api_comment_v2(request: web.Request, owner, api, version, body) -> web.Response:
    """Add a new comment

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewComment.from_dict(body)
    return web.Response(status=200)


async def clone_api(request: web.Request, owner, api, version, new_version) -> web.Response:
    """Create a new API version

    Use this operation to clone an existing API version as a new version. The new version will have the same YAML content but with updated &#x60;info.version&#x60;.  **Note:** Comments, integrations, and codegen options are not copied to the new version. The default version also remains unchanged.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: The version to clone (case-sensitive)
    :type version: str
    :param new_version: An object that contains the new version number and other parameters. The version number must be in the format described in the [documentation](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format).
    :type new_version: dict | bytes

    """
    new_version = NewVersion.from_dict(new_version)
    return web.Response(status=200)


async def delete_api(request: web.Request, owner, api) -> web.Response:
    """Delete an API

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str

    """
    return web.Response(status=200)


async def delete_api_comment_reply_v2(request: web.Request, owner, api, version, comment, reply) -> web.Response:
    """Delete a comment reply

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param reply: Reply identifier
    :type reply: str

    """
    return web.Response(status=200)


async def delete_api_comment_v2(request: web.Request, owner, api, version, comment) -> web.Response:
    """Delete a comment

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str

    """
    return web.Response(status=200)


async def delete_api_version(request: web.Request, owner, api, version) -> web.Response:
    """Delete an API version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def fork_api(request: web.Request, owner, api, version, fork_version) -> web.Response:
    """Fork an API

    Creates a [fork](https://support.smartbear.com/swaggerhub/docs/apis/forking-api.html) of the specified API definition and version. The fork can be created as a new API, or as a new version in another existing API.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param fork_version: Fork parameters
    :type fork_version: dict | bytes

    """
    fork_version = ForkVersion.from_dict(fork_version)
    return web.Response(status=200)


async def get_api_comments_v2(request: web.Request, owner, api, version) -> web.Response:
    """Get comments for the specified API version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_api_default_version(request: web.Request, owner, api) -> web.Response:
    """Get the default version of an API

    This operation returns the version identifier, such as &#x60;1.0.0&#x60;. To get the definition itself, use &#x60;GET /apis/{owner}/{api}/{version}&#x60;.

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str

    """
    return web.Response(status=200)


async def get_api_versions(request: web.Request, owner, api) -> web.Response:
    """Get a list of API versions

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str

    """
    return web.Response(status=200)


async def get_definition(request: web.Request, owner, api, version, resolved=None, flatten=None) -> web.Response:
    """Get the OpenAPI definition of the specified API version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param resolved: Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
    :type resolved: bool
    :param flatten: If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    :type flatten: bool

    """
    return web.Response(status=200)


async def get_json_definition(request: web.Request, owner, api, version, resolved=None, flatten=None) -> web.Response:
    """Get the OpenAPI definition for the specified API version in JSON format

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param resolved: Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
    :type resolved: bool
    :param flatten: If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    :type flatten: bool

    """
    return web.Response(status=200)


async def get_lifecycle_settings(request: web.Request, owner, api, version) -> web.Response:
    """Get the published status for the specified API and version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_owner_apis(request: web.Request, owner, page=None, limit=None, sort=None, order=None) -> web.Response:
    """Get a list of APIs of the specified owner

    

    :param owner: API owner (organization or user, case-sensitive)
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


async def get_private_settings(request: web.Request, owner, api, version) -> web.Response:
    """Get the visibility (public or private) of API version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_standardization_errors(request: web.Request, owner, api, version) -> web.Response:
    """Retrieve the standardization errors for a given API definition

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: 
    :type api: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_validation(request: web.Request, owner, api, version) -> web.Response:
    """Deprecated Get API Standardization errors and warnings

    **Note:** This endpoint is deprecated. Use the following new endpoint instead: GET /apis/{owner}/{api}/{version}/standardization   If your organization has [API standardization](https://support.smartbear.com/swaggerhub/docs/organizations/api-standardization.html) configured, you can use this operation to validate a specific API version and get a list of errors or warnings with line numbers.  This operation checks for standardization errors only and does not return OpenAPI syntax errors (such as misspelled keywords) or YAML syntax errors.

    :param owner: Organization name (case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_yaml_definition(request: web.Request, owner, api, version, resolved=None, flatten=None) -> web.Response:
    """Get the OpenAPI definition for the specified API version in YAML format

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param resolved: Set to true to get the resolved version of the API definition. The content of all external $refs will be included in the resulting file.
    :type resolved: bool
    :param flatten: If set to &#x60;true&#x60;, it creates models from inline schemas in OpenAPI definition. AsyncAPI definitions cannot be flattened.
    :type flatten: bool

    """
    return web.Response(status=200)


async def rename_api(request: web.Request, owner, api, new_name) -> web.Response:
    """Rename an API

    The new name must follow the [naming rules](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html).

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param new_name: New name
    :type new_name: str

    """
    return web.Response(status=200)


async def save_definition(request: web.Request, owner, api, definition, is_private=None, version=None, force=None) -> web.Response:
    """Create or update an API

    Use this operation to create a new API or update an existing API by uploading its OpenAPI definition in YAML or JSON format. The authenticating user must have permissions to create or update APIs in the specified &#x60;owner&#x60; account.  The API name and version must follow SwaggerHub naming rules, otherwise the request will be rejected. Refer to:    * [API name format](https://support.smartbear.com/swaggerhub/docs/apis/creating-api.html)  * [Version format](https://support.smartbear.com/swaggerhub/docs/apis/versioning.html#format)   When a new version of an existing API is created, it does not automatically become the default version. You can use &#x60;PUT /apis/{owner}/{api}/settings/default&#x60; to set the default version.  ### cURL example Line breaks are added for readability.      curl -X POST \&quot;https://api.swaggerhub.com/apis/OWNER/API_TO_CREATE_OR_UPDATE\&quot;          -H \&quot;Authorization: SWAGGERHUB_API_KEY\&quot;          -H \&quot;Content-Type: application/yaml\&quot;          --data-binary @C:\\work\\swagger.yaml  **Note:** Use &#x60;--data-binary&#x60; (not &#x60;-d&#x60;) when uploading YAML files using cURL, and remember to specify the correct &#x60;Content-Type&#x60; header.

    :param owner: API owner name (organization or user name, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param definition: OpenAPI definition in the YAML or JSON format. The content must be syntactically valid YAML or JSON.
    :type definition: str
    :param is_private: Whether to make the API private (&#x60;true&#x60;) or public (&#x60;false&#x60;)
    :type is_private: bool
    :param version: API version to create or update. If omitted, the version is extracted from the &#x60;info.version&#x60; field of the provided OpenAPI definition.  Either the &#x60;version&#x60; parameter or the &#x60;info.version&#x60; value must be specified, otherwise the request will be rejected. If both are specified, the &#x60;version&#x60; parameter overrides the &#x60;info.version&#x60; value.  If this API version already exists, it will be updated with the new definition (unless that version has been published - in this case the update will be rejected).
    :type version: str
    :param force: Force update
    :type force: bool

    """
    return web.Response(status=200)


async def search_apis(request: web.Request, query=None, state=None, page=None, limit=None, sort=None, order=None) -> web.Response:
    """Search APIs

    This is a convenience alias for &#x60;GET /specs?specType&#x3D;API&#x60;.

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


async def search_apis_and_domains(request: web.Request, spec_type=None, visibility=None, state=None, owner=None, query=None, page=None, limit=None, sort=None, order=None) -> web.Response:
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


async def set_api_comment_status_v2(request: web.Request, owner, api, version, comment, status) -> web.Response:
    """Resolve or reopen a comment

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param status: Comment status
    :type status: str

    """
    return web.Response(status=200)


async def set_api_default_version(request: web.Request, owner, api, default_version) -> web.Response:
    """Set the default API version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param default_version: An object that specifies the default version for this API
    :type default_version: dict | bytes

    """
    default_version = DefaultVersion.from_dict(default_version)
    return web.Response(status=200)


async def set_lifecycle_settings(request: web.Request, owner, api, version, settings, force=None) -> web.Response:
    """Publish or unpublish an API version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param settings: An object that specifies the new &#x60;published&#x60; state: &#x60;true&#x60; means published, &#x60;false&#x60; - unpublished
    :type settings: dict | bytes
    :param force: To publish an API that references _unpublished_ domains, this parameter must be &#x60;true&#x60;. Otherwise, the request will be rejected with status code 424.
    :type force: bool

    """
    settings = LifecycleSettings.from_dict(settings)
    return web.Response(status=200)


async def set_private_settings(request: web.Request, owner, api, version, settings) -> web.Response:
    """Set the visibility (public or private) of an API version

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param settings: An object that specifies the new visibility level: &#x60;true&#x60; means private, &#x60;false&#x60; - public
    :type settings: dict | bytes

    """
    settings = VisibilitySettings.from_dict(settings)
    return web.Response(status=200)


async def update_api_comment_reply_v2(request: web.Request, owner, api, version, comment, reply, body=None) -> web.Response:
    """Update a comment reply

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
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


async def update_api_comment_v2(request: web.Request, owner, api, version, comment, body=None) -> web.Response:
    """Update a comment

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param comment: Comment identifier
    :type comment: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClosableCommentPatch.from_dict(body)
    return web.Response(status=200)


async def update_api_comments_v2(request: web.Request, owner, api, version, body) -> web.Response:
    """Bulk update comments

    

    :param owner: API owner (organization or user, case-sensitive)
    :type owner: str
    :param api: API name (case-sensitive)
    :type api: str
    :param version: Version identifier
    :type version: str
    :param body: 
    :type body: dict | bytes

    """
    body = CommentsBatch.from_dict(body)
    return web.Response(status=200)
