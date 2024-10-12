# SeveraPublicRestApiDocumentation.PhaseInputModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** |  | [optional] 
**deadline** | **Date** |  | [optional] 
**defaultWorkType** | [**ModelWithName**](ModelWithName.md) |  | [optional] 
**isClosed** | **Boolean** |  | [optional] [default to false]
**isCompleted** | **Boolean** |  | [optional] [default to false]
**isLocked** | **Boolean** |  | [optional] [default to false]
**name** | **String** |  | 
**originalDeadline** | **Date** |  | [optional] 
**originalStartDate** | **Date** |  | [optional] 
**originalWorkHoursEstimate** | **Number** |  | [optional] 
**parentPhase** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | 
**phaseStatus** | [**PhaseStatusInputModel**](PhaseStatusInputModel.md) |  | [optional] 
**project** | [**ModelBaseWithRequiredGuid**](ModelBaseWithRequiredGuid.md) |  | [optional] 
**sortOrder** | **Number** |  | [optional] 
**startDate** | **Date** |  | [optional] 
**workHoursEstimate** | **Number** |  | [optional] 


