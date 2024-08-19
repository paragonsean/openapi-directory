# KustoManagementClient.ClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataIngestionUri** | **String** | The cluster data ingestion URI. | [optional] [readonly] 
**enableDiskEncryption** | **Boolean** | A boolean value that indicates if the cluster&#39;s disks are encrypted. | [optional] 
**enableStreamingIngest** | **Boolean** | A boolean value that indicates if the streaming ingest is enabled. | [optional] [default to false]
**keyVaultProperties** | [**KeyVaultProperties**](KeyVaultProperties.md) |  | [optional] 
**optimizedAutoscale** | [**OptimizedAutoscale**](OptimizedAutoscale.md) |  | [optional] 
**provisioningState** | **String** | The provisioned state of the resource. | [optional] [readonly] 
**state** | **String** | The state of the resource. | [optional] [readonly] 
**trustedExternalTenants** | [**[TrustedExternalTenant]**](TrustedExternalTenant.md) | The cluster&#39;s external tenants. | [optional] 
**uri** | **String** | The cluster URI. | [optional] [readonly] 
**virtualNetworkConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Running` (value: `"Running"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Moving` (value: `"Moving"`)





## Enum: StateEnum


* `Creating` (value: `"Creating"`)

* `Unavailable` (value: `"Unavailable"`)

* `Running` (value: `"Running"`)

* `Deleting` (value: `"Deleting"`)

* `Deleted` (value: `"Deleted"`)

* `Stopping` (value: `"Stopping"`)

* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)

* `Updating` (value: `"Updating"`)




