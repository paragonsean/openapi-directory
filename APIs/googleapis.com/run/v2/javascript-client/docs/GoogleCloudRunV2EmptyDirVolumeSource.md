# CloudRunAdminApi.GoogleCloudRunV2EmptyDirVolumeSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**medium** | **String** | The medium on which the data is stored. Acceptable values today is only MEMORY or none. When none, the default will currently be backed by memory but could change over time. +optional | [optional] 
**sizeLimit** | **String** | Limit on the storage usable by this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers. The default is nil which means that the limit is undefined. More info: https://cloud.google.com/run/docs/configuring/in-memory-volumes#configure-volume. Info in Kubernetes: https://kubernetes.io/docs/concepts/storage/volumes/#emptydir | [optional] 



## Enum: MediumEnum


* `MEDIUM_UNSPECIFIED` (value: `"MEDIUM_UNSPECIFIED"`)

* `MEMORY` (value: `"MEMORY"`)




