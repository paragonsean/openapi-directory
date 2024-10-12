# AmazonEventBridgePipes.CreatePipeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the pipe. | [optional] 
**desiredState** | **String** | The state the pipe should be in. | [optional] 
**enrichment** | **String** | The ARN of the enrichment resource. | [optional] 
**enrichmentParameters** | [**UpdatePipeRequestEnrichmentParameters**](UpdatePipeRequestEnrichmentParameters.md) |  | [optional] 
**roleArn** | **String** | The ARN of the role that allows the pipe to send data to the target. | 
**source** | **String** | The ARN of the source resource. | 
**sourceParameters** | [**CreatePipeRequestSourceParameters**](CreatePipeRequestSourceParameters.md) |  | [optional] 
**tags** | **{String: String}** | The list of key-value pairs to associate with the pipe. | [optional] 
**target** | **String** | The ARN of the target resource. | 
**targetParameters** | [**UpdatePipeRequestTargetParameters**](UpdatePipeRequestTargetParameters.md) |  | [optional] 



## Enum: DesiredStateEnum


* `RUNNING` (value: `"RUNNING"`)

* `STOPPED` (value: `"STOPPED"`)




