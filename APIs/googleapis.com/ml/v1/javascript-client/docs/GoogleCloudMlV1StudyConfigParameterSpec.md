# AiPlatformTrainingPredictionApi.GoogleCloudMlV1StudyConfigParameterSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoricalValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecCategoricalValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecCategoricalValueSpec.md) |  | [optional] 
**childParameterSpecs** | [**[GoogleCloudMlV1StudyConfigParameterSpec]**](GoogleCloudMlV1StudyConfigParameterSpec.md) | A child node is active if the parameter&#39;s value matches the child node&#39;s matching_parent_values. If two items in child_parameter_specs have the same name, they must have disjoint matching_parent_values. | [optional] 
**discreteValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecDiscreteValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecDiscreteValueSpec.md) |  | [optional] 
**doubleValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecDoubleValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecDoubleValueSpec.md) |  | [optional] 
**integerValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecIntegerValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecIntegerValueSpec.md) |  | [optional] 
**parameter** | **String** | Required. The parameter name must be unique amongst all ParameterSpecs. | [optional] 
**parentCategoricalValues** | [**GoogleCloudMlV1StudyConfigParameterSpecMatchingParentCategoricalValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecMatchingParentCategoricalValueSpec.md) |  | [optional] 
**parentDiscreteValues** | [**GoogleCloudMlV1StudyConfigParameterSpecMatchingParentDiscreteValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecMatchingParentDiscreteValueSpec.md) |  | [optional] 
**parentIntValues** | [**GoogleCloudMlV1StudyConfigParameterSpecMatchingParentIntValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecMatchingParentIntValueSpec.md) |  | [optional] 
**scaleType** | **String** | How the parameter should be scaled. Leave unset for categorical parameters. | [optional] 
**type** | **String** | Required. The type of the parameter. | [optional] 



## Enum: ScaleTypeEnum


* `SCALE_TYPE_UNSPECIFIED` (value: `"SCALE_TYPE_UNSPECIFIED"`)

* `UNIT_LINEAR_SCALE` (value: `"UNIT_LINEAR_SCALE"`)

* `UNIT_LOG_SCALE` (value: `"UNIT_LOG_SCALE"`)

* `UNIT_REVERSE_LOG_SCALE` (value: `"UNIT_REVERSE_LOG_SCALE"`)





## Enum: TypeEnum


* `PARAMETER_TYPE_UNSPECIFIED` (value: `"PARAMETER_TYPE_UNSPECIFIED"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `INTEGER` (value: `"INTEGER"`)

* `CATEGORICAL` (value: `"CATEGORICAL"`)

* `DISCRETE` (value: `"DISCRETE"`)




