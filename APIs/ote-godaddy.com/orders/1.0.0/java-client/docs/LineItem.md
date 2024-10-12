

# LineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domains** | **List&lt;String&gt;** | A collection of domain names purchased if the current product is domain |  [optional] |
|**label** | **String** | Human readable description of the current product |  |
|**period** | **Double** |  |  [optional] |
|**periodUnit** | [**PeriodUnitEnum**](#PeriodUnitEnum) | The unit of time that periodCount is measured in |  [optional] |
|**pfid** | **Integer** | Unique identifier of the current product |  [optional] |
|**pricing** | [**LineItemPricing**](LineItemPricing.md) |  |  |
|**quantity** | **Integer** | Number of the current product included in the specified order |  |
|**taxCollector** | [**LineItemTaxCollector**](LineItemTaxCollector.md) |  |  [optional] |



## Enum: PeriodUnitEnum

| Name | Value |
|---- | -----|
| MONTH | &quot;MONTH&quot; |
| QUARTER | &quot;QUARTER&quot; |
| SEMI_ANNUAL | &quot;SEMI_ANNUAL&quot; |
| YEAR | &quot;YEAR&quot; |
| ONE_TIME | &quot;ONE_TIME&quot; |



