

# CreateWorkflowRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | A name for the workflow. |  [optional] |
|**description** | **String** | A description for the workflow. |  [optional] |
|**engine** | [**EngineEnum**](#EngineEnum) | An engine for the workflow. |  [optional] |
|**definitionZip** | **String** | A ZIP archive for the workflow. |  [optional] |
|**definitionUri** | **String** | The URI of a definition for the workflow. |  [optional] |
|**main** | **String** | The path of the main definition file for the workflow. |  [optional] |
|**parameterTemplate** | [**Map&lt;String, WorkflowParameter&gt;**](WorkflowParameter.md) | A parameter template for the workflow. |  [optional] |
|**storageCapacity** | **Integer** | A storage capacity for the workflow in gigabytes. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags for the workflow. |  [optional] |
|**requestId** | **String** | To ensure that requests don&#39;t run multiple times, specify a unique ID for each request. |  |
|**accelerators** | [**AcceleratorsEnum**](#AcceleratorsEnum) |  The computational accelerator specified to run the workflow.  |  [optional] |



## Enum: EngineEnum

| Name | Value |
|---- | -----|
| WDL | &quot;WDL&quot; |
| NEXTFLOW | &quot;NEXTFLOW&quot; |
| CWL | &quot;CWL&quot; |



## Enum: AcceleratorsEnum

| Name | Value |
|---- | -----|
| GPU | &quot;GPU&quot; |



