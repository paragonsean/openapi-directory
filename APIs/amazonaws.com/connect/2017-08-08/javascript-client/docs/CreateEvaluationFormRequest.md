# AmazonConnectService.CreateEvaluationFormRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **String** | A title of the evaluation form. | 
**description** | **String** | The description of the evaluation form. | [optional] 
**items** | [**[EvaluationFormItem]**](EvaluationFormItem.md) | Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section. | 
**scoringStrategy** | [**CreateEvaluationFormRequestScoringStrategy**](CreateEvaluationFormRequestScoringStrategy.md) |  | [optional] 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. | [optional] 


