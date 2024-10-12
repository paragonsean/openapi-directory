# GkeHubApi.ConfigManagementOciConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcpServiceAccountEmail** | **String** | The Google Cloud Service Account Email used for auth when secret_type is gcpServiceAccount. | [optional] 
**policyDir** | **String** | The absolute path of the directory that contains the local resources. Default: the root directory of the image. | [optional] 
**secretType** | **String** | Type of secret configured for access to the Git repo. | [optional] 
**syncRepo** | **String** | The OCI image repository URL for the package to sync from. e.g. &#x60;LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME&#x60;. | [optional] 
**syncWaitSecs** | **String** | Period in seconds between consecutive syncs. Default: 15. | [optional] 


