

# GoogleCloudMlV1StudyConfigParameterSpec

Represents a single parameter to optimize.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoricalValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecCategoricalValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecCategoricalValueSpec.md) |  |  [optional] |
|**childParameterSpecs** | [**List&lt;GoogleCloudMlV1StudyConfigParameterSpec&gt;**](GoogleCloudMlV1StudyConfigParameterSpec.md) | A child node is active if the parameter&#39;s value matches the child node&#39;s matching_parent_values. If two items in child_parameter_specs have the same name, they must have disjoint matching_parent_values. |  [optional] |
|**discreteValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecDiscreteValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecDiscreteValueSpec.md) |  |  [optional] |
|**doubleValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecDoubleValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecDoubleValueSpec.md) |  |  [optional] |
|**integerValueSpec** | [**GoogleCloudMlV1StudyConfigParameterSpecIntegerValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecIntegerValueSpec.md) |  |  [optional] |
|**parameter** | **String** | Required. The parameter name must be unique amongst all ParameterSpecs. |  [optional] |
|**parentCategoricalValues** | [**GoogleCloudMlV1StudyConfigParameterSpecMatchingParentCategoricalValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecMatchingParentCategoricalValueSpec.md) |  |  [optional] |
|**parentDiscreteValues** | [**GoogleCloudMlV1StudyConfigParameterSpecMatchingParentDiscreteValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecMatchingParentDiscreteValueSpec.md) |  |  [optional] |
|**parentIntValues** | [**GoogleCloudMlV1StudyConfigParameterSpecMatchingParentIntValueSpec**](GoogleCloudMlV1StudyConfigParameterSpecMatchingParentIntValueSpec.md) |  |  [optional] |
|**scaleType** | [**ScaleTypeEnum**](#ScaleTypeEnum) | How the parameter should be scaled. Leave unset for categorical parameters. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the parameter. |  [optional] |



## Enum: ScaleTypeEnum

| Name | Value |
|---- | -----|
| SCALE_TYPE_UNSPECIFIED | &quot;SCALE_TYPE_UNSPECIFIED&quot; |
| UNIT_LINEAR_SCALE | &quot;UNIT_LINEAR_SCALE&quot; |
| UNIT_LOG_SCALE | &quot;UNIT_LOG_SCALE&quot; |
| UNIT_REVERSE_LOG_SCALE | &quot;UNIT_REVERSE_LOG_SCALE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PARAMETER_TYPE_UNSPECIFIED | &quot;PARAMETER_TYPE_UNSPECIFIED&quot; |
| DOUBLE | &quot;DOUBLE&quot; |
| INTEGER | &quot;INTEGER&quot; |
| CATEGORICAL | &quot;CATEGORICAL&quot; |
| DISCRETE | &quot;DISCRETE&quot; |



