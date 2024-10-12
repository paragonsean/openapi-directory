# DataflowApi.InstructionInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outputNum** | **Number** | The output index (origin zero) within the producer. | [optional] 
**producerInstructionIndex** | **Number** | The index (origin zero) of the parallel instruction that produces the output to be consumed by this input. This index is relative to the list of instructions in this input&#39;s instruction&#39;s containing MapTask. | [optional] 


