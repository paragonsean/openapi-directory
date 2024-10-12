# CloudChannelApi.GoogleCloudChannelV1ParameterDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedValues** | [**[GoogleCloudChannelV1Value]**](GoogleCloudChannelV1Value.md) | If not empty, parameter values must be drawn from this list. For example, [us-west1, us-west2, ...] Applicable to STRING parameter type. | [optional] 
**maxValue** | [**GoogleCloudChannelV1Value**](GoogleCloudChannelV1Value.md) |  | [optional] 
**minValue** | [**GoogleCloudChannelV1Value**](GoogleCloudChannelV1Value.md) |  | [optional] 
**name** | **String** | Name of the parameter. | [optional] 
**optional** | **Boolean** | If set to true, parameter is optional to purchase this Offer. | [optional] 
**parameterType** | **String** | Data type of the parameter. Minimal value, Maximum value and allowed values will use specified data type here. | [optional] 



## Enum: ParameterTypeEnum


* `PARAMETER_TYPE_UNSPECIFIED` (value: `"PARAMETER_TYPE_UNSPECIFIED"`)

* `INT64` (value: `"INT64"`)

* `STRING` (value: `"STRING"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `BOOLEAN` (value: `"BOOLEAN"`)




