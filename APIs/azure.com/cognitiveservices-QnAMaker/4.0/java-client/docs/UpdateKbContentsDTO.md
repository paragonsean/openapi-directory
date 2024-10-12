

# UpdateKbContentsDTO

PATCH body schema for Update operation in Update Kb

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Friendly name for the knowledgebase. |  [optional] |
|**qnaList** | [**List&lt;UpdateQnaDTO&gt;**](UpdateQnaDTO.md) | List of Q-A (UpdateQnaDTO) to be added to the knowledgebase. |  [optional] |
|**urls** | **List&lt;String&gt;** | List of existing URLs to be refreshed. The content will be extracted again and re-indexed. |  [optional] |



