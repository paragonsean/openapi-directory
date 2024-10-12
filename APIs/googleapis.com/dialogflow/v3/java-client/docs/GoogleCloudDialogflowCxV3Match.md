

# GoogleCloudDialogflowCxV3Match

Represents one match result of MatchIntent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | **Float** | The confidence of this match. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. |  [optional] |
|**event** | **String** | The event that matched the query. Filled for &#x60;EVENT&#x60;, &#x60;NO_MATCH&#x60; and &#x60;NO_INPUT&#x60; match types. |  [optional] |
|**intent** | [**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md) |  |  [optional] |
|**matchType** | [**MatchTypeEnum**](#MatchTypeEnum) | Type of this Match. |  [optional] |
|**parameters** | **Map&lt;String, Object&gt;** | The collection of parameters extracted from the query. Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs: * MapKey type: string * MapKey value: parameter name * MapValue type: If parameter&#39;s entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map. * MapValue value: If parameter&#39;s entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value. |  [optional] |
|**resolvedInput** | **String** | Final text input which was matched during MatchIntent. This value can be different from original input sent in request because of spelling correction or other processing. |  [optional] |



## Enum: MatchTypeEnum

| Name | Value |
|---- | -----|
| MATCH_TYPE_UNSPECIFIED | &quot;MATCH_TYPE_UNSPECIFIED&quot; |
| INTENT | &quot;INTENT&quot; |
| DIRECT_INTENT | &quot;DIRECT_INTENT&quot; |
| PARAMETER_FILLING | &quot;PARAMETER_FILLING&quot; |
| NO_MATCH | &quot;NO_MATCH&quot; |
| NO_INPUT | &quot;NO_INPUT&quot; |
| EVENT | &quot;EVENT&quot; |



