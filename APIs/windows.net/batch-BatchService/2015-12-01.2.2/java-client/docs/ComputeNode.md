

# ComputeNode

A compute node in the Batch service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affinityId** | **String** | Gets or sets an identifier which can be passed in the Add Task API to request that the task be scheduled close to this compute node. |  [optional] |
|**allocationTime** | **OffsetDateTime** | Gets or sets the time at which this compute node was allocated to the pool. |  [optional] |
|**certificateReferences** | [**List&lt;CertificateReference&gt;**](CertificateReference.md) | Gets or sets the list of certificates installed on the compute node. |  [optional] |
|**errors** | [**List&lt;ComputeNodeError&gt;**](ComputeNodeError.md) | Gets or sets the list of errors that are currently being encountered by the compute node. |  [optional] |
|**id** | **String** | Gets or sets the id of the compute node. |  [optional] |
|**ipAddress** | **String** | Gets or sets the IP address that other compute nodes can use to communicate with this compute node. |  [optional] |
|**lastBootTime** | **OffsetDateTime** | Gets or sets the time at which the compute node was started. |  [optional] |
|**recentTasks** | [**List&lt;TaskInformation&gt;**](TaskInformation.md) | Gets or sets the list of tasks that are currently running on the compute node. |  [optional] |
|**schedulingState** | [**SchedulingStateEnum**](#SchedulingStateEnum) | Gets or sets whether the compute node should be available for task scheduling. |  [optional] |
|**startTask** | [**StartTask**](StartTask.md) |  |  [optional] |
|**startTaskInfo** | [**StartTaskInformation**](StartTaskInformation.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the current state of the compute node. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the compute node entered its current state. |  [optional] |
|**totalTasksRun** | **Integer** | Gets or sets the total number of job tasks completed on the compute node. This includes Job Preparation, Job Release and Job Manager tasks, but not the pool start task. |  [optional] |
|**url** | **String** | Gets or sets the URL of the compute node. |  [optional] |
|**vmSize** | **String** | Gets or sets the size of the virtual machine hosting the compute node. |  [optional] |



## Enum: SchedulingStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| IDLE | &quot;idle&quot; |
| REBOOTING | &quot;rebooting&quot; |
| REIMAGING | &quot;reimaging&quot; |
| RUNNING | &quot;running&quot; |
| UNUSABLE | &quot;unusable&quot; |
| CREATING | &quot;creating&quot; |
| STARTING | &quot;starting&quot; |
| WAITINGFORSTARTTASK | &quot;waitingforstarttask&quot; |
| STARTTASKFAILED | &quot;starttaskfailed&quot; |
| UNKNOWN | &quot;unknown&quot; |
| LEAVINGPOOL | &quot;leavingpool&quot; |
| OFFLINE | &quot;offline&quot; |



