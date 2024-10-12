

# ExperimentProperties

Defines the properties of an experiment

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the details or intents of the Experiment |  [optional] |
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | The state of the Experiment |  [optional] |
|**endpointA** | [**Endpoint**](Endpoint.md) |  |  [optional] |
|**endpointB** | [**Endpoint**](Endpoint.md) |  |  [optional] |
|**resourceState** | **NetworkExperimentResourceState** |  |  [optional] |
|**scriptFileUri** | **String** | The uri to the Script used in the Experiment |  [optional] [readonly] |
|**status** | **String** | The description of Experiment status from the server side |  [optional] [readonly] |



## Enum: EnabledStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



