

# BillbeeInterfacesBillbeeAPIModelInvoiceApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalFees** | [**List&lt;BillbeeInterfacesBillbeeAPIModelAdditionalFeeApiModel&gt;**](BillbeeInterfacesBillbeeAPIModelAdditionalFeeApiModel.md) |  |  [optional] |
|**billbeeId** | **Long** |  |  [optional] |
|**company** | **String** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**customerNumber** | **Integer** |  |  [optional] |
|**customerVatId** | **String** | The vat-id, that was given by the customer to fulfill this order |  [optional] |
|**debtorNumber** | **Integer** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**invoiceDate** | **OffsetDateTime** |  |  [optional] |
|**invoiceNumber** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**merchantVatId** | **String** | The vat-id, that should be displayed on the invoice and other order documents |  [optional] |
|**orderNumber** | **String** |  |  [optional] |
|**payDate** | **OffsetDateTime** |  |  [optional] |
|**paymentTypeId** | **Integer** |  |  [optional] |
|**positions** | [**List&lt;BillbeeInterfacesBillbeeAPIModelInvoiceApiPositionApiModel&gt;**](BillbeeInterfacesBillbeeAPIModelInvoiceApiPositionApiModel.md) |  |  [optional] |
|**salutation** | **String** |  |  [optional] |
|**shippingCountry** | **String** | two letters for CountryCode Identification |  [optional] |
|**shopName** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**totalGross** | **Double** |  |  [optional] |
|**totalNet** | **Double** |  |  [optional] |
|**transactionId** | **String** |  |  [optional] |
|**type** | **String** |  |  [optional] |
|**vatFlags** | [**BillbeeInterfacesOrderVatDetailsRecognizedHistoryEntryVatDetectionFlags**](BillbeeInterfacesOrderVatDetailsRecognizedHistoryEntryVatDetectionFlags.md) |  |  [optional] |
|**vatMode** | [**VatModeEnum**](#VatModeEnum) |  |  [optional] |



## Enum: VatModeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |



