# SnykApi.IgnoreRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disregardIfFixable** | **Boolean** | Only ignore the issue if no upgrade or patch is available. | 
**expires** | **String** | The timestamp that the issue will no longer be ignored. | [optional] 
**ignorePath** | **String** | The path to ignore (default is &#x60;*&#x60; which represents all paths). | [optional] 
**reason** | **String** | The reason that the issue was ignored. | [optional] 
**reasonType** | **String** | The classification of the ignore. | 



## Enum: ReasonTypeEnum


* `not-vulnerable` (value: `"not-vulnerable"`)

* `wont-fix` (value: `"wont-fix"`)

* `temporary-ignore` (value: `"temporary-ignore"`)




