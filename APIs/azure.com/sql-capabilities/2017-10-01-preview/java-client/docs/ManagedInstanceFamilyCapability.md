

# ManagedInstanceFamilyCapability

The managed server family capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  |  [optional] |
|**name** | **String** | Family name. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**sku** | **String** | SKU name. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedLicenseTypes** | [**List&lt;LicenseTypeCapability&gt;**](LicenseTypeCapability.md) | List of supported license types. |  [optional] [readonly] |
|**supportedStorageSizes** | [**List&lt;MaxSizeRangeCapability&gt;**](MaxSizeRangeCapability.md) | Storage size ranges. |  [optional] [readonly] |
|**supportedVcoresValues** | [**List&lt;ManagedInstanceVcoresCapability&gt;**](ManagedInstanceVcoresCapability.md) | List of supported virtual cores values. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



