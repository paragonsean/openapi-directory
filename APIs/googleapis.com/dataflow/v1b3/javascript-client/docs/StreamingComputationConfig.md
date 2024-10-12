# DataflowApi.StreamingComputationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computationId** | **String** | Unique identifier for this computation. | [optional] 
**instructions** | [**[ParallelInstruction]**](ParallelInstruction.md) | Instructions that comprise the computation. | [optional] 
**stageName** | **String** | Stage name of this computation. | [optional] 
**systemName** | **String** | System defined name for this computation. | [optional] 
**transformUserNameToStateFamily** | **{String: String}** | Map from user name of stateful transforms in this stage to their state family. | [optional] 


