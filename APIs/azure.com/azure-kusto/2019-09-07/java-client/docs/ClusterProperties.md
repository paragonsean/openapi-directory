

# ClusterProperties

Class representing the Kusto cluster properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataIngestionUri** | **String** | The cluster data ingestion URI. |  [optional] [readonly] |
|**enableDiskEncryption** | **Boolean** | A boolean value that indicates if the cluster&#39;s disks are encrypted. |  [optional] |
|**enableStreamingIngest** | **Boolean** | A boolean value that indicates if the streaming ingest is enabled. |  [optional] |
|**keyVaultProperties** | [**KeyVaultProperties**](KeyVaultProperties.md) |  |  [optional] |
|**optimizedAutoscale** | [**OptimizedAutoscale**](OptimizedAutoscale.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioned state of the resource. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The state of the resource. |  [optional] [readonly] |
|**trustedExternalTenants** | [**List&lt;TrustedExternalTenant&gt;**](TrustedExternalTenant.md) | The cluster&#39;s external tenants. |  [optional] |
|**uri** | **String** | The cluster URI. |  [optional] [readonly] |
|**virtualNetworkConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| MOVING | &quot;Moving&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UNAVAILABLE | &quot;Unavailable&quot; |
| RUNNING | &quot;Running&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |
| STOPPING | &quot;Stopping&quot; |
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| UPDATING | &quot;Updating&quot; |



