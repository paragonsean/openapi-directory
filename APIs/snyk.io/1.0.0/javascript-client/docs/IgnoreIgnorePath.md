# SnykApi.IgnoreIgnorePath

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **String** | The timestamp that the issue was ignored. | [optional] 
**disregardIfFixable** | **Boolean** | Only ignore the issue if no upgrade or patch is available. | [optional] 
**expires** | **String** | The timestamp that the issue will no longer be ignored. | [optional] 
**ignoredBy** | [**IgnoreIgnorePathIgnoredBy**](IgnoreIgnorePathIgnoredBy.md) |  | [optional] 
**reason** | **String** | The reason that the issue was ignored. | [optional] 
**reasonType** | **String** | The classification of the ignore. | [optional] 



## Enum: ReasonTypeEnum


* `not-vulnerable` (value: `"not-vulnerable"`)

* `wont-fix` (value: `"wont-fix"`)

* `temporary-ignore` (value: `"temporary-ignore"`)




