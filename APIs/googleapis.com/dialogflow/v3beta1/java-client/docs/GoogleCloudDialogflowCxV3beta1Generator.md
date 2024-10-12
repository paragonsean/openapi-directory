

# GoogleCloudDialogflowCxV3beta1Generator

Generators contain prompt to be sent to the LLM model to generate text. The prompt can contain parameters which will be resolved before calling the model. It can optionally contain banned phrases to ensure the model responses are safe.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Required. The human-readable name of the generator, unique within the agent. The prompt contains pre-defined parameters such as $conversation, $last-user-utterance, etc. populated by Dialogflow. It can also contain custom placeholders which will be resolved during fulfillment. |  [optional] |
|**name** | **String** | The unique identifier of the generator. Must be set for the Generators.UpdateGenerator method. Generators.CreateGenerate populates the name automatically. Format: &#x60;projects//locations//agents//generators/&#x60;. |  [optional] |
|**placeholders** | [**List&lt;GoogleCloudDialogflowCxV3beta1GeneratorPlaceholder&gt;**](GoogleCloudDialogflowCxV3beta1GeneratorPlaceholder.md) | Optional. List of custom placeholders in the prompt text. |  [optional] |
|**promptText** | [**GoogleCloudDialogflowCxV3beta1Phrase**](GoogleCloudDialogflowCxV3beta1Phrase.md) |  |  [optional] |



