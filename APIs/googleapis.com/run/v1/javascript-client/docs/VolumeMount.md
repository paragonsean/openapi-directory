# CloudRunAdminApi.VolumeMount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mountPath** | **String** | Required. Path within the container at which the volume should be mounted. Must not contain &#39;:&#39;. | [optional] 
**name** | **String** | Required. The name of the volume. There must be a corresponding Volume with the same name. | [optional] 
**readOnly** | **Boolean** | Sets the mount to be read-only or read-write. Not used by Cloud Run. | [optional] 
**subPath** | **String** | Path within the volume from which the container&#39;s volume should be mounted. Defaults to \&quot;\&quot; (volume&#39;s root). | [optional] 


