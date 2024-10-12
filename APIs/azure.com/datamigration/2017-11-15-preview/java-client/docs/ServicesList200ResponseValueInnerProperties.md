

# ServicesList200ResponseValueInnerProperties

Properties of the Data Migration service instance

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The resource&#39;s provisioning state |  [optional] [readonly] |
|**publicKey** | **String** | The public key of the service, used to encrypt secrets sent to the service |  [optional] |
|**virtualSubnetId** | **String** | The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| DELETING | &quot;Deleting&quot; |
| DEPLOYING | &quot;Deploying&quot; |
| STOPPED | &quot;Stopped&quot; |
| STOPPING | &quot;Stopping&quot; |
| STARTING | &quot;Starting&quot; |
| FAILED_TO_START | &quot;FailedToStart&quot; |
| FAILED_TO_STOP | &quot;FailedToStop&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |



