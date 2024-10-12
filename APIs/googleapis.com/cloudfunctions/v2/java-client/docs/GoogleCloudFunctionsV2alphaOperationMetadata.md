

# GoogleCloudFunctionsV2alphaOperationMetadata

Represents the metadata of the long-running operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | API version used to start the operation. |  [optional] |
|**cancelRequested** | **Boolean** | Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have google.longrunning.Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;. |  [optional] |
|**createTime** | **String** | The time the operation was created. |  [optional] |
|**endTime** | **String** | The time the operation finished running. |  [optional] |
|**operationType** | [**OperationTypeEnum**](#OperationTypeEnum) | The operation type. |  [optional] |
|**requestResource** | **Map&lt;String, Object&gt;** | The original request that started the operation. |  [optional] |
|**sourceToken** | **String** | An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments. |  [optional] |
|**stages** | [**List&lt;GoogleCloudFunctionsV2alphaStage&gt;**](GoogleCloudFunctionsV2alphaStage.md) | Mechanism for reporting in-progress stages |  [optional] |
|**statusDetail** | **String** | Human-readable status of the operation, if any. |  [optional] |
|**target** | **String** | Server-defined resource path for the target of the operation. |  [optional] |
|**verb** | **String** | Name of the verb executed by the operation. |  [optional] |



## Enum: OperationTypeEnum

| Name | Value |
|---- | -----|
| OPERATIONTYPE_UNSPECIFIED | &quot;OPERATIONTYPE_UNSPECIFIED&quot; |
| CREATE_FUNCTION | &quot;CREATE_FUNCTION&quot; |
| UPDATE_FUNCTION | &quot;UPDATE_FUNCTION&quot; |
| DELETE_FUNCTION | &quot;DELETE_FUNCTION&quot; |
| REDIRECT_FUNCTION_UPGRADE_TRAFFIC | &quot;REDIRECT_FUNCTION_UPGRADE_TRAFFIC&quot; |
| ROLLBACK_FUNCTION_UPGRADE_TRAFFIC | &quot;ROLLBACK_FUNCTION_UPGRADE_TRAFFIC&quot; |
| SETUP_FUNCTION_UPGRADE_CONFIG | &quot;SETUP_FUNCTION_UPGRADE_CONFIG&quot; |
| ABORT_FUNCTION_UPGRADE | &quot;ABORT_FUNCTION_UPGRADE&quot; |
| COMMIT_FUNCTION_UPGRADE | &quot;COMMIT_FUNCTION_UPGRADE&quot; |



