from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_datacatalog_v1_entry import GoogleCloudDatacatalogV1Entry
from openapi_server import util


async def datacatalog_entries_lookup(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, fully_qualified_name=None, linked_resource=None, location=None, project=None, sql_resource=None) -> web.Response:
    """datacatalog_entries_lookup

    Gets an entry by its target resource name. The resource name comes from the source Google Cloud Platform service.

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
    :param fully_qualified_name: [Fully Qualified Name (FQN)](https://cloud.google.com//data-catalog/docs/fully-qualified-names) of the resource. FQNs take two forms: * For non-regionalized resources: &#x60;{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}&#x60; * For regionalized resources: &#x60;{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}&#x60; Example for a DPMS table: &#x60;dataproc_metastore:{PROJECT_ID}.{LOCATION_ID}.{INSTANCE_ID}.{DATABASE_ID}.{TABLE_ID}&#x60;
    :type fully_qualified_name: str
    :param linked_resource: The full name of the Google Cloud Platform resource the Data Catalog entry represents. For more information, see [Full Resource Name] (https://cloud.google.com/apis/design/resource_names#full_resource_name). Full names are case-sensitive. For example: * &#x60;//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}&#x60; * &#x60;//pubsub.googleapis.com/projects/{PROJECT_ID}/topics/{TOPIC_ID}&#x60;
    :type linked_resource: str
    :param location: Location where the lookup should be performed. Required to lookup entry that is not a part of &#x60;DPMS&#x60; or &#x60;DATAPLEX&#x60; &#x60;integrated_system&#x60; using its &#x60;fully_qualified_name&#x60;. Ignored in other cases.
    :type location: str
    :param project: Project where the lookup should be performed. Required to lookup entry that is not a part of &#x60;DPMS&#x60; or &#x60;DATAPLEX&#x60; &#x60;integrated_system&#x60; using its &#x60;fully_qualified_name&#x60;. Ignored in other cases.
    :type project: str
    :param sql_resource: The SQL name of the entry. SQL names are case-sensitive. Examples: * &#x60;pubsub.topic.{PROJECT_ID}.{TOPIC_ID}&#x60; * &#x60;pubsub.topic.{PROJECT_ID}.&#x60;\\&#x60;&#x60;{TOPIC.ID.SEPARATED.WITH.DOTS}&#x60;\\&#x60; * &#x60;bigquery.table.{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}&#x60; * &#x60;bigquery.dataset.{PROJECT_ID}.{DATASET_ID}&#x60; * &#x60;datacatalog.entry.{PROJECT_ID}.{LOCATION_ID}.{ENTRY_GROUP_ID}.{ENTRY_ID}&#x60; Identifiers (&#x60;*_ID&#x60;) should comply with the [Lexical structure in Standard SQL] (https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical).
    :type sql_resource: str

    """
    return web.Response(status=200)
