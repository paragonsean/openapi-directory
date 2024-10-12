from typing import List, Dict
from aiohttp import web

from openapi_server.models.beacon import Beacon
from openapi_server.models.beacon_attachment import BeaconAttachment
from openapi_server.models.delete_attachments_response import DeleteAttachmentsResponse
from openapi_server.models.list_beacon_attachments_response import ListBeaconAttachmentsResponse
from openapi_server.models.list_beacons_response import ListBeaconsResponse
from openapi_server.models.list_diagnostics_response import ListDiagnosticsResponse
from openapi_server import util


async def proximitybeacon_beacons_activate(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_activate

    Activates a beacon. A beacon that is active will return information and attachment data when queried via &#x60;beaconinfo.getforobserved&#x60;. Calling this method on an already active beacon will do nothing (but will return a successful response code). Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Beacon that should be activated. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param project_id: The project id of the beacon to activate. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_attachments_batch_delete(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, namespaced_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_attachments_batch_delete

    Deletes multiple attachments on a given beacon. This operation is permanent and cannot be undone. You can optionally specify &#x60;namespacedType&#x60; to choose which attachments should be deleted. If you do not specify &#x60;namespacedType&#x60;, all your attachments on the given beacon will be deleted. You also may explicitly specify &#x60;*/*&#x60; to delete all. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: The beacon whose attachments should be deleted. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param namespaced_type: Specifies the namespace and type of attachments to delete in &#x60;namespace/type&#x60; format. Accepts &#x60;*/*&#x60; to specify \&quot;all types in all namespaces\&quot;. Optional.
    :type namespaced_type: str
    :param project_id: The project id to delete beacon attachments under. This field can be used when \&quot;*\&quot; is specified to mean all attachment namespaces. Projects may have multiple attachments with multiple namespaces. If \&quot;*\&quot; is specified and the projectId string is empty, then the project making the request is used. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_attachments_create(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None, body=None) -> web.Response:
    """proximitybeacon_beacons_attachments_create

    Associates the given data with the specified beacon. Attachment data must contain two parts: - A namespaced type. - The actual attachment data itself. The namespaced type consists of two parts, the namespace and the type. The namespace must be one of the values returned by the &#x60;namespaces&#x60; endpoint, while the type can be a string of any characters except for the forward slash (&#x60;/&#x60;) up to 100 characters in length. Attachment data can be up to 1024 bytes long. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Beacon on which the attachment should be created. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param project_id: The project id of the project the attachment will belong to. If the project id is not specified then the project making the request is used. Optional.
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BeaconAttachment.from_dict(body)
    return web.Response(status=200)


async def proximitybeacon_beacons_attachments_delete(request: web.Request, attachment_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_attachments_delete

    Deletes the specified attachment for the given beacon. Each attachment has a unique attachment name (&#x60;attachmentName&#x60;) which is returned when you fetch the attachment data via this API. You specify this with the delete request to control which attachment is removed. This operation cannot be undone. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param attachment_name: The attachment name (&#x60;attachmentName&#x60;) of the attachment to remove. For example: &#x60;beacons/3!893737abc9/attachments/c5e937-af0-494-959-ec49d12738&#x60;. For Eddystone-EID beacons, the beacon ID portion (&#x60;3!893737abc9&#x60;) may be the beacon&#39;s current EID, or its \&quot;stable\&quot; Eddystone-UID. Required.
    :type attachment_name: str
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
    :param project_id: The project id of the attachment to delete. If not provided, the project that is making the request is used. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_attachments_list(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, namespaced_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_attachments_list

    Returns the attachments for the specified beacon that match the specified namespaced-type pattern. To control which namespaced types are returned, you add the &#x60;namespacedType&#x60; query parameter to the request. You must either use &#x60;*/*&#x60;, to return all attachments, or the namespace must be one of the ones returned from the &#x60;namespaces&#x60; endpoint. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Beacon whose attachments should be fetched. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param namespaced_type: Specifies the namespace and type of attachment to include in response in namespace/type format. Accepts &#x60;*/*&#x60; to specify \&quot;all types in all namespaces\&quot;.
    :type namespaced_type: str
    :param project_id: The project id to list beacon attachments under. This field can be used when \&quot;*\&quot; is specified to mean all attachment namespaces. Projects may have multiple attachments with multiple namespaces. If \&quot;*\&quot; is specified and the projectId string is empty, then the project making the request is used. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_deactivate(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_deactivate

    Deactivates a beacon. Once deactivated, the API will not return information nor attachment data for the beacon when queried via &#x60;beaconinfo.getforobserved&#x60;. Calling this method on an already inactive beacon will do nothing (but will return a successful response code). Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Beacon that should be deactivated. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param project_id: The project id of the beacon to deactivate. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_decommission(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_decommission

    Decommissions the specified beacon in the service. This beacon will no longer be returned from &#x60;beaconinfo.getforobserved&#x60;. This operation is permanent -- you will not be able to re-register a beacon with this ID again. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Beacon that should be decommissioned. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID of the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param project_id: The project id of the beacon to decommission. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_delete(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_delete

    Deletes the specified beacon including all diagnostics data for the beacon as well as any attachments on the beacon (including those belonging to other projects). This operation cannot be undone. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Beacon that should be deleted. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param project_id: The project id of the beacon to delete. If not provided, the project that is making the request is used. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_diagnostics_list(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, alert_filter=None, page_size=None, page_token=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_diagnostics_list

    List the diagnostics for a single beacon. You can also list diagnostics for all the beacons owned by your Google Developers Console project by using the beacon name &#x60;beacons/-&#x60;. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Beacon that the diagnostics are for.
    :type beacon_name: str
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
    :param alert_filter: Requests only beacons that have the given alert. For example, to find beacons that have low batteries use &#x60;alert_filter&#x3D;LOW_BATTERY&#x60;.
    :type alert_filter: str
    :param page_size: Specifies the maximum number of results to return. Defaults to 10. Maximum 1000. Optional.
    :type page_size: int
    :param page_token: Requests results that occur after the &#x60;page_token&#x60;, obtained from the response to a previous request. Optional.
    :type page_token: str
    :param project_id: Requests only diagnostic records for the given project id. If not set, then the project making the request will be used for looking up diagnostic records. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_get(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None) -> web.Response:
    """proximitybeacon_beacons_get

    Returns detailed information about the specified beacon. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project. Requests may supply an Eddystone-EID beacon name in the form: &#x60;beacons/4!beaconId&#x60; where the &#x60;beaconId&#x60; is the base16 ephemeral ID broadcast by the beacon. The returned &#x60;Beacon&#x60; object will contain the beacon&#39;s stable Eddystone-UID. Clients not authorized to resolve the beacon&#39;s ephemeral Eddystone-EID broadcast will receive an error.

    :param beacon_name: Resource name of this beacon. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required.
    :type beacon_name: str
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
    :param project_id: The project id of the beacon to request. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    :type project_id: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, project_id=None, q=None) -> web.Response:
    """proximitybeacon_beacons_list

    Searches the beacon registry for beacons that match the given search criteria. Only those beacons that the client has permission to list will be returned. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project.

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
    :param page_size: The maximum number of records to return for this request, up to a server-defined upper limit.
    :type page_size: int
    :param page_token: A pagination token obtained from a previous request to list beacons.
    :type page_token: str
    :param project_id: The project id to list beacons under. If not present then the project credential that made the request is used as the project. Optional.
    :type project_id: str
    :param q: Filter query string that supports the following field filters: * **description:&#x60;\&quot;\&quot;&#x60;** For example: **description:\&quot;Room 3\&quot;** Returns beacons whose description matches tokens in the string \&quot;Room 3\&quot; (not necessarily that exact string). The string must be double-quoted. * **status:&#x60;&#x60;** For example: **status:active** Returns beacons whose status matches the given value. Values must be one of the Beacon.Status enum values (case insensitive). Accepts multiple filters which will be combined with OR logic. * **stability:&#x60;&#x60;** For example: **stability:mobile** Returns beacons whose expected stability matches the given value. Values must be one of the Beacon.Stability enum values (case insensitive). Accepts multiple filters which will be combined with OR logic. * **place\\_id:&#x60;\&quot;\&quot;&#x60;** For example: **place\\_id:\&quot;ChIJVSZzVR8FdkgRXGmmm6SslKw&#x3D;\&quot;** Returns beacons explicitly registered at the given place, expressed as a Place ID obtained from [Google Places API](/places/place-id). Does not match places inside the given place. Does not consider the beacon&#39;s actual location (which may be different from its registered place). Accepts multiple filters that will be combined with OR logic. The place ID must be double-quoted. * **registration\\_time&#x60;[&lt;|&gt;|&lt;&#x3D;|&gt;&#x3D;]&#x60;** For example: **registration\\_time&gt;&#x3D;1433116800** Returns beacons whose registration time matches the given filter. Supports the operators: &lt;, &gt;, &lt;&#x3D;, and &gt;&#x3D;. Timestamp must be expressed as an integer number of seconds since midnight January 1, 1970 UTC. Accepts at most two filters that will be combined with AND logic, to support \&quot;between\&quot; semantics. If more than two are supplied, the latter ones are ignored. * **lat:&#x60; lng: radius:&#x60;** For example: **lat:51.1232343 lng:-1.093852 radius:1000** Returns beacons whose registered location is within the given circle. When any of these fields are given, all are required. Latitude and longitude must be decimal degrees between -90.0 and 90.0 and between -180.0 and 180.0 respectively. Radius must be an integer number of meters between 10 and 1,000,000 (1000 km). * **property:&#x60;\&quot;&#x3D;\&quot;&#x60;** For example: **property:\&quot;battery-type&#x3D;CR2032\&quot;** Returns beacons which have a property of the given name and value. Supports multiple filters which will be combined with OR logic. The entire name&#x3D;value string must be double-quoted as one string. * **attachment\\_type:&#x60;\&quot;\&quot;&#x60;** For example: **attachment_type:\&quot;my-namespace/my-type\&quot;** Returns beacons having at least one attachment of the given namespaced type. Supports \&quot;any within this namespace\&quot; via the partial wildcard syntax: \&quot;my-namespace/*\&quot;. Supports multiple filters which will be combined with OR logic. The string must be double-quoted. * **indoor\\_level:&#x60;\&quot;\&quot;&#x60;** For example: **indoor\\_level:\&quot;1\&quot;** Returns beacons which are located on the given indoor level. Accepts multiple filters that will be combined with OR logic. Multiple filters on the same field are combined with OR logic (except registration_time which is combined with AND logic). Multiple filters on different fields are combined with AND logic. Filters should be separated by spaces. As with any HTTP query string parameter, the whole filter expression must be URL-encoded. Example REST request: &#x60;GET /v1beta1/beacons?q&#x3D;status:active%20lat:51.123%20lng:-1.095%20radius:1000&#x60;
    :type q: str

    """
    return web.Response(status=200)


async def proximitybeacon_beacons_register(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None, body=None) -> web.Response:
    """proximitybeacon_beacons_register

    Registers a previously unregistered beacon given its &#x60;advertisedId&#x60;. These IDs are unique within the system. An ID can be registered only once. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

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
    :param project_id: The project id of the project the beacon will be registered to. If the project id is not specified then the project making the request is used. Optional.
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Beacon.from_dict(body)
    return web.Response(status=200)


async def proximitybeacon_beacons_update(request: web.Request, beacon_name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, project_id=None, body=None) -> web.Response:
    """proximitybeacon_beacons_update

    Updates the information about the specified beacon. **Any field that you do not populate in the submitted beacon will be permanently erased**, so you should follow the \&quot;read, modify, write\&quot; pattern to avoid inadvertently destroying data. Changes to the beacon status via this method will be silently ignored. To update beacon status, use the separate methods on this API for activation, deactivation, and decommissioning. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

    :param beacon_name: Resource name of this beacon. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. This field must be left empty when registering. After reading a beacon, clients can use the name for future operations.
    :type beacon_name: str
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
    :param project_id: The project id of the beacon to update. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Beacon.from_dict(body)
    return web.Response(status=200)
