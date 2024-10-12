# Schemas.GetDiscoveredSchemaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **[String]** | An array of strings where each string is a JSON event. These are the events that were used to generate the schema. The array includes a single type of event and has a maximum size of 10 events. | 
**type** | **String** | The type of event. | 



## Enum: TypeEnum


* `OpenApi3` (value: `"OpenApi3"`)

* `JSONSchemaDraft4` (value: `"JSONSchemaDraft4"`)




