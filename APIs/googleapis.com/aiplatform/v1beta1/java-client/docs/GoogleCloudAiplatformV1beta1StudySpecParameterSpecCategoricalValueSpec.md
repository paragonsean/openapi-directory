

# GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec

Value specification for a parameter in `CATEGORICAL` type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | **String** | A default value for a &#x60;CATEGORICAL&#x60; parameter that is assumed to be a relatively good starting point. Unset value signals that there is no offered starting point. Currently only supported by the Vertex AI Vizier service. Not supported by HyperparameterTuningJob or TrainingPipeline. |  [optional] |
|**values** | **List&lt;String&gt;** | Required. The list of possible categories. |  [optional] |



