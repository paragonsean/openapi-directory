

# Volume

Volume represents a named volume in a container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configMap** | [**ConfigMapVolumeSource**](ConfigMapVolumeSource.md) |  |  [optional] |
|**csi** | [**CSIVolumeSource**](CSIVolumeSource.md) |  |  [optional] |
|**emptyDir** | [**EmptyDirVolumeSource**](EmptyDirVolumeSource.md) |  |  [optional] |
|**name** | **String** | Volume&#39;s name. In Cloud Run Fully Managed, the name &#39;cloudsql&#39; is reserved. |  [optional] |
|**nfs** | [**NFSVolumeSource**](NFSVolumeSource.md) |  |  [optional] |
|**secret** | [**SecretVolumeSource**](SecretVolumeSource.md) |  |  [optional] |



