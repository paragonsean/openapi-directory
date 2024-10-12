# CloudDatastoreApi.GoogleDatastoreAdminV1CommonMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | The time the operation ended, either successfully or otherwise. | [optional] 
**labels** | **{String: String}** | The client-assigned labels which were provided when the operation was created. May also include additional labels. | [optional] 
**operationType** | **String** | The type of the operation. Can be used as a filter in ListOperationsRequest. | [optional] 
**startTime** | **String** | The time that work began on the operation. | [optional] 
**state** | **String** | The current state of the Operation. | [optional] 



## Enum: OperationTypeEnum


* `OPERATION_TYPE_UNSPECIFIED` (value: `"OPERATION_TYPE_UNSPECIFIED"`)

* `EXPORT_ENTITIES` (value: `"EXPORT_ENTITIES"`)

* `IMPORT_ENTITIES` (value: `"IMPORT_ENTITIES"`)

* `CREATE_INDEX` (value: `"CREATE_INDEX"`)

* `DELETE_INDEX` (value: `"DELETE_INDEX"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INITIALIZING` (value: `"INITIALIZING"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `FINALIZING` (value: `"FINALIZING"`)

* `SUCCESSFUL` (value: `"SUCCESSFUL"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)




