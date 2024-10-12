

# NFSVolumeSource

Represents a persistent volume that will be mounted using NFS. This volume will be shared between all instances of the Service and data will not be deleted when the instance is shut down.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** | Path that is exported by the NFS server. |  [optional] |
|**readOnly** | **Boolean** | If true, mount the NFS volume as read only. Defaults to false. |  [optional] |
|**server** | **String** | Hostname or IP address of the NFS server. |  [optional] |



