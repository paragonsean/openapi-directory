

# UnmanagedObjectSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveStorage** | **Long** | Storage being taken up in the archival location by unmanaged snapshots. |  |
|**autoSnapshotCount** | **Long** | Number of policy-based snapshots to retain for the specified object. |  |
|**hasSnapshotsWithPolicy** | **Boolean** | A boolean that specifies whether any of the snapshots for this object are being retained by a SLA  at any location.  |  |
|**id** | **String** |  |  |
|**isRemote** | **Boolean** | A boolean that specifies if the object is remote or local. When this value is true, the object is remote. |  [optional] |
|**localStorage** | **Long** | Storage being taken up on the local cluster by unmanaged snapshots. |  |
|**manualSnapshotCount** | **Long** | Number of on-demand snapshots and snapshots retrieved from an archival location for specified object. |  |
|**name** | **String** |  |  |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | The type of the unmanaged object. This may be VirtualMachine, MssqlDatabase, LinuxFileset, ShareFileset, WindowsFileset, NutanixVirtualMachine, Ec2Instance or StorageArrayVolumeGroup. |  |
|**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  |  [optional] |
|**physicalLocation** | [**List&lt;LocationPathPoint&gt;**](LocationPathPoint.md) | Brief info of all the objects in the physical path to this Object. |  |
|**recoveryInfo** | [**SnappableRecoveryInfo**](SnappableRecoveryInfo.md) |  |  [optional] |
|**retentionSlaDomainId** | **String** | ID assigned to an SLA retention policy. |  |
|**retentionSlaDomainName** | **String** | Name of an SLA retention policy. |  |
|**retentionSlaDomainPolarisManagedId** | **String** | Optional field with the ID assigned to an SLA Domain by Polaris. |  [optional] |
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



