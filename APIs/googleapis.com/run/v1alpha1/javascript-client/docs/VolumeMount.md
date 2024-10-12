# CloudRunAdminApi.VolumeMount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mountPath** | **String** | Path within the container at which the volume should be mounted. Must not contain &#39;:&#39;. | [optional] 
**name** | **String** | The name of the volume. There must be a corresponding Volume with the same name. | [optional] 
**readOnly** | **Boolean** | (Optional) Only true is accepted. Defaults to true. | [optional] 
**subPath** | **String** | (Optional) Path within the volume from which the container&#39;s volume should be mounted. Defaults to \&quot;\&quot; (volume&#39;s root). | [optional] 


