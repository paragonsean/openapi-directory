# AnthosOnPremApi.OperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersion** | **String** | Output only. API version used to start the operation. | [optional] [readonly] 
**controlPlaneDisconnected** | **Boolean** | Output only. Denotes if the local managing cluster&#39;s control plane is currently disconnected. This is expected to occur temporarily during self-managed cluster upgrades. | [optional] [readonly] 
**createTime** | **String** | Output only. The time the operation was created. | [optional] [readonly] 
**endTime** | **String** | Output only. The time the operation finished running. | [optional] [readonly] 
**progress** | [**OperationProgress**](OperationProgress.md) |  | [optional] 
**requestedCancellation** | **Boolean** | Output only. Identifies whether the user has requested cancellation of the operation. Operations that have successfully been cancelled have [Operation.error] value with a [google.rpc.Status.code] of 1, corresponding to &#x60;Code.CANCELLED&#x60;. | [optional] [readonly] 
**statusMessage** | **String** | Output only. Human-readable status of the operation, if any. | [optional] [readonly] 
**target** | **String** | Output only. Server-defined resource path for the target of the operation. | [optional] [readonly] 
**type** | **String** | Output only. Type of operation being executed. | [optional] [readonly] 
**verb** | **String** | Output only. Name of the verb executed by the operation. | [optional] [readonly] 



## Enum: TypeEnum


* `OPERATION_TYPE_UNSPECIFIED` (value: `"OPERATION_TYPE_UNSPECIFIED"`)

* `CREATE` (value: `"CREATE"`)

* `DELETE` (value: `"DELETE"`)

* `UPDATE` (value: `"UPDATE"`)

* `UPGRADE` (value: `"UPGRADE"`)

* `PLATFORM_UPGRADE` (value: `"PLATFORM_UPGRADE"`)




