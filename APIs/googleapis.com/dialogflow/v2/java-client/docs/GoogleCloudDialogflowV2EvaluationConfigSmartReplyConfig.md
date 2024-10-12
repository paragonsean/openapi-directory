

# GoogleCloudDialogflowV2EvaluationConfigSmartReplyConfig

Smart reply specific configuration for evaluation job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowlistDocument** | **String** | The allowlist document resource name. Format: &#x60;projects//knowledgeBases//documents/&#x60;. Only used for smart reply model. |  [optional] |
|**maxResultCount** | **Integer** | Required. The model to be evaluated can return multiple results with confidence score on each query. These results will be sorted by the descending order of the scores and we only keep the first max_result_count results as the final results to evaluate. |  [optional] |



