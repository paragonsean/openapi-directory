

# GoogleCloudRunV2EmptyDirVolumeSource

In memory (tmpfs) ephemeral storage. It is ephemeral in the sense that when the sandbox is taken down, the data is destroyed with it (it does not persist across sandbox runs).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**medium** | [**MediumEnum**](#MediumEnum) | The medium on which the data is stored. Acceptable values today is only MEMORY or none. When none, the default will currently be backed by memory but could change over time. +optional |  [optional] |
|**sizeLimit** | **String** | Limit on the storage usable by this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers. The default is nil which means that the limit is undefined. More info: https://cloud.google.com/run/docs/configuring/in-memory-volumes#configure-volume. Info in Kubernetes: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir |  [optional] |



## Enum: MediumEnum

| Name | Value |
|---- | -----|
| MEDIUM_UNSPECIFIED | &quot;MEDIUM_UNSPECIFIED&quot; |
| MEMORY | &quot;MEMORY&quot; |



