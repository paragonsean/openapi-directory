# FinSpacePublicApi.CreateDatasetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | Idempotence Token for API operations | [optional] 
**datasetTitle** | **String** | Title for a given Dataset | 
**kind** | **String** | Dataset Kind | 
**datasetDescription** | **String** | Description of a dataset | [optional] 
**ownerInfo** | [**CreateDatasetRequestOwnerInfo**](CreateDatasetRequestOwnerInfo.md) |  | [optional] 
**permissionGroupParams** | [**CreateDatasetRequestPermissionGroupParams**](CreateDatasetRequestPermissionGroupParams.md) |  | 
**alias** | **String** | The unique resource identifier for a Dataset. | [optional] 
**schemaDefinition** | [**CreateDatasetRequestSchemaDefinition**](CreateDatasetRequestSchemaDefinition.md) |  | [optional] 



## Enum: KindEnum


* `TABULAR` (value: `"TABULAR"`)

* `NON_TABULAR` (value: `"NON_TABULAR"`)




