

# GoogleCloudDialogflowV2beta1SuggestionInput

Represents the selection of a suggestion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerRecord** | **String** | Required. The ID of a suggestion selected by the human agent. The suggestion(s) were generated in a previous call to request Dialogflow assist. The format is: &#x60;projects//locations//answerRecords/&#x60; where is an alphanumeric string. |  [optional] |
|**intentInput** | [**GoogleCloudDialogflowV2beta1IntentInput**](GoogleCloudDialogflowV2beta1IntentInput.md) |  |  [optional] |
|**parameters** | **Map&lt;String, Object&gt;** | In Dialogflow assist for v3, the user can submit a form by sending a SuggestionInput. The form is uniquely determined by the answer_record field, which identifies a v3 QueryResult containing the current page. The form parameters are specified via the parameters field. Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs: * MapKey type: string * MapKey value: parameter name * MapValue type: If parameter&#39;s entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map. * MapValue value: If parameter&#39;s entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value. |  [optional] |
|**textOverride** | [**GoogleCloudDialogflowV2beta1TextInput**](GoogleCloudDialogflowV2beta1TextInput.md) |  |  [optional] |



