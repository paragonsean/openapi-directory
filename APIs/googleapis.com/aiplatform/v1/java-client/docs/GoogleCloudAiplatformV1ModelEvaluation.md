

# GoogleCloudAiplatformV1ModelEvaluation

A collection of metrics calculated by comparing Model's predictions on all of the test data against annotations from the test data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSchemaUri** | **String** | Points to a YAML file stored on Google Cloud Storage describing EvaluatedDataItemView.predictions, EvaluatedDataItemView.ground_truths, EvaluatedAnnotation.predictions, and EvaluatedAnnotation.ground_truths. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). This field is not populated if there are neither EvaluatedDataItemViews nor EvaluatedAnnotations under this ModelEvaluation. |  [optional] |
|**createTime** | **String** | Output only. Timestamp when this ModelEvaluation was created. |  [optional] [readonly] |
|**dataItemSchemaUri** | **String** | Points to a YAML file stored on Google Cloud Storage describing EvaluatedDataItemView.data_item_payload and EvaluatedAnnotation.data_item_payload. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). This field is not populated if there are neither EvaluatedDataItemViews nor EvaluatedAnnotations under this ModelEvaluation. |  [optional] |
|**displayName** | **String** | The display name of the ModelEvaluation. |  [optional] |
|**explanationSpecs** | [**List&lt;GoogleCloudAiplatformV1ModelEvaluationModelEvaluationExplanationSpec&gt;**](GoogleCloudAiplatformV1ModelEvaluationModelEvaluationExplanationSpec.md) | Describes the values of ExplanationSpec that are used for explaining the predicted values on the evaluated data. |  [optional] |
|**metadata** | **Object** | The metadata of the ModelEvaluation. For the ModelEvaluation uploaded from Managed Pipeline, metadata contains a structured value with keys of \&quot;pipeline_job_id\&quot;, \&quot;evaluation_dataset_type\&quot;, \&quot;evaluation_dataset_path\&quot;, \&quot;row_based_metrics_path\&quot;. |  [optional] |
|**metrics** | **Object** | Evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri |  [optional] |
|**metricsSchemaUri** | **String** | Points to a YAML file stored on Google Cloud Storage describing the metrics of this ModelEvaluation. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). |  [optional] |
|**modelExplanation** | [**GoogleCloudAiplatformV1ModelExplanation**](GoogleCloudAiplatformV1ModelExplanation.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the ModelEvaluation. |  [optional] [readonly] |
|**sliceDimensions** | **List&lt;String&gt;** | All possible dimensions of ModelEvaluationSlices. The dimensions can be used as the filter of the ModelService.ListModelEvaluationSlices request, in the form of &#x60;slice.dimension &#x3D; &#x60;. |  [optional] |



