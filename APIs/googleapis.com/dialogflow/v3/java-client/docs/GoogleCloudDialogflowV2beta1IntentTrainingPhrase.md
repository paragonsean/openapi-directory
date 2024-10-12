

# GoogleCloudDialogflowV2beta1IntentTrainingPhrase

Represents an example that the agent is trained on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. The unique identifier of this training phrase. |  [optional] |
|**parts** | [**List&lt;GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart&gt;**](GoogleCloudDialogflowV2beta1IntentTrainingPhrasePart.md) | Required. The ordered list of training phrase parts. The parts are concatenated in order to form the training phrase. Note: The API does not automatically annotate training phrases like the Dialogflow Console does. Note: Do not forget to include whitespace at part boundaries, so the training phrase is well formatted when the parts are concatenated. If the training phrase does not need to be annotated with parameters, you just need a single part with only the Part.text field set. If you want to annotate the training phrase, you must create multiple parts, where the fields of each part are populated in one of two ways: - &#x60;Part.text&#x60; is set to a part of the phrase that has no parameters. - &#x60;Part.text&#x60; is set to a part of the phrase that you want to annotate, and the &#x60;entity_type&#x60;, &#x60;alias&#x60;, and &#x60;user_defined&#x60; fields are all set. |  [optional] |
|**timesAddedCount** | **Integer** | Optional. Indicates how many times this example was added to the intent. Each time a developer adds an existing sample by editing an intent or training, this counter is increased. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the training phrase. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| EXAMPLE | &quot;EXAMPLE&quot; |
| TEMPLATE | &quot;TEMPLATE&quot; |



