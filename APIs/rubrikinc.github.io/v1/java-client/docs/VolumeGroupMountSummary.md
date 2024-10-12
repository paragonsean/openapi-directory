

# VolumeGroupMountSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canUnmount** | **Boolean** | Indicates if the logged-in user has the authority to remove the specified mount. |  [optional] |
|**id** | **String** | The unique ID of the mount. |  |
|**isReady** | **Boolean** | Specifies whether the volume mount operation has successfully completed and is ready to use. |  |
|**mountRequestId** | **String** | The ID of the job instance that initiated the request for the specified mount. |  [optional] |
|**mountedDate** | **OffsetDateTime** | The UTC timestamp at which the mount was created. |  |
|**mountedVolumes** | [**List&lt;VolumeMountInfo&gt;**](VolumeMountInfo.md) | Configuration details for each of the mounted Volumes in the Volume Group. |  |
|**name** | **String** | The name of the Volume Group. |  |
|**restoreScriptSmbPath** | **String** | The link to the script that can perform bare-metal recovery for the mounted snapshot. |  [optional] |
|**snapshotDate** | **OffsetDateTime** | The UTC timestamp at which the snapshot was originally taken. |  |
|**snapshotSourceVersion** | **VolumeGroupReleaseVersion** |  |  |
|**sourceHostId** | **String** | The ID of the Host on which the snapshot was originally taken. |  |
|**sourceHostName** | **String** | The name of the Host on which the snapshot was originally taken. |  |
|**sourceVolumeGroupId** | **String** | The ID of the Volume Group from which this snapshot was created. |  |
|**targetHostId** | **String** | The ID of the host where the volumes are mounted. |  [optional] |
|**targetHostName** | **String** | The name of the host where the volumes are mounted. |  [optional] |
|**unmountRequestId** | **String** | The ID of the job instance that initiated the request to remove the specified mount. |  [optional] |



