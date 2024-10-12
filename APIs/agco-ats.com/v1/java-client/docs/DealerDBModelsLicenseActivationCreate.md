

# DealerDBModelsLicenseActivationCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dealerCode** | **String** | The Dealer Code of the dealer activating the license |  |
|**licenseActivationType** | [**LicenseActivationTypeEnum**](#LicenseActivationTypeEnum) | The type of license to create (e.g. EDT, EDT Lite) |  [optional] |
|**postalCode** | **String** | The dealer&#39;s postal code (zip code) |  |
|**systemInfo** | **String** | Information about  the system being activated |  |
|**voucherCode** | **String** | The Voucher Code to use for activation |  |



## Enum: LicenseActivationTypeEnum

| Name | Value |
|---- | -----|
| EDT | &quot;EDT&quot; |
| EDT_LITE | &quot;EDTLite&quot; |



