# BatchApi.AgentMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **String** | When the VM agent started. Use agent_startup_time instead. | [optional] 
**creator** | **String** | Full name of the entity that created this vm. For MIG, this path is: projects/{project}/regions/{region}/InstanceGroupManagers/{igm} The value is retrieved from the vm metadata key of \&quot;created-by\&quot;. | [optional] 
**imageVersion** | **String** | image version for the VM that this agent is installed on. | [optional] 
**instance** | **String** | GCP instance name (go/instance-name). | [optional] 
**instanceId** | **String** | GCP instance ID (go/instance-id). | [optional] 
**instancePreemptionNoticeReceived** | **Boolean** | If the GCP instance has received preemption notice. | [optional] 
**osRelease** | **{String: String}** | parsed contents of /etc/os-release | [optional] 
**version** | **String** | agent binary version running on VM | [optional] 
**zone** | **String** | Agent zone. | [optional] 


