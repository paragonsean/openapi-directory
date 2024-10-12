

# GoogleCloudPaymentsResellerSubscriptionV1Product

A Product resource that defines a subscription service that can be resold.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundleDetails** | [**ProductBundleDetails**](ProductBundleDetails.md) |  |  [optional] |
|**finiteBillingCycleDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails**](GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails.md) |  |  [optional] |
|**name** | **String** | Identifier. Response only. Resource name of the product. It will have the format of \&quot;partners/{partner_id}/products/{product_id}\&quot; |  [optional] |
|**priceConfigs** | [**List&lt;GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfig&gt;**](GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfig.md) | Output only. Price configs for the product in the available regions. |  [optional] [readonly] |
|**productType** | [**ProductTypeEnum**](#ProductTypeEnum) | Output only. Output Only. Specifies the type of the product. |  [optional] [readonly] |
|**regionCodes** | **List&lt;String&gt;** | Output only. 2-letter ISO region code where the product is available in. Ex. \&quot;US\&quot; Please refers to: https://en.wikipedia.org/wiki/ISO_3166-1 |  [optional] [readonly] |
|**subscriptionBillingCycleDuration** | [**GoogleCloudPaymentsResellerSubscriptionV1Duration**](GoogleCloudPaymentsResellerSubscriptionV1Duration.md) |  |  [optional] |
|**titles** | [**List&lt;GoogleTypeLocalizedText&gt;**](GoogleTypeLocalizedText.md) | Output only. Localized human readable name of the product. |  [optional] [readonly] |



## Enum: ProductTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRODUCT_TYPE_UNSPECIFIED&quot; |
| SUBSCRIPTION | &quot;PRODUCT_TYPE_SUBSCRIPTION&quot; |
| BUNDLE_SUBSCRIPTION | &quot;PRODUCT_TYPE_BUNDLE_SUBSCRIPTION&quot; |



