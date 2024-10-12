# LinodeApi.Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **Date** | When this Invoice was generated. | [optional] [readonly] 
**id** | **Number** | The Invoice&#39;s unique ID. | [optional] [readonly] 
**label** | **String** | The Invoice&#39;s display label. | [optional] [readonly] 
**subtotal** | **Number** | The amount of the Invoice before taxes in US Dollars. | [optional] [readonly] 
**tax** | **Number** | The amount of tax levied on the Invoice in US Dollars. | [optional] [readonly] 
**taxSummary** | [**[InvoiceTaxSummaryInner]**](InvoiceTaxSummaryInner.md) | The amount of tax broken down into subtotals by source. | [optional] [readonly] 
**total** | **Number** | The amount of the Invoice after taxes in US Dollars. | [optional] [readonly] 


