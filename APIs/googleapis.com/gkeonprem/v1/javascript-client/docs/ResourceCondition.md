# AnthosOnPremApi.ResourceCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastTransitionTime** | **String** | Last time the condition transit from one status to another. | [optional] 
**message** | **String** | Human-readable message indicating details about last transition. | [optional] 
**reason** | **String** | Machine-readable message indicating details about last transition. | [optional] 
**state** | **String** | state of the condition. | [optional] 
**type** | **String** | Type of the condition. (e.g., ClusterRunning, NodePoolRunning or ServerSidePreflightReady) | [optional] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `TRUE` (value: `"STATE_TRUE"`)

* `FALSE` (value: `"STATE_FALSE"`)

* `UNKNOWN` (value: `"STATE_UNKNOWN"`)




