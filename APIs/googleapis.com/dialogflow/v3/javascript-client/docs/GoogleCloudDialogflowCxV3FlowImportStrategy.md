# DialogflowApi.GoogleCloudDialogflowCxV3FlowImportStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**globalImportStrategy** | **String** | Optional. Import strategy for resource conflict resolution, applied globally throughout the flow. It will be applied for all display name conflicts in the imported content. If not specified, &#39;CREATE_NEW&#39; is assumed. | [optional] 



## Enum: GlobalImportStrategyEnum


* `UNSPECIFIED` (value: `"IMPORT_STRATEGY_UNSPECIFIED"`)

* `CREATE_NEW` (value: `"IMPORT_STRATEGY_CREATE_NEW"`)

* `REPLACE` (value: `"IMPORT_STRATEGY_REPLACE"`)

* `KEEP` (value: `"IMPORT_STRATEGY_KEEP"`)

* `MERGE` (value: `"IMPORT_STRATEGY_MERGE"`)

* `THROW_ERROR` (value: `"IMPORT_STRATEGY_THROW_ERROR"`)




