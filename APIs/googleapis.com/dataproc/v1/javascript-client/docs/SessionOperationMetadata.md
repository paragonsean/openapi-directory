# CloudDataprocApi.SessionOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time when the operation was created. | [optional] 
**description** | **String** | Short description of the operation. | [optional] 
**doneTime** | **String** | The time when the operation was finished. | [optional] 
**labels** | **{String: String}** | Labels associated with the operation. | [optional] 
**operationType** | **String** | The operation type. | [optional] 
**session** | **String** | Name of the session for the operation. | [optional] 
**sessionUuid** | **String** | Session UUID for the operation. | [optional] 
**warnings** | **[String]** | Warnings encountered during operation execution. | [optional] 



## Enum: OperationTypeEnum


* `SESSION_OPERATION_TYPE_UNSPECIFIED` (value: `"SESSION_OPERATION_TYPE_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `TERMINATE` (value: `"TERMINATE"`)

* `DELETE` (value: `"DELETE"`)




