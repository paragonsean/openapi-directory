

# ReimbursedWorkHourOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**endTime** | **OffsetDateTime** |  |  [optional] |
|**eventDate** | **LocalDate** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**invoiceGuid** | **String** |  |  [optional] |
|**invoiceQuantity** | **Double** |  |  [optional] |
|**invoiceRowComment** | **String** |  |  [optional] |
|**invoiceRowDescription** | **String** |  |  [optional] |
|**invoiceRowGuid** | **String** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**overtime** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**phase** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**plannedInvoiceQuantity** | **Double** |  |  [optional] |
|**project** | [**ReimbursedWorkHourProjectSubModel**](ReimbursedWorkHourProjectSubModel.md) |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**startTime** | **OffsetDateTime** |  |  [optional] |
|**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**user** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**workType** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |



