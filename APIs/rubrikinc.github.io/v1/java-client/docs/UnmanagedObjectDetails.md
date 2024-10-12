

# UnmanagedObjectDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveStorage** | **Long** | The amount of storage on the archival location used by unmanaged snapshots. |  |
|**hasSnapshotsWithPolicy** | **Boolean** | A boolean that specifies whether any of the snapshots for this object are being retained by a SLA Domain at any location.  |  |
|**id** | **String** |  |  |
|**isRemote** | **Boolean** | Boolean that specifies whether the object is remote or local. A value of true indicates that the object is remote.  |  [optional] |
|**localStorage** | **Long** | The amount of storage on the local cluster used by unmanaged snapshots. |  |
|**name** | **String** |  |  |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | The type of the unmanaged object. Valid object types are VirtualMachine, MssqlDatabase, LinuxFileset, ShareFileset, WindowsFileset, NutanixVirtualMachine, Ec2Instance and StorageArrayVolumeGroup. |  |
|**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  |  [optional] |
|**physicalLocation** | [**List&lt;LocationPathPoint&gt;**](LocationPathPoint.md) | Summary information of all objects on the physical path to this object. |  |
|**recoveryInfo** | [**SnappableRecoveryInfo**](SnappableRecoveryInfo.md) |  |  [optional] |
|**retentionSlaDomainId** | **String** | ID assigned to an SLA Domain retention policy. |  |
|**retentionSlaDomainName** | **String** | Name of an SLA Domain retention policy. |  |
|**retentionSlaDomainPolarisManagedId** | **String** | Optional field with the ID assigned to an SLA Domain by Polaris. |  [optional] |
|**snapshotCount** | **Long** | Total number of snapshots to for the specified object. |  |
|**unmanagedStatus** | [**UnmanagedStatusEnum**](#UnmanagedStatusEnum) | Unmanaged Status of this object. Protected means that this object is still protected by an SLA Policy. Unprotected means that this object has become unprotected. Relic means that Rubrik has lost contact with this object. |  |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| VIRTUAL_MACHINE | &quot;VirtualMachine&quot; |
| MSSQL_DATABASE | &quot;MssqlDatabase&quot; |
| LINUX_FILESET | &quot;LinuxFileset&quot; |
| WINDOWS_FILESET | &quot;WindowsFileset&quot; |
| SHARE_FILESET | &quot;ShareFileset&quot; |
| NUTANIX_VIRTUAL_MACHINE | &quot;NutanixVirtualMachine&quot; |
| HYPERV_VIRTUAL_MACHINE | &quot;HypervVirtualMachine&quot; |
| MANAGED_VOLUME | &quot;ManagedVolume&quot; |
| EC2_INSTANCE | &quot;Ec2Instance&quot; |
| STORAGE_ARRAY_VOLUME_GROUP | &quot;StorageArrayVolumeGroup&quot; |
| VCD_VAPP | &quot;VcdVapp&quot; |
| LINUX_HOST | &quot;LinuxHost&quot; |
| WINDOWS_HOST | &quot;WindowsHost&quot; |
| ORACLE_DATABASE | &quot;OracleDatabase&quot; |
| VOLUME_GROUP | &quot;VolumeGroup&quot; |
| APP_BLUEPRINT | &quot;AppBlueprint&quot; |



## Enum: UnmanagedStatusEnum

| Name | Value |
|---- | -----|
| PROTECTED | &quot;Protected&quot; |
| RELIC | &quot;Relic&quot; |
| UNPROTECTED | &quot;Unprotected&quot; |
| REPLICATED_RELIC | &quot;ReplicatedRelic&quot; |
| REMOTE_UNPROTECTED | &quot;RemoteUnprotected&quot; |



