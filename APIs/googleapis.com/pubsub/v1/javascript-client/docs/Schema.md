# CloudPubSubApi.Schema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | **String** | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in &#x60;type&#x60;. | [optional] 
**name** | **String** | Required. Name of the schema. Format is &#x60;projects/{project}/schemas/{schema}&#x60;. | [optional] 
**revisionCreateTime** | **String** | Output only. The timestamp that the revision was created. | [optional] [readonly] 
**revisionId** | **String** | Output only. Immutable. The revision ID of the schema. | [optional] [readonly] 
**type** | **String** | The type of the schema definition. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `PROTOCOL_BUFFER` (value: `"PROTOCOL_BUFFER"`)

* `AVRO` (value: `"AVRO"`)




