

# GoogleCloudChannelV1ConditionalOverride

Specifies the override to conditionally apply.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustment** | [**GoogleCloudChannelV1RepricingAdjustment**](GoogleCloudChannelV1RepricingAdjustment.md) |  |  [optional] |
|**rebillingBasis** | [**RebillingBasisEnum**](#RebillingBasisEnum) | Required. The RebillingBasis to use for the applied override. Shows the relative cost based on your repricing costs. |  [optional] |
|**repricingCondition** | [**GoogleCloudChannelV1RepricingCondition**](GoogleCloudChannelV1RepricingCondition.md) |  |  [optional] |



## Enum: RebillingBasisEnum

| Name | Value |
|---- | -----|
| REBILLING_BASIS_UNSPECIFIED | &quot;REBILLING_BASIS_UNSPECIFIED&quot; |
| COST_AT_LIST | &quot;COST_AT_LIST&quot; |
| DIRECT_CUSTOMER_COST | &quot;DIRECT_CUSTOMER_COST&quot; |



