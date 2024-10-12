

# UpdateContextDTO

Update Body schema to represent context to be updated

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isContextOnly** | **Boolean** | To mark if a prompt is relevant only with a previous question or not. true - Do not include this QnA as search result for queries without context false - ignores context and includes this QnA in search result |  [optional] |
|**promptsToAdd** | [**List&lt;PromptDTO&gt;**](PromptDTO.md) | List of prompts to be added to the qna. |  [optional] |
|**promptsToDelete** | **List&lt;Integer&gt;** | List of prompts associated with qna to be deleted |  [optional] |



