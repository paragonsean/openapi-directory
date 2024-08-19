# AwsEntityResolution.CreateSchemaMappingRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the schema. | [optional] 
**mappedInputFields** | [**[SchemaInputAttribute]**](SchemaInputAttribute.md) | A list of &lt;code&gt;MappedInputFields&lt;/code&gt;. Each &lt;code&gt;MappedInputField&lt;/code&gt; corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching. | [optional] 
**schemaName** | **String** | The name of the schema. There cannot be multiple &lt;code&gt;SchemaMappings&lt;/code&gt; with the same name. | 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. | [optional] 


