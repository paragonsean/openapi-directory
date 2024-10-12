# AwsStorageGateway.CachediSCSIVolume

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumeARN** | **String** |  | [optional] 
**volumeId** | **String** |  | [optional] 
**volumeType** | **String** |  | [optional] 
**volumeStatus** | **String** |  | [optional] 
**volumeAttachmentStatus** | **String** |  | [optional] 
**volumeSizeInBytes** | **Number** |  | [optional] 
**volumeProgress** | **Number** |  | [optional] 
**sourceSnapshotId** | **String** |  | [optional] 
**volumeiSCSIAttributes** | [**CachediSCSIVolumeVolumeiSCSIAttributes**](CachediSCSIVolumeVolumeiSCSIAttributes.md) |  | [optional] 
**createdDate** | **Date** |  | [optional] 
**volumeUsedInBytes** | **Number** |  | [optional] 
**kMSKey** | **String** | The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when &lt;code&gt;KMSEncrypted&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. Optional. | [optional] 
**targetName** | **String** |  | [optional] 


