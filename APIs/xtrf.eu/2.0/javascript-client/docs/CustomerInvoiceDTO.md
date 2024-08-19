# XtrfHomePortalApi.CustomerInvoiceDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyId** | **Number** |  | [optional] 
**customerDetails** | [**CustomerDetailsDTO**](CustomerDetailsDTO.md) |  | [optional] 
**customerId** | **Number** |  | [optional] 
**dates** | [**CustomerInvoiceDatesDTO**](CustomerInvoiceDatesDTO.md) |  | [optional] 
**id** | **Number** |  | [optional] 
**invoiceNumber** | **String** |  | [optional] 
**paymentMethodId** | **Number** |  | [optional] 
**paymentTerms** | [**PaymentTermsDTO**](PaymentTermsDTO.md) |  | [optional] 
**status** | **String** |  | [optional] 
**tasks** | [**[TaskDTO]**](TaskDTO.md) |  | [optional] 
**tasksValue** | **Number** |  | [optional] 
**totalGross** | **Number** |  | [optional] 
**totalInWords** | **String** |  | [optional] 
**totalNetto** | **Number** |  | [optional] 
**type** | **String** |  | [optional] 
**vatCalculationRule** | **String** |  | [optional] 



## Enum: StatusEnum


* `NOT_READY` (value: `"NOT_READY"`)

* `READY` (value: `"READY"`)

* `SENT` (value: `"SENT"`)





## Enum: TypeEnum


* `FINAL` (value: `"FINAL"`)

* `DRAFT` (value: `"DRAFT"`)

* `CREDIT_NOTE` (value: `"CREDIT_NOTE"`)





## Enum: VatCalculationRuleEnum


* `SUM_ITEMS` (value: `"SUM_ITEMS"`)

* `BY_NET_TOTAL` (value: `"BY_NET_TOTAL"`)




