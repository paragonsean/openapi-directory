

# GoogleCloudDialogflowCxV3beta1FlowImportStrategy

The flow import strategy used for resource conflict resolution associated with an ImportFlowRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**globalImportStrategy** | [**GlobalImportStrategyEnum**](#GlobalImportStrategyEnum) | Optional. Global flow import strategy for resource conflict resolution. The import Import strategy for resource conflict resolution, applied globally throughout the flow. It will be applied for all display name conflicts in the imported content. If not specified, &#39;CREATE_NEW&#39; is assumed. |  [optional] |



## Enum: GlobalImportStrategyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPORT_STRATEGY_UNSPECIFIED&quot; |
| CREATE_NEW | &quot;IMPORT_STRATEGY_CREATE_NEW&quot; |
| REPLACE | &quot;IMPORT_STRATEGY_REPLACE&quot; |
| KEEP | &quot;IMPORT_STRATEGY_KEEP&quot; |
| MERGE | &quot;IMPORT_STRATEGY_MERGE&quot; |
| THROW_ERROR | &quot;IMPORT_STRATEGY_THROW_ERROR&quot; |



