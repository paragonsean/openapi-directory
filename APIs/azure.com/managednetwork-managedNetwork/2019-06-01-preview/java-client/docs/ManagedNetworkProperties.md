

# ManagedNetworkProperties

Properties of Managed Network

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectivity** | [**ConnectivityCollection**](ConnectivityCollection.md) |  |  [optional] |
|**scope** | [**Scope**](Scope.md) |  |  [optional] |
|**etag** | **String** | A unique read-only string that changes whenever the resource is updated. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the ManagedNetwork resource. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



