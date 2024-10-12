

# PhaseModelWithHierarchyInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**currencyCode** | [**CurrencyBaseModel**](CurrencyBaseModel.md) |  |  [optional] |
|**customer** | [**PhaseCustomerSubModel**](PhaseCustomerSubModel.md) |  |  [optional] |
|**deadline** | **LocalDate** |  |  [optional] |
|**defaultWorkType** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**hasChildren** | **Boolean** |  |  [optional] |
|**isCompleted** | **Boolean** |  |  [optional] |
|**isLocked** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**level** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**originalDeadline** | **LocalDate** |  |  [optional] |
|**originalStartDate** | **LocalDate** |  |  [optional] |
|**originalWorkHoursEstimate** | **Double** |  |  [optional] |
|**parentPhase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  [optional] |
|**phaseStatus** | [**PhaseStatusOutputModel**](PhaseStatusOutputModel.md) |  |  [optional] |
|**project** | [**PhaseProjectSubModel**](PhaseProjectSubModel.md) |  |  [optional] |
|**sortOrder** | **Integer** |  |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |
|**workHoursEstimate** | **Double** |  |  [optional] |



