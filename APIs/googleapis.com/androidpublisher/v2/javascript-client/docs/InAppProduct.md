# GooglePlayDeveloper.InAppProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultLanguage** | **String** | The default language of the localized data, as defined by BCP 47. e.g. \&quot;en-US\&quot;, \&quot;en-GB\&quot;. | [optional] 
**defaultPrice** | [**Price**](Price.md) |  | [optional] 
**gracePeriod** | **String** | Grace period of the subscription, specified in ISO 8601 format. It will allow developers to give their subscribers a grace period when the payment for the new recurrence period is declined. Acceptable values &#x3D; \&quot;P3D\&quot; (three days), \&quot;P7D\&quot; (seven days), \&quot;P14D\&quot; (fourteen days), and \&quot;P30D\&quot; (thirty days) | [optional] 
**listings** | [**{String: InAppProductListing}**](InAppProductListing.md) | List of localized title and description data. | [optional] 
**packageName** | **String** | The package name of the parent app. | [optional] 
**prices** | [**{String: Price}**](Price.md) | Prices per buyer region. None of these prices should be zero. In-app products can never be free. | [optional] 
**purchaseType** | **String** | Purchase type enum value. Unmodifiable after creation. | [optional] 
**sku** | **String** | The stock-keeping-unit (SKU) of the product, unique within an app. | [optional] 
**status** | **String** |  | [optional] 
**subscriptionPeriod** | **String** | Subscription period, specified in ISO 8601 format. Acceptable values are \&quot;P1W\&quot; (one week), \&quot;P1M\&quot; (one month), \&quot;P3M\&quot; (three months), \&quot;P6M\&quot; (six months), and \&quot;P1Y\&quot; (one year). | [optional] 
**trialPeriod** | **String** | Trial period, specified in ISO 8601 format. Acceptable values are anything between \&quot;P7D\&quot; (seven days) and \&quot;P999D\&quot; (999 days). Seasonal subscriptions cannot have a trial period. | [optional] 


