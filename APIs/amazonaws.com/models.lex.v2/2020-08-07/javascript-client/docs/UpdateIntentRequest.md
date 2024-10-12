# AmazonLexModelBuildingV2.UpdateIntentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intentName** | **String** | The new name for the intent. | 
**description** | **String** | The new description of the intent. | [optional] 
**parentIntentSignature** | **String** | The signature of the new built-in intent to use as the parent of this intent. | [optional] 
**sampleUtterances** | [**[SampleUtterance]**](SampleUtterance.md) | New utterances used to invoke the intent. | [optional] 
**dialogCodeHook** | [**CreateIntentRequestDialogCodeHook**](CreateIntentRequestDialogCodeHook.md) |  | [optional] 
**fulfillmentCodeHook** | [**CreateIntentRequestFulfillmentCodeHook**](CreateIntentRequestFulfillmentCodeHook.md) |  | [optional] 
**slotPriorities** | [**[SlotPriority]**](SlotPriority.md) | A new list of slots and their priorities that are contained by the intent. | [optional] 
**intentConfirmationSetting** | [**CreateIntentRequestIntentConfirmationSetting**](CreateIntentRequestIntentConfirmationSetting.md) |  | [optional] 
**intentClosingSetting** | [**CreateIntentRequestIntentClosingSetting**](CreateIntentRequestIntentClosingSetting.md) |  | [optional] 
**inputContexts** | [**[InputContext]**](InputContext.md) | A new list of contexts that must be active in order for Amazon Lex to consider the intent. | [optional] 
**outputContexts** | [**[OutputContext]**](OutputContext.md) | A new list of contexts that Amazon Lex activates when the intent is fulfilled. | [optional] 
**kendraConfiguration** | [**CreateIntentRequestKendraConfiguration**](CreateIntentRequestKendraConfiguration.md) |  | [optional] 
**initialResponseSetting** | [**CreateIntentRequestInitialResponseSetting**](CreateIntentRequestInitialResponseSetting.md) |  | [optional] 


