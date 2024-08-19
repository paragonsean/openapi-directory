# SeveraPublicRestApiDocumentation.InvoiceRowOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**InvoiceRowCategory**](InvoiceRowCategory.md) |  | [optional] 
**code** | **[String]** |  | [optional] 
**costCenter** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**flatRateGuid** | **String** |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**hasInvoiceComment** | **Boolean** |  | [optional] 
**invoiceGuid** | **String** |  | [optional] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**measurementUnit** | **String** |  | [optional] 
**quantity** | **Number** |  | [optional] 
**recurringSalesAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  | [optional] 
**rowType** | [**InvoiceRowType**](InvoiceRowType.md) |  | [optional] 
**salesAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  | [optional] 
**salesReceivableAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  | [optional] 
**sortOrder** | **Number** |  | [optional] 
**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**vatAccount** | [**InvoiceRowAccountingSubModel**](InvoiceRowAccountingSubModel.md) |  | [optional] 
**vatRate** | **Number** |  | [optional] 


