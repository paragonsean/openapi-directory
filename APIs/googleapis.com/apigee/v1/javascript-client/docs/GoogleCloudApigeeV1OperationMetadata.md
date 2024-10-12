# ApigeeApi.GoogleCloudApigeeV1OperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operationType** | **String** |  | [optional] 
**progress** | [**GoogleCloudApigeeV1OperationMetadataProgress**](GoogleCloudApigeeV1OperationMetadataProgress.md) |  | [optional] 
**state** | **String** |  | [optional] 
**targetResourceName** | **String** | Name of the resource for which the operation is operating on. | [optional] 
**warnings** | **[String]** | Warnings encountered while executing the operation. | [optional] 



## Enum: OperationTypeEnum


* `OPERATION_TYPE_UNSPECIFIED` (value: `"OPERATION_TYPE_UNSPECIFIED"`)

* `INSERT` (value: `"INSERT"`)

* `DELETE` (value: `"DELETE"`)

* `UPDATE` (value: `"UPDATE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `FINISHED` (value: `"FINISHED"`)




