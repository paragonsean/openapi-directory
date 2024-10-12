# AiPlatformTrainingPredictionApi.GoogleCloudMlV1ParameterSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoricalValues** | **[String]** | Required if type is &#x60;CATEGORICAL&#x60;. The list of possible categories. | [optional] 
**discreteValues** | **[Number]** | Required if type is &#x60;DISCRETE&#x60;. A list of feasible points. The list should be in strictly increasing order. For instance, this parameter might have possible settings of 1.5, 2.5, and 4.0. This list should not contain more than 1,000 values. | [optional] 
**maxValue** | **Number** | Required if type is &#x60;DOUBLE&#x60; or &#x60;INTEGER&#x60;. This field should be unset if type is &#x60;CATEGORICAL&#x60;. This value should be integers if type is &#x60;INTEGER&#x60;. | [optional] 
**minValue** | **Number** | Required if type is &#x60;DOUBLE&#x60; or &#x60;INTEGER&#x60;. This field should be unset if type is &#x60;CATEGORICAL&#x60;. This value should be integers if type is INTEGER. | [optional] 
**parameterName** | **String** | Required. The parameter name must be unique amongst all ParameterConfigs in a HyperparameterSpec message. E.g., \&quot;learning_rate\&quot;. | [optional] 
**scaleType** | **String** | Optional. How the parameter should be scaled to the hypercube. Leave unset for categorical parameters. Some kind of scaling is strongly recommended for real or integral parameters (e.g., &#x60;UNIT_LINEAR_SCALE&#x60;). | [optional] 
**type** | **String** | Required. The type of the parameter. | [optional] 



## Enum: ScaleTypeEnum


* `NONE` (value: `"NONE"`)

* `UNIT_LINEAR_SCALE` (value: `"UNIT_LINEAR_SCALE"`)

* `UNIT_LOG_SCALE` (value: `"UNIT_LOG_SCALE"`)

* `UNIT_REVERSE_LOG_SCALE` (value: `"UNIT_REVERSE_LOG_SCALE"`)





## Enum: TypeEnum


* `PARAMETER_TYPE_UNSPECIFIED` (value: `"PARAMETER_TYPE_UNSPECIFIED"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `INTEGER` (value: `"INTEGER"`)

* `CATEGORICAL` (value: `"CATEGORICAL"`)

* `DISCRETE` (value: `"DISCRETE"`)




