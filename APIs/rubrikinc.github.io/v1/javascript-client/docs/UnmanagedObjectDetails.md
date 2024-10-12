# RubrikRestApi.UnmanagedObjectDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveStorage** | **Number** | The amount of storage on the archival location used by unmanaged snapshots. | 
**hasSnapshotsWithPolicy** | **Boolean** | A boolean that specifies whether any of the snapshots for this object are being retained by a SLA Domain at any location.  | 
**id** | **String** |  | 
**isRemote** | **Boolean** | Boolean that specifies whether the object is remote or local. A value of true indicates that the object is remote.  | [optional] 
**localStorage** | **Number** | The amount of storage on the local cluster used by unmanaged snapshots. | 
**name** | **String** |  | 
**objectType** | **String** | The type of the unmanaged object. Valid object types are VirtualMachine, MssqlDatabase, LinuxFileset, ShareFileset, WindowsFileset, NutanixVirtualMachine, Ec2Instance and StorageArrayVolumeGroup. | 
**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  | [optional] 
**physicalLocation** | [**[LocationPathPoint]**](LocationPathPoint.md) | Summary information of all objects on the physical path to this object. | 
**recoveryInfo** | [**SnappableRecoveryInfo**](SnappableRecoveryInfo.md) |  | [optional] 
**retentionSlaDomainId** | **String** | ID assigned to an SLA Domain retention policy. | 
**retentionSlaDomainName** | **String** | Name of an SLA Domain retention policy. | 
**retentionSlaDomainPolarisManagedId** | **String** | Optional field with the ID assigned to an SLA Domain by Polaris. | [optional] 
**snapshotCount** | **Number** | Total number of snapshots to for the specified object. | 
**unmanagedStatus** | **String** | Unmanaged Status of this object. Protected means that this object is still protected by an SLA Policy. Unprotected means that this object has become unprotected. Relic means that Rubrik has lost contact with this object. | 



## Enum: ObjectTypeEnum


* `VirtualMachine` (value: `"VirtualMachine"`)

* `MssqlDatabase` (value: `"MssqlDatabase"`)

* `LinuxFileset` (value: `"LinuxFileset"`)

* `WindowsFileset` (value: `"WindowsFileset"`)

* `ShareFileset` (value: `"ShareFileset"`)

* `NutanixVirtualMachine` (value: `"NutanixVirtualMachine"`)

* `HypervVirtualMachine` (value: `"HypervVirtualMachine"`)

* `ManagedVolume` (value: `"ManagedVolume"`)

* `Ec2Instance` (value: `"Ec2Instance"`)

* `StorageArrayVolumeGroup` (value: `"StorageArrayVolumeGroup"`)

* `VcdVapp` (value: `"VcdVapp"`)

* `LinuxHost` (value: `"LinuxHost"`)

* `WindowsHost` (value: `"WindowsHost"`)

* `OracleDatabase` (value: `"OracleDatabase"`)

* `VolumeGroup` (value: `"VolumeGroup"`)

* `AppBlueprint` (value: `"AppBlueprint"`)





## Enum: UnmanagedStatusEnum


* `Protected` (value: `"Protected"`)

* `Relic` (value: `"Relic"`)

* `Unprotected` (value: `"Unprotected"`)

* `ReplicatedRelic` (value: `"ReplicatedRelic"`)

* `RemoteUnprotected` (value: `"RemoteUnprotected"`)




