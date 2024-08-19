

# GoogleCloudAiplatformV1beta1StudySpecParameterSpec

Represents a single parameter to optimize.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoricalValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec.md) |  |  [optional] |
|**conditionalParameterSpecs** | [**List&lt;GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec&gt;**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec.md) | A conditional parameter node is active if the parameter&#39;s value matches the conditional node&#39;s parent_value_condition. If two items in conditional_parameter_specs have the same name, they must have disjoint parent_value_condition. |  [optional] |
|**discreteValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec.md) |  |  [optional] |
|**doubleValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec.md) |  |  [optional] |
|**integerValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec.md) |  |  [optional] |
|**parameterId** | **String** | Required. The ID of the parameter. Must not contain whitespaces and must be unique amongst all ParameterSpecs. |  [optional] |
|**scaleType** | [**ScaleTypeEnum**](#ScaleTypeEnum) | How the parameter should be scaled. Leave unset for &#x60;CATEGORICAL&#x60; parameters. |  [optional] |



## Enum: ScaleTypeEnum

| Name | Value |
|---- | -----|
| SCALE_TYPE_UNSPECIFIED | &quot;SCALE_TYPE_UNSPECIFIED&quot; |
| UNIT_LINEAR_SCALE | &quot;UNIT_LINEAR_SCALE&quot; |
| UNIT_LOG_SCALE | &quot;UNIT_LOG_SCALE&quot; |
| UNIT_REVERSE_LOG_SCALE | &quot;UNIT_REVERSE_LOG_SCALE&quot; |



