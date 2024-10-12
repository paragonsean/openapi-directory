

# ClusterProperties

Cluster properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterId** | **String** | The ID associated with the cluster. |  [optional] [readonly] |
|**encryptionKeyUri** | **String** | The Key Vault key or certificate path associated with the Log Analytics cluster. |  [optional] |
|**nextLink** | **String** | The link used to get the next page of recommendations. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the cluster. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| DELETING | &quot;Deleting&quot; |
| PROVISIONING_ACCOUNT | &quot;ProvisioningAccount&quot; |



