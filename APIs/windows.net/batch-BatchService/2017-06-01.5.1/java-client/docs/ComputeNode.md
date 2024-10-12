

# ComputeNode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affinityId** | **String** | Note that this is just a soft affinity. If the target node is busy or unavailable at the time the task is scheduled, then the task will be scheduled elsewhere. |  [optional] |
|**allocationTime** | **OffsetDateTime** |  |  [optional] |
|**certificateReferences** | [**List&lt;CertificateReference&gt;**](CertificateReference.md) | For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. |  [optional] |
|**endpointConfiguration** | [**ComputeNodeEndpointConfiguration**](ComputeNodeEndpointConfiguration.md) |  |  [optional] |
|**errors** | [**List&lt;ComputeNodeError&gt;**](ComputeNodeError.md) |  |  [optional] |
|**id** | **String** | Every node that is added to a pool is assigned a unique ID. Whenever a node is removed from a pool, all of its local files are deleted, and the ID is reclaimed and could be reused for new nodes. |  [optional] |
|**ipAddress** | **String** | Every node that is added to a pool is assigned a unique IP address. Whenever a node is removed from a pool, all of its local files are deleted, and the IP address is reclaimed and could be reused for new nodes. |  [optional] |
|**isDedicated** | **Boolean** |  |  [optional] |
|**lastBootTime** | **OffsetDateTime** | This property may not be present if the node state is unusable. |  [optional] |
|**recentTasks** | [**List&lt;TaskInformation&gt;**](TaskInformation.md) | This property is present only if at least one task has run on this node since it was assigned to the pool. |  [optional] |
|**runningTasksCount** | **Integer** |  |  [optional] |
|**schedulingState** | [**SchedulingStateEnum**](#SchedulingStateEnum) | Values are:   enabled - Tasks can be scheduled on the node.  disabled - No new tasks will be scheduled on the node. Tasks already running on the node may still run to completion. All nodes start with scheduling enabled. |  [optional] |
|**startTask** | [**StartTask**](StartTask.md) |  |  [optional] |
|**startTaskInfo** | [**StartTaskInformation**](StartTaskInformation.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Values are:   idle - The node is not currently running a task.  rebooting - The node is rebooting.  reimaging - The node is reimaging.  running - The node is running one or more tasks (other than a start task).  unusable - The node cannot be used for task execution due to errors.  creating - The Batch service has obtained the underlying virtual machine from Azure Compute, but it has not yet started to join the pool.  starting - the Batch service is starting on the underlying virtual machine.  waitingforstarttask - The start task has started running on the compute node, but waitForSuccess is set and the start task has not yet completed.  starttaskfailed - The start task has failed on the compute node (and exhausted all retries), and waitForSuccess is set. The node is not usable for running tasks.  unknown - The Batch service has lost contact with the node, and does not know its true state.  leavingpool - The node is leaving the pool, either because the user explicitly removed it or because the pool is resizing or autoscaling down.  offline - The node is not currently running a task, and scheduling of new tasks to the node is disabled.  preempted - The low-priority node has been preempted. Tasks which were running on the node when it was preempted will be rescheduled when another node becomes available. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** |  |  [optional] |
|**totalTasksRun** | **Integer** |  |  [optional] |
|**totalTasksSucceeded** | **Integer** |  |  [optional] |
|**url** | **String** |  |  [optional] |
|**vmSize** | **String** | For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall, A1V2 and A2V2. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series). |  [optional] |



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
| WAITING_FOR_START_TASK | &quot;waitingForStartTask&quot; |
| START_TASK_FAILED | &quot;startTaskFailed&quot; |
| UNKNOWN | &quot;unknown&quot; |
| LEAVING_POOL | &quot;leavingPool&quot; |
| OFFLINE | &quot;offline&quot; |
| PREEMPTED | &quot;preempted&quot; |



