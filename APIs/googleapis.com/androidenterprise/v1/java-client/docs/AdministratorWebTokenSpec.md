

# AdministratorWebTokenSpec

Specification for a token used to generate iframes. The token specifies what data the admin is allowed to modify and the URI the iframe is allowed to communiate with.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managedConfigurations** | [**AdministratorWebTokenSpecManagedConfigurations**](AdministratorWebTokenSpecManagedConfigurations.md) |  |  [optional] |
|**parent** | **String** | The URI of the parent frame hosting the iframe. To prevent XSS, the iframe may not be hosted at other URIs. This URI must be https. Use whitespaces to separate multiple parent URIs. |  [optional] |
|**permission** | [**List&lt;PermissionEnum&gt;**](#List&lt;PermissionEnum&gt;) | Deprecated. Use PlaySearch.approveApps. |  [optional] |
|**playSearch** | [**AdministratorWebTokenSpecPlaySearch**](AdministratorWebTokenSpecPlaySearch.md) |  |  [optional] |
|**privateApps** | [**AdministratorWebTokenSpecPrivateApps**](AdministratorWebTokenSpecPrivateApps.md) |  |  [optional] |
|**storeBuilder** | [**AdministratorWebTokenSpecStoreBuilder**](AdministratorWebTokenSpecStoreBuilder.md) |  |  [optional] |
|**webApps** | [**AdministratorWebTokenSpecWebApps**](AdministratorWebTokenSpecWebApps.md) |  |  [optional] |
|**zeroTouch** | [**AdministratorWebTokenSpecZeroTouch**](AdministratorWebTokenSpecZeroTouch.md) |  |  [optional] |



## Enum: List&lt;PermissionEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| APPROVE_APPS | &quot;approveApps&quot; |
| MANAGE_MCM | &quot;manageMcm&quot; |



