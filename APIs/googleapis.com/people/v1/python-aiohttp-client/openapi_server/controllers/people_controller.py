from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_create_contacts_request import BatchCreateContactsRequest
from openapi_server.models.batch_create_contacts_response import BatchCreateContactsResponse
from openapi_server.models.batch_delete_contacts_request import BatchDeleteContactsRequest
from openapi_server.models.batch_update_contacts_request import BatchUpdateContactsRequest
from openapi_server.models.batch_update_contacts_response import BatchUpdateContactsResponse
from openapi_server.models.delete_contact_photo_response import DeleteContactPhotoResponse
from openapi_server.models.get_people_response import GetPeopleResponse
from openapi_server.models.list_connections_response import ListConnectionsResponse
from openapi_server.models.list_directory_people_response import ListDirectoryPeopleResponse
from openapi_server.models.person import Person
from openapi_server.models.search_directory_people_response import SearchDirectoryPeopleResponse
from openapi_server.models.search_response import SearchResponse
from openapi_server.models.update_contact_photo_request import UpdateContactPhotoRequest
from openapi_server.models.update_contact_photo_response import UpdateContactPhotoResponse
from openapi_server import util


async def people_people_batch_create_contacts(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """people_people_batch_create_contacts

    Create a batch of new contacts and return the PersonResponses for the newly Mutate requests for the same user should be sent sequentially to avoid increased latency and failures.

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
    body = BatchCreateContactsRequest.from_dict(body)
    return web.Response(status=200)


async def people_people_batch_delete_contacts(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """people_people_batch_delete_contacts

    Delete a batch of contacts. Any non-contact data will not be deleted. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures.

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
    body = BatchDeleteContactsRequest.from_dict(body)
    return web.Response(status=200)


async def people_people_batch_update_contacts(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """people_people_batch_update_contacts

    Update a batch of contacts and return a map of resource names to PersonResponses for the updated contacts. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures.

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
    body = BatchUpdateContactsRequest.from_dict(body)
    return web.Response(status=200)


async def people_people_connections_list(request: web.Request, resource_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, person_fields=None, request_mask_include_field=None, request_sync_token=None, sort_order=None, sources=None, sync_token=None) -> web.Response:
    """people_people_connections_list

    Provides a list of the authenticated user&#39;s contacts. Sync tokens expire 7 days after the full sync. A request with an expired sync token will get an error with an [google.rpc.ErrorInfo](https://cloud.google.com/apis/design/errors#error_info) with reason \&quot;EXPIRED_SYNC_TOKEN\&quot;. In the case of such an error clients should make a full sync request without a &#x60;sync_token&#x60;. The first page of a full sync request has an additional quota. If the quota is exceeded, a 429 error will be returned. This quota is fixed and can not be increased. When the &#x60;sync_token&#x60; is specified, resources deleted since the last sync will be returned as a person with &#x60;PersonMetadata.deleted&#x60; set to true. When the &#x60;page_token&#x60; or &#x60;sync_token&#x60; is specified, all other request parameters must match the first call. Writes may have a propagation delay of several minutes for sync requests. Incremental syncs are not intended for read-after-write use cases. See example usage at [List the user&#39;s contacts that have changed](/people/v1/contacts#list_the_users_contacts_that_have_changed).

    :param resource_name: Required. The resource name to return connections for. Only &#x60;people/me&#x60; is valid.
    :type resource_name: str
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
    :param page_size: Optional. The number of connections to include in the response. Valid values are between 1 and 1000, inclusive. Defaults to 100 if not set or set to 0.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous response &#x60;next_page_token&#x60;. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;people.connections.list&#x60; must match the first call that provided the page token.
    :type page_token: str
    :param person_fields: Required. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type person_fields: str
    :param request_mask_include_field: Required. Comma-separated list of person fields to be included in the response. Each path should start with &#x60;person.&#x60;: for example, &#x60;person.names&#x60; or &#x60;person.photos&#x60;.
    :type request_mask_include_field: str
    :param request_sync_token: Optional. Whether the response should return &#x60;next_sync_token&#x60; on the last page of results. It can be used to get incremental changes since the last request by setting it on the request &#x60;sync_token&#x60;. More details about sync behavior at &#x60;people.connections.list&#x60;.
    :type request_sync_token: bool
    :param sort_order: Optional. The order in which the connections should be sorted. Defaults to &#x60;LAST_MODIFIED_ASCENDING&#x60;.
    :type sort_order: str
    :param sources: Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set.
    :type sources: List[str]
    :param sync_token: Optional. A sync token, received from a previous response &#x60;next_sync_token&#x60; Provide this to retrieve only the resources changed since the last request. When syncing, all other parameters provided to &#x60;people.connections.list&#x60; must match the first call that provided the sync token. More details about sync behavior at &#x60;people.connections.list&#x60;.
    :type sync_token: str

    """
    return web.Response(status=200)


async def people_people_create_contact(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, person_fields=None, sources=None, body=None) -> web.Response:
    """people_people_create_contact

    Create a new contact and return the person resource for that contact. The request returns a 400 error if more than one field is specified on a field that is a singleton for contact sources: * biographies * birthdays * genders * names Mutate requests for the same user should be sent sequentially to avoid increased latency and failures.

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
    :param person_fields: Required. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Defaults to all fields if not set. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type person_fields: str
    :param sources: Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set.
    :type sources: List[str]
    :param body: 
    :type body: dict | bytes

    """
    body = Person.from_dict(body)
    return web.Response(status=200)


async def people_people_delete_contact(request: web.Request, resource_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """people_people_delete_contact

    Delete a contact person. Any non-contact data will not be deleted. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures.

    :param resource_name: Required. The resource name of the contact to delete.
    :type resource_name: str
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


async def people_people_delete_contact_photo(request: web.Request, resource_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, person_fields=None, sources=None) -> web.Response:
    """people_people_delete_contact_photo

    Delete a contact&#39;s photo. Mutate requests for the same user should be done sequentially to avoid // lock contention.

    :param resource_name: Required. The resource name of the contact whose photo will be deleted.
    :type resource_name: str
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
    :param person_fields: Optional. A field mask to restrict which fields on the person are returned. Multiple fields can be specified by separating them with commas. Defaults to empty if not set, which will skip the post mutate get. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type person_fields: str
    :param sources: Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set.
    :type sources: List[str]

    """
    return web.Response(status=200)


async def people_people_get(request: web.Request, resource_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, person_fields=None, request_mask_include_field=None, sources=None) -> web.Response:
    """people_people_get

    Provides information about a person by specifying a resource name. Use &#x60;people/me&#x60; to indicate the authenticated user. The request returns a 400 error if &#39;personFields&#39; is not specified.

    :param resource_name: Required. The resource name of the person to provide information about. - To get information about the authenticated user, specify &#x60;people/me&#x60;. - To get information about a google account, specify &#x60;people/{account_id}&#x60;. - To get information about a contact, specify the resource name that identifies the contact as returned by &#x60;people.connections.list&#x60;.
    :type resource_name: str
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
    :param person_fields: Required. A field mask to restrict which fields on the person are returned. Multiple fields can be specified by separating them with commas. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type person_fields: str
    :param request_mask_include_field: Required. Comma-separated list of person fields to be included in the response. Each path should start with &#x60;person.&#x60;: for example, &#x60;person.names&#x60; or &#x60;person.photos&#x60;.
    :type request_mask_include_field: str
    :param sources: Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_PROFILE and READ_SOURCE_TYPE_CONTACT if not set.
    :type sources: List[str]

    """
    return web.Response(status=200)


async def people_people_get_batch_get(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, person_fields=None, request_mask_include_field=None, resource_names=None, sources=None) -> web.Response:
    """people_people_get_batch_get

    Provides information about a list of specific people by specifying a list of requested resource names. Use &#x60;people/me&#x60; to indicate the authenticated user. The request returns a 400 error if &#39;personFields&#39; is not specified.

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
    :param person_fields: Required. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type person_fields: str
    :param request_mask_include_field: Required. Comma-separated list of person fields to be included in the response. Each path should start with &#x60;person.&#x60;: for example, &#x60;person.names&#x60; or &#x60;person.photos&#x60;.
    :type request_mask_include_field: str
    :param resource_names: Required. The resource names of the people to provide information about. It&#39;s repeatable. The URL query parameter should be resourceNames&#x3D;&lt;name1&gt;&amp;resourceNames&#x3D;&lt;name2&gt;&amp;... - To get information about the authenticated user, specify &#x60;people/me&#x60;. - To get information about a google account, specify &#x60;people/{account_id}&#x60;. - To get information about a contact, specify the resource name that identifies the contact as returned by &#x60;people.connections.list&#x60;. There is a maximum of 200 resource names.
    :type resource_names: List[str]
    :param sources: Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set.
    :type sources: List[str]

    """
    return web.Response(status=200)


async def people_people_list_directory_people(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, merge_sources=None, page_size=None, page_token=None, read_mask=None, request_sync_token=None, sources=None, sync_token=None) -> web.Response:
    """people_people_list_directory_people

    Provides a list of domain profiles and domain contacts in the authenticated user&#39;s domain directory. When the &#x60;sync_token&#x60; is specified, resources deleted since the last sync will be returned as a person with &#x60;PersonMetadata.deleted&#x60; set to true. When the &#x60;page_token&#x60; or &#x60;sync_token&#x60; is specified, all other request parameters must match the first call. Writes may have a propagation delay of several minutes for sync requests. Incremental syncs are not intended for read-after-write use cases. See example usage at [List the directory people that have changed](/people/v1/directory#list_the_directory_people_that_have_changed).

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
    :param merge_sources: Optional. Additional data to merge into the directory sources if they are connected through verified join keys such as email addresses or phone numbers.
    :type merge_sources: List[str]
    :param page_size: Optional. The number of people to include in the response. Valid values are between 1 and 1000, inclusive. Defaults to 100 if not set or set to 0.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous response &#x60;next_page_token&#x60;. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;people.listDirectoryPeople&#x60; must match the first call that provided the page token.
    :type page_token: str
    :param read_mask: Required. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type read_mask: str
    :param request_sync_token: Optional. Whether the response should return &#x60;next_sync_token&#x60;. It can be used to get incremental changes since the last request by setting it on the request &#x60;sync_token&#x60;. More details about sync behavior at &#x60;people.listDirectoryPeople&#x60;.
    :type request_sync_token: bool
    :param sources: Required. Directory sources to return.
    :type sources: List[str]
    :param sync_token: Optional. A sync token, received from a previous response &#x60;next_sync_token&#x60; Provide this to retrieve only the resources changed since the last request. When syncing, all other parameters provided to &#x60;people.listDirectoryPeople&#x60; must match the first call that provided the sync token. More details about sync behavior at &#x60;people.listDirectoryPeople&#x60;.
    :type sync_token: str

    """
    return web.Response(status=200)


async def people_people_search_contacts(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, query=None, read_mask=None, sources=None) -> web.Response:
    """people_people_search_contacts

    Provides a list of contacts in the authenticated user&#39;s grouped contacts that matches the search query. The query matches on a contact&#39;s &#x60;names&#x60;, &#x60;nickNames&#x60;, &#x60;emailAddresses&#x60;, &#x60;phoneNumbers&#x60;, and &#x60;organizations&#x60; fields that are from the CONTACT source. **IMPORTANT**: Before searching, clients should send a warmup request with an empty query to update the cache. See https://developers.google.com/people/v1/contacts#search_the_users_contacts

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
    :param page_size: Optional. The number of results to return. Defaults to 10 if field is not set, or set to 0. Values greater than 30 will be capped to 30.
    :type page_size: int
    :param query: Required. The plain-text query for the request. The query is used to match prefix phrases of the fields on a person. For example, a person with name \&quot;foo name\&quot; matches queries such as \&quot;f\&quot;, \&quot;fo\&quot;, \&quot;foo\&quot;, \&quot;foo n\&quot;, \&quot;nam\&quot;, etc., but not \&quot;oo n\&quot;.
    :type query: str
    :param read_mask: Required. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type read_mask: str
    :param sources: Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT if not set.
    :type sources: List[str]

    """
    return web.Response(status=200)


async def people_people_search_directory_people(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, merge_sources=None, page_size=None, page_token=None, query=None, read_mask=None, sources=None) -> web.Response:
    """people_people_search_directory_people

    Provides a list of domain profiles and domain contacts in the authenticated user&#39;s domain directory that match the search query.

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
    :param merge_sources: Optional. Additional data to merge into the directory sources if they are connected through verified join keys such as email addresses or phone numbers.
    :type merge_sources: List[str]
    :param page_size: Optional. The number of people to include in the response. Valid values are between 1 and 500, inclusive. Defaults to 100 if not set or set to 0.
    :type page_size: int
    :param page_token: Optional. A page token, received from a previous response &#x60;next_page_token&#x60;. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;SearchDirectoryPeople&#x60; must match the first call that provided the page token.
    :type page_token: str
    :param query: Required. Prefix query that matches fields in the person. Does NOT use the read_mask for determining what fields to match.
    :type query: str
    :param read_mask: Required. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type read_mask: str
    :param sources: Required. Directory sources to return.
    :type sources: List[str]

    """
    return web.Response(status=200)


async def people_people_update_contact(request: web.Request, resource_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, person_fields=None, sources=None, update_person_fields=None, body=None) -> web.Response:
    """people_people_update_contact

    Update contact data for an existing contact person. Any non-contact data will not be modified. Any non-contact data in the person to update will be ignored. All fields specified in the &#x60;update_mask&#x60; will be replaced. The server returns a 400 error if &#x60;person.metadata.sources&#x60; is not specified for the contact to be updated or if there is no contact source. The server returns a 400 error with reason &#x60;\&quot;failedPrecondition\&quot;&#x60; if &#x60;person.metadata.sources.etag&#x60; is different than the contact&#39;s etag, which indicates the contact has changed since its data was read. Clients should get the latest person and merge their updates into the latest person. The server returns a 400 error if &#x60;memberships&#x60; are being updated and there are no contact group memberships specified on the person. The server returns a 400 error if more than one field is specified on a field that is a singleton for contact sources: * biographies * birthdays * genders * names Mutate requests for the same user should be sent sequentially to avoid increased latency and failures.

    :param resource_name: The resource name for the person, assigned by the server. An ASCII string in the form of &#x60;people/{person_id}&#x60;.
    :type resource_name: str
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
    :param person_fields: Optional. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. Defaults to all fields if not set. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined
    :type person_fields: str
    :param sources: Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set.
    :type sources: List[str]
    :param update_person_fields: Required. A field mask to restrict which fields on the person are updated. Multiple fields can be specified by separating them with commas. All updated fields will be replaced. Valid values are: * addresses * biographies * birthdays * calendarUrls * clientData * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * relations * sipAddresses * urls * userDefined
    :type update_person_fields: str
    :param body: 
    :type body: dict | bytes

    """
    body = Person.from_dict(body)
    return web.Response(status=200)


async def people_people_update_contact_photo(request: web.Request, resource_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """people_people_update_contact_photo

    Update a contact&#39;s photo. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures.

    :param resource_name: Required. Person resource name
    :type resource_name: str
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
    body = UpdateContactPhotoRequest.from_dict(body)
    return web.Response(status=200)
