# AzureMachineLearningWorkspaces.AmlComputeNodeInformation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeId** | **String** | ID of the compute node. | [optional] [readonly] 
**nodeState** | **String** | State of the compute node. Values are idle, running, preparing, unusable, leaving and preempted. | [optional] [readonly] 
**port** | **Number** | SSH port number of the node. | [optional] [readonly] 
**privateIpAddress** | **String** | Private IP address of the compute node. | [optional] [readonly] 
**publicIpAddress** | **String** | Public IP address of the compute node. | [optional] [readonly] 
**runId** | **String** | ID of the Experiment running on the node, if any else null. | [optional] [readonly] 



## Enum: NodeStateEnum


* `idle` (value: `"idle"`)

* `running` (value: `"running"`)

* `preparing` (value: `"preparing"`)

* `unusable` (value: `"unusable"`)

* `leaving` (value: `"leaving"`)

* `preempted` (value: `"preempted"`)




