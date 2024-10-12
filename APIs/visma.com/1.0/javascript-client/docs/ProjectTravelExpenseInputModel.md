# SeveraPublicRestApiDocumentation.ProjectTravelExpenseInputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingDependencyPhase** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**billingSchedule** | [**ProjectTravelExpenseBillingScheduleType**](ProjectTravelExpenseBillingScheduleType.md) |  | [optional] 
**costAccount** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**costCenter** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**description** | **String** |  | [optional] 
**eventDate** | **Date** |  | [optional] 
**invoice** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**invoiceQuantity** | **Number** |  | [optional] 
**invoiceRowComment** | **String** |  | [optional] 
**invoiceRowDescription** | **String** |  | [optional] 
**isBillable** | **Boolean** |  | [optional] 
**measurementUnit** | **String** |  | [optional] 
**phase** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  | 
**plannedBillingDate** | **Date** |  | [optional] 
**project** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  | 
**purchaseVatRate** | **Number** |  | [optional] 
**quantity** | **Number** |  | 
**salesAccount** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**travelEndTime** | **Date** |  | [optional] 
**travelExpense** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  | 
**travelReimbursement** | [**SimpleInputModel**](SimpleInputModel.md) |  | [optional] 
**travelReimbursementRequired** | **Boolean** |  | [optional] [default to true]
**travelStartTime** | **Date** |  | [optional] 
**unitCost** | [**MoneyInputModel**](MoneyInputModel.md) |  | [optional] 
**unitPrice** | [**MoneyInputModel**](MoneyInputModel.md) |  | [optional] 
**user** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  | 
**vatRate** | **Number** |  | [optional] 


