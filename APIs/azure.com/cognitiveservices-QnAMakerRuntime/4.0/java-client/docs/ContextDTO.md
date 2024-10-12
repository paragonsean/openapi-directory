

# ContextDTO

Context associated with Qna.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isContextOnly** | **Boolean** | To mark if a prompt is relevant only with a previous question or not. true - Do not include this QnA as search result for queries without context false - ignores context and includes this QnA in search result |  [optional] |
|**prompts** | [**List&lt;PromptDTO&gt;**](PromptDTO.md) | List of prompts associated with the answer. |  [optional] |



