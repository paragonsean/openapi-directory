# VertexAiApi.GoogleCloudAiplatformV1beta1StudySpecParameterSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoricalValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecCategoricalValueSpec.md) |  | [optional] 
**conditionalParameterSpecs** | [**[GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec]**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecConditionalParameterSpec.md) | A conditional parameter node is active if the parameter&#39;s value matches the conditional node&#39;s parent_value_condition. If two items in conditional_parameter_specs have the same name, they must have disjoint parent_value_condition. | [optional] 
**discreteValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecDiscreteValueSpec.md) |  | [optional] 
**doubleValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecDoubleValueSpec.md) |  | [optional] 
**integerValueSpec** | [**GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec**](GoogleCloudAiplatformV1beta1StudySpecParameterSpecIntegerValueSpec.md) |  | [optional] 
**parameterId** | **String** | Required. The ID of the parameter. Must not contain whitespaces and must be unique amongst all ParameterSpecs. | [optional] 
**scaleType** | **String** | How the parameter should be scaled. Leave unset for &#x60;CATEGORICAL&#x60; parameters. | [optional] 



## Enum: ScaleTypeEnum


* `SCALE_TYPE_UNSPECIFIED` (value: `"SCALE_TYPE_UNSPECIFIED"`)

* `UNIT_LINEAR_SCALE` (value: `"UNIT_LINEAR_SCALE"`)

* `UNIT_LOG_SCALE` (value: `"UNIT_LOG_SCALE"`)

* `UNIT_REVERSE_LOG_SCALE` (value: `"UNIT_REVERSE_LOG_SCALE"`)




