

# ClusterProperties

Class representing the Kusto cluster properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataIngestionUri** | **String** | The cluster data ingestion URI. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioned state of the resource. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The state of the resource. |  [optional] [readonly] |
|**trustedExternalTenants** | [**List&lt;TrustedExternalTenant&gt;**](TrustedExternalTenant.md) | The cluster&#39;s external tenants. |  [optional] |
|**uri** | **String** | The cluster URI. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |



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



