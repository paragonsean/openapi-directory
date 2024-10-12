

# WorkContractOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**dailyHours** | **Double** |  |  [optional] |
|**endDate** | **LocalDate** |  |  [optional] |
|**flextimeLimitPerDay** | **Double** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**hourCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  |  [optional] |
|**isFlextimeActive** | **Boolean** |  |  [optional] |
|**isOvertimeAllowed** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**role** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**startDate** | **LocalDate** |  |  |
|**title** | **String** |  |  |
|**user** | [**UserWithPhotoFileModelAndRequiredGuid**](UserWithPhotoFileModelAndRequiredGuid.md) |  |  [optional] |
|**workWeek** | **List&lt;Workweek&gt;** |  |  [optional] |



