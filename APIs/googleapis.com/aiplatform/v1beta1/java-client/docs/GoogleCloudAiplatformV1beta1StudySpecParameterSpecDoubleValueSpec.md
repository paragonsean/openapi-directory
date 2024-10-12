

# GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec

Value specification for a parameter in `DOUBLE` type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | **Double** | A default value for a &#x60;DOUBLE&#x60; parameter that is assumed to be a relatively good starting point. Unset value signals that there is no offered starting point. Currently only supported by the Vertex AI Vizier service. Not supported by HyperparameterTuningJob or TrainingPipeline. |  [optional] |
|**maxValue** | **Double** | Required. Inclusive maximum value of the parameter. |  [optional] |
|**minValue** | **Double** | Required. Inclusive minimum value of the parameter. |  [optional] |



