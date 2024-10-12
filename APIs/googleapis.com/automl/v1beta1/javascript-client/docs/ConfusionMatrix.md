# CloudAutoMlApi.ConfusionMatrix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotationSpecId** | **[String]** | Output only. IDs of the annotation specs used in the confusion matrix. For Tables CLASSIFICATION prediction_type only list of annotation_spec_display_name-s is populated. | [optional] 
**displayName** | **[String]** | Output only. Display name of the annotation specs used in the confusion matrix, as they were at the moment of the evaluation. For Tables CLASSIFICATION prediction_type-s, distinct values of the target column at the moment of the model evaluation are populated here. | [optional] 
**row** | [**[ClassificationEvaluationMetricsConfusionMatrixRow]**](ClassificationEvaluationMetricsConfusionMatrixRow.md) | Output only. Rows in the confusion matrix. The number of rows is equal to the size of &#x60;annotation_spec_id&#x60;. &#x60;row[i].example_count[j]&#x60; is the number of examples that have ground truth of the &#x60;annotation_spec_id[i]&#x60; and are predicted as &#x60;annotation_spec_id[j]&#x60; by the model being evaluated. | [optional] 


