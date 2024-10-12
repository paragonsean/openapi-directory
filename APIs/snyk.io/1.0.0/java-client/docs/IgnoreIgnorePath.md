

# IgnoreIgnorePath

The path that should be ignored. Wildcards can be specified with a `*`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** | The timestamp that the issue was ignored. |  [optional] |
|**disregardIfFixable** | **Boolean** | Only ignore the issue if no upgrade or patch is available. |  [optional] |
|**expires** | **String** | The timestamp that the issue will no longer be ignored. |  [optional] |
|**ignoredBy** | [**IgnoreIgnorePathIgnoredBy**](IgnoreIgnorePathIgnoredBy.md) |  |  [optional] |
|**reason** | **String** | The reason that the issue was ignored. |  [optional] |
|**reasonType** | [**ReasonTypeEnum**](#ReasonTypeEnum) | The classification of the ignore. |  [optional] |



## Enum: ReasonTypeEnum

| Name | Value |
|---- | -----|
| NOT_VULNERABLE | &quot;not-vulnerable&quot; |
| WONT_FIX | &quot;wont-fix&quot; |
| TEMPORARY_IGNORE | &quot;temporary-ignore&quot; |



