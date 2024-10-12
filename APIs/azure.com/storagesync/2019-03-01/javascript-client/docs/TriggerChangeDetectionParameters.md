# MicrosoftStorageSync.TriggerChangeDetectionParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changeDetectionMode** | **String** | Change Detection Mode. Applies to a directory specified in directoryPath parameter. | [optional] 
**directoryPath** | **String** | Relative path to a directory Azure File share for which change detection is to be performed. | [optional] 
**paths** | **[String]** | Array of relative paths on the Azure File share to be included in the change detection. Can be files and directories. | [optional] 



## Enum: ChangeDetectionModeEnum


* `Default` (value: `"Default"`)

* `Recursive` (value: `"Recursive"`)




