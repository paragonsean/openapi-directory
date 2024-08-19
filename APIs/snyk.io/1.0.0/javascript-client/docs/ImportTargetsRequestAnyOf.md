# SnykApi.ImportTargetsRequestAnyOf

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusionGlobs** | **String** | a comma-separated list of up to 10 folder names to exclude from scanning (each folder name must not exceed 100 characters). If not specified, it will default to \&quot;fixtures, tests, \\_\\_tests\\_\\_, node_modules\&quot;. If an empty string is provided - no folders will be excluded. This attribute is only respected with Open Source and Container scan targets. | [optional] 
**files** | **[Object]** | an array of file objects | [optional] 
**target** | [**ImportTargetsRequestAnyOfTarget**](ImportTargetsRequestAnyOfTarget.md) |  | [optional] 


