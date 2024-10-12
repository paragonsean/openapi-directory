from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_asset_v1p7beta1_export_assets_request import GoogleCloudAssetV1p7beta1ExportAssetsRequest
from openapi_server.models.operation import Operation
from openapi_server import util


async def cloudasset_export_assets(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """cloudasset_export_assets

    Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a google.cloud.asset.v1p7beta1.Asset in the JSON format; for BigQuery table destinations, the output table stores the fields in asset proto as columns. This API implements the google.longrunning.Operation API , which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

    :param parent: Required. The relative name of the root asset. This can only be an organization number (such as \&quot;organizations/123\&quot;), a project ID (such as \&quot;projects/my-project-id\&quot;), or a project number (such as \&quot;projects/12345\&quot;), or a folder number (such as \&quot;folders/123\&quot;).
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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudAssetV1p7beta1ExportAssetsRequest.from_dict(body)
    return web.Response(status=200)
