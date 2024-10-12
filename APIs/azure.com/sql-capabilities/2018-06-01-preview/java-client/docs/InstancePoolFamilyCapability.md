

# InstancePoolFamilyCapability

The instance pool family capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Family name. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedLicenseTypes** | [**List&lt;LicenseTypeCapability&gt;**](LicenseTypeCapability.md) | List of supported license types. |  [optional] [readonly] |
|**supportedVcoresValues** | [**List&lt;InstancePoolVcoresCapability&gt;**](InstancePoolVcoresCapability.md) | List of supported virtual cores values. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



