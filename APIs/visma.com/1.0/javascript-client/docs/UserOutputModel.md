# SeveraPublicRestApiDocumentation.UserOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** |  | [optional] 
**bankAccountNumber** | **String** |  | [optional] 
**birthDate** | **Date** |  | [optional] 
**businessUnit** | [**BusinessUnitSubModel**](BusinessUnitSubModel.md) |  | [optional] 
**city** | **String** |  | [optional] 
**code** | **String** |  | [optional] 
**country** | [**UserCountrySubModel**](UserCountrySubModel.md) |  | [optional] 
**countryRegion** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**culture** | [**UserCultureSubModel**](UserCultureSubModel.md) |  | [optional] 
**defaultActivityType** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**email** | **String** |  | [optional] 
**firstName** | **String** |  | 
**guid** | **String** |  | [optional] [readonly] 
**isActive** | **Boolean** |  | [optional] [default to true]
**keywords** | [**[UserKeywordSubModel]**](UserKeywordSubModel.md) |  | [optional] 
**language** | [**UserLanguageSubModel**](UserLanguageSubModel.md) |  | [optional] 
**lastLogin** | **Date** |  | [optional] 
**lastName** | **String** |  | 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**notes** | **String** |  | [optional] 
**permissionProfile** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**phone** | **String** |  | [optional] 
**postalCode** | **String** |  | [optional] 
**salutation** | [**SalutationType**](SalutationType.md) |  | [optional] 
**satisfaction** | [**SatisfactionLevelType**](SatisfactionLevelType.md) |  | [optional] 
**socialSecurityNumber** | **String** |  | [optional] 
**superiorUser** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | [optional] 
**timezone** | [**TimezoneModel**](TimezoneModel.md) |  | [optional] 
**title** | **String** |  | [optional] 
**userType** | [**LicenseUserType**](LicenseUserType.md) |  | [optional] 
**workContract** | [**UserWorkContractSubModel**](UserWorkContractSubModel.md) |  | [optional] 
**workType** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | [optional] 


