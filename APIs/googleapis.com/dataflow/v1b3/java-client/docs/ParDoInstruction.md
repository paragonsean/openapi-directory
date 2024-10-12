

# ParDoInstruction

An instruction that does a ParDo operation. Takes one main input and zero or more side inputs, and produces zero or more outputs. Runs user code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**input** | [**InstructionInput**](InstructionInput.md) |  |  [optional] |
|**multiOutputInfos** | [**List&lt;MultiOutputInfo&gt;**](MultiOutputInfo.md) | Information about each of the outputs, if user_fn is a MultiDoFn. |  [optional] |
|**numOutputs** | **Integer** | The number of outputs. |  [optional] |
|**sideInputs** | [**List&lt;SideInputInfo&gt;**](SideInputInfo.md) | Zero or more side inputs. |  [optional] |
|**userFn** | **Map&lt;String, Object&gt;** | The user function to invoke. |  [optional] |



