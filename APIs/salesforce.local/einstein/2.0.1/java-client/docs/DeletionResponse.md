

# DeletionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedObjectId** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**_object** | **String** |  |  [optional] |
|**organizationId** | **String** |  |  [optional] |
|**progress** | **Double** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;QUEUED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED_WAITING_FOR_CACHE_REMOVAL | &quot;SUCCEEDED_WAITING_FOR_CACHE_REMOVAL&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| KILLED | &quot;KILLED&quot; |
| FAILED | &quot;FAILED&quot; |
| RETRY | &quot;RETRY&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATASET | &quot;DATASET&quot; |
| MODEL | &quot;MODEL&quot; |



