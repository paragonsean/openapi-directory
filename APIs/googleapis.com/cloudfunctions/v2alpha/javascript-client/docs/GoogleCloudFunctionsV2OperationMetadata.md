# CloudFunctionsApi.GoogleCloudFunctionsV2OperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersion** | **String** | API version used to start the operation. | [optional] 
**cancelRequested** | **Boolean** | Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have google.longrunning.Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;. | [optional] 
**createTime** | **String** | The time the operation was created. | [optional] 
**endTime** | **String** | The time the operation finished running. | [optional] 
**operationType** | **String** | The operation type. | [optional] 
**requestResource** | **{String: Object}** | The original request that started the operation. | [optional] 
**sourceToken** | **String** | An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments. | [optional] 
**stages** | [**[GoogleCloudFunctionsV2Stage]**](GoogleCloudFunctionsV2Stage.md) | Mechanism for reporting in-progress stages | [optional] 
**statusDetail** | **String** | Human-readable status of the operation, if any. | [optional] 
**target** | **String** | Server-defined resource path for the target of the operation. | [optional] 
**verb** | **String** | Name of the verb executed by the operation. | [optional] 



## Enum: OperationTypeEnum


* `OPERATIONTYPE_UNSPECIFIED` (value: `"OPERATIONTYPE_UNSPECIFIED"`)

* `CREATE_FUNCTION` (value: `"CREATE_FUNCTION"`)

* `UPDATE_FUNCTION` (value: `"UPDATE_FUNCTION"`)

* `DELETE_FUNCTION` (value: `"DELETE_FUNCTION"`)

* `REDIRECT_FUNCTION_UPGRADE_TRAFFIC` (value: `"REDIRECT_FUNCTION_UPGRADE_TRAFFIC"`)

* `ROLLBACK_FUNCTION_UPGRADE_TRAFFIC` (value: `"ROLLBACK_FUNCTION_UPGRADE_TRAFFIC"`)

* `SETUP_FUNCTION_UPGRADE_CONFIG` (value: `"SETUP_FUNCTION_UPGRADE_CONFIG"`)

* `ABORT_FUNCTION_UPGRADE` (value: `"ABORT_FUNCTION_UPGRADE"`)

* `COMMIT_FUNCTION_UPGRADE` (value: `"COMMIT_FUNCTION_UPGRADE"`)




