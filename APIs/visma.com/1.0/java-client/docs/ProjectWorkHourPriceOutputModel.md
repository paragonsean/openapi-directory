

# ProjectWorkHourPriceOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**guid** | **String** |  |  [optional] [readonly] |
|**isAvailable** | **Boolean** |  |  [optional] |
|**isBillable** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**phase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  [optional] |
|**project** | [**ProjectSubModel**](ProjectSubModel.md) |  |  [optional] |
|**unitPrice** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**user** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**workType** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |



