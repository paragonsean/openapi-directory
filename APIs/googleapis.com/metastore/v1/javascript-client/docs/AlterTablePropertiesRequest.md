# DataprocMetastoreApi.AlterTablePropertiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **{String: String}** | A map that describes the desired values to mutate. If update_mask is empty, the properties will not update. Otherwise, the properties only alters the value whose associated paths exist in the update mask | [optional] 
**tableName** | **String** | Required. The name of the table containing the properties you&#39;re altering in the following format.databases/{database_id}/tables/{table_id} | [optional] 
**updateMask** | **String** | A field mask that specifies the metadata table properties that are overwritten by the update. Fields specified in the update_mask are relative to the resource (not to the full request). A field is overwritten if it is in the mask.For example, given the target properties: properties { a: 1 b: 2 } And an update properties: properties { a: 2 b: 3 c: 4 } then if the field mask is:paths: \&quot;properties.b\&quot;, \&quot;properties.c\&quot;then the result will be: properties { a: 1 b: 3 c: 4 }  | [optional] 


