

# HostVolumeSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileSystemType** | **FileSystemType** |  |  |
|**id** | **String** | The unique ID of the snapshot volume summary. |  |
|**mountPoints** | **List&lt;String&gt;** | The mount points of the volume on the host. |  |
|**size** | **Long** | The size of the volume in bytes. |  |
|**isCurrentlyPresentOnSystem** | **Boolean** | Indicates whether a volume is present on the host. When &#39;true&#39;, the volume is present. When &#39;false&#39;, the volume is not present. Volumes that are not present on the host are still included in snapshots and trigger warnings until the missing volumes are excluded from snapshots. |  |
|**naturalId** | **String** | The unique ID of the volume on the Windows host. |  |
|**volumeGroupId** | **String** | The unique ID of the Volume Group. |  [optional] |



