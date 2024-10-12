

# UncommittedFileChange

Represents the Git state of a file with uncommitted changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** | The file&#39;s full path including filename, relative to the workspace root. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Indicates the status of the file. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ADDED | &quot;ADDED&quot; |
| DELETED | &quot;DELETED&quot; |
| MODIFIED | &quot;MODIFIED&quot; |
| HAS_CONFLICTS | &quot;HAS_CONFLICTS&quot; |



