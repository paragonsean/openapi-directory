# XtrfHomePortalApi.ProviderInvoiceDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyId** | **Number** |  | [optional] 
**dates** | [**ProviderInvoiceDatesDTO**](ProviderInvoiceDatesDTO.md) |  | [optional] 
**draftNumber** | **String** |  | [optional] 
**finalNumber** | **String** |  | [optional] 
**id** | **Number** |  | [optional] 
**internalNumber** | **String** |  | [optional] 
**jobsNetValue** | **Number** |  | [optional] 
**notesFromProvider** | **String** |  | [optional] 
**paymentStatus** | **String** |  | [optional] 
**providerId** | **Number** |  | [optional] 
**status** | **String** |  | [optional] 
**totalGross** | **Number** |  | [optional] 
**totalGrossInWords** | **String** |  | [optional] 
**totalNetto** | **Number** |  | [optional] 



## Enum: PaymentStatusEnum


* `NOT_PAID` (value: `"NOT_PAID"`)

* `FULLY_PAID` (value: `"FULLY_PAID"`)

* `IRRECOVERABLE` (value: `"IRRECOVERABLE"`)

* `PARTIALLY_PAID` (value: `"PARTIALLY_PAID"`)





## Enum: StatusEnum


* `POSTPONED` (value: `"POSTPONED"`)

* `TO_BE_SENT` (value: `"TO_BE_SENT"`)

* `SENT` (value: `"SENT"`)

* `CONFIRMED` (value: `"CONFIRMED"`)

* `BILL_CREATED` (value: `"BILL_CREATED"`)




