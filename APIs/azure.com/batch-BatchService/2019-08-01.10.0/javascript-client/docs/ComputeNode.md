# BatchService.ComputeNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinityId** | **String** | Note that this is just a soft affinity. If the target Compute Node is busy or unavailable at the time the Task is scheduled, then the Task will be scheduled elsewhere. | [optional] 
**allocationTime** | **Date** | This is the time when the Compute Node was initially allocated and doesn&#39;t change once set. It is not updated when the Compute Node is service healed or preempted. | [optional] 
**certificateReferences** | [**[CertificateReference]**](CertificateReference.md) | For Windows Nodes, the Batch service installs the Certificates to the specified Certificate store and location. For Linux Compute Nodes, the Certificates are stored in a directory inside the Task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the Task to query for this location. For Certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and Certificates are placed in that directory. | [optional] 
**endpointConfiguration** | [**ComputeNodeEndpointConfiguration**](ComputeNodeEndpointConfiguration.md) |  | [optional] 
**errors** | [**[ComputeNodeError]**](ComputeNodeError.md) |  | [optional] 
**id** | **String** | Every Compute Node that is added to a Pool is assigned a unique ID. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the ID is reclaimed and could be reused for new Compute Nodes. | [optional] 
**ipAddress** | **String** | Every Compute Node that is added to a Pool is assigned a unique IP address. Whenever a Compute Node is removed from a Pool, all of its local files are deleted, and the IP address is reclaimed and could be reused for new Compute Nodes. | [optional] 
**isDedicated** | **Boolean** |  | [optional] 
**lastBootTime** | **Date** | This property may not be present if the Compute Node state is unusable. | [optional] 
**nodeAgentInfo** | [**NodeAgentInformation**](NodeAgentInformation.md) |  | [optional] 
**recentTasks** | [**[TaskInformation]**](TaskInformation.md) | This property is present only if at least one Task has run on this Compute Node since it was assigned to the Pool. | [optional] 
**runningTasksCount** | **Number** |  | [optional] 
**schedulingState** | **String** |  | [optional] 
**startTask** | [**StartTask**](StartTask.md) |  | [optional] 
**startTaskInfo** | [**StartTaskInformation**](StartTaskInformation.md) |  | [optional] 
**state** | **String** | The low-priority Compute Node has been preempted. Tasks which were running on the Compute Node when it was preempted will be rescheduled when another Compute Node becomes available. | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**totalTasksRun** | **Number** |  | [optional] 
**totalTasksSucceeded** | **Number** |  | [optional] 
**url** | **String** |  | [optional] 
**vmSize** | **String** | For information about available sizes of virtual machines in Pools, see Choose a VM size for Compute Nodes in an Azure Batch Pool (https://docs.microsoft.com/azure/batch/batch-pool-vm-sizes). | [optional] 



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

* `preempted` (value: `"preempted"`)




