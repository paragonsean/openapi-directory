# MigrationCenterApi.FileValidationReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileErrors** | [**[ImportError]**](ImportError.md) | List of file level errors. | [optional] 
**fileName** | **String** | The name of the file. | [optional] 
**partialReport** | **Boolean** | Flag indicating that processing was aborted due to maximum number of errors. | [optional] 
**rowErrors** | [**[ImportRowError]**](ImportRowError.md) | Partial list of rows that encountered validation error. | [optional] 


