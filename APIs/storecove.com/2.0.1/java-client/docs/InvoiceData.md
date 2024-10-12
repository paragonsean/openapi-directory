

# InvoiceData

The invoice to send, in base64 encoded format. Provide either invoice, or invoiceData, but not both.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversionStrategy** | [**ConversionStrategyEnum**](#ConversionStrategyEnum) | How to interpret the document. |  [optional] |
|**document** | **String** | The base64 encoded version of the document. |  [optional] |



## Enum: ConversionStrategyEnum

| Name | Value |
|---- | -----|
| UBL | &quot;ubl&quot; |
| CII | &quot;cii&quot; |
| IDOC | &quot;idoc&quot; |



