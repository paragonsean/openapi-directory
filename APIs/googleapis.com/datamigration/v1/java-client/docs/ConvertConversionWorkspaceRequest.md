

# ConvertConversionWorkspaceRequest

Request message for 'ConvertConversionWorkspace' request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCommit** | **Boolean** | Optional. Specifies whether the conversion workspace is to be committed automatically after the conversion. |  [optional] |
|**convertFullPath** | **Boolean** | Optional. Automatically convert the full entity path for each entity specified by the filter. For example, if the filter specifies a table, that table schema (and database if there is one) will also be converted. |  [optional] |
|**filter** | **String** | Optional. Filter the entities to convert. Leaving this field empty will convert all of the entities. Supports Google AIP-160 style filtering. |  [optional] |



