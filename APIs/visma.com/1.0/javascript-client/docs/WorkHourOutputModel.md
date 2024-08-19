# SeveraPublicRestApiDocumentation.WorkHourOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billableStatus** | [**BillableStatusType**](BillableStatusType.md) |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**customer** | [**WorkHourCustomerSubModel**](WorkHourCustomerSubModel.md) |  | [optional] 
**description** | **String** |  | [optional] 
**endTime** | **Date** |  | [optional] 
**eventDate** | **Date** |  | 
**guid** | **String** |  | [optional] [readonly] 
**invoice** | [**WorkHourInvoiceSubModel**](WorkHourInvoiceSubModel.md) |  | [optional] 
**invoiceQuantity** | **Number** |  | [optional] 
**invoiceRowComment** | **String** |  | [optional] 
**invoiceRowDescription** | **String** |  | [optional] 
**invoiceRowGuid** | **String** |  | [optional] 
**isApproved** | **Boolean** |  | [optional] 
**isBillable** | **Boolean** |  | [optional] 
**isModifiable** | **Boolean** |  | [optional] 
**isProductive** | **Boolean** |  | [optional] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**overtime** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**phase** | [**WorkHourPhaseSubModel**](WorkHourPhaseSubModel.md) |  | [optional] 
**plannedInvoiceQuantity** | **Number** |  | [optional] 
**project** | [**WorkHourProjectSubModel**](WorkHourProjectSubModel.md) |  | [optional] 
**quantity** | **Number** |  | [optional] 
**startTime** | **Date** |  | [optional] 
**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**user** | [**UserWithFirstNameLastNamePhotoFileModelAndRequiredGuid**](UserWithFirstNameLastNamePhotoFileModelAndRequiredGuid.md) |  | [optional] 
**workType** | [**WorkHourWorkTypeSubModel**](WorkHourWorkTypeSubModel.md) |  | [optional] 


