

# Segments

Dimensions according to which metrics are segmented in the response. Values of product dimensions, such as `offer_id`, reflect the state of a product at the time of the corresponding event, for example, impression or order. Segment fields cannot be selected in queries without also selecting at least one metric field. Values are only set for dimensions requested explicitly in the request's search query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Brand of the product. |  [optional] |
|**categoryL1** | **String** | [Product category (1st level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in Google&#39;s product taxonomy. |  [optional] |
|**categoryL2** | **String** | [Product category (2nd level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in Google&#39;s product taxonomy. |  [optional] |
|**categoryL3** | **String** | [Product category (3rd level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in Google&#39;s product taxonomy. |  [optional] |
|**categoryL4** | **String** | [Product category (4th level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in Google&#39;s product taxonomy. |  [optional] |
|**categoryL5** | **String** | [Product category (5th level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in Google&#39;s product taxonomy. |  [optional] |
|**currencyCode** | **String** | Currency in which price metrics are represented, for example, if you select &#x60;ordered_item_sales_micros&#x60;, the returned value will be represented by this currency. |  [optional] |
|**customLabel0** | **String** | Custom label 0 for custom grouping of products. |  [optional] |
|**customLabel1** | **String** | Custom label 1 for custom grouping of products. |  [optional] |
|**customLabel2** | **String** | Custom label 2 for custom grouping of products. |  [optional] |
|**customLabel3** | **String** | Custom label 3 for custom grouping of products. |  [optional] |
|**customLabel4** | **String** | Custom label 4 for custom grouping of products. |  [optional] |
|**customerCountryCode** | **String** | Code of the country where the customer is located at the time of the event. Represented in the ISO 3166 format. If the customer country cannot be determined, a special &#39;ZZ&#39; code is returned. |  [optional] |
|**date** | [**Date**](Date.md) |  |  [optional] |
|**offerId** | **String** | Merchant-provided id of the product. |  [optional] |
|**productTypeL1** | **String** | [Product type (1st level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in merchant&#39;s own product taxonomy. |  [optional] |
|**productTypeL2** | **String** | [Product type (2nd level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in merchant&#39;s own product taxonomy. |  [optional] |
|**productTypeL3** | **String** | [Product type (3rd level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in merchant&#39;s own product taxonomy. |  [optional] |
|**productTypeL4** | **String** | [Product type (4th level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in merchant&#39;s own product taxonomy. |  [optional] |
|**productTypeL5** | **String** | [Product type (5th level)](https://developers.google.com/shopping-content/guides/reports/segmentation#category_and_product_type) in merchant&#39;s own product taxonomy. |  [optional] |
|**program** | [**ProgramEnum**](#ProgramEnum) | Program to which metrics apply, for example, Free Product Listing. |  [optional] |
|**title** | **String** | Title of the product. |  [optional] |
|**week** | [**Date**](Date.md) |  |  [optional] |



## Enum: ProgramEnum

| Name | Value |
|---- | -----|
| PROGRAM_UNSPECIFIED | &quot;PROGRAM_UNSPECIFIED&quot; |
| SHOPPING_ADS | &quot;SHOPPING_ADS&quot; |
| FREE_PRODUCT_LISTING | &quot;FREE_PRODUCT_LISTING&quot; |
| FREE_LOCAL_PRODUCT_LISTING | &quot;FREE_LOCAL_PRODUCT_LISTING&quot; |
| BUY_ON_GOOGLE_LISTING | &quot;BUY_ON_GOOGLE_LISTING&quot; |



