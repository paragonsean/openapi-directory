# SeveraPublicRestApiDocumentation.PhaseModelWithHierarchyInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** |  | [optional] 
**createdBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**createdDateTime** | **Date** |  | [optional] [readonly] 
**currencyCode** | [**CurrencyBaseModel**](CurrencyBaseModel.md) |  | [optional] 
**customer** | [**PhaseCustomerSubModel**](PhaseCustomerSubModel.md) |  | [optional] 
**deadline** | **Date** |  | [optional] 
**defaultWorkType** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**guid** | **String** |  | [optional] [readonly] 
**hasChildren** | **Boolean** |  | [optional] 
**isCompleted** | **Boolean** |  | [optional] [default to false]
**isLocked** | **Boolean** |  | [optional] [default to false]
**lastUpdatedBy** | [**UserWithFirstNameLastNameAndPhotoFileModel**](UserWithFirstNameLastNameAndPhotoFileModel.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** |  | [optional] [readonly] 
**level** | **Number** |  | [optional] 
**name** | **String** |  | 
**originalDeadline** | **Date** |  | [optional] 
**originalStartDate** | **Date** |  | [optional] 
**originalWorkHoursEstimate** | **Number** |  | [optional] 
**parentPhase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | [optional] 
**phaseStatus** | [**PhaseStatusOutputModel**](PhaseStatusOutputModel.md) |  | [optional] 
**project** | [**PhaseProjectSubModel**](PhaseProjectSubModel.md) |  | [optional] 
**sortOrder** | **Number** |  | [optional] 
**startDate** | **Date** |  | [optional] 
**workHoursEstimate** | **Number** |  | [optional] 


