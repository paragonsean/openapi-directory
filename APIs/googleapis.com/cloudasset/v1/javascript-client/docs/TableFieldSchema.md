# CloudAssetApi.TableFieldSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **String** | The field name. The name must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_), and must start with a letter or underscore. The maximum length is 128 characters. | [optional] 
**fields** | [**[TableFieldSchema]**](TableFieldSchema.md) | Describes the nested schema fields if the type property is set to RECORD. | [optional] 
**mode** | **String** | The field mode. Possible values include NULLABLE, REQUIRED and REPEATED. The default value is NULLABLE. | [optional] 
**type** | **String** | The field data type. Possible values include * STRING * BYTES * INTEGER * FLOAT * BOOLEAN * TIMESTAMP * DATE * TIME * DATETIME * GEOGRAPHY, * NUMERIC, * BIGNUMERIC, * RECORD (where RECORD indicates that the field contains a nested schema). | [optional] 


