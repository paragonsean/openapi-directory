

# GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequest

Deletes one of more Label Permissions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requests** | [**List&lt;GoogleAppsDriveLabelsV2DeleteLabelPermissionRequest&gt;**](GoogleAppsDriveLabelsV2DeleteLabelPermissionRequest.md) | Required. The request message specifying the resources to update. |  [optional] |
|**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. If this is set, the use_admin_access field in the DeleteLabelPermissionRequest messages must either be empty or match this field. |  [optional] |



