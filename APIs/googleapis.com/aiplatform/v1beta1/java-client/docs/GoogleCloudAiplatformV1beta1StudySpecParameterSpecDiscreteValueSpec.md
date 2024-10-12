

# GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec

Value specification for a parameter in `DISCRETE` type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | **Double** | A default value for a &#x60;DISCRETE&#x60; parameter that is assumed to be a relatively good starting point. Unset value signals that there is no offered starting point. It automatically rounds to the nearest feasible discrete point. Currently only supported by the Vertex AI Vizier service. Not supported by HyperparameterTuningJob or TrainingPipeline. |  [optional] |
|**values** | **List&lt;Double&gt;** | Required. A list of possible values. The list should be in increasing order and at least 1e-10 apart. For instance, this parameter might have possible settings of 1.5, 2.5, and 4.0. This list should not contain more than 1,000 values. |  [optional] |



