# SeveraPublicRestApiDocumentation.ProjectTravelExpenseOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachmentCount** | **Number** |  | [optional] 
**billingDependencyPhase** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**billingSchedule** | [**ProjectTravelExpenseBillingScheduleType**](ProjectTravelExpenseBillingScheduleType.md) |  | [optional] 
**costAccount** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**costCenter** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**customer** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**description** | **String** |  | [optional] 
**eventDate** | **Date** |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**invoice** | [**InvoiceSubModel**](InvoiceSubModel.md) |  | [optional] 
**invoiceQuantity** | **Number** |  | [optional] 
**invoiceRowComment** | **String** |  | [optional] 
**invoiceRowDescription** | **String** |  | [optional] 
**invoiceRowGuid** | **String** |  | [optional] 
**isBillable** | **Boolean** |  | [optional] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**measurementUnit** | **String** |  | [optional] 
**phase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | [optional] 
**plannedBillingDate** | **Date** |  | [optional] 
**project** | [**ProjectTravelExpenseProjectSubModel**](ProjectTravelExpenseProjectSubModel.md) |  | [optional] 
**purchaseVatRate** | **Number** |  | [optional] 
**quantity** | **Number** |  | [optional] 
**salesAccount** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**travelEndTime** | **Date** |  | [optional] 
**travelExpense** | [**TravelExpenseSubModel**](TravelExpenseSubModel.md) |  | [optional] 
**travelReimbursement** | [**TravelReimbursementSubModel**](TravelReimbursementSubModel.md) |  | [optional] 
**travelReimbursementRequired** | **Boolean** |  | [optional] [default to true]
**travelStartTime** | **Date** |  | [optional] 
**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**unitCostExcludingPurchaseVat** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**user** | [**UserRequiredSubModel**](UserRequiredSubModel.md) |  | [optional] 
**vatRate** | **Number** |  | [optional] 


