# CloudRunAdminApi.CSIVolumeSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **String** | name of the CSI driver for the requested storage system. Cloud Run supports the following drivers: * gcsfuse.run.googleapis.com : Mount a Cloud Storage Bucket as a volume. | [optional] 
**readOnly** | **Boolean** | If true, mount the volume as read only. Defaults to false. | [optional] 
**volumeAttributes** | **{String: String}** | stores driver specific attributes. For Google Cloud Storage volumes, the following attributes are supported: * bucketName: the name of the Cloud Storage bucket to mount. The Cloud Run Service identity must have access to this bucket. | [optional] 


