# RubrikRestApi.HostHierarchyObjectSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | A user-specified string that returns this host in searches for host/share hierarchy objects. Only valid for host object. | [optional] 
**descendantCount** | [**HostHierarchyObjectDescendantCount**](HostHierarchyObjectDescendantCount.md) |  | 
**domain** | **String** | The share domain name. This value is only valid for host share objects. | [optional] 
**exportPoint** | **String** | The export point of host/share hierarchy objects. Only valid for share object. | [optional] 
**filesets** | [**[FilesetSummary]**](FilesetSummary.md) | Fileset summary for the host/share hierarchy object. Only valid for share object. | [optional] 
**hostId** | **String** | The host ID of host/share hierarchy objects. Only valid for share object. | [optional] 
**hostname** | **String** | The host name of host/share hierarchy objects. Only valid for share object. | [optional] 
**id** | **String** | ID assigned to the host/share hierarchy object. | 
**isChangeList** | **Boolean** | A Boolean that specifies whether ChangeList is enabled for the host/share hierarchy object. Only valid for share objects. | [optional] 
**isOnSnapMirrorDestVolume** | **Boolean** | Indicates if the NetApp SnapMirror destination volume includes the NAS share. Only valid for share objects. | [optional] 
**isSnapDiff** | **Boolean** | A Boolean that specifies whether SnapDiff is enabled for the host/share hierarchy object. Only valid for share objects. | [optional] 
**isilonChangelistEnabledDescendantCount** | **Number** | The number of host shares that have the Isilon Changelist feature enabled which improves incremental backup performance by tracking the difference between two snapshots, reducing the metadata scanning time during a backup job. This value is only valid for physical host objects. | [optional] 
**name** | **String** | The name of host/share hierarchy objects. Only valid for host object. | [optional] 
**nasBaseConfig** | [**NasBaseConfig**](NasBaseConfig.md) |  | [optional] 
**objectType** | [**HostObjectType**](HostObjectType.md) |  | 
**operatingSystem** | **String** | The operating system detailed information of host/share hierarchy objects. Only valid for physical host object. | [optional] 
**operatingSystemType** | **String** | The operating system type of host/share hierarchy objects. Only valid for physical host object. | [optional] 
**primaryClusterId** | **String** |  | 
**shareType** | **String** |  | [optional] 
**slaAssignment** | [**SlaAssignment**](SlaAssignment.md) |  | [optional] 
**snapDiffEnabledDescendantCount** | **Number** | The number of host shares that have enabled SnapDiff. This value is only valid for physical host objects. | [optional] 
**status** | **String** |  | 
**username** | **String** | The share user name. This value is only valid for host share objects. | [optional] 



## Enum: ShareTypeEnum


* `NFS` (value: `"NFS"`)

* `SMB` (value: `"SMB"`)




