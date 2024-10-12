# SeveraPublicRestApiDocumentation.WorkContractOutputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**dailyHours** | **Number** |  | [optional] 
**endDate** | **Date** |  | [optional] 
**flextimeLimitPerDay** | **Number** |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**hourCost** | [**MoneyOutputModel**](MoneyOutputModel.md) |  | [optional] 
**isFlextimeActive** | **Boolean** |  | [optional] [default to true]
**isOvertimeAllowed** | **Boolean** |  | [optional] 
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**role** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**startDate** | **Date** |  | 
**title** | **String** |  | 
**user** | [**UserWithPhotoFileModelAndRequiredGuid**](UserWithPhotoFileModelAndRequiredGuid.md) |  | [optional] 
**workWeek** | [**[Workweek]**](Workweek.md) |  | [optional] 


