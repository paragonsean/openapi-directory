# SearchAds360Api.Conversion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroupId** | **String** | DS ad group ID. | [optional] 
**adId** | **String** | DS ad ID. | [optional] 
**adUserDataConsent** | **String** | Represents consent for core platform services (CPS) preferences in settings. No default value. Acceptable values are: GRANTED: The desired consent status is to grant. Read the CPS preferences from GTE settings. DENIED: The desired consent status is to deny; CPS list is empty. | [optional] 
**advertiserId** | **String** | DS advertiser ID. | [optional] 
**agencyId** | **String** | DS agency ID. | [optional] 
**attributionModel** | **String** | Available to advertisers only after contacting DoubleClick Search customer support. | [optional] 
**campaignId** | **String** | DS campaign ID. | [optional] 
**channel** | **String** | Sales channel for the product. Acceptable values are: - \&quot;&#x60;local&#x60;\&quot;: a physical store - \&quot;&#x60;online&#x60;\&quot;: an online store  | [optional] 
**clickId** | **String** | DS click ID for the conversion. | [optional] 
**conversionId** | **String** | For offline conversions, advertisers provide this ID. Advertisers can specify any ID that is meaningful to them. Each conversion in a request must specify a unique ID, and the combination of ID and timestamp must be unique amongst all conversions within the advertiser. For online conversions, DS copies the &#x60;dsConversionId&#x60; or &#x60;floodlightOrderId&#x60; into this property depending on the advertiser&#39;s Floodlight instructions. | [optional] 
**conversionModifiedTimestamp** | **String** | The time at which the conversion was last modified, in epoch millis UTC. | [optional] 
**conversionTimestamp** | **String** | The time at which the conversion took place, in epoch millis UTC. | [optional] 
**countMillis** | **String** | Available to advertisers only after contacting DoubleClick Search customer support. | [optional] 
**criterionId** | **String** | DS criterion (keyword) ID. | [optional] 
**currencyCode** | **String** | The currency code for the conversion&#39;s revenue. Should be in ISO 4217 alphabetic (3-char) format. | [optional] 
**customDimension** | [**[CustomDimension]**](CustomDimension.md) | Custom dimensions for the conversion, which can be used to filter data in a report. | [optional] 
**customMetric** | [**[CustomMetric]**](CustomMetric.md) | Custom metrics for the conversion. | [optional] 
**customerId** | **String** | Customer ID of a client account in the new Search Ads 360 experience. | [optional] 
**deviceType** | **String** | The type of device on which the conversion occurred. | [optional] 
**dsConversionId** | **String** | ID that DoubleClick Search generates for each conversion. | [optional] 
**engineAccountId** | **String** | DS engine account ID. | [optional] 
**floodlightOrderId** | **String** | The Floodlight order ID provided by the advertiser for the conversion. | [optional] 
**inventoryAccountId** | **String** | ID that DS generates and uses to uniquely identify the inventory account that contains the product. | [optional] 
**productCountry** | **String** | The country registered for the Merchant Center feed that contains the product. Use an ISO 3166 code to specify a country. | [optional] 
**productGroupId** | **String** | DS product group ID. | [optional] 
**productId** | **String** | The product ID (SKU). | [optional] 
**productLanguage** | **String** | The language registered for the Merchant Center feed that contains the product. Use an ISO 639 code to specify a language. | [optional] 
**quantityMillis** | **String** | The quantity of this conversion, in millis. | [optional] 
**revenueMicros** | **String** | The revenue amount of this &#x60;TRANSACTION&#x60; conversion, in micros (value multiplied by 1000000, no decimal). For example, to specify a revenue value of \&quot;10\&quot; enter \&quot;10000000\&quot; (10 million) in your request. | [optional] 
**segmentationId** | **String** | The numeric segmentation identifier (for example, DoubleClick Search Floodlight activity ID). | [optional] 
**segmentationName** | **String** | The friendly segmentation identifier (for example, DoubleClick Search Floodlight activity name). | [optional] 
**segmentationType** | **String** | The segmentation type of this conversion (for example, &#x60;FLOODLIGHT&#x60;). | [optional] 
**state** | **String** | The state of the conversion, that is, either &#x60;ACTIVE&#x60; or &#x60;REMOVED&#x60;. Note: state DELETED is deprecated. | [optional] 
**storeId** | **String** | The ID of the local store for which the product was advertised. Applicable only when the channel is \&quot;&#x60;local&#x60;\&quot;. | [optional] 
**type** | **String** | The type of the conversion, that is, either &#x60;ACTION&#x60; or &#x60;TRANSACTION&#x60;. An &#x60;ACTION&#x60; conversion is an action by the user that has no monetarily quantifiable value, while a &#x60;TRANSACTION&#x60; conversion is an action that does have a monetarily quantifiable value. Examples are email list signups (&#x60;ACTION&#x60;) versus ecommerce purchases (&#x60;TRANSACTION&#x60;). | [optional] 



## Enum: AdUserDataConsentEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `GRANTED` (value: `"GRANTED"`)

* `DENIED` (value: `"DENIED"`)




