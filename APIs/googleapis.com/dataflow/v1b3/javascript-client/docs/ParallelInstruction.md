# DataflowApi.ParallelInstruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flatten** | [**FlattenInstruction**](FlattenInstruction.md) |  | [optional] 
**name** | **String** | User-provided name of this operation. | [optional] 
**originalName** | **String** | System-defined name for the operation in the original workflow graph. | [optional] 
**outputs** | [**[InstructionOutput]**](InstructionOutput.md) | Describes the outputs of the instruction. | [optional] 
**parDo** | [**ParDoInstruction**](ParDoInstruction.md) |  | [optional] 
**partialGroupByKey** | [**PartialGroupByKeyInstruction**](PartialGroupByKeyInstruction.md) |  | [optional] 
**read** | [**ReadInstruction**](ReadInstruction.md) |  | [optional] 
**systemName** | **String** | System-defined name of this operation. Unique across the workflow. | [optional] 
**write** | [**WriteInstruction**](WriteInstruction.md) |  | [optional] 


