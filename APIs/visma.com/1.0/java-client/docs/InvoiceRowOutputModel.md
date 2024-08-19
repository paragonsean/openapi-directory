

# InvoiceRowOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **InvoiceRowCategory** |  |  [optional] |
|**code** | **List&lt;String&gt;** |  |  [optional] |
|**costCenter** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**flatRateGuid** | **String** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**hasInvoiceComment** | **Boolean** |  |  [optional] |
|**invoiceGuid** | **String** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**measurementUnit** | **String** |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**recurringSalesAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  |  [optional] |
|**rowType** | **InvoiceRowType** |  |  [optional] |
|**salesAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  |  [optional] |
|**salesReceivableAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  |  [optional] |
|**sortOrder** | **Integer** |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**vatAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  |  [optional] |
|**vatRate** | **Double** |  |  [optional] |



