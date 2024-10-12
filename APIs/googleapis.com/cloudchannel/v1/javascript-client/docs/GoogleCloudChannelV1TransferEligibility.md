# CloudChannelApi.GoogleCloudChannelV1TransferEligibility

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Localized description if reseller is not eligible to transfer the SKU. | [optional] 
**ineligibilityReason** | **String** | Specified the reason for ineligibility. | [optional] 
**isEligible** | **Boolean** | Whether reseller is eligible to transfer the SKU. | [optional] 



## Enum: IneligibilityReasonEnum


* `REASON_UNSPECIFIED` (value: `"REASON_UNSPECIFIED"`)

* `PENDING_TOS_ACCEPTANCE` (value: `"PENDING_TOS_ACCEPTANCE"`)

* `SKU_NOT_ELIGIBLE` (value: `"SKU_NOT_ELIGIBLE"`)

* `SKU_SUSPENDED` (value: `"SKU_SUSPENDED"`)

* `CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU` (value: `"CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU"`)




