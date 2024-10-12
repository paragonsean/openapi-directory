

# GoogleCloudDatalabelingV1beta1EvaluationJobConfig

Configures specific details of how a continuous evaluation job works. Provide this configuration when you create an EvaluationJob.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryImportKeys** | **Map&lt;String, String&gt;** | Required. Prediction keys that tell Data Labeling Service where to find the data for evaluation in your BigQuery table. When the service samples prediction input and output from your model version and saves it to BigQuery, the data gets stored as JSON strings in the BigQuery table. These keys tell Data Labeling Service how to parse the JSON. You can provide the following entries in this field: * &#x60;data_json_key&#x60;: the data key for prediction input. You must provide either this key or &#x60;reference_json_key&#x60;. * &#x60;reference_json_key&#x60;: the data reference key for prediction input. You must provide either this key or &#x60;data_json_key&#x60;. * &#x60;label_json_key&#x60;: the label key for prediction output. Required. * &#x60;label_score_json_key&#x60;: the score key for prediction output. Required. * &#x60;bounding_box_json_key&#x60;: the bounding box key for prediction output. Required if your model version perform image object detection. Learn [how to configure prediction keys](/ml-engine/docs/continuous-evaluation/create-job#prediction-keys). |  [optional] |
|**boundingPolyConfig** | [**GoogleCloudDatalabelingV1beta1BoundingPolyConfig**](GoogleCloudDatalabelingV1beta1BoundingPolyConfig.md) |  |  [optional] |
|**evaluationConfig** | [**GoogleCloudDatalabelingV1beta1EvaluationConfig**](GoogleCloudDatalabelingV1beta1EvaluationConfig.md) |  |  [optional] |
|**evaluationJobAlertConfig** | [**GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfig**](GoogleCloudDatalabelingV1beta1EvaluationJobAlertConfig.md) |  |  [optional] |
|**exampleCount** | **Integer** | Required. The maximum number of predictions to sample and save to BigQuery during each evaluation interval. This limit overrides &#x60;example_sample_percentage&#x60;: even if the service has not sampled enough predictions to fulfill &#x60;example_sample_perecentage&#x60; during an interval, it stops sampling predictions when it meets this limit. |  [optional] |
|**exampleSamplePercentage** | **Double** | Required. Fraction of predictions to sample and save to BigQuery during each evaluation interval. For example, 0.1 means 10% of predictions served by your model version get saved to BigQuery. |  [optional] |
|**humanAnnotationConfig** | [**GoogleCloudDatalabelingV1beta1HumanAnnotationConfig**](GoogleCloudDatalabelingV1beta1HumanAnnotationConfig.md) |  |  [optional] |
|**imageClassificationConfig** | [**GoogleCloudDatalabelingV1beta1ImageClassificationConfig**](GoogleCloudDatalabelingV1beta1ImageClassificationConfig.md) |  |  [optional] |
|**inputConfig** | [**GoogleCloudDatalabelingV1beta1InputConfig**](GoogleCloudDatalabelingV1beta1InputConfig.md) |  |  [optional] |
|**textClassificationConfig** | [**GoogleCloudDatalabelingV1beta1TextClassificationConfig**](GoogleCloudDatalabelingV1beta1TextClassificationConfig.md) |  |  [optional] |



