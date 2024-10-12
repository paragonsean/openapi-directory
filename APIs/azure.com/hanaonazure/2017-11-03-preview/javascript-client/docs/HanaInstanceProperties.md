# HanaManagementClient.HanaInstanceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hanaInstanceId** | **String** | Specifies the HANA instance unique ID. | [optional] [readonly] 
**hardwareProfile** | [**HardwareProfile**](HardwareProfile.md) |  | [optional] 
**hwRevision** | **String** | Hardware revision of a HANA instance | [optional] [readonly] 
**networkProfile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**osProfile** | [**OSProfile**](OSProfile.md) |  | [optional] 
**partnerNodeId** | **String** | ARM ID of another HanaInstance that will share a network with this HanaInstance | [optional] 
**powerState** | **String** | Resource power state | [optional] [readonly] 
**provisioningState** | **String** | State of provisioning of the HanaInstance | [optional] [readonly] 
**proximityPlacementGroup** | **String** | Resource proximity placement group | [optional] [readonly] 
**storageProfile** | [**StorageProfile**](StorageProfile.md) |  | [optional] 



## Enum: PowerStateEnum


* `starting` (value: `"starting"`)

* `started` (value: `"started"`)

* `stopping` (value: `"stopping"`)

* `stopped` (value: `"stopped"`)

* `restarting` (value: `"restarting"`)

* `unknown` (value: `"unknown"`)





## Enum: ProvisioningStateEnum


* `Accepted` (value: `"Accepted"`)

* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)

* `Deleting` (value: `"Deleting"`)

* `Migrating` (value: `"Migrating"`)




