

# UpdateQnaDTO

PATCH Body schema for Update Qna List

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answer** | **String** | Answer text |  [optional] |
|**context** | [**UpdateContextDTO**](UpdateContextDTO.md) | Context associated with Qna to be updated. |  [optional] |
|**id** | **Integer** | Unique id for the Q-A |  [optional] |
|**metadata** | [**UpdateMetadataDTO**](UpdateMetadataDTO.md) | List of metadata associated with the answer to be updated |  [optional] |
|**questions** | [**UpdateQuestionsDTO**](UpdateQuestionsDTO.md) | List of questions associated with the answer. |  [optional] |
|**source** | **String** | Source from which Q-A was indexed. eg. https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/FAQs |  [optional] |



