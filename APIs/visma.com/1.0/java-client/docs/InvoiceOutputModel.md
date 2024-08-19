

# InvoiceOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingCustomer** | [**InvoiceCustomerSubModel**](InvoiceCustomerSubModel.md) |  |  [optional] |
|**canBeDeleted** | **Boolean** |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**creditNoteInvoice** | [**RelatedInvoiceSubModel**](RelatedInvoiceSubModel.md) |  |  [optional] |
|**culture** | [**FormattingCultureSubModel2**](FormattingCultureSubModel2.md) |  |  [optional] |
|**currency** | [**CurrencySubModel**](CurrencySubModel.md) |  |  [optional] |
|**currencyRate** | **Double** |  |  [optional] |
|**customer** | [**InvoiceCustomerSubModel**](InvoiceCustomerSubModel.md) |  |  [optional] |
|**date** | **LocalDate** |  |  [optional] |
|**dueDate** | **LocalDate** |  |  [optional] |
|**entryDate** | **LocalDate** |  |  [optional] |
|**flatRatesTotalExcludingTax** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**freeText1** | [**FreeTextModel2**](FreeTextModel2.md) |  |  [optional] |
|**freeText2** | [**FreeTextModel2**](FreeTextModel2.md) |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**invoiceNumberBusinessUnitGuid** | **String** |  |  [optional] |
|**invoiceTemplate** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**isCreditNote** | **Boolean** |  |  [optional] |
|**language** | [**InvoiceLanguageSubModel**](InvoiceLanguageSubModel.md) |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**notes** | **String** |  |  [optional] |
|**number** | **Integer** |  |  [optional] |
|**orderNumber** | **String** |  |  [optional] |
|**ourReference** | **String** |  |  [optional] |
|**overdueInterest** | **Double** |  |  [optional] |
|**paymentDate** | **LocalDate** |  |  [optional] |
|**paymentTerm** | **Integer** |  |  [optional] |
|**projectFeesTotalExcludingTax** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**projectTravelExpensesTotalExcludingTax** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**projects** | [**List&lt;InvoiceProjectSubModel&gt;**](InvoiceProjectSubModel.md) |  |  [optional] |
|**receiverAddress** | [**InvoiceReceiverAddressSubModel**](InvoiceReceiverAddressSubModel.md) |  |  [optional] |
|**receiverContactEmail** | **String** |  |  [optional] |
|**receiverContactGuid** | **String** |  |  [optional] |
|**receiverContactName** | **String** |  |  [optional] |
|**receiverCustomerName** | **String** |  |  [optional] |
|**receiverKvkNumber** | **String** |  |  [optional] |
|**receiverVatNumber** | **String** |  |  [optional] |
|**referenceNumber** | **String** |  |  [optional] |
|**reimburseInvoice** | [**RelatedInvoiceSubModel**](RelatedInvoiceSubModel.md) |  |  [optional] |
|**senderAddress** | [**InvoiceSenderAddressSubModel**](InvoiceSenderAddressSubModel.md) |  |  [optional] |
|**senderContactGuid** | **String** |  |  [optional] |
|**senderContactName** | **String** |  |  [optional] |
|**senderKvkNumber** | **String** |  |  [optional] |
|**senderName** | **String** |  |  [optional] |
|**senderVatNumber** | **String** |  |  [optional] |
|**status** | [**InvoiceStatusSubModel**](InvoiceStatusSubModel.md) |  |  [optional] |
|**totalExcludingTax** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**totalIncludingTax** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**totalTax** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**workHourValueAddedTax** | **Double** |  |  [optional] |
|**workHoursQuantity** | **Double** |  |  [optional] |
|**workHoursTotalExcludingTax** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**yourReference** | **String** |  |  [optional] |



