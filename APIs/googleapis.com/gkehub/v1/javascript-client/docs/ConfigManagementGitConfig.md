# GkeHubApi.ConfigManagementGitConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcpServiceAccountEmail** | **String** | The Google Cloud Service Account Email used for auth when secret_type is gcpServiceAccount. | [optional] 
**httpsProxy** | **String** | URL for the HTTPS proxy to be used when communicating with the Git repo. | [optional] 
**policyDir** | **String** | The path within the Git repository that represents the top level of the repo to sync. Default: the root directory of the repository. | [optional] 
**secretType** | **String** | Type of secret configured for access to the Git repo. Must be one of ssh, cookiefile, gcenode, token, gcpserviceaccount or none. The validation of this is case-sensitive. Required. | [optional] 
**syncBranch** | **String** | The branch of the repository to sync from. Default: master. | [optional] 
**syncRepo** | **String** | The URL of the Git repository to use as the source of truth. | [optional] 
**syncRev** | **String** | Git revision (tag or hash) to check out. Default HEAD. | [optional] 
**syncWaitSecs** | **String** | Period in seconds between consecutive syncs. Default: 15. | [optional] 


