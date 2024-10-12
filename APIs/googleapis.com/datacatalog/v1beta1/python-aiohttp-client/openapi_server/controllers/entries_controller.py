from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_datacatalog_v1beta1_entry import GoogleCloudDatacatalogV1beta1Entry
from openapi_server import util


async def datacatalog_entries_lookup(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, linked_resource=None, sql_resource=None) -> web.Response:
    """datacatalog_entries_lookup

    Get an entry by target resource name. This method allows clients to use the resource name from the source Google Cloud Platform service to get the Data Catalog Entry.

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
    :param linked_resource: The full name of the Google Cloud Platform resource the Data Catalog entry represents. See: https://cloud.google.com/apis/design/resource_names#full_resource_name. Full names are case-sensitive. Examples: * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId * //pubsub.googleapis.com/projects/projectId/topics/topicId
    :type linked_resource: str
    :param sql_resource: The SQL name of the entry. SQL names are case-sensitive. Examples: * &#x60;pubsub.project_id.topic_id&#x60; * &#x60;&#x60;pubsub.project_id.&#x60;topic.id.with.dots&#x60; &#x60;&#x60; * &#x60;bigquery.table.project_id.dataset_id.table_id&#x60; * &#x60;bigquery.dataset.project_id.dataset_id&#x60; * &#x60;datacatalog.entry.project_id.location_id.entry_group_id.entry_id&#x60; &#x60;*_id&#x60;s should satisfy the standard SQL rules for identifiers. https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical.
    :type sql_resource: str

    """
    return web.Response(status=200)
