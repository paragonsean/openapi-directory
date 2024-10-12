

# GoogleCloudMlV1ParameterSpec

Represents a single hyperparameter to optimize.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoricalValues** | **List&lt;String&gt;** | Required if type is &#x60;CATEGORICAL&#x60;. The list of possible categories. |  [optional] |
|**discreteValues** | **List&lt;Double&gt;** | Required if type is &#x60;DISCRETE&#x60;. A list of feasible points. The list should be in strictly increasing order. For instance, this parameter might have possible settings of 1.5, 2.5, and 4.0. This list should not contain more than 1,000 values. |  [optional] |
|**maxValue** | **Double** | Required if type is &#x60;DOUBLE&#x60; or &#x60;INTEGER&#x60;. This field should be unset if type is &#x60;CATEGORICAL&#x60;. This value should be integers if type is &#x60;INTEGER&#x60;. |  [optional] |
|**minValue** | **Double** | Required if type is &#x60;DOUBLE&#x60; or &#x60;INTEGER&#x60;. This field should be unset if type is &#x60;CATEGORICAL&#x60;. This value should be integers if type is INTEGER. |  [optional] |
|**parameterName** | **String** | Required. The parameter name must be unique amongst all ParameterConfigs in a HyperparameterSpec message. E.g., \&quot;learning_rate\&quot;. |  [optional] |
|**scaleType** | [**ScaleTypeEnum**](#ScaleTypeEnum) | Optional. How the parameter should be scaled to the hypercube. Leave unset for categorical parameters. Some kind of scaling is strongly recommended for real or integral parameters (e.g., &#x60;UNIT_LINEAR_SCALE&#x60;). |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the parameter. |  [optional] |



## Enum: ScaleTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
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



