

# NewPermissionsEvent

An event generated when new permissions are added to an app.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvedPermissions** | **List&lt;String&gt;** | The set of permissions that the enterprise admin has already approved for this application. Use Permissions.Get on the EMM API to retrieve details about these permissions. |  [optional] |
|**productId** | **String** | The id of the product (e.g. \&quot;app:com.google.android.gm\&quot;) for which new permissions were added. This field will always be present. |  [optional] |
|**requestedPermissions** | **List&lt;String&gt;** | The set of permissions that the app is currently requesting. Use Permissions.Get on the EMM API to retrieve details about these permissions. |  [optional] |



