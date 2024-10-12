# DialogflowApi.GoogleCloudDialogflowCxV3Match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **Number** | The confidence of this match. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. | [optional] 
**event** | **String** | The event that matched the query. Filled for &#x60;EVENT&#x60;, &#x60;NO_MATCH&#x60; and &#x60;NO_INPUT&#x60; match types. | [optional] 
**intent** | [**GoogleCloudDialogflowCxV3Intent**](GoogleCloudDialogflowCxV3Intent.md) |  | [optional] 
**matchType** | **String** | Type of this Match. | [optional] 
**parameters** | **{String: Object}** | The collection of parameters extracted from the query. Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs: * MapKey type: string * MapKey value: parameter name * MapValue type: If parameter&#39;s entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map. * MapValue value: If parameter&#39;s entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value. | [optional] 
**resolvedInput** | **String** | Final text input which was matched during MatchIntent. This value can be different from original input sent in request because of spelling correction or other processing. | [optional] 



## Enum: MatchTypeEnum


* `MATCH_TYPE_UNSPECIFIED` (value: `"MATCH_TYPE_UNSPECIFIED"`)

* `INTENT` (value: `"INTENT"`)

* `DIRECT_INTENT` (value: `"DIRECT_INTENT"`)

* `PARAMETER_FILLING` (value: `"PARAMETER_FILLING"`)

* `NO_MATCH` (value: `"NO_MATCH"`)

* `NO_INPUT` (value: `"NO_INPUT"`)

* `EVENT` (value: `"EVENT"`)




