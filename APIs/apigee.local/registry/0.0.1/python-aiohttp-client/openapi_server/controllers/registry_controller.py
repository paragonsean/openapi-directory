from typing import List, Dict
from aiohttp import web

from openapi_server.models.api import Api
from openapi_server.models.api_deployment import ApiDeployment
from openapi_server.models.api_spec import ApiSpec
from openapi_server.models.api_version import ApiVersion
from openapi_server.models.artifact import Artifact
from openapi_server.models.list_api_deployment_revisions_response import ListApiDeploymentRevisionsResponse
from openapi_server.models.list_api_deployments_response import ListApiDeploymentsResponse
from openapi_server.models.list_api_spec_revisions_response import ListApiSpecRevisionsResponse
from openapi_server.models.list_api_specs_response import ListApiSpecsResponse
from openapi_server.models.list_api_versions_response import ListApiVersionsResponse
from openapi_server.models.list_apis_response import ListApisResponse
from openapi_server.models.list_artifacts_response import ListArtifactsResponse
from openapi_server.models.rollback_api_deployment_request import RollbackApiDeploymentRequest
from openapi_server.models.rollback_api_spec_request import RollbackApiSpecRequest
from openapi_server.models.status import Status
from openapi_server.models.tag_api_deployment_revision_request import TagApiDeploymentRevisionRequest
from openapi_server.models.tag_api_spec_revision_request import TagApiSpecRevisionRequest
from openapi_server import util


async def registry_create_api(request: web.Request, project, location, body, api_id=None) -> web.Response:
    """registry_create_api

    CreateApi creates a specified API.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param body: 
    :type body: dict | bytes
    :param api_id: Required. The ID to use for the api, which will become the final component of the api&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
    :type api_id: str

    """
    body = Api.from_dict(body)
    return web.Response(status=200)


async def registry_create_api_deployment(request: web.Request, project, location, api, body, api_deployment_id=None) -> web.Response:
    """registry_create_api_deployment

    CreateApiDeployment creates a specified deployment.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param body: 
    :type body: dict | bytes
    :param api_deployment_id: Required. The ID to use for the deployment, which will become the final component of the deployment&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
    :type api_deployment_id: str

    """
    body = ApiDeployment.from_dict(body)
    return web.Response(status=200)


async def registry_create_api_spec(request: web.Request, project, location, api, version, body, api_spec_id=None) -> web.Response:
    """registry_create_api_spec

    CreateApiSpec creates a specified spec.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param body: 
    :type body: dict | bytes
    :param api_spec_id: Required. The ID to use for the spec, which will become the final component of the spec&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
    :type api_spec_id: str

    """
    body = ApiSpec.from_dict(body)
    return web.Response(status=200)


async def registry_create_api_version(request: web.Request, project, location, api, body, api_version_id=None) -> web.Response:
    """registry_create_api_version

    CreateApiVersion creates a specified version.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param body: 
    :type body: dict | bytes
    :param api_version_id: Required. The ID to use for the version, which will become the final component of the version&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
    :type api_version_id: str

    """
    body = ApiVersion.from_dict(body)
    return web.Response(status=200)


async def registry_create_artifact(request: web.Request, project, location, body, artifact_id=None) -> web.Response:
    """registry_create_artifact

    CreateArtifact creates a specified artifact.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param body: 
    :type body: dict | bytes
    :param artifact_id: Required. The ID to use for the artifact, which will become the final component of the artifact&#39;s resource name. This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. Following AIP-162, IDs must not have the form of a UUID.
    :type artifact_id: str

    """
    body = Artifact.from_dict(body)
    return web.Response(status=200)


async def registry_delete_api(request: web.Request, project, location, api, force=None) -> web.Response:
    """registry_delete_api

    DeleteApi removes a specified API and all of the resources that it  owns.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param force: If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
    :type force: bool

    """
    return web.Response(status=200)


async def registry_delete_api_deployment(request: web.Request, project, location, api, deployment, force=None) -> web.Response:
    """registry_delete_api_deployment

    DeleteApiDeployment removes a specified deployment, all revisions, and all  child resources (e.g. artifacts).

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param deployment: The deployment id.
    :type deployment: str
    :param force: If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
    :type force: bool

    """
    return web.Response(status=200)


async def registry_delete_api_deployment_revision(request: web.Request, project, location, api, deployment) -> web.Response:
    """registry_delete_api_deployment_revision

    DeleteApiDeploymentRevision deletes a revision of a deployment.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param deployment: The deployment id.
    :type deployment: str

    """
    return web.Response(status=200)


async def registry_delete_api_spec(request: web.Request, project, location, api, version, spec, force=None) -> web.Response:
    """registry_delete_api_spec

    DeleteApiSpec removes a specified spec, all revisions, and all child  resources (e.g. artifacts).

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str
    :param force: If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
    :type force: bool

    """
    return web.Response(status=200)


async def registry_delete_api_spec_revision(request: web.Request, project, location, api, version, spec) -> web.Response:
    """registry_delete_api_spec_revision

    DeleteApiSpecRevision deletes a revision of a spec.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str

    """
    return web.Response(status=200)


async def registry_delete_api_version(request: web.Request, project, location, api, version, force=None) -> web.Response:
    """registry_delete_api_version

    DeleteApiVersion removes a specified version and all of the resources that  it owns.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param force: If set to true, any child resources will also be deleted. (Otherwise, the request will only work if there are no child resources.)
    :type force: bool

    """
    return web.Response(status=200)


async def registry_delete_artifact(request: web.Request, project, location, artifact) -> web.Response:
    """registry_delete_artifact

    DeleteArtifact removes a specified artifact.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param artifact: The artifact id.
    :type artifact: str

    """
    return web.Response(status=200)


async def registry_get_api(request: web.Request, project, location, api) -> web.Response:
    """registry_get_api

    GetApi returns a specified API.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str

    """
    return web.Response(status=200)


async def registry_get_api_deployment(request: web.Request, project, location, api, deployment) -> web.Response:
    """registry_get_api_deployment

    GetApiDeployment returns a specified deployment.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param deployment: The deployment id.
    :type deployment: str

    """
    return web.Response(status=200)


async def registry_get_api_spec(request: web.Request, project, location, api, version, spec) -> web.Response:
    """registry_get_api_spec

    GetApiSpec returns a specified spec.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str

    """
    return web.Response(status=200)


async def registry_get_api_spec_contents(request: web.Request, project, location, api, version, spec) -> web.Response:
    """registry_get_api_spec_contents

    GetApiSpecContents returns the contents of a specified spec.  If specs are stored with GZip compression, the default behavior  is to return the spec uncompressed (the mime_type response field  indicates the exact format returned).

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str

    """
    return web.Response(status=200)


async def registry_get_api_version(request: web.Request, project, location, api, version) -> web.Response:
    """registry_get_api_version

    GetApiVersion returns a specified version.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str

    """
    return web.Response(status=200)


async def registry_get_artifact(request: web.Request, project, location, artifact) -> web.Response:
    """registry_get_artifact

    GetArtifact returns a specified artifact.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param artifact: The artifact id.
    :type artifact: str

    """
    return web.Response(status=200)


async def registry_get_artifact_contents(request: web.Request, project, location, artifact) -> web.Response:
    """registry_get_artifact_contents

    GetArtifactContents returns the contents of a specified artifact.  If artifacts are stored with GZip compression, the default behavior  is to return the artifact uncompressed (the mime_type response field  indicates the exact format returned).

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param artifact: The artifact id.
    :type artifact: str

    """
    return web.Response(status=200)


async def registry_list_api_deployment_revisions(request: web.Request, project, location, api, deployment, page_size=None, page_token=None) -> web.Response:
    """registry_list_api_deployment_revisions

    ListApiDeploymentRevisions lists all revisions of a deployment.  Revisions are returned in descending order of revision creation time.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param deployment: The deployment id.
    :type deployment: str
    :param page_size: The maximum number of revisions to return per page.
    :type page_size: int
    :param page_token: The page token, received from a previous ListApiDeploymentRevisions call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def registry_list_api_deployments(request: web.Request, project, location, api, page_size=None, page_token=None, filter=None) -> web.Response:
    """registry_list_api_deployments

    ListApiDeployments returns matching deployments.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param page_size: The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListApiDeployments&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApiDeployments&#x60; must match the call that provided the page token.
    :type page_token: str
    :param filter: An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.
    :type filter: str

    """
    return web.Response(status=200)


async def registry_list_api_spec_revisions(request: web.Request, project, location, api, version, spec, page_size=None, page_token=None) -> web.Response:
    """registry_list_api_spec_revisions

    ListApiSpecRevisions lists all revisions of a spec.  Revisions are returned in descending order of revision creation time.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str
    :param page_size: The maximum number of revisions to return per page.
    :type page_size: int
    :param page_token: The page token, received from a previous ListApiSpecRevisions call. Provide this to retrieve the subsequent page.
    :type page_token: str

    """
    return web.Response(status=200)


async def registry_list_api_specs(request: web.Request, project, location, api, version, page_size=None, page_token=None, filter=None) -> web.Response:
    """registry_list_api_specs

    ListApiSpecs returns matching specs.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param page_size: The maximum number of specs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListApiSpecs&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApiSpecs&#x60; must match the call that provided the page token.
    :type page_token: str
    :param filter: An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.
    :type filter: str

    """
    return web.Response(status=200)


async def registry_list_api_versions(request: web.Request, project, location, api, page_size=None, page_token=None, filter=None) -> web.Response:
    """registry_list_api_versions

    ListApiVersions returns matching versions.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param page_size: The maximum number of versions to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListApiVersions&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApiVersions&#x60; must match the call that provided the page token.
    :type page_token: str
    :param filter: An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.
    :type filter: str

    """
    return web.Response(status=200)


async def registry_list_apis(request: web.Request, project, location, page_size=None, page_token=None, filter=None) -> web.Response:
    """registry_list_apis

    ListApis returns matching APIs.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param page_size: The maximum number of APIs to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListApis&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListApis&#x60; must match the call that provided the page token.
    :type page_token: str
    :param filter: An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields.
    :type filter: str

    """
    return web.Response(status=200)


async def registry_list_artifacts(request: web.Request, project, location, page_size=None, page_token=None, filter=None) -> web.Response:
    """registry_list_artifacts

    ListArtifacts returns matching artifacts.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param page_size: The maximum number of artifacts to return. The service may return fewer than this value. If unspecified, at most 50 values will be returned. The maximum is 1000; values above 1000 will be coerced to 1000.
    :type page_size: int
    :param page_token: A page token, received from a previous &#x60;ListArtifacts&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListArtifacts&#x60; must match the call that provided the page token.
    :type page_token: str
    :param filter: An expression that can be used to filter the list. Filters use the Common Expression Language and can refer to all message fields except contents.
    :type filter: str

    """
    return web.Response(status=200)


async def registry_replace_artifact(request: web.Request, project, location, artifact, body) -> web.Response:
    """registry_replace_artifact

    ReplaceArtifact can be used to replace a specified artifact.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param artifact: The artifact id.
    :type artifact: str
    :param body: 
    :type body: dict | bytes

    """
    body = Artifact.from_dict(body)
    return web.Response(status=200)


async def registry_rollback_api_deployment(request: web.Request, project, location, api, deployment, body) -> web.Response:
    """registry_rollback_api_deployment

    RollbackApiDeployment sets the current revision to a specified prior  revision. Note that this creates a new revision with a new revision ID.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param deployment: The deployment id.
    :type deployment: str
    :param body: 
    :type body: dict | bytes

    """
    body = RollbackApiDeploymentRequest.from_dict(body)
    return web.Response(status=200)


async def registry_rollback_api_spec(request: web.Request, project, location, api, version, spec, body) -> web.Response:
    """registry_rollback_api_spec

    RollbackApiSpec sets the current revision to a specified prior revision.  Note that this creates a new revision with a new revision ID.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str
    :param body: 
    :type body: dict | bytes

    """
    body = RollbackApiSpecRequest.from_dict(body)
    return web.Response(status=200)


async def registry_tag_api_deployment_revision(request: web.Request, project, location, api, deployment, body) -> web.Response:
    """registry_tag_api_deployment_revision

    TagApiDeploymentRevision adds a tag to a specified revision of a  deployment.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param deployment: The deployment id.
    :type deployment: str
    :param body: 
    :type body: dict | bytes

    """
    body = TagApiDeploymentRevisionRequest.from_dict(body)
    return web.Response(status=200)


async def registry_tag_api_spec_revision(request: web.Request, project, location, api, version, spec, body) -> web.Response:
    """registry_tag_api_spec_revision

    TagApiSpecRevision adds a tag to a specified revision of a spec.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str
    :param body: 
    :type body: dict | bytes

    """
    body = TagApiSpecRevisionRequest.from_dict(body)
    return web.Response(status=200)


async def registry_update_api(request: web.Request, project, location, api, body, update_mask=None, allow_missing=None) -> web.Response:
    """registry_update_api

    UpdateApi can be used to modify a specified API.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request.
    :type update_mask: str
    :param allow_missing: If set to true, and the api is not found, a new api_versions will be created. In this situation, &#x60;update_mask&#x60; is ignored.
    :type allow_missing: bool

    """
    body = Api.from_dict(body)
    return web.Response(status=200)


async def registry_update_api_deployment(request: web.Request, project, location, api, deployment, body, update_mask=None, allow_missing=None) -> web.Response:
    """registry_update_api_deployment

    UpdateApiDeployment can be used to modify a specified deployment.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param deployment: The deployment id.
    :type deployment: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request.
    :type update_mask: str
    :param allow_missing: If set to true, and the deployment is not found, a new deployment will be created. In this situation, &#x60;update_mask&#x60; is ignored.
    :type allow_missing: bool

    """
    body = ApiDeployment.from_dict(body)
    return web.Response(status=200)


async def registry_update_api_spec(request: web.Request, project, location, api, version, spec, body, update_mask=None, allow_missing=None) -> web.Response:
    """registry_update_api_spec

    UpdateApiSpec can be used to modify a specified spec.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param spec: The spec id.
    :type spec: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request.
    :type update_mask: str
    :param allow_missing: If set to true, and the spec is not found, a new spec will be created. In this situation, &#x60;update_mask&#x60; is ignored.
    :type allow_missing: bool

    """
    body = ApiSpec.from_dict(body)
    return web.Response(status=200)


async def registry_update_api_version(request: web.Request, project, location, api, version, body, update_mask=None, allow_missing=None) -> web.Response:
    """registry_update_api_version

    UpdateApiVersion can be used to modify a specified version.

    :param project: The project id.
    :type project: str
    :param location: The location id.
    :type location: str
    :param api: The api id.
    :type api: str
    :param version: The version id.
    :type version: str
    :param body: 
    :type body: dict | bytes
    :param update_mask: The list of fields to be updated. If omitted, all fields are updated that are set in the request message (fields set to default values are ignored). If a \&quot;*\&quot; is specified, all fields are updated, including fields that are unspecified/default in the request.
    :type update_mask: str
    :param allow_missing: If set to true, and the version is not found, a new version will be created. In this situation, &#x60;update_mask&#x60; is ignored.
    :type allow_missing: bool

    """
    body = ApiVersion.from_dict(body)
    return web.Response(status=200)
