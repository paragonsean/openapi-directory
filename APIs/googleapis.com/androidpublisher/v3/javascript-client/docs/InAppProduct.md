# GooglePlayAndroidDeveloperApi.InAppProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultLanguage** | **String** | Default language of the localized data, as defined by BCP-47. e.g. \&quot;en-US\&quot;. | [optional] 
**defaultPrice** | [**Price**](Price.md) |  | [optional] 
**gracePeriod** | **String** | Grace period of the subscription, specified in ISO 8601 format. Allows developers to give their subscribers a grace period when the payment for the new recurrence period is declined. Acceptable values are P0D (zero days), P3D (three days), P7D (seven days), P14D (14 days), and P30D (30 days). | [optional] 
**listings** | [**{String: InAppProductListing}**](InAppProductListing.md) | List of localized title and description data. Map key is the language of the localized data, as defined by BCP-47, e.g. \&quot;en-US\&quot;. | [optional] 
**managedProductTaxesAndComplianceSettings** | [**ManagedProductTaxAndComplianceSettings**](ManagedProductTaxAndComplianceSettings.md) |  | [optional] 
**packageName** | **String** | Package name of the parent app. | [optional] 
**prices** | [**{String: Price}**](Price.md) | Prices per buyer region. None of these can be zero, as in-app products are never free. Map key is region code, as defined by ISO 3166-2. | [optional] 
**purchaseType** | **String** | The type of the product, e.g. a recurring subscription. | [optional] 
**sku** | **String** | Stock-keeping-unit (SKU) of the product, unique within an app. | [optional] 
**status** | **String** | The status of the product, e.g. whether it&#39;s active. | [optional] 
**subscriptionPeriod** | **String** | Subscription period, specified in ISO 8601 format. Acceptable values are P1W (one week), P1M (one month), P3M (three months), P6M (six months), and P1Y (one year). | [optional] 
**subscriptionTaxesAndComplianceSettings** | [**SubscriptionTaxAndComplianceSettings**](SubscriptionTaxAndComplianceSettings.md) |  | [optional] 
**trialPeriod** | **String** | Trial period, specified in ISO 8601 format. Acceptable values are anything between P7D (seven days) and P999D (999 days). | [optional] 



## Enum: PurchaseTypeEnum


* `purchaseTypeUnspecified` (value: `"purchaseTypeUnspecified"`)

* `managedUser` (value: `"managedUser"`)

* `subscription` (value: `"subscription"`)





## Enum: StatusEnum


* `statusUnspecified` (value: `"statusUnspecified"`)

* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)




