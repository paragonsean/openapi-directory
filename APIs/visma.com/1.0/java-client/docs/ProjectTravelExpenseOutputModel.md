

# ProjectTravelExpenseOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachmentCount** | **Integer** |  |  [optional] |
|**billingDependencyPhase** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**billingSchedule** | **ProjectTravelExpenseBillingScheduleType** |  |  [optional] |
|**costAccount** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**costCenter** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**eventDate** | **LocalDate** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**invoice** | [**InvoiceSubModel**](InvoiceSubModel.md) |  |  [optional] |
|**invoiceQuantity** | **Double** |  |  [optional] |
|**invoiceRowComment** | **String** |  |  [optional] |
|**invoiceRowDescription** | **String** |  |  [optional] |
|**invoiceRowGuid** | **String** |  |  [optional] |
|**isBillable** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**measurementUnit** | **String** |  |  [optional] |
|**phase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  [optional] |
|**plannedBillingDate** | **LocalDate** |  |  [optional] |
|**project** | [**ProjectTravelExpenseProjectSubModel**](ProjectTravelExpenseProjectSubModel.md) |  |  [optional] |
|**purchaseVatRate** | **Double** |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**salesAccount** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**travelEndTime** | **OffsetDateTime** |  |  [optional] |
|**travelExpense** | [**TravelExpenseSubModel**](TravelExpenseSubModel.md) |  |  [optional] |
|**travelReimbursement** | [**TravelReimbursementSubModel**](TravelReimbursementSubModel.md) |  |  [optional] |
|**travelReimbursementRequired** | **Boolean** |  |  [optional] |
|**travelStartTime** | **OffsetDateTime** |  |  [optional] |
|**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**unitCostExcludingPurchaseVat** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**user** | [**UserRequiredSubModel**](UserRequiredSubModel.md) |  |  [optional] |
|**vatRate** | **Double** |  |  [optional] |



