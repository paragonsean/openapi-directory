# CloudComposerApi.LoadSnapshotRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skipAirflowOverridesSetting** | **Boolean** | Whether or not to skip setting Airflow overrides when loading the environment&#39;s state. | [optional] 
**skipEnvironmentVariablesSetting** | **Boolean** | Whether or not to skip setting environment variables when loading the environment&#39;s state. | [optional] 
**skipGcsDataCopying** | **Boolean** | Whether or not to skip copying Cloud Storage data when loading the environment&#39;s state. | [optional] 
**skipPypiPackagesInstallation** | **Boolean** | Whether or not to skip installing Pypi packages when loading the environment&#39;s state. | [optional] 
**snapshotPath** | **String** | A Cloud Storage path to a snapshot to load, e.g.: \&quot;gs://my-bucket/snapshots/project_location_environment_timestamp\&quot;. | [optional] 


