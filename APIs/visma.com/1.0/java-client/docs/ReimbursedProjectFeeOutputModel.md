

# ReimbursedProjectFeeOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**eventDate** | **LocalDate** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**invoiceGuid** | **String** |  |  [optional] |
|**invoiceQuantity** | **Double** |  |  [optional] |
|**invoiceRowDescription** | **String** |  |  [optional] |
|**invoiceRowGuid** | **String** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**measurementUnit** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**phase** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**product** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**productType** | **ProductType** |  |  [optional] |
|**project** | [**ReimbursedProjectFeeProjectSubModel**](ReimbursedProjectFeeProjectSubModel.md) |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**unitCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**user** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**vatRate** | **Double** |  |  [optional] |



