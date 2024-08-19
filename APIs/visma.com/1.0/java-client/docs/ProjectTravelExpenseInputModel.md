

# ProjectTravelExpenseInputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingDependencyPhase** | [**SimpleInputModel**](SimpleInputModel.md) |  |  [optional] |
|**billingSchedule** | **ProjectTravelExpenseBillingScheduleType** |  |  [optional] |
|**costAccount** | [**SimpleInputModel**](SimpleInputModel.md) |  |  [optional] |
|**costCenter** | [**SimpleInputModel**](SimpleInputModel.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**eventDate** | **LocalDate** |  |  [optional] |
|**invoice** | [**SimpleInputModel**](SimpleInputModel.md) |  |  [optional] |
|**invoiceQuantity** | **Double** |  |  [optional] |
|**invoiceRowComment** | **String** |  |  [optional] |
|**invoiceRowDescription** | **String** |  |  [optional] |
|**isBillable** | **Boolean** |  |  [optional] |
|**measurementUnit** | **String** |  |  [optional] |
|**phase** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  |  |
|**plannedBillingDate** | **LocalDate** |  |  [optional] |
|**project** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  |  |
|**purchaseVatRate** | **Double** |  |  [optional] |
|**quantity** | **Double** |  |  |
|**salesAccount** | [**SimpleInputModel**](SimpleInputModel.md) |  |  [optional] |
|**travelEndTime** | **OffsetDateTime** |  |  [optional] |
|**travelExpense** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  |  |
|**travelReimbursement** | [**SimpleInputModel**](SimpleInputModel.md) |  |  [optional] |
|**travelReimbursementRequired** | **Boolean** |  |  [optional] |
|**travelStartTime** | **OffsetDateTime** |  |  [optional] |
|**unitCost** | [**MoneyInputModel**](MoneyInputModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyInputModel**](MoneyInputModel.md) |  |  [optional] |
|**user** | [**SimpleInputRequiredModel**](SimpleInputRequiredModel.md) |  |  |
|**vatRate** | **Double** |  |  [optional] |



