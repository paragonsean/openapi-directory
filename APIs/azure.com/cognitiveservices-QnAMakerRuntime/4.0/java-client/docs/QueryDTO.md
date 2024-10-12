

# QueryDTO

POST body schema to query the knowledgebase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**QueryContextDTO**](QueryContextDTO.md) | Context object with previous QnA&#39;s information. |  [optional] |
|**isTest** | **Boolean** | Query against the test index. |  [optional] |
|**qnaId** | **String** | Exact qnaId to fetch from the knowledgebase, this field takes priority over question. |  [optional] |
|**question** | **String** | User question to query against the knowledge base. |  [optional] |
|**rankerType** | **String** | Optional field. Set to &#39;QuestionOnly&#39; for using a question only Ranker. |  [optional] |
|**scoreThreshold** | **BigDecimal** | Threshold for answers returned based on score. |  [optional] |
|**strictFilters** | [**List&lt;MetadataDTO&gt;**](MetadataDTO.md) | Find only answers that contain these metadata. |  [optional] |
|**top** | **Integer** | Max number of answers to be returned for the question. |  [optional] |
|**userId** | **String** | Unique identifier for the user. |  [optional] |



