

# FileValidationReport

A resource that aggregates the validation errors found in an import job file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileErrors** | [**List&lt;ImportError&gt;**](ImportError.md) | List of file level errors. |  [optional] |
|**fileName** | **String** | The name of the file. |  [optional] |
|**partialReport** | **Boolean** | Flag indicating that processing was aborted due to maximum number of errors. |  [optional] |
|**rowErrors** | [**List&lt;ImportRowError&gt;**](ImportRowError.md) | Partial list of rows that encountered validation error. |  [optional] |



