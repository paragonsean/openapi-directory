

# Invoice

Account Invoice object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **OffsetDateTime** | When this Invoice was generated. |  [optional] [readonly] |
|**id** | **Integer** | The Invoice&#39;s unique ID. |  [optional] [readonly] |
|**label** | **String** | The Invoice&#39;s display label. |  [optional] [readonly] |
|**subtotal** | **BigDecimal** | The amount of the Invoice before taxes in US Dollars. |  [optional] [readonly] |
|**tax** | **BigDecimal** | The amount of tax levied on the Invoice in US Dollars. |  [optional] [readonly] |
|**taxSummary** | [**List&lt;InvoiceTaxSummaryInner&gt;**](InvoiceTaxSummaryInner.md) | The amount of tax broken down into subtotals by source. |  [optional] [readonly] |
|**total** | **BigDecimal** | The amount of the Invoice after taxes in US Dollars. |  [optional] [readonly] |



