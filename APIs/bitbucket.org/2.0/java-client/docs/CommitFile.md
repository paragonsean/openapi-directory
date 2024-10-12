

# CommitFile

A file object, representing a file at a commit in a repository

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**AttributesEnum**](#AttributesEnum) |  |  [optional] |
|**commit** | [**Commit**](Commit.md) |  |  [optional] |
|**escapedPath** | **String** | The escaped version of the path as it appears in a diff. If the path does not require escaping this will be the same as path. |  [optional] |
|**path** | **String** | The path in the repository |  [optional] |
|**type** | **String** |  |  |



## Enum: AttributesEnum

| Name | Value |
|---- | -----|
| LINK | &quot;link&quot; |
| EXECUTABLE | &quot;executable&quot; |
| SUBREPOSITORY | &quot;subrepository&quot; |
| BINARY | &quot;binary&quot; |
| LFS | &quot;lfs&quot; |



