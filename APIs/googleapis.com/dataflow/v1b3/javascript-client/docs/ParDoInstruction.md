# DataflowApi.ParDoInstruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**InstructionInput**](InstructionInput.md) |  | [optional] 
**multiOutputInfos** | [**[MultiOutputInfo]**](MultiOutputInfo.md) | Information about each of the outputs, if user_fn is a MultiDoFn. | [optional] 
**numOutputs** | **Number** | The number of outputs. | [optional] 
**sideInputs** | [**[SideInputInfo]**](SideInputInfo.md) | Zero or more side inputs. | [optional] 
**userFn** | **{String: Object}** | The user function to invoke. | [optional] 


