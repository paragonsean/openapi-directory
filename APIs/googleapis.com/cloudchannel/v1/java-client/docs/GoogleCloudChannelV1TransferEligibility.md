

# GoogleCloudChannelV1TransferEligibility

Specifies transfer eligibility of a SKU.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Localized description if reseller is not eligible to transfer the SKU. |  [optional] |
|**ineligibilityReason** | [**IneligibilityReasonEnum**](#IneligibilityReasonEnum) | Specified the reason for ineligibility. |  [optional] |
|**isEligible** | **Boolean** | Whether reseller is eligible to transfer the SKU. |  [optional] |



## Enum: IneligibilityReasonEnum

| Name | Value |
|---- | -----|
| REASON_UNSPECIFIED | &quot;REASON_UNSPECIFIED&quot; |
| PENDING_TOS_ACCEPTANCE | &quot;PENDING_TOS_ACCEPTANCE&quot; |
| SKU_NOT_ELIGIBLE | &quot;SKU_NOT_ELIGIBLE&quot; |
| SKU_SUSPENDED | &quot;SKU_SUSPENDED&quot; |
| CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU | &quot;CHANNEL_PARTNER_NOT_AUTHORIZED_FOR_SKU&quot; |



