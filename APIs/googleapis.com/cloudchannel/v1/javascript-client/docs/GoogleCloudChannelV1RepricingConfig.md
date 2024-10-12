# CloudChannelApi.GoogleCloudChannelV1RepricingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment** | [**GoogleCloudChannelV1RepricingAdjustment**](GoogleCloudChannelV1RepricingAdjustment.md) |  | [optional] 
**channelPartnerGranularity** | **Object** | Applies the repricing configuration at the channel partner level. The channel partner value is derived from the resource name. Takes an empty json object. Deprecated: This is no longer supported. Use RepricingConfig.EntitlementGranularity instead. | [optional] 
**conditionalOverrides** | [**[GoogleCloudChannelV1ConditionalOverride]**](GoogleCloudChannelV1ConditionalOverride.md) | The conditional overrides to apply for this configuration. If you list multiple overrides, only the first valid override is used. If you don&#39;t list any overrides, the API uses the normal adjustment and rebilling basis. | [optional] 
**effectiveInvoiceMonth** | [**GoogleTypeDate**](GoogleTypeDate.md) |  | [optional] 
**entitlementGranularity** | [**GoogleCloudChannelV1RepricingConfigEntitlementGranularity**](GoogleCloudChannelV1RepricingConfigEntitlementGranularity.md) |  | [optional] 
**rebillingBasis** | **String** | Required. The RebillingBasis to use for this bill. Specifies the relative cost based on repricing costs you will apply. | [optional] 



## Enum: RebillingBasisEnum


* `REBILLING_BASIS_UNSPECIFIED` (value: `"REBILLING_BASIS_UNSPECIFIED"`)

* `COST_AT_LIST` (value: `"COST_AT_LIST"`)

* `DIRECT_CUSTOMER_COST` (value: `"DIRECT_CUSTOMER_COST"`)




