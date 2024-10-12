# AzureDataMigrationServiceResourceProvider.ServicesList200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioningState** | **String** | The resource&#39;s provisioning state | [optional] [readonly] 
**publicKey** | **String** | The public key of the service, used to encrypt secrets sent to the service | [optional] 
**virtualSubnetId** | **String** | The ID of the Microsoft.Network/virtualNetworks/subnets resource to which the service should be joined | 



## Enum: ProvisioningStateEnum


* `Accepted` (value: `"Accepted"`)

* `Deleting` (value: `"Deleting"`)

* `Deploying` (value: `"Deploying"`)

* `Stopped` (value: `"Stopped"`)

* `Stopping` (value: `"Stopping"`)

* `Starting` (value: `"Starting"`)

* `FailedToStart` (value: `"FailedToStart"`)

* `FailedToStop` (value: `"FailedToStop"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




