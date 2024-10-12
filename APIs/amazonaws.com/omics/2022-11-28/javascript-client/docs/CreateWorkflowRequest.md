# AmazonOmics.CreateWorkflowRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | A name for the workflow. | [optional] 
**description** | **String** | A description for the workflow. | [optional] 
**engine** | **String** | An engine for the workflow. | [optional] 
**definitionZip** | **String** | A ZIP archive for the workflow. | [optional] 
**definitionUri** | **String** | The URI of a definition for the workflow. | [optional] 
**main** | **String** | The path of the main definition file for the workflow. | [optional] 
**parameterTemplate** | [**{String: WorkflowParameter}**](WorkflowParameter.md) | A parameter template for the workflow. | [optional] 
**storageCapacity** | **Number** | A storage capacity for the workflow in gigabytes. | [optional] 
**tags** | **{String: String}** | Tags for the workflow. | [optional] 
**requestId** | **String** | To ensure that requests don&#39;t run multiple times, specify a unique ID for each request. | 
**accelerators** | **String** |  The computational accelerator specified to run the workflow.  | [optional] 



## Enum: EngineEnum


* `WDL` (value: `"WDL"`)

* `NEXTFLOW` (value: `"NEXTFLOW"`)

* `CWL` (value: `"CWL"`)





## Enum: AcceleratorsEnum


* `GPU` (value: `"GPU"`)




