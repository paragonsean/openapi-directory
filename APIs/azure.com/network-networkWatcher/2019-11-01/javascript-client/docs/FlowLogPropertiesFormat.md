# NetworkManagementClient.FlowLogPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Flag to enable/disable flow logging. | [optional] 
**flowAnalyticsConfiguration** | [**TrafficAnalyticsProperties**](TrafficAnalyticsProperties.md) |  | [optional] 
**format** | [**FlowLogFormatParameters**](FlowLogFormatParameters.md) |  | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**retentionPolicy** | [**RetentionPolicyParameters**](RetentionPolicyParameters.md) |  | [optional] 
**storageId** | **String** | ID of the storage account which is used to store the flow log. | 
**targetResourceGuid** | **String** | Guid of network security group to which flow log will be applied. | [optional] [readonly] 
**targetResourceId** | **String** | ID of network security group to which flow log will be applied. | 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




