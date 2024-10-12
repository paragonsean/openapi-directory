# GooglePlayEmmApi.ProductsApproveRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvalUrlInfo** | [**ApprovalUrlInfo**](ApprovalUrlInfo.md) |  | [optional] 
**approvedPermissions** | **String** | Sets how new permission requests for the product are handled. \&quot;allPermissions\&quot; automatically approves all current and future permissions for the product. \&quot;currentPermissionsOnly\&quot; approves the current set of permissions for the product, but any future permissions added through updates will require manual reapproval. If not specified, only the current set of permissions will be approved. | [optional] 



## Enum: ApprovedPermissionsEnum


* `currentPermissionsOnly` (value: `"currentPermissionsOnly"`)

* `allPermissions` (value: `"allPermissions"`)




