

# ContactModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressGuid** | **String** |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customer** | [**ContactCustomer**](ContactCustomer.md) |  |  |
|**dateOfBirth** | **LocalDate** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**emails** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**firstName** | **String** |  |  |
|**guid** | **String** |  |  [optional] [readonly] |
|**isActive** | **Boolean** |  |  [optional] |
|**isDeleted** | **Boolean** |  |  [optional] [readonly] |
|**isEmailAllowed** | **Boolean** |  |  [optional] |
|**jobTitle** | **String** |  |  [optional] |
|**language** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**lastName** | **String** |  |  |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] [readonly] |
|**phoneNumbers** | **List&lt;String&gt;** |  |  [optional] [readonly] |
|**role** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**salutation** | **SalutationType** |  |  [optional] |
|**satisfactionLevel** | **SatisfactionLevelType** |  |  [optional] |
|**timeZone** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |



