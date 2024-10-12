# CloudAutoMlApi.ModelEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSpecId** | **String** | Output only. The ID of the annotation spec that the model evaluation applies to. The The ID is empty for the overall model evaluation. For Tables annotation specs in the dataset do not exist and this ID is always not set, but for CLASSIFICATION prediction_type-s the display_name field is used. | [optional] 
**classificationEvaluationMetrics** | [**ClassificationEvaluationMetrics**](ClassificationEvaluationMetrics.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp when this model evaluation was created. | [optional] 
**displayName** | **String** | Output only. The value of display_name at the moment when the model was trained. Because this field returns a value at model training time, for different models trained from the same dataset, the values may differ, since display names could had been changed between the two model&#39;s trainings. For Tables CLASSIFICATION prediction_type-s distinct values of the target column at the moment of the model evaluation are populated here. The display_name is empty for the overall model evaluation. | [optional] 
**evaluatedExampleCount** | **Number** | Output only. The number of examples used for model evaluation, i.e. for which ground truth from time of model creation is compared against the predicted annotations created by the model. For overall ModelEvaluation (i.e. with annotation_spec_id not set) this is the total number of all examples used for evaluation. Otherwise, this is the count of examples that according to the ground truth were annotated by the annotation_spec_id. | [optional] 
**imageObjectDetectionEvaluationMetrics** | [**ImageObjectDetectionEvaluationMetrics**](ImageObjectDetectionEvaluationMetrics.md) |  | [optional] 
**name** | **String** | Output only. Resource name of the model evaluation. Format: &#x60;projects/{project_id}/locations/{location_id}/models/{model_id}/modelEvaluations/{model_evaluation_id}&#x60; | [optional] 
**regressionEvaluationMetrics** | [**RegressionEvaluationMetrics**](RegressionEvaluationMetrics.md) |  | [optional] 
**textExtractionEvaluationMetrics** | [**TextExtractionEvaluationMetrics**](TextExtractionEvaluationMetrics.md) |  | [optional] 
**textSentimentEvaluationMetrics** | [**TextSentimentEvaluationMetrics**](TextSentimentEvaluationMetrics.md) |  | [optional] 
**translationEvaluationMetrics** | [**TranslationEvaluationMetrics**](TranslationEvaluationMetrics.md) |  | [optional] 
**videoObjectTrackingEvaluationMetrics** | [**VideoObjectTrackingEvaluationMetrics**](VideoObjectTrackingEvaluationMetrics.md) |  | [optional] 


