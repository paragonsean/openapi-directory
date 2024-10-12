

# GoogleCloudDialogflowV2EventInput

Events allow for matching intents by event name instead of the natural language input. For instance, input `` can trigger a personalized welcome response. The parameter `name` may be used by the agent in the response: `\"Hello #welcome_event.name! What can I do for you today?\"`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | Required. The language of this query. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. This field is ignored when used in the context of a WebhookResponse.followup_event_input field, because the language was already defined in the originating detect intent request. |  [optional] |
|**name** | **String** | Required. The unique identifier of the event. |  [optional] |
|**parameters** | **Map&lt;String, Object&gt;** | The collection of parameters associated with the event. Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs: * MapKey type: string * MapKey value: parameter name * MapValue type: If parameter&#39;s entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map. * MapValue value: If parameter&#39;s entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value. |  [optional] |



