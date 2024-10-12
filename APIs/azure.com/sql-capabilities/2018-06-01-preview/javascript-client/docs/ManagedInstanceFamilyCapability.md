# SqlManagementClient.ManagedInstanceFamilyCapability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Family name. | [optional] [readonly] 
**reason** | **String** | The reason for the capability not being available. | [optional] 
**sku** | **String** | SKU name. | [optional] [readonly] 
**status** | **String** | The status of the capability. | [optional] [readonly] 
**supportedLicenseTypes** | [**[LicenseTypeCapability]**](LicenseTypeCapability.md) | List of supported license types. | [optional] [readonly] 
**supportedVcoresValues** | [**[ManagedInstanceVcoresCapability]**](ManagedInstanceVcoresCapability.md) | List of supported virtual cores values. | [optional] [readonly] 



## Enum: StatusEnum


* `Visible` (value: `"Visible"`)

* `Available` (value: `"Available"`)

* `Default` (value: `"Default"`)

* `Disabled` (value: `"Disabled"`)




