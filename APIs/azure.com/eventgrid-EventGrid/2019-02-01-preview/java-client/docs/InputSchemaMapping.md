

# InputSchemaMapping

By default, Event Grid expects events to be in the Event Grid event schema. Specifying an input schema mapping enables publishing to Event Grid using a custom input schema. Currently, the only supported type of InputSchemaMapping is 'JsonInputSchemaMapping'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputSchemaMappingType** | [**InputSchemaMappingTypeEnum**](#InputSchemaMappingTypeEnum) | Type of the custom mapping |  [optional] |



## Enum: InputSchemaMappingTypeEnum

| Name | Value |
|---- | -----|
| JSON | &quot;Json&quot; |



