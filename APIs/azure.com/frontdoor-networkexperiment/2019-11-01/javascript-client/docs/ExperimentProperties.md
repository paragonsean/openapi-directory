# NetworkExperiments.ExperimentProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the details or intents of the Experiment | [optional] 
**enabledState** | **String** | The state of the Experiment | [optional] 
**endpointA** | [**Endpoint**](Endpoint.md) |  | [optional] 
**endpointB** | [**Endpoint**](Endpoint.md) |  | [optional] 
**resourceState** | [**NetworkExperimentResourceState**](NetworkExperimentResourceState.md) |  | [optional] 
**scriptFileUri** | **String** | The uri to the Script used in the Experiment | [optional] [readonly] 
**status** | **String** | The description of Experiment status from the server side | [optional] [readonly] 



## Enum: EnabledStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




