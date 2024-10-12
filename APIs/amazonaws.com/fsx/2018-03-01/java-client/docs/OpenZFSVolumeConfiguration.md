

# OpenZFSVolumeConfiguration

The configuration of an Amazon FSx for OpenZFS volume.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parentVolumeId** | [**String**](String.md) |  |  [optional] |
|**volumePath** | [**String**](String.md) |  |  [optional] |
|**storageCapacityReservationGiB** | [**Integer**](Integer.md) |  |  [optional] |
|**storageCapacityQuotaGiB** | [**Integer**](Integer.md) |  |  [optional] |
|**recordSizeKiB** | [**Integer**](Integer.md) |  |  [optional] |
|**dataCompressionType** | [**OpenZFSDataCompressionType**](OpenZFSDataCompressionType.md) |  |  [optional] |
|**copyTagsToSnapshots** | [**Boolean**](Boolean.md) |  |  [optional] |
|**originSnapshot** | [**OpenZFSVolumeConfigurationOriginSnapshot**](OpenZFSVolumeConfigurationOriginSnapshot.md) |  |  [optional] |
|**readOnly** | [**Boolean**](Boolean.md) |  |  [optional] |
|**nfsExports** | [**List**](List.md) |  |  [optional] |
|**userAndGroupQuotas** | [**List**](List.md) |  |  [optional] |
|**restoreToSnapshot** | [**String**](String.md) |  |  [optional] |
|**deleteIntermediateSnaphots** | [**Boolean**](Boolean.md) |  |  [optional] |
|**deleteClonedVolumes** | [**Boolean**](Boolean.md) |  |  [optional] |



