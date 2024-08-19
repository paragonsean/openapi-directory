

# WorkHourOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billableStatus** | **BillableStatusType** |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**WorkHourCustomerSubModel**](WorkHourCustomerSubModel.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**endTime** | **OffsetDateTime** |  |  [optional] |
|**eventDate** | **LocalDate** |  |  |
|**guid** | **String** |  |  [optional] [readonly] |
|**invoice** | [**WorkHourInvoiceSubModel**](WorkHourInvoiceSubModel.md) |  |  [optional] |
|**invoiceQuantity** | **Double** |  |  [optional] |
|**invoiceRowComment** | **String** |  |  [optional] |
|**invoiceRowDescription** | **String** |  |  [optional] |
|**invoiceRowGuid** | **String** |  |  [optional] |
|**isApproved** | **Boolean** |  |  [optional] |
|**isBillable** | **Boolean** |  |  [optional] |
|**isModifiable** | **Boolean** |  |  [optional] |
|**isProductive** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**overtime** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**phase** | [**WorkHourPhaseSubModel**](WorkHourPhaseSubModel.md) |  |  [optional] |
|**plannedInvoiceQuantity** | **Double** |  |  [optional] |
|**project** | [**WorkHourProjectSubModel**](WorkHourProjectSubModel.md) |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**startTime** | **OffsetDateTime** |  |  [optional] |
|**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**user** | [**UserWithFirstNameLastNamePhotoFileModelAndRequiredGuid**](UserWithFirstNameLastNamePhotoFileModelAndRequiredGuid.md) |  |  [optional] |
|**workType** | [**WorkHourWorkTypeSubModel**](WorkHourWorkTypeSubModel.md) |  |  [optional] |



