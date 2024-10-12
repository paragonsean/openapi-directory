# BatchService.ComputeNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityId** | **String** |  | [optional] 
**allocationTime** | **Date** |  | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | For Windows compute nodes, the Batch service installs the certificates to the specified certificate store and location. For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. | [optional] 
**errors** | [**[ComputeNodeError]**](ComputeNodeError.md) |  | [optional] 
**id** | **String** | Every node that is added to a pool is assigned a unique ID. Whenever a node is removed from a pool, all of its local files are deleted, and the ID is reclaimed and could be reused for new nodes. | [optional] 
**ipAddress** | **String** | Every node that is added to a pool is assigned a unique IP address. Whenever a node is removed from a pool, all of its local files are deleted, and the IP address is reclaimed and could be reused for new nodes. | [optional] 
**isDedicated** | **Boolean** |  | [optional] 
**lastBootTime** | **Date** | This property may not be present if the node state is unusable. | [optional] 
**recentTasks** | [**[TaskInformation]**](TaskInformation.md) |  | [optional] 
**runningTasksCount** | **Number** |  | [optional] 
**schedulingState** | **String** | enabled - Tasks can be scheduled on the node. disabled - No new tasks will be scheduled on the node. Tasks already running on the node may still run to completion. All nodes start with scheduling enabled. | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**startTaskInfo** | [**StartTaskInformation**](StartTaskInformation.md) |  | [optional] 
**state** | **String** |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**totalTasksRun** | **Number** |  | [optional] 
**totalTasksSucceeded** | **Number** |  | [optional] 
**url** | **String** |  | [optional] 
**vmSize** | **String** | For information about available sizes of virtual machines for Cloud Services pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall, A1V2 and A2V2. For information about available VM sizes for pools using images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series). | [optional] 



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

* `waitingForStartTask` (value: `"waitingForStartTask"`)

* `startTaskFailed` (value: `"startTaskFailed"`)

* `unknown` (value: `"unknown"`)

* `leavingPool` (value: `"leavingPool"`)

* `offline` (value: `"offline"`)

* `preempted` (value: `"preempted"`)




