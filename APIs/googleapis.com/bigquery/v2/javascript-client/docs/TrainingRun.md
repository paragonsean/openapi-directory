# BigQueryApi.TrainingRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classLevelGlobalExplanations** | [**[GlobalExplanation]**](GlobalExplanation.md) | Output only. Global explanation contains the explanation of top features on the class level. Applies to classification models only. | [optional] [readonly] 
**dataSplitResult** | [**DataSplitResult**](DataSplitResult.md) |  | [optional] 
**evaluationMetrics** | [**EvaluationMetrics**](EvaluationMetrics.md) |  | [optional] 
**modelLevelGlobalExplanation** | [**GlobalExplanation**](GlobalExplanation.md) |  | [optional] 
**results** | [**[IterationResult]**](IterationResult.md) | Output only. Output of each iteration run, results.size() &lt;&#x3D; max_iterations. | [optional] [readonly] 
**startTime** | **String** | Output only. The start time of this training run. | [optional] [readonly] 
**trainingOptions** | [**TrainingOptions**](TrainingOptions.md) |  | [optional] 
**trainingStartTime** | **String** | Output only. The start time of this training run, in milliseconds since epoch. | [optional] [readonly] 
**vertexAiModelId** | **String** | The model id in the [Vertex AI Model Registry](https://cloud.google.com/vertex-ai/docs/model-registry/introduction) for this training run. | [optional] 
**vertexAiModelVersion** | **String** | Output only. The model version in the [Vertex AI Model Registry](https://cloud.google.com/vertex-ai/docs/model-registry/introduction) for this training run. | [optional] [readonly] 


