

# ProjectRecurringFeeRuleOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costCenter** | [**ProjectCostCenterSubModel**](ProjectCostCenterSubModel.md) |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**ProjectFeeCustomerSubModel**](ProjectFeeCustomerSubModel.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**displayPeriodStartDate** | **LocalDate** |  |  [optional] |
|**frequency** | **Integer** |  |  [optional] |
|**generatedTimes** | **Integer** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**hasVolumePricing** | **Boolean** |  |  [optional] |
|**isActive** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**measurementUnit** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**phase** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**product** | [**ProjectFeeProductSubModel**](ProjectFeeProductSubModel.md) |  |  [optional] |
|**productType** | **ProductType** |  |  [optional] |
|**project** | [**ProjectFeeProjectSubModel**](ProjectFeeProjectSubModel.md) |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**recurrenceEndDate** | **LocalDate** |  |  [optional] |
|**recurrenceEndType** | **RecurrenceEndTypes** |  |  [optional] |
|**recurrenceStartDate** | **LocalDate** |  |  [optional] |
|**recurrenceTimes** | **Integer** |  |  [optional] |
|**recurringSalesAccount** | [**ProjectSalesAccountSubModel**](ProjectSalesAccountSubModel.md) |  |  [optional] |
|**salesAccount** | [**ProjectSalesAccountSubModel**](ProjectSalesAccountSubModel.md) |  |  [optional] |
|**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**user** | [**UserSubModel**](UserSubModel.md) |  |  [optional] |
|**vatRate** | **Double** |  |  [optional] |



