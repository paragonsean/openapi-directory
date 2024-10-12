

# DealerDBModelsLicense


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | True if license is active. |  [optional] |
|**createdDate** | **OffsetDateTime** | The date the license was created. |  [optional] |
|**deactivatedDate** | **OffsetDateTime** | The date the license was deactivated. |  [optional] |
|**licenseActivationType** | [**LicenseActivationTypeEnum**](#LicenseActivationTypeEnum) | The type of license (e.g. EDT, EDT Lite) |  [optional] |
|**licenseID** | **String** | The LicenseID |  [optional] |
|**licenseVersion** | **String** | The version of the license. |  [optional] |
|**refreshDate** | **OffsetDateTime** | The date the license was refreshed. |  [optional] |
|**systemInfo** | **String** | Information about the system which is licensed. |  [optional] |
|**updatedLicenseVersion** | **String** | The updated version of the license.  A value in this field indicates that the update has not been confirmed. |  [optional] |
|**voucherCode** | **String** | The voucher code that generated the license. |  [optional] |



## Enum: LicenseActivationTypeEnum

| Name | Value |
|---- | -----|
| EDT | &quot;EDT&quot; |
| EDT_LITE | &quot;EDTLite&quot; |



