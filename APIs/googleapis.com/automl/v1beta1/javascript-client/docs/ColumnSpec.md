# CloudAutoMlApi.ColumnSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataStats** | [**DataStats**](DataStats.md) |  | [optional] 
**dataType** | [**DataType**](DataType.md) |  | [optional] 
**displayName** | **String** | Output only. The name of the column to show in the interface. The name can be up to 100 characters long and can consist only of ASCII Latin letters A-Z and a-z, ASCII digits 0-9, underscores(_), and forward slashes(/), and must start with a letter or a digit. | [optional] 
**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**name** | **String** | Output only. The resource name of the column specs. Form: &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/tableSpecs/{table_spec_id}/columnSpecs/{column_spec_id}&#x60; | [optional] 
**topCorrelatedColumns** | [**[CorrelatedColumn]**](CorrelatedColumn.md) | Deprecated. | [optional] 


