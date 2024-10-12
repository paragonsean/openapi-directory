

# PartialGroupByKeyInstruction

An instruction that does a partial group-by-key. One input and one output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**input** | [**InstructionInput**](InstructionInput.md) |  |  [optional] |
|**inputElementCodec** | **Map&lt;String, Object&gt;** | The codec to use for interpreting an element in the input PTable. |  [optional] |
|**originalCombineValuesInputStoreName** | **String** | If this instruction includes a combining function this is the name of the intermediate store between the GBK and the CombineValues. |  [optional] |
|**originalCombineValuesStepName** | **String** | If this instruction includes a combining function, this is the name of the CombineValues instruction lifted into this instruction. |  [optional] |
|**sideInputs** | [**List&lt;SideInputInfo&gt;**](SideInputInfo.md) | Zero or more side inputs. |  [optional] |
|**valueCombiningFn** | **Map&lt;String, Object&gt;** | The value combining function to invoke. |  [optional] |



