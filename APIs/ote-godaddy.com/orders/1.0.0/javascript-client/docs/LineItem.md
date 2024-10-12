# OpenapiJsClient.LineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **[String]** | A collection of domain names purchased if the current product is domain | [optional] 
**label** | **String** | Human readable description of the current product | 
**period** | **Number** |  | [optional] [default to 1]
**periodUnit** | **String** | The unit of time that periodCount is measured in | [optional] [default to &#39;MONTH&#39;]
**pfid** | **Number** | Unique identifier of the current product | [optional] 
**pricing** | [**LineItemPricing**](LineItemPricing.md) |  | 
**quantity** | **Number** | Number of the current product included in the specified order | 
**taxCollector** | [**LineItemTaxCollector**](LineItemTaxCollector.md) |  | [optional] 



## Enum: PeriodUnitEnum


* `MONTH` (value: `"MONTH"`)

* `QUARTER` (value: `"QUARTER"`)

* `SEMI_ANNUAL` (value: `"SEMI_ANNUAL"`)

* `YEAR` (value: `"YEAR"`)

* `ONE_TIME` (value: `"ONE_TIME"`)




