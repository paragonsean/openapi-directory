

# DocumentInvoiceResponse

The invoice response to send or received.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clarifications** | [**List&lt;InvoiceResponseClarification&gt;**](InvoiceResponseClarification.md) | A list of clarifications why a received invoice was rejected (RE) or under query (UQ) and what action to take. |  [optional] |
|**effectiveDate** | **String** | The date when the status became effective. Format: yyyy-mm-dd. |  [optional] |
|**note** | **String** | A note to add to the invoice reponse |  [optional] |
|**responseCode** | [**ResponseCodeEnum**](#ResponseCodeEnum) | The response code. For details see https://docs.peppol.eu/poacc/upgrade-3/codelist/UNCL4343-T111/ |  |



## Enum: ResponseCodeEnum

| Name | Value |
|---- | -----|
| AB | &quot;AB&quot; |
| IP | &quot;IP&quot; |
| UQ | &quot;UQ&quot; |
| CA | &quot;CA&quot; |
| RE | &quot;RE&quot; |
| AP | &quot;AP&quot; |
| PD | &quot;PD&quot; |



