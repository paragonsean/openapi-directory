

# ActivityModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityType** | [**ActivityActivityType**](ActivityActivityType.md) |  |  |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**ActivityCustomer**](ActivityCustomer.md) |  |  [optional] |
|**endDateTime** | **OffsetDateTime** |  |  [optional] |
|**guid** | **String** |  |  [optional] [readonly] |
|**hasDuration** | **Boolean** |  |  [optional] |
|**hasHours** | **Boolean** |  |  [optional] [readonly] |
|**isAllDay** | **Boolean** |  |  [optional] |
|**isClosed** | **Boolean** |  |  [optional] |
|**isUnassigned** | **Boolean** |  |  [optional] |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**location** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**notes** | **String** |  |  [optional] |
|**ownerUser** | [**ActivityOwnerModel**](ActivityOwnerModel.md) |  |  |
|**phase** | [**ActivityPhase**](ActivityPhase.md) |  |  [optional] |
|**projectTaskStatus** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**recurrence** | [**ActivityRecurrenceModel**](ActivityRecurrenceModel.md) |  |  [optional] |
|**recurrenceParentActivityGuid** | **String** |  |  [optional] |
|**recurrenceRule** | **String** |  |  [optional] [readonly] |
|**recurrenceType** | **RecurrenceType** |  |  [optional] |
|**startDateTime** | **OffsetDateTime** |  |  |



