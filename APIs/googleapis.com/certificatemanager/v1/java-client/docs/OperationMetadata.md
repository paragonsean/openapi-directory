

# OperationMetadata

Represents the metadata of the long-running operation. Output only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | API version used to start the operation. |  [optional] |
|**createTime** | **String** | The time the operation was created. |  [optional] |
|**endTime** | **String** | The time the operation finished running. |  [optional] |
|**requestedCancellation** | **Boolean** | Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have Operation.error value with a google.rpc.Status.code of 1, corresponding to &#x60;Code.CANCELLED&#x60;. |  [optional] |
|**statusMessage** | **String** | Human-readable status of the operation, if any. |  [optional] |
|**target** | **String** | Server-defined resource path for the target of the operation. |  [optional] |
|**verb** | **String** | Name of the verb executed by the operation. |  [optional] |



