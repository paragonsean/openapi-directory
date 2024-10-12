# ContentApiForShopping.ProductView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregatedDestinationStatus** | **String** | Aggregated destination status. | [optional] 
**availability** | **String** | Availability of the product. | [optional] 
**brand** | **String** | Brand of the product. | [optional] 
**categoryL1** | **String** | First level of the product category in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**categoryL2** | **String** | Second level of the product category in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**categoryL3** | **String** | Third level of the product category in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**categoryL4** | **String** | Fourth level of the product category in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**categoryL5** | **String** | Fifth level of the product category in [Google&#39;s product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**channel** | **String** | Channel of the product (online versus local). | [optional] 
**condition** | **String** | Condition of the product. | [optional] 
**creationTime** | **String** | The time the merchant created the product in timestamp seconds. | [optional] 
**currencyCode** | **String** | Product price currency code (for example, ISO 4217). Absent if product price is not available. | [optional] 
**expirationDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**gtin** | **[String]** | GTIN of the product. | [optional] 
**id** | **String** | The REST ID of the product, in the form of channel:contentLanguage:targetCountry:offerId. Content API methods that operate on products take this as their productId parameter. Should always be included in the SELECT clause. | [optional] 
**itemGroupId** | **String** | Item group ID provided by the merchant for grouping variants together. | [optional] 
**itemIssues** | [**[ProductViewItemIssue]**](ProductViewItemIssue.md) | List of item issues for the product. | [optional] 
**languageCode** | **String** | Language code of the product in BCP 47 format. | [optional] 
**offerId** | **String** | Merchant-provided id of the product. | [optional] 
**priceMicros** | **String** | Product price specified as micros (1 millionth of a standard unit, 1 USD &#x3D; 1000000 micros) in the product currency. Absent in case the information about the price of the product is not available. | [optional] 
**productTypeL1** | **String** | First level of the product type in merchant&#39;s own [product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**productTypeL2** | **String** | Second level of the product type in merchant&#39;s own [product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**productTypeL3** | **String** | Third level of the product type in merchant&#39;s own [product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**productTypeL4** | **String** | Fourth level of the product type in merchant&#39;s own [product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**productTypeL5** | **String** | Fifth level of the product type in merchant&#39;s own [product taxonomy](https://support.google.com/merchants/answer/6324436). | [optional] 
**shippingLabel** | **String** | The normalized shipping label specified in the feed | [optional] 
**title** | **String** | Title of the product. | [optional] 



## Enum: AggregatedDestinationStatusEnum


* `AGGREGATED_STATUS_UNSPECIFIED` (value: `"AGGREGATED_STATUS_UNSPECIFIED"`)

* `NOT_ELIGIBLE_OR_DISAPPROVED` (value: `"NOT_ELIGIBLE_OR_DISAPPROVED"`)

* `PENDING` (value: `"PENDING"`)

* `ELIGIBLE_LIMITED` (value: `"ELIGIBLE_LIMITED"`)

* `ELIGIBLE` (value: `"ELIGIBLE"`)





## Enum: ChannelEnum


* `CHANNEL_UNSPECIFIED` (value: `"CHANNEL_UNSPECIFIED"`)

* `LOCAL` (value: `"LOCAL"`)

* `ONLINE` (value: `"ONLINE"`)




