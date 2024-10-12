# NetworkManagementClient.BastionHostPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsName** | **String** | FQDN for the endpoint on which bastion host is accessible. | [optional] 
**ipConfigurations** | [**[BastionHostIPConfiguration]**](BastionHostIPConfiguration.md) | IP configuration of the Bastion Host resource. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




