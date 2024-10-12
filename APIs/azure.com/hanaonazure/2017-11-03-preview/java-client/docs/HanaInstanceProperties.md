

# HanaInstanceProperties

Describes the properties of a HANA instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hanaInstanceId** | **String** | Specifies the HANA instance unique ID. |  [optional] [readonly] |
|**hardwareProfile** | [**HardwareProfile**](HardwareProfile.md) |  |  [optional] |
|**hwRevision** | **String** | Hardware revision of a HANA instance |  [optional] [readonly] |
|**networkProfile** | [**NetworkProfile**](NetworkProfile.md) |  |  [optional] |
|**osProfile** | [**OSProfile**](OSProfile.md) |  |  [optional] |
|**partnerNodeId** | **String** | ARM ID of another HanaInstance that will share a network with this HanaInstance |  [optional] |
|**powerState** | [**PowerStateEnum**](#PowerStateEnum) | Resource power state |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | State of provisioning of the HanaInstance |  [optional] [readonly] |
|**proximityPlacementGroup** | **String** | Resource proximity placement group |  [optional] [readonly] |
|**storageProfile** | [**StorageProfile**](StorageProfile.md) |  |  [optional] |



## Enum: PowerStateEnum

| Name | Value |
|---- | -----|
| STARTING | &quot;starting&quot; |
| STARTED | &quot;started&quot; |
| STOPPING | &quot;stopping&quot; |
| STOPPED | &quot;stopped&quot; |
| RESTARTING | &quot;restarting&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| DELETING | &quot;Deleting&quot; |
| MIGRATING | &quot;Migrating&quot; |



