

# BastionHostPropertiesFormat

Properties of the Bastion Host.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsName** | **String** | FQDN for the endpoint on which bastion host is accessible. |  [optional] |
|**ipConfigurations** | [**List&lt;BastionHostIPConfiguration&gt;**](BastionHostIPConfiguration.md) | IP configuration of the Bastion Host resource. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



