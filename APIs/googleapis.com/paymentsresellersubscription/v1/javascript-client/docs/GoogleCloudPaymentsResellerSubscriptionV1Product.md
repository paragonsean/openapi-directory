# PaymentsResellerSubscriptionApi.GoogleCloudPaymentsResellerSubscriptionV1Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundleDetails** | [**ProductBundleDetails**](ProductBundleDetails.md) |  | [optional] 
**finiteBillingCycleDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails**](GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails.md) |  | [optional] 
**name** | **String** | Identifier. Response only. Resource name of the product. It will have the format of \&quot;partners/{partner_id}/products/{product_id}\&quot; | [optional] 
**priceConfigs** | [**[GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfig]**](GoogleCloudPaymentsResellerSubscriptionV1ProductPriceConfig.md) | Output only. Price configs for the product in the available regions. | [optional] [readonly] 
**productType** | **String** | Output only. Output Only. Specifies the type of the product. | [optional] [readonly] 
**regionCodes** | **[String]** | Output only. 2-letter ISO region code where the product is available in. Ex. \&quot;US\&quot; Please refers to: https://en.wikipedia.org/wiki/ISO_3166-1 | [optional] [readonly] 
**subscriptionBillingCycleDuration** | [**GoogleCloudPaymentsResellerSubscriptionV1Duration**](GoogleCloudPaymentsResellerSubscriptionV1Duration.md) |  | [optional] 
**titles** | [**[GoogleTypeLocalizedText]**](GoogleTypeLocalizedText.md) | Output only. Localized human readable name of the product. | [optional] [readonly] 



## Enum: ProductTypeEnum


* `UNSPECIFIED` (value: `"PRODUCT_TYPE_UNSPECIFIED"`)

* `SUBSCRIPTION` (value: `"PRODUCT_TYPE_SUBSCRIPTION"`)

* `BUNDLE_SUBSCRIPTION` (value: `"PRODUCT_TYPE_BUNDLE_SUBSCRIPTION"`)




