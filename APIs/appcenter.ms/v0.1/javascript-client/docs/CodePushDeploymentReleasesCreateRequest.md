# AppCenterClient.CodePushDeploymentReleasesCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploymentName** | **String** | This specifies which deployment you want to release the update to. Default is Staging. | [optional] 
**description** | **String** | This provides an optional \&quot;change log\&quot; for the deployment. | [optional] 
**disabled** | **Boolean** | This specifies whether an update should be downloadable by end users or not. | [optional] 
**mandatory** | **Boolean** | This specifies whether the update should be considered mandatory or not (e.g. it includes a critical security fix). | [optional] 
**noDuplicateReleaseError** | **Boolean** | This specifies that if the update is identical to the latest release on the deployment, the CLI should generate a warning instead of an error. | [optional] 
**releaseUpload** | [**CodePushDeploymentReleasesCreateRequestReleaseUpload**](CodePushDeploymentReleasesCreateRequestReleaseUpload.md) |  | 
**rollout** | **Number** | This specifies the percentage of users (as an integer between 1 and 100) that should be eligible to receive this update. | [optional] 
**targetBinaryVersion** | **String** | the binary version of the application | 


