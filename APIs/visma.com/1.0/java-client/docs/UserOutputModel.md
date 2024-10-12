

# UserOutputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** |  |  [optional] |
|**bankAccountNumber** | **String** |  |  [optional] |
|**birthDate** | **OffsetDateTime** |  |  [optional] |
|**businessUnit** | [**BusinessUnitSubModel**](BusinessUnitSubModel.md) |  |  [optional] |
|**city** | **String** |  |  [optional] |
|**code** | **String** |  |  [optional] |
|**country** | [**UserCountrySubModel**](UserCountrySubModel.md) |  |  [optional] |
|**countryRegion** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**culture** | [**UserCultureSubModel**](UserCultureSubModel.md) |  |  [optional] |
|**defaultActivityType** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**firstName** | **String** |  |  |
|**guid** | **String** |  |  [optional] [readonly] |
|**isActive** | **Boolean** |  |  [optional] |
|**keywords** | [**List&lt;UserKeywordSubModel&gt;**](UserKeywordSubModel.md) |  |  [optional] |
|**language** | [**UserLanguageSubModel**](UserLanguageSubModel.md) |  |  [optional] |
|**lastLogin** | **OffsetDateTime** |  |  [optional] |
|**lastName** | **String** |  |  |
|**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**notes** | **String** |  |  [optional] |
|**permissionProfile** | [**ModelWithName**](ModelWithName.md) |  |  [optional] |
|**phone** | **String** |  |  [optional] |
|**postalCode** | **String** |  |  [optional] |
|**salutation** | **SalutationType** |  |  [optional] |
|**satisfaction** | **SatisfactionLevelType** |  |  [optional] |
|**socialSecurityNumber** | **String** |  |  [optional] |
|**superiorUser** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  [optional] |
|**timezone** | [**TimezoneModel**](TimezoneModel.md) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**userType** | **LicenseUserType** |  |  [optional] |
|**workContract** | [**UserWorkContractSubModel**](UserWorkContractSubModel.md) |  |  [optional] |
|**workType** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  |  [optional] |



