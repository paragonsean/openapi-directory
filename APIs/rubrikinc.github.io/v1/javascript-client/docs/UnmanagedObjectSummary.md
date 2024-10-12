# RubrikRestApi.UnmanagedObjectSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveStorage** | **Number** | Storage being taken up in the archival location by unmanaged snapshots. | 
**autoSnapshotCount** | **Number** | Number of policy-based snapshots to retain for the specified object. | 
**hasSnapshotsWithPolicy** | **Boolean** | A boolean that specifies whether any of the snapshots for this object are being retained by a SLA  at any location.  | 
**id** | **String** |  | 
**isRemote** | **Boolean** | A boolean that specifies if the object is remote or local. When this value is true, the object is remote. | [optional] 
**localStorage** | **Number** | Storage being taken up on the local cluster by unmanaged snapshots. | 
**manualSnapshotCount** | **Number** | Number of on-demand snapshots and snapshots retrieved from an archival location for specified object. | 
**name** | **String** |  | 
**objectType** | **String** | The type of the unmanaged object. This may be VirtualMachine, MssqlDatabase, LinuxFileset, ShareFileset, WindowsFileset, NutanixVirtualMachine, Ec2Instance or StorageArrayVolumeGroup. | 
**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  | [optional] 
**physicalLocation** | [**[LocationPathPoint]**](LocationPathPoint.md) | Brief info of all the objects in the physical path to this Object. | 
**recoveryInfo** | [**SnappableRecoveryInfo**](SnappableRecoveryInfo.md) |  | [optional] 
**retentionSlaDomainId** | **String** | ID assigned to an SLA retention policy. | 
**retentionSlaDomainName** | **String** | Name of an SLA retention policy. | 
**retentionSlaDomainPolarisManagedId** | **String** | Optional field with the ID assigned to an SLA Domain by Polaris. | [optional] 
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




