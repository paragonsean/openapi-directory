

# ManagedNetworkGroupProperties

Properties of a Managed Network Group

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managementGroups** | [**List&lt;ResourceId&gt;**](ResourceId.md) | The collection of management groups covered by the Managed Network |  [optional] |
|**subnets** | [**List&lt;ResourceId&gt;**](ResourceId.md) | The collection of  subnets covered by the Managed Network |  [optional] |
|**subscriptions** | [**List&lt;ResourceId&gt;**](ResourceId.md) | The collection of subscriptions covered by the Managed Network |  [optional] |
|**virtualNetworks** | [**List&lt;ResourceId&gt;**](ResourceId.md) | The collection of virtual nets covered by the Managed Network |  [optional] |
|**etag** | **String** | A unique read-only string that changes whenever the resource is updated. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the ManagedNetwork resource. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



