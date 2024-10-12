# DataflowApi.PartialGroupByKeyInstruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**InstructionInput**](InstructionInput.md) |  | [optional] 
**inputElementCodec** | **{String: Object}** | The codec to use for interpreting an element in the input PTable. | [optional] 
**originalCombineValuesInputStoreName** | **String** | If this instruction includes a combining function this is the name of the intermediate store between the GBK and the CombineValues. | [optional] 
**originalCombineValuesStepName** | **String** | If this instruction includes a combining function, this is the name of the CombineValues instruction lifted into this instruction. | [optional] 
**sideInputs** | [**[SideInputInfo]**](SideInputInfo.md) | Zero or more side inputs. | [optional] 
**valueCombiningFn** | **{String: Object}** | The value combining function to invoke. | [optional] 


