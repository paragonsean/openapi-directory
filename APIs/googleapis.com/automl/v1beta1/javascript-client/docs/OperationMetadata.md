# CloudAutoMlApi.OperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchPredictDetails** | [**BatchPredictOperationMetadata**](BatchPredictOperationMetadata.md) |  | [optional] 
**createModelDetails** | **Object** | Details of CreateModel operation. | [optional] 
**createTime** | **String** | Output only. Time when the operation was created. | [optional] 
**deleteDetails** | **Object** | Details of operations that perform deletes of any entities. | [optional] 
**deployModelDetails** | **Object** | Details of DeployModel operation. | [optional] 
**exportDataDetails** | [**ExportDataOperationMetadata**](ExportDataOperationMetadata.md) |  | [optional] 
**exportEvaluatedExamplesDetails** | [**ExportEvaluatedExamplesOperationMetadata**](ExportEvaluatedExamplesOperationMetadata.md) |  | [optional] 
**exportModelDetails** | [**ExportModelOperationMetadata**](ExportModelOperationMetadata.md) |  | [optional] 
**importDataDetails** | **Object** | Details of ImportData operation. | [optional] 
**partialFailures** | [**[Status]**](Status.md) | Output only. Partial failures encountered. E.g. single files that couldn&#39;t be read. This field should never exceed 20 entries. Status details field will contain standard GCP error details. | [optional] 
**progressPercent** | **Number** | Output only. Progress of operation. Range: [0, 100]. Not used currently. | [optional] 
**undeployModelDetails** | **Object** | Details of UndeployModel operation. | [optional] 
**updateTime** | **String** | Output only. Time when the operation was updated for the last time. | [optional] 


