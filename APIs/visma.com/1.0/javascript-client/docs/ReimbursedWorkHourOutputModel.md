# SeveraPublicRestApiDocumentation.ReimbursedWorkHourOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**customer** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**description** | **String** |  | [optional] 
**endTime** | **Date** |  | [optional] 
**eventDate** | **Date** |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**invoiceGuid** | **String** |  | [optional] 
**invoiceQuantity** | **Number** |  | [optional] 
**invoiceRowComment** | **String** |  | [optional] 
**invoiceRowDescription** | **String** |  | [optional] 
**invoiceRowGuid** | **String** |  | [optional] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**overtime** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**phase** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**plannedInvoiceQuantity** | **Number** |  | [optional] 
**project** | [**ReimbursedWorkHourProjectSubModel**](ReimbursedWorkHourProjectSubModel.md) |  | [optional] 
**quantity** | **Number** |  | [optional] 
**startTime** | **Date** |  | [optional] 
**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**user** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**workType** | [**ModelWithName**](ModelWithName.md) |  | [optional] 


