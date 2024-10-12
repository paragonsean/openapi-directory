# BatchService.OutputFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**OutputFileDestination**](OutputFileDestination.md) |  | 
**filePattern** | **String** | Both relative and absolute paths are supported. Relative paths are relative to the task working directory. For wildcards, use * to match any character and ** to match any directory. For example, **\\*.txt matches any file ending in .txt in the task working directory or any subdirectory. Note that \\ and / are treated interchangeably and mapped to the correct directory separator on the compute node operating system. | 
**uploadOptions** | [**OutputFileUploadOptions**](OutputFileUploadOptions.md) |  | 


