# KustoManagementClient.ClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataIngestionUri** | **String** | The cluster data ingestion URI. | [optional] [readonly] 
**provisioningState** | **String** | The provisioned state of the resource. | [optional] [readonly] 
**state** | **String** | The state of the resource. | [optional] [readonly] 
**trustedExternalTenants** | [**[TrustedExternalTenant]**](TrustedExternalTenant.md) | The cluster&#39;s external tenants. | [optional] 
**uri** | **String** | The cluster URI. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Running` (value: `"Running"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)





## Enum: StateEnum


* `Creating` (value: `"Creating"`)

* `Unavailable` (value: `"Unavailable"`)

* `Running` (value: `"Running"`)

* `Deleting` (value: `"Deleting"`)

* `Deleted` (value: `"Deleted"`)

* `Stopping` (value: `"Stopping"`)

* `Stopped` (value: `"Stopped"`)

* `Starting` (value: `"Starting"`)




