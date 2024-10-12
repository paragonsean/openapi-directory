# AmazonEventBridgePipes.UpdatePipeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the pipe. | [optional] 
**desiredState** | **String** | The state the pipe should be in. | [optional] 
**enrichment** | **String** | The ARN of the enrichment resource. | [optional] 
**enrichmentParameters** | [**UpdatePipeRequestEnrichmentParameters**](UpdatePipeRequestEnrichmentParameters.md) |  | [optional] 
**roleArn** | **String** | The ARN of the role that allows the pipe to send data to the target. | 
**sourceParameters** | [**UpdatePipeRequestSourceParameters**](UpdatePipeRequestSourceParameters.md) |  | [optional] 
**target** | **String** | The ARN of the target resource. | [optional] 
**targetParameters** | [**UpdatePipeRequestTargetParameters**](UpdatePipeRequestTargetParameters.md) |  | [optional] 



## Enum: DesiredStateEnum


* `RUNNING` (value: `"RUNNING"`)

* `STOPPED` (value: `"STOPPED"`)




