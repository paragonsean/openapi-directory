

# SubSlotValueElicitationSetting

<p>Subslot elicitation settings.</p> <p> <code>DefaultValueSpecification</code> is a list of default values for a constituent sub slot in a composite slot. Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values. This is similar to <code>DefaultValueSpecification</code> for slots.</p> <p> <code>PromptSpecification</code> is the prompt that Amazon Lex uses to elicit the sub slot value from the user. This is similar to <code>PromptSpecification</code> for slots.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValueSpecification** | [**SlotDefaultValueSpecification**](SlotDefaultValueSpecification.md) |  |  [optional] |
|**promptSpecification** | [**PromptSpecification**](PromptSpecification.md) |  |  |
|**sampleUtterances** | [**List**](List.md) |  |  [optional] |
|**waitAndContinueSpecification** | [**WaitAndContinueSpecification**](WaitAndContinueSpecification.md) |  |  [optional] |



