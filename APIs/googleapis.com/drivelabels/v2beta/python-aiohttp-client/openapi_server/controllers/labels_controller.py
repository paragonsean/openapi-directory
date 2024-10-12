from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_apps_drive_labels_v2beta_batch_delete_label_permissions_request import GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest
from openapi_server.models.google_apps_drive_labels_v2beta_batch_update_label_permissions_request import GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest
from openapi_server.models.google_apps_drive_labels_v2beta_batch_update_label_permissions_response import GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse
from openapi_server.models.google_apps_drive_labels_v2beta_delta_update_label_request import GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest
from openapi_server.models.google_apps_drive_labels_v2beta_delta_update_label_response import GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse
from openapi_server.models.google_apps_drive_labels_v2beta_disable_label_request import GoogleAppsDriveLabelsV2betaDisableLabelRequest
from openapi_server.models.google_apps_drive_labels_v2beta_enable_label_request import GoogleAppsDriveLabelsV2betaEnableLabelRequest
from openapi_server.models.google_apps_drive_labels_v2beta_label import GoogleAppsDriveLabelsV2betaLabel
from openapi_server.models.google_apps_drive_labels_v2beta_label_permission import GoogleAppsDriveLabelsV2betaLabelPermission
from openapi_server.models.google_apps_drive_labels_v2beta_list_label_locks_response import GoogleAppsDriveLabelsV2betaListLabelLocksResponse
from openapi_server.models.google_apps_drive_labels_v2beta_list_label_permissions_response import GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse
from openapi_server.models.google_apps_drive_labels_v2beta_list_labels_response import GoogleAppsDriveLabelsV2betaListLabelsResponse
from openapi_server.models.google_apps_drive_labels_v2beta_publish_label_request import GoogleAppsDriveLabelsV2betaPublishLabelRequest
from openapi_server.models.google_apps_drive_labels_v2beta_update_label_copy_mode_request import GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest
from openapi_server import util


async def drivelabels_labels_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None, use_admin_access=None, body=None) -> web.Response:
    """drivelabels_labels_create

    Creates a new Label.

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
    :param language_code: The BCP-47 language code to use for evaluating localized Field labels in response. When not specified, values in the default configured language will be used.
    :type language_code: str
    :param use_admin_access: Set to &#x60;true&#x60; in order to use the user&#39;s admin privileges. The server will verify the user is an admin before allowing access.
    :type use_admin_access: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsDriveLabelsV2betaLabel.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_delta(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drivelabels_labels_delta

    Updates a single Label by applying a set of update requests resulting in a new draft revision. The batch update is all-or-nothing: If any of the update requests are invalid, no changes are applied. The resulting draft revision must be published before the changes may be used with Drive Items.

    :param name: Required. The resource name of the Label to update.
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
    body = GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_disable(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drivelabels_labels_disable

    Disable a published Label. Disabling a Label will result in a new disabled published revision based on the current published revision. If there is a draft revision, a new disabled draft revision will be created based on the latest draft revision. Older draft revisions will be deleted. Once disabled, a label may be deleted with &#x60;DeleteLabel&#x60;.

    :param name: Required. Label resource name.
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
    body = GoogleAppsDriveLabelsV2betaDisableLabelRequest.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_enable(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drivelabels_labels_enable

    Enable a disabled Label and restore it to its published state. This will result in a new published revision based on the current disabled published revision. If there is an existing disabled draft revision, a new revision will be created based on that draft and will be enabled.

    :param name: Required. Label resource name.
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
    body = GoogleAppsDriveLabelsV2betaEnableLabelRequest.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, customer=None, language_code=None, minimum_role=None, page_size=None, page_token=None, published_only=None, use_admin_access=None, view=None) -> web.Response:
    """drivelabels_labels_list

    List labels.

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
    :param customer: The customer to scope this list request to. For example: \&quot;customers/abcd1234\&quot;. If unset, will return all labels within the current customer.
    :type customer: str
    :param language_code: The BCP-47 language code to use for evaluating localized field labels. When not specified, values in the default configured language are used.
    :type language_code: str
    :param minimum_role: Specifies the level of access the user must have on the returned Labels. The minimum role a user must have on a label. Defaults to &#x60;READER&#x60;.
    :type minimum_role: str
    :param page_size: Maximum number of labels to return per page. Default: 50. Max: 200.
    :type page_size: int
    :param page_token: The token of the page to return.
    :type page_token: str
    :param published_only: Whether to include only published labels in the results. * When &#x60;true&#x60;, only the current published label revisions are returned. Disabled labels are included. Returned label resource names reference the published revision (&#x60;labels/{id}/{revision_id}&#x60;). * When &#x60;false&#x60;, the current label revisions are returned, which might not be published. Returned label resource names don&#39;t reference a specific revision (&#x60;labels/{id}&#x60;).
    :type published_only: bool
    :param use_admin_access: Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. This will return all Labels within the customer.
    :type use_admin_access: bool
    :param view: When specified, only certain fields belonging to the indicated view are returned.
    :type view: str

    """
    return web.Response(status=200)


async def drivelabels_labels_publish(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drivelabels_labels_publish

    Publish all draft changes to the Label. Once published, the Label may not return to its draft state. See &#x60;google.apps.drive.labels.v2.Lifecycle&#x60; for more information. Publishing a Label will result in a new published revision. All previous draft revisions will be deleted. Previous published revisions will be kept but are subject to automated deletion as needed. Once published, some changes are no longer permitted. Generally, any change that would invalidate or cause new restrictions on existing metadata related to the Label will be rejected. For example, the following changes to a Label will be rejected after the Label is published: * The label cannot be directly deleted. It must be disabled first, then deleted. * Field.FieldType cannot be changed. * Changes to Field validation options cannot reject something that was previously accepted. * Reducing the max entries.

    :param name: Required. Label resource name.
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
    body = GoogleAppsDriveLabelsV2betaPublishLabelRequest.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_revisions_locks_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """drivelabels_labels_revisions_locks_list

    Lists the LabelLocks on a Label.

    :param parent: Required. Label on which Locks are applied. Format: labels/{label}
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
    :param page_size: Maximum number of Locks to return per page. Default: 100. Max: 200.
    :type page_size: int
    :param page_token: The token of the page to return.
    :type page_token: str

    """
    return web.Response(status=200)


async def drivelabels_labels_revisions_permissions_batch_delete(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drivelabels_labels_revisions_permissions_batch_delete

    Deletes Label permissions. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

    :param parent: Required. The parent Label resource name shared by all permissions being deleted. Format: labels/{label} If this is set, the parent field in the UpdateLabelPermissionRequest messages must either be empty or match this field.
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
    body = GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_revisions_permissions_batch_update(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drivelabels_labels_revisions_permissions_batch_update

    Updates Label permissions. If a permission for the indicated principal doesn&#39;t exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

    :param parent: Required. The parent Label resource name shared by all permissions being updated. Format: labels/{label} If this is set, the parent field in the UpdateLabelPermissionRequest messages must either be empty or match this field.
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
    body = GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_revisions_permissions_create(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, use_admin_access=None, body=None) -> web.Response:
    """drivelabels_labels_revisions_permissions_create

    Updates a Label&#39;s permissions. If a permission for the indicated principal doesn&#39;t exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

    :param parent: Required. The parent Label resource name on the Label Permission is created. Format: labels/{label}
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
    :param use_admin_access: Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access.
    :type use_admin_access: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsDriveLabelsV2betaLabelPermission.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_revisions_permissions_delete(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, use_admin_access=None, write_control_required_revision_id=None) -> web.Response:
    """drivelabels_labels_revisions_permissions_delete

    Deletes a Label&#39;s permission. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

    :param name: Required. Label Permission resource name.
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
    :param use_admin_access: Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access.
    :type use_admin_access: bool
    :param write_control_required_revision_id: The revision_id of the label that the write request will be applied to. If this is not the latest revision of the label, the request will not be processed and will return a 400 Bad Request error.
    :type write_control_required_revision_id: str

    """
    return web.Response(status=200)


async def drivelabels_labels_revisions_permissions_list(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None, use_admin_access=None) -> web.Response:
    """drivelabels_labels_revisions_permissions_list

    Lists a Label&#39;s permissions.

    :param parent: Required. The parent Label resource name on which Label Permission are listed. Format: labels/{label}
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
    :param page_size: Maximum number of permissions to return per page. Default: 50. Max: 200.
    :type page_size: int
    :param page_token: The token of the page to return.
    :type page_token: str
    :param use_admin_access: Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access.
    :type use_admin_access: bool

    """
    return web.Response(status=200)


async def drivelabels_labels_revisions_update_permissions(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, use_admin_access=None, body=None) -> web.Response:
    """drivelabels_labels_revisions_update_permissions

    Updates a Label&#39;s permissions. If a permission for the indicated principal doesn&#39;t exist, a new Label Permission is created, otherwise the existing permission is updated. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

    :param parent: Required. The parent Label resource name.
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
    :param use_admin_access: Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access.
    :type use_admin_access: bool
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleAppsDriveLabelsV2betaLabelPermission.from_dict(body)
    return web.Response(status=200)


async def drivelabels_labels_update_label_copy_mode(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """drivelabels_labels_update_label_copy_mode

    Updates a Label&#39;s &#x60;CopyMode&#x60;. Changes to this policy are not revisioned, do not require publishing, and take effect immediately.

    :param name: Required. The resource name of the Label to update.
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
    body = GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest.from_dict(body)
    return web.Response(status=200)
