# StorecoveApi.DocumentInvoiceResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clarifications** | [**[InvoiceResponseClarification]**](InvoiceResponseClarification.md) | A list of clarifications why a received invoice was rejected (RE) or under query (UQ) and what action to take. | [optional] 
**effectiveDate** | **String** | The date when the status became effective. Format: yyyy-mm-dd. | [optional] 
**note** | **String** | A note to add to the invoice reponse | [optional] 
**responseCode** | **String** | The response code. For details see https://docs.peppol.eu/poacc/upgrade-3/codelist/UNCL4343-T111/ | 



## Enum: ResponseCodeEnum


* `AB` (value: `"AB"`)

* `IP` (value: `"IP"`)

* `UQ` (value: `"UQ"`)

* `CA` (value: `"CA"`)

* `RE` (value: `"RE"`)

* `AP` (value: `"AP"`)

* `PD` (value: `"PD"`)




