# RubrikRestApi.VolumeMountInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileSystemType** | [**FileSystemType**](FileSystemType.md) |  | 
**hostMountedPath** | **String** | The mount path of volume on the new host. | [optional] 
**id** | **String** | The unique ID of the mount. | 
**originalMountPoints** | **[String]** | The source host mount points of the specified volume. | 
**size** | **Number** | The size of the volume in bytes. | 
**smbPath** | **String** | The SMB path to the VHD file that contains the snapshot volume. This path is available when the mount is ready. | [optional] 


