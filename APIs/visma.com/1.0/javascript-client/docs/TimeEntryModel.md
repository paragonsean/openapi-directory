# SeveraPublicRestApiDocumentation.TimeEntryModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**customer** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**description** | **String** |  | [optional] 
**endTime** | **Date** |  | [optional] 
**eventDate** | **Date** |  | 
**guid** | **String** |  | [optional] [readonly] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**phase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | 
**project** | [**TimeEntryProject**](TimeEntryProject.md) |  | [optional] 
**quantity** | **Number** |  | [optional] 
**startTime** | **Date** |  | [optional] 
**timeEntryType** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | 
**user** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | 


