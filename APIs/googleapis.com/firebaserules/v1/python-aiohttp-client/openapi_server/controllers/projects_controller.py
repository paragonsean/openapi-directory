from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_release_executable_response import GetReleaseExecutableResponse
from openapi_server.models.list_releases_response import ListReleasesResponse
from openapi_server.models.list_rulesets_response import ListRulesetsResponse
from openapi_server.models.release import Release
from openapi_server.models.ruleset import Ruleset
from openapi_server.models.test_ruleset_request import TestRulesetRequest
from openapi_server.models.test_ruleset_response import TestRulesetResponse
from openapi_server.models.update_release_request import UpdateReleaseRequest
from openapi_server import util


async def firebaserules_projects_releases_create(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebaserules_projects_releases_create

    Create a &#x60;Release&#x60;. Release names should reflect the developer&#39;s deployment practices. For example, the release name may include the environment name, application name, application version, or any other name meaningful to the developer. Once a &#x60;Release&#x60; refers to a &#x60;Ruleset&#x60;, the rules can be enforced by Firebase Rules-enabled services. More than one &#x60;Release&#x60; may be &#39;live&#39; concurrently. Consider the following three &#x60;Release&#x60; names for &#x60;projects/foo&#x60; and the &#x60;Ruleset&#x60; to which they refer. Release Name -&gt; Ruleset Name * projects/foo/releases/prod -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/beta -&gt; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/v23 -&gt; projects/foo/rulesets/uuid456 The relationships reflect a &#x60;Ruleset&#x60; rollout in progress. The &#x60;prod&#x60; and &#x60;prod/beta&#x60; releases refer to the same &#x60;Ruleset&#x60;. However, &#x60;prod/v23&#x60; refers to a new &#x60;Ruleset&#x60;. The &#x60;Ruleset&#x60; reference for a &#x60;Release&#x60; may be updated using the UpdateRelease method.

    :param name: Required. Resource name for the project which owns this &#x60;Release&#x60;. Format: &#x60;projects/{project_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Release.from_dict(body)
    return web.Response(status=200)


async def firebaserules_projects_releases_get_executable(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, executable_version=None) -> web.Response:
    """firebaserules_projects_releases_get_executable

    Get the &#x60;Release&#x60; executable to use when enforcing rules.

    :param name: Required. Resource name of the &#x60;Release&#x60;. Format: &#x60;projects/{project_id}/releases/{release_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param executable_version: The requested runtime executable version. Defaults to FIREBASE_RULES_EXECUTABLE_V1.
    :type executable_version: str

    """
    return web.Response(status=200)


async def firebaserules_projects_releases_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firebaserules_projects_releases_list

    List the &#x60;Release&#x60; values for a project. This list may optionally be filtered by &#x60;Release&#x60; name, &#x60;Ruleset&#x60; name, &#x60;TestSuite&#x60; name, or any combination thereof.

    :param name: Required. Resource name for the project. Format: &#x60;projects/{project_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: &#x60;Release&#x60; filter. The list method supports filters with restrictions on the &#x60;Release.name&#x60;, and &#x60;Release.ruleset_name&#x60;. Example 1: A filter of &#39;name&#x3D;prod*&#39; might return &#x60;Release&#x60;s with names within &#39;projects/foo&#39; prefixed with &#39;prod&#39;: Name -&gt; Ruleset Name: * projects/foo/releases/prod -&gt; projects/foo/rulesets/uuid1234 * projects/foo/releases/prod/v1 -&gt; projects/foo/rulesets/uuid1234 * projects/foo/releases/prod/v2 -&gt; projects/foo/rulesets/uuid8888 Example 2: A filter of &#x60;name&#x3D;prod* ruleset_name&#x3D;uuid1234&#x60; would return only &#x60;Release&#x60; instances for &#39;projects/foo&#39; with names prefixed with &#39;prod&#39; referring to the same &#x60;Ruleset&#x60; name of &#39;uuid1234&#39;: Name -&gt; Ruleset Name: * projects/foo/releases/prod -&gt; projects/foo/rulesets/1234 * projects/foo/releases/prod/v1 -&gt; projects/foo/rulesets/1234 In the examples, the filter parameters refer to the search filters are relative to the project. Fully qualified prefixed may also be used.
    :type filter: str
    :param page_size: Page size to load. Maximum of 100. Defaults to 10. Note: &#x60;page_size&#x60; is just a hint and the service may choose to load fewer than &#x60;page_size&#x60; results due to the size of the output. To traverse all of the releases, the caller should iterate until the &#x60;page_token&#x60; on the response is empty.
    :type page_size: int
    :param page_token: Next page token for the next batch of &#x60;Release&#x60; instances.
    :type page_token: str

    """
    return web.Response(status=200)


async def firebaserules_projects_releases_patch(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebaserules_projects_releases_patch

    Update a &#x60;Release&#x60; via PATCH. Only updates to &#x60;ruleset_name&#x60; will be honored. &#x60;Release&#x60; rename is not supported. To create a &#x60;Release&#x60; use the CreateRelease method.

    :param name: Required. Resource name for the project which owns this &#x60;Release&#x60;. Format: &#x60;projects/{project_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateReleaseRequest.from_dict(body)
    return web.Response(status=200)


async def firebaserules_projects_rulesets_create(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebaserules_projects_rulesets_create

    Create a &#x60;Ruleset&#x60; from &#x60;Source&#x60;. The &#x60;Ruleset&#x60; is given a unique generated name which is returned to the caller. &#x60;Source&#x60; containing syntactic or semantics errors will result in an error response indicating the first error encountered. For a detailed view of &#x60;Source&#x60; issues, use TestRuleset.

    :param name: Required. Resource name for Project which owns this &#x60;Ruleset&#x60;. Format: &#x60;projects/{project_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Ruleset.from_dict(body)
    return web.Response(status=200)


async def firebaserules_projects_rulesets_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firebaserules_projects_rulesets_delete

    Delete a &#x60;Ruleset&#x60; by resource name. If the &#x60;Ruleset&#x60; is referenced by a &#x60;Release&#x60; the operation will fail.

    :param name: Required. Resource name for the ruleset to delete. Format: &#x60;projects/{project_id}/rulesets/{ruleset_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def firebaserules_projects_rulesets_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """firebaserules_projects_rulesets_get

    Get a &#x60;Ruleset&#x60; by name including the full &#x60;Source&#x60; contents.

    :param name: Required. Resource name for the ruleset to get. Format: &#x60;projects/{project_id}/rulesets/{ruleset_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def firebaserules_projects_rulesets_list(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """firebaserules_projects_rulesets_list

    List &#x60;Ruleset&#x60; metadata only and optionally filter the results by &#x60;Ruleset&#x60; name. The full &#x60;Source&#x60; contents of a &#x60;Ruleset&#x60; may be retrieved with GetRuleset.

    :param name: Required. Resource name for the project. Format: &#x60;projects/{project_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param filter: &#x60;Ruleset&#x60; filter. The list method supports filters with restrictions on &#x60;Ruleset.name&#x60;. Filters on &#x60;Ruleset.create_time&#x60; should use the &#x60;date&#x60; function which parses strings that conform to the RFC 3339 date/time specifications. Example: &#x60;create_time &gt; date(\&quot;2017-01-01T00:00:00Z\&quot;) AND name&#x3D;UUID-*&#x60;
    :type filter: str
    :param page_size: Page size to load. Maximum of 100. Defaults to 10. Note: &#x60;page_size&#x60; is just a hint and the service may choose to load less than &#x60;page_size&#x60; due to the size of the output. To traverse all of the releases, caller should iterate until the &#x60;page_token&#x60; is empty.
    :type page_size: int
    :param page_token: Next page token for loading the next batch of &#x60;Ruleset&#x60; instances.
    :type page_token: str

    """
    return web.Response(status=200)


async def firebaserules_projects_test(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """firebaserules_projects_test

    Test &#x60;Source&#x60; for syntactic and semantic correctness. Issues present, if any, will be returned to the caller with a description, severity, and source location. The test method may be executed with &#x60;Source&#x60; or a &#x60;Ruleset&#x60; name. Passing &#x60;Source&#x60; is useful for unit testing new rules. Passing a &#x60;Ruleset&#x60; name is useful for regression testing an existing rule. The following is an example of &#x60;Source&#x60; that permits users to upload images to a bucket bearing their user id and matching the correct metadata: _*Example*_ // Users are allowed to subscribe and unsubscribe to the blog. service firebase.storage { match /users/{userId}/images/{imageName} { allow write: if userId &#x3D;&#x3D; request.auth.uid &amp;&amp; (imageName.matches(&#39;*.png$&#39;) || imageName.matches(&#39;*.jpg$&#39;)) &amp;&amp; resource.mimeType.matches(&#39;^image/&#39;) } }

    :param name: Required. Tests may either provide &#x60;source&#x60; or a &#x60;Ruleset&#x60; resource name. For tests against &#x60;source&#x60;, the resource name must refer to the project: Format: &#x60;projects/{project_id}&#x60; For tests against a &#x60;Ruleset&#x60;, this must be the &#x60;Ruleset&#x60; resource name: Format: &#x60;projects/{project_id}/rulesets/{ruleset_id}&#x60;
    :type name: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestRulesetRequest.from_dict(body)
    return web.Response(status=200)
