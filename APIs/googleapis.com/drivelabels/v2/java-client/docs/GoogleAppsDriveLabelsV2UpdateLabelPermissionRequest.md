

# GoogleAppsDriveLabelsV2UpdateLabelPermissionRequest

Updates a Label Permission. Permissions affect the Label resource as a whole, are not revisioned, and do not require publishing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labelPermission** | [**GoogleAppsDriveLabelsV2LabelPermission**](GoogleAppsDriveLabelsV2LabelPermission.md) |  |  [optional] |
|**parent** | **String** | Required. The parent Label resource name. |  [optional] |
|**useAdminAccess** | **Boolean** | Set to &#x60;true&#x60; in order to use the user&#39;s admin credentials. The server will verify the user is an admin for the Label before allowing access. |  [optional] |



