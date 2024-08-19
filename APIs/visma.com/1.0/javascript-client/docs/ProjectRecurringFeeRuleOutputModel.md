# SeveraPublicRestApiDocumentation.ProjectRecurringFeeRuleOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costCenter** | [**ProjectCostCenterSubModel**](ProjectCostCenterSubModel.md) |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**customer** | [**ProjectFeeCustomerSubModel**](ProjectFeeCustomerSubModel.md) |  | [optional] 
**description** | **String** |  | [optional] 
**displayPeriodStartDate** | **Date** |  | [optional] 
**frequency** | **Number** |  | [optional] 
**generatedTimes** | **Number** |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**hasVolumePricing** | **Boolean** |  | [optional] 
**isActive** | **Boolean** |  | [optional] [default to true]
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**measurementUnit** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**phase** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**product** | [**ProjectFeeProductSubModel**](ProjectFeeProductSubModel.md) |  | [optional] 
**productType** | [**ProductType**](ProductType.md) |  | [optional] 
**project** | [**ProjectFeeProjectSubModel**](ProjectFeeProjectSubModel.md) |  | [optional] 
**quantity** | **Number** |  | [optional] 
**recurrenceEndDate** | **Date** |  | [optional] 
**recurrenceEndType** | [**RecurrenceEndTypes**](RecurrenceEndTypes.md) |  | [optional] 
**recurrenceStartDate** | **Date** |  | [optional] 
**recurrenceTimes** | **Number** |  | [optional] 
**recurringSalesAccount** | [**ProjectSalesAccountSubModel**](ProjectSalesAccountSubModel.md) |  | [optional] 
**salesAccount** | [**ProjectSalesAccountSubModel**](ProjectSalesAccountSubModel.md) |  | [optional] 
**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**user** | [**UserSubModel**](UserSubModel.md) |  | [optional] 
**vatRate** | **Number** |  | [optional] 


