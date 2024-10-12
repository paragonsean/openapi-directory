# CloudAutoMlApi.InputConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigquerySource** | [**BigQuerySource**](BigQuerySource.md) |  | [optional] 
**gcsSource** | [**GcsSource**](GcsSource.md) |  | [optional] 
**params** | **{String: String}** | Additional domain-specific parameters describing the semantic of the imported data, any string must be up to 25000 characters long. * For Tables: &#x60;schema_inference_version&#x60; - (integer) Required. The version of the algorithm that should be used for the initial inference of the schema (columns&#39; DataTypes) of the table the data is being imported into. Allowed values: \&quot;1\&quot;. | [optional] 


