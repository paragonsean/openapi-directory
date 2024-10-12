

# GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequest

Updates one or more Label Permissions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**requests** | [**List&lt;GoogleAppsDriveLabelsV2UpdateLabelPermissionRequest&gt;**](GoogleAppsDriveLabelsV2UpdateLabelPermissionRequest.md) | Required. The request message specifying the resources to update. |  [optional] |
|**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. If this is set, the use_admin_access field in the UpdateLabelPermissionRequest messages must either be empty or match this field. |  [optional] |



