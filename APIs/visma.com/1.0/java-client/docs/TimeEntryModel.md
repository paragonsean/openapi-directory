

# TimeEntryModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**endTime** | **OffsetDateTime** |  |  [optional] |
|**eventDate** | **LocalDate** |  |  |
|**guid** | **String** |  |  [optional] [readonly] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**phase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  |
|**project** | [**TimeEntryProject**](TimeEntryProject.md) |  |  [optional] |
|**quantity** | **Double** |  |  [optional] |
|**startTime** | **OffsetDateTime** |  |  [optional] |
|**timeEntryType** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  |
|**user** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  |



