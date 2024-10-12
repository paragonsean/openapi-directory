# BillbeeApi.BillbeeInterfacesBillbeeAPIModelInvoiceApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalFees** | [**[BillbeeInterfacesBillbeeAPIModelAdditionalFeeApiModel]**](BillbeeInterfacesBillbeeAPIModelAdditionalFeeApiModel.md) |  | [optional] 
**billbeeId** | **Number** |  | [optional] 
**company** | **String** |  | [optional] 
**currency** | **String** |  | [optional] 
**customerNumber** | **Number** |  | [optional] 
**customerVatId** | **String** | The vat-id, that was given by the customer to fulfill this order | [optional] 
**debtorNumber** | **Number** |  | [optional] 
**email** | **String** |  | [optional] 
**firstName** | **String** |  | [optional] 
**invoiceDate** | **Date** |  | [optional] 
**invoiceNumber** | **String** |  | [optional] 
**lastName** | **String** |  | [optional] 
**merchantVatId** | **String** | The vat-id, that should be displayed on the invoice and other order documents | [optional] 
**orderNumber** | **String** |  | [optional] 
**payDate** | **Date** |  | [optional] 
**paymentTypeId** | **Number** |  | [optional] 
**positions** | [**[BillbeeInterfacesBillbeeAPIModelInvoiceApiPositionApiModel]**](BillbeeInterfacesBillbeeAPIModelInvoiceApiPositionApiModel.md) |  | [optional] 
**salutation** | **String** |  | [optional] 
**shippingCountry** | **String** | two letters for CountryCode Identification | [optional] 
**shopName** | **String** |  | [optional] 
**title** | **String** |  | [optional] 
**totalGross** | **Number** |  | [optional] 
**totalNet** | **Number** |  | [optional] 
**transactionId** | **String** |  | [optional] 
**type** | **String** |  | [optional] 
**vatFlags** | [**BillbeeInterfacesOrderVatDetailsRecognizedHistoryEntryVatDetectionFlags**](BillbeeInterfacesOrderVatDetailsRecognizedHistoryEntryVatDetectionFlags.md) |  | [optional] 
**vatMode** | **Number** |  | [optional] 



## Enum: VatModeEnum


* `0` (value: `0`)

* `1` (value: `1`)

* `2` (value: `2`)

* `3` (value: `3`)

* `4` (value: `4`)

* `5` (value: `5`)




