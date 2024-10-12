

# ItemStatus

This contains item's status and any errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Status code. |  [optional] |
|**processingErrors** | [**List&lt;ProcessingError&gt;**](ProcessingError.md) | Error details in case the item is in ERROR state. |  [optional] |
|**repositoryErrors** | [**List&lt;RepositoryError&gt;**](RepositoryError.md) | Repository error reported by connector. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| ERROR | &quot;ERROR&quot; |
| MODIFIED | &quot;MODIFIED&quot; |
| NEW_ITEM | &quot;NEW_ITEM&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |



