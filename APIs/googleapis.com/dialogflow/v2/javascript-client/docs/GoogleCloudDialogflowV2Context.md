# DialogflowApi.GoogleCloudDialogflowV2Context

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifespanCount** | **Number** | Optional. The number of conversational query requests after which the context expires. The default is &#x60;0&#x60;. If set to &#x60;0&#x60;, the context expires immediately. Contexts expire automatically after 20 minutes if there are no matching queries. | [optional] 
**name** | **String** | Required. The unique identifier of the context. Format: &#x60;projects//agent/sessions//contexts/&#x60;, or &#x60;projects//agent/environments//users//sessions//contexts/&#x60;. The &#x60;Context ID&#x60; is always converted to lowercase, may only contain characters in &#x60;a-zA-Z0-9_-%&#x60; and may be at most 250 bytes long. If &#x60;Environment ID&#x60; is not specified, we assume default &#39;draft&#39; environment. If &#x60;User ID&#x60; is not specified, we assume default &#39;-&#39; user. The following context names are reserved for internal use by Dialogflow. You should not use these contexts or create contexts with these names: * &#x60;__system_counters__&#x60; * &#x60;*_id_dialog_context&#x60; * &#x60;*_dialog_params_size&#x60; | [optional] 
**parameters** | **{String: Object}** | Optional. The collection of parameters associated with this context. Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs: * MapKey type: string * MapKey value: parameter name * MapValue type: If parameter&#39;s entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map. * MapValue value: If parameter&#39;s entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value. | [optional] 


