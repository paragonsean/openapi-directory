

# ActionInformation

The Information about an Action of a device

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**ActionTypeEnum**](#ActionTypeEnum) | The Type of this action. |  [optional] |
|**maxValue** | **Double** | The maximum value of this action (e.g. for an AnalogAction) |  [optional] |
|**minValue** | **Double** | The minimum value of this action (e.g. for an AnalogAction) |  [optional] |
|**name** | **String** | The Name of this action |  [optional] |
|**obisCode** | **String** | The Obis Code of this action. This is used as ID. |  [optional] |



## Enum: ActionTypeEnum

| Name | Value |
|---- | -----|
| ON_OFF_ACTION | &quot;OnOffAction&quot; |
| ANALOG_ACTION | &quot;AnalogAction&quot; |



