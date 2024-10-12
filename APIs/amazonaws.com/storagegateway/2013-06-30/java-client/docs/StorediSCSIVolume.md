

# StorediSCSIVolume

Describes an iSCSI stored volume.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**volumeARN** | [**String**](String.md) |  |  [optional] |
|**volumeId** | [**String**](String.md) |  |  [optional] |
|**volumeType** | [**String**](String.md) |  |  [optional] |
|**volumeStatus** | [**String**](String.md) |  |  [optional] |
|**volumeAttachmentStatus** | [**String**](String.md) |  |  [optional] |
|**volumeSizeInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**volumeProgress** | [**Double**](Double.md) |  |  [optional] |
|**volumeDiskId** | [**String**](String.md) |  |  [optional] |
|**sourceSnapshotId** | [**String**](String.md) |  |  [optional] |
|**preservedExistingData** | [**Boolean**](Boolean.md) |  |  [optional] |
|**volumeiSCSIAttributes** | [**CachediSCSIVolumeVolumeiSCSIAttributes**](CachediSCSIVolumeVolumeiSCSIAttributes.md) |  |  [optional] |
|**createdDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**volumeUsedInBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**kmSKey** | **String** | The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when &lt;code&gt;KMSEncrypted&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. Optional. |  [optional] |
|**targetName** | [**String**](String.md) |  |  [optional] |



