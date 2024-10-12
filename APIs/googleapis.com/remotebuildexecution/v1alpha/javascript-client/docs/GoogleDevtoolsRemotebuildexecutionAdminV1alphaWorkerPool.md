# RemoteBuildExecutionApi.GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscale** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaAutoscale.md) |  | [optional] 
**channel** | **String** | Channel specifies the release channel of the pool. | [optional] 
**hostOs** | **String** | HostOS specifies the OS version of the image for the worker VMs. | [optional] 
**name** | **String** | WorkerPool resource name formatted as: &#x60;projects/[PROJECT_ID]/instances/[INSTANCE_ID]/workerpools/[POOL_ID]&#x60;. name should not be populated when creating a worker pool since it is provided in the &#x60;poolId&#x60; field. | [optional] 
**state** | **String** | Output only. State of the worker pool. | [optional] 
**workerConfig** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig.md) |  | [optional] 
**workerCount** | **String** | The desired number of workers in the worker pool. Must be a value between 0 and 15000. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `RUNNING` (value: `"RUNNING"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `INACTIVE` (value: `"INACTIVE"`)




