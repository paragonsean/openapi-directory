

# GoogleCloudChannelV1RepricingConfig

Configuration for repricing a Google bill over a period of time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustment** | [**GoogleCloudChannelV1RepricingAdjustment**](GoogleCloudChannelV1RepricingAdjustment.md) |  |  [optional] |
|**channelPartnerGranularity** | **Object** | Applies the repricing configuration at the channel partner level. The channel partner value is derived from the resource name. Takes an empty json object. Deprecated: This is no longer supported. Use RepricingConfig.EntitlementGranularity instead. |  [optional] |
|**conditionalOverrides** | [**List&lt;GoogleCloudChannelV1ConditionalOverride&gt;**](GoogleCloudChannelV1ConditionalOverride.md) | The conditional overrides to apply for this configuration. If you list multiple overrides, only the first valid override is used. If you don&#39;t list any overrides, the API uses the normal adjustment and rebilling basis. |  [optional] |
|**effectiveInvoiceMonth** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**entitlementGranularity** | [**GoogleCloudChannelV1RepricingConfigEntitlementGranularity**](GoogleCloudChannelV1RepricingConfigEntitlementGranularity.md) |  |  [optional] |
|**rebillingBasis** | [**RebillingBasisEnum**](#RebillingBasisEnum) | Required. The RebillingBasis to use for this bill. Specifies the relative cost based on repricing costs you will apply. |  [optional] |



## Enum: RebillingBasisEnum

| Name | Value |
|---- | -----|
| REBILLING_BASIS_UNSPECIFIED | &quot;REBILLING_BASIS_UNSPECIFIED&quot; |
| COST_AT_LIST | &quot;COST_AT_LIST&quot; |
| DIRECT_CUSTOMER_COST | &quot;DIRECT_CUSTOMER_COST&quot; |



