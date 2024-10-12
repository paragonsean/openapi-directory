

# GoogleCloudAiplatformV1beta1ModelEvaluationSlice

A collection of metrics calculated by comparing Model's predictions on a slice of the test data against ground truth annotations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when this ModelEvaluationSlice was created. |  [optional] [readonly] |
|**metrics** | **Object** | Output only. Sliced evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri |  [optional] [readonly] |
|**metricsSchemaUri** | **String** | Output only. Points to a YAML file stored on Google Cloud Storage describing the metrics of this ModelEvaluationSlice. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). |  [optional] [readonly] |
|**modelExplanation** | [**GoogleCloudAiplatformV1beta1ModelExplanation**](GoogleCloudAiplatformV1beta1ModelExplanation.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the ModelEvaluationSlice. |  [optional] [readonly] |
|**slice** | [**GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice**](GoogleCloudAiplatformV1beta1ModelEvaluationSliceSlice.md) |  |  [optional] |



