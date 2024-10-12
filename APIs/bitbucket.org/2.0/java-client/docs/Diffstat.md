

# Diffstat

A diffstat object that includes a summary of changes made to a file between two commits.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**linesAdded** | **Integer** |  |  [optional] |
|**linesRemoved** | **Integer** |  |  [optional] |
|**_new** | **CommitFile** |  |  [optional] |
|**old** | **CommitFile** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**type** | **String** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ADDED | &quot;added&quot; |
| REMOVED | &quot;removed&quot; |
| MODIFIED | &quot;modified&quot; |
| RENAMED | &quot;renamed&quot; |



