# BatchService.ComputeNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityId** | **String** | Gets or sets an identifier which can be passed in the Add Task API to request that the task be scheduled close to this compute node. | [optional] 
**allocationTime** | **Date** | Gets or sets the time at which this compute node was allocated to the pool. | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | Gets or sets the list of certificates installed on the compute node. | [optional] 
**errors** | [**[ComputeNodeError]**](ComputeNodeError.md) | Gets or sets the list of errors that are currently being encountered by the compute node. | [optional] 
**id** | **String** | Gets or sets the id of the compute node. | [optional] 
**ipAddress** | **String** | Gets or sets the IP address that other compute nodes can use to communicate with this compute node. | [optional] 
**lastBootTime** | **Date** | Gets or sets the time at which the compute node was started. | [optional] 
**recentTasks** | [**[TaskInformation]**](TaskInformation.md) | Gets or sets the list of tasks that are currently running on the compute node. | [optional] 
**schedulingState** | **String** | Gets or sets whether the compute node should be available for task scheduling. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**startTaskInfo** | [**StartTaskInformation**](StartTaskInformation.md) |  | [optional] 
**state** | **String** | Gets or sets the current state of the compute node. | [optional] 
**stateTransitionTime** | **Date** | Gets or sets the time at which the compute node entered its current state. | [optional] 
**totalTasksRun** | **Number** | Gets or sets the total number of job tasks completed on the compute node. This includes Job Preparation, Job Release and Job Manager tasks, but not the pool start task. | [optional] 
**url** | **String** | Gets or sets the URL of the compute node. | [optional] 
**vmSize** | **String** | Gets or sets the size of the virtual machine hosting the compute node. | [optional] 



## Enum: SchedulingStateEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)





## Enum: StateEnum


* `idle` (value: `"idle"`)

* `rebooting` (value: `"rebooting"`)

* `reimaging` (value: `"reimaging"`)

* `running` (value: `"running"`)

* `unusable` (value: `"unusable"`)

* `creating` (value: `"creating"`)

* `starting` (value: `"starting"`)

* `waitingforstarttask` (value: `"waitingforstarttask"`)

* `starttaskfailed` (value: `"starttaskfailed"`)

* `unknown` (value: `"unknown"`)

* `leavingpool` (value: `"leavingpool"`)

* `offline` (value: `"offline"`)




