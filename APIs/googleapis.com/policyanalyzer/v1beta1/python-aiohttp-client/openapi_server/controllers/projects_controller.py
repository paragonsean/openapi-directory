from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_policyanalyzer_v1beta1_query_activity_response import GoogleCloudPolicyanalyzerV1beta1QueryActivityResponse
from openapi_server import util


async def policyanalyzer_projects_locations_activity_types_activities_query(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """policyanalyzer_projects_locations_activity_types_activities_query

    Queries policy activities on GCP resources.

    :param parent: Required. The container resource on which to execute the request. Acceptable formats: &#x60;projects/[PROJECT_ID|PROJECT_NUMBER]/locations/[LOCATION]/activityTypes/[ACTIVITY_TYPE]&#x60; LOCATION here refers to GCP Locations: https://cloud.google.com/about/locations/
    :type parent: str
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
    :param filter: Optional. Optional filter expression to restrict the activities returned. Supported filters are: - service_account_last_authn.full_resource_name {&#x3D;} - service_account_key_last_authn.full_resource_name {&#x3D;} 
    :type filter: str
    :param page_size: Optional. The maximum number of results to return from this request. Max limit is 1000. Non-positive values are ignored. The presence of &#x60;nextPageToken&#x60; in the response indicates that more results might be available.
    :type page_size: int
    :param page_token: Optional. If present, then retrieve the next batch of results from the preceding call to this method. &#x60;pageToken&#x60; must be the value of &#x60;nextPageToken&#x60; from the previous response. The values of other method parameters should be identical to those in the previous call.
    :type page_token: str

    """
    return web.Response(status=200)
