# SeveraPublicRestApiDocumentation.ProjectFeeOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingDependencyPhase** | [**ProjectFeePhaseSubModel**](ProjectFeePhaseSubModel.md) |  | [optional] 
**billingSchedule** | [**ProjectFeeBillingScheduleType**](ProjectFeeBillingScheduleType.md) |  | [optional] 
**costCenter** | [**ProjectCostCenterSubModel**](ProjectCostCenterSubModel.md) |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**customer** | [**ProjectFeeCustomerSubModel**](ProjectFeeCustomerSubModel.md) |  | [optional] 
**description** | **String** |  | [optional] 
**displayPeriodStartDate** | **Date** |  | [optional] 
**eventDate** | **Date** |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**hasVolumePricing** | **Boolean** |  | [optional] 
**invoice** | [**ProjectFeeInvoiceSubModel**](ProjectFeeInvoiceSubModel.md) |  | [optional] 
**invoiceQuantity** | **Number** |  | [optional] 
**invoiceRowComment** | **String** |  | [optional] 
**invoiceRowDescription** | **String** |  | [optional] 
**invoiceRowGuid** | **String** |  | [optional] 
**isBillable** | **Boolean** |  | [optional] 
**isRecurrenceRule** | **Boolean** |  | [optional] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**measurementUnit** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**phase** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**plannedBillingDate** | **Date** |  | [optional] 
**product** | [**ProjectFeeProductSubModel**](ProjectFeeProductSubModel.md) |  | [optional] 
**productType** | [**ProductType**](ProductType.md) |  | [optional] 
**project** | [**ProjectFeeProjectSubModel**](ProjectFeeProjectSubModel.md) |  | [optional] 
**quantity** | **Number** |  | [optional] 
**recurrenceRuleGuid** | **String** |  | [optional] 
**salesAccount** | [**ProjectSalesAccountSubModel**](ProjectSalesAccountSubModel.md) |  | [optional] 
**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**user** | [**UserSubModel**](UserSubModel.md) |  | [optional] 
**vatRate** | **Number** |  | [optional] 


