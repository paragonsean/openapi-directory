

# GetDiscoveredSchemaRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**events** | **List&lt;String&gt;** | An array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of event. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OPEN_API3 | &quot;OpenApi3&quot; |
| JSON_SCHEMA_DRAFT4 | &quot;JSONSchemaDraft4&quot; |



