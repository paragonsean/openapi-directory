# GooglePlayEmmApi.AdministratorWebTokenSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managedConfigurations** | [**AdministratorWebTokenSpecManagedConfigurations**](AdministratorWebTokenSpecManagedConfigurations.md) |  | [optional] 
**parent** | **String** | The URI of the parent frame hosting the iframe. To prevent XSS, the iframe may not be hosted at other URIs. This URI must be https. Use whitespaces to separate multiple parent URIs. | [optional] 
**permission** | **[String]** | Deprecated. Use PlaySearch.approveApps. | [optional] 
**playSearch** | [**AdministratorWebTokenSpecPlaySearch**](AdministratorWebTokenSpecPlaySearch.md) |  | [optional] 
**privateApps** | [**AdministratorWebTokenSpecPrivateApps**](AdministratorWebTokenSpecPrivateApps.md) |  | [optional] 
**storeBuilder** | [**AdministratorWebTokenSpecStoreBuilder**](AdministratorWebTokenSpecStoreBuilder.md) |  | [optional] 
**webApps** | [**AdministratorWebTokenSpecWebApps**](AdministratorWebTokenSpecWebApps.md) |  | [optional] 
**zeroTouch** | [**AdministratorWebTokenSpecZeroTouch**](AdministratorWebTokenSpecZeroTouch.md) |  | [optional] 



## Enum: [PermissionEnum]


* `unknown` (value: `"unknown"`)

* `approveApps` (value: `"approveApps"`)

* `manageMcm` (value: `"manageMcm"`)




