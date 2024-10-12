

# JsonFieldWithDefault

This is used to express the source of an input schema mapping for a single target field  in the Event Grid Event schema. This is currently used in the mappings for the 'subject',  'eventtype' and 'dataversion' properties. This represents a field in the input event schema  along with a default value to be used, and at least one of these two properties should be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | **String** | The default value to be used for mapping when a SourceField is not provided or if there&#39;s no property with the specified name in the published JSON event payload. |  [optional] |
|**sourceField** | **String** | Name of a field in the input event schema that&#39;s to be used as the source of a mapping. |  [optional] |



