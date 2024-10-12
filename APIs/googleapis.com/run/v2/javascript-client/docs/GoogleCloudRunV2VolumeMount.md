# CloudRunAdminApi.GoogleCloudRunV2VolumeMount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mountPath** | **String** | Required. Path within the container at which the volume should be mounted. Must not contain &#39;:&#39;. For Cloud SQL volumes, it can be left empty, or must otherwise be &#x60;/cloudsql&#x60;. All instances defined in the Volume will be available as &#x60;/cloudsql/[instance]&#x60;. For more information on Cloud SQL volumes, visit https://cloud.google.com/sql/docs/mysql/connect-run | [optional] 
**name** | **String** | Required. This must match the Name of a Volume. | [optional] 


