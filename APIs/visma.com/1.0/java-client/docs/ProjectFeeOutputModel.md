

# ProjectFeeOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingDependencyPhase** | [**ProjectFeePhaseSubModel**](ProjectFeePhaseSubModel.md) |  |  [optional] |
|**billingSchedule** | **ProjectFeeBillingScheduleType** |  |  [optional] |
|**costCenter** | [**ProjectCostCenterSubModel**](ProjectCostCenterSubModel.md) |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**ProjectFeeCustomerSubModel**](ProjectFeeCustomerSubModel.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**displayPeriodStartDate** | **LocalDate** |  |  [optional] |
|**eventDate** | **LocalDate** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**hasVolumePricing** | **Boolean** |  |  [optional] |
|**invoice** | [**ProjectFeeInvoiceSubModel**](ProjectFeeInvoiceSubModel.md) |  |  [optional] |
|**invoiceQuantity** | **Double** |  |  [optional] |
|**invoiceRowComment** | **String** |  |  [optional] |
|**invoiceRowDescription** | **String** |  |  [optional] |
|**invoiceRowGuid** | **String** |  |  [optional] |
|**isBillable** | **Boolean** |  |  [optional] |
|**isRecurrenceRule** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**measurementUnit** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**phase** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**plannedBillingDate** | **LocalDate** |  |  [optional] |
|**product** | [**ProjectFeeProductSubModel**](ProjectFeeProductSubModel.md) |  |  [optional] |
|**productType** | **ProductType** |  |  [optional] |
|**project** | [**ProjectFeeProjectSubModel**](ProjectFeeProjectSubModel.md) |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**recurrenceRuleGuid** | **String** |  |  [optional] |
|**salesAccount** | [**ProjectSalesAccountSubModel**](ProjectSalesAccountSubModel.md) |  |  [optional] |
|**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**user** | [**UserSubModel**](UserSubModel.md) |  |  [optional] |
|**vatRate** | **Double** |  |  [optional] |



