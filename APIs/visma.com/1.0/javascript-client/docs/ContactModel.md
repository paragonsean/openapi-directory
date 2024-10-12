# SeveraPublicRestApiDocumentation.ContactModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressGuid** | **String** |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**customer** | [**ContactCustomer**](ContactCustomer.md) |  | 
**dateOfBirth** | **Date** |  | [optional] 
**description** | **String** |  | [optional] 
**emails** | **[String]** |  | [optional] [readonly] 
**firstName** | **String** |  | 
**guid** | **String** |  | [optional] [readonly] 
**isActive** | **Boolean** |  | [optional] [default to true]
**isDeleted** | **Boolean** |  | [optional] [readonly] 
**isEmailAllowed** | **Boolean** |  | [optional] [default to false]
**jobTitle** | **String** |  | [optional] 
**language** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**lastName** | **String** |  | 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**name** | **String** |  | [optional] [readonly] 
**phoneNumbers** | **[String]** |  | [optional] [readonly] 
**role** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**salutation** | [**SalutationType**](SalutationType.md) |  | [optional] 
**satisfactionLevel** | [**SatisfactionLevelType**](SatisfactionLevelType.md) |  | [optional] 
**timeZone** | [**ModelWithName**](ModelWithName.md) |  | [optional] 


