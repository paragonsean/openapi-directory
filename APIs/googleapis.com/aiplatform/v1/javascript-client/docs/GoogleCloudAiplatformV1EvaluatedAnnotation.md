# VertexAiApi.GoogleCloudAiplatformV1EvaluatedAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataItemPayload** | **Object** | Output only. The data item payload that the Model predicted this EvaluatedAnnotation on. | [optional] [readonly] 
**errorAnalysisAnnotations** | [**[GoogleCloudAiplatformV1ErrorAnalysisAnnotation]**](GoogleCloudAiplatformV1ErrorAnalysisAnnotation.md) | Annotations of model error analysis results. | [optional] 
**evaluatedDataItemViewId** | **String** | Output only. ID of the EvaluatedDataItemView under the same ancestor ModelEvaluation. The EvaluatedDataItemView consists of all ground truths and predictions on data_item_payload. | [optional] [readonly] 
**explanations** | [**[GoogleCloudAiplatformV1EvaluatedAnnotationExplanation]**](GoogleCloudAiplatformV1EvaluatedAnnotationExplanation.md) | Explanations of predictions. Each element of the explanations indicates the explanation for one explanation Method. The attributions list in the EvaluatedAnnotationExplanation.explanation object corresponds to the predictions list. For example, the second element in the attributions list explains the second element in the predictions list. | [optional] 
**groundTruths** | **[Object]** | Output only. The ground truth Annotations, i.e. the Annotations that exist in the test data the Model is evaluated on. For true positive, there is one and only one ground truth annotation, which matches the only prediction in predictions. For false positive, there are zero or more ground truth annotations that are similar to the only prediction in predictions, but not enough for a match. For false negative, there is one and only one ground truth annotation, which doesn&#39;t match any predictions created by the model. The schema of the ground truth is stored in ModelEvaluation.annotation_schema_uri | [optional] [readonly] 
**predictions** | **[Object]** | Output only. The model predicted annotations. For true positive, there is one and only one prediction, which matches the only one ground truth annotation in ground_truths. For false positive, there is one and only one prediction, which doesn&#39;t match any ground truth annotation of the corresponding data_item_view_id. For false negative, there are zero or more predictions which are similar to the only ground truth annotation in ground_truths but not enough for a match. The schema of the prediction is stored in ModelEvaluation.annotation_schema_uri | [optional] [readonly] 
**type** | **String** | Output only. Type of the EvaluatedAnnotation. | [optional] [readonly] 



## Enum: TypeEnum


* `EVALUATED_ANNOTATION_TYPE_UNSPECIFIED` (value: `"EVALUATED_ANNOTATION_TYPE_UNSPECIFIED"`)

* `TRUE_POSITIVE` (value: `"TRUE_POSITIVE"`)

* `FALSE_POSITIVE` (value: `"FALSE_POSITIVE"`)

* `FALSE_NEGATIVE` (value: `"FALSE_NEGATIVE"`)




