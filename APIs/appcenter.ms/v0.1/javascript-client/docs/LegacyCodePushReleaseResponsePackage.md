# AppCenterClient.LegacyCodePushReleaseResponsePackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appVersion** | **String** | The version of the release | [optional] 
**blobUrl** | **String** | Location (URL) of release package | [optional] 
**diffPackageMap** | **Object** | Object containing URL and size of changed package hashes contained in the release | [optional] 
**isDisabled** | **Boolean** | Flag used to determine if release is disabled | [optional] 
**isMandatory** | **Boolean** | Flag used to determine if release is mandatory | [optional] 
**label** | **String** | Release label (aka release name) | [optional] 
**manifestBlobUrl** | **String** | The URL location of the package&#39;s manifest file. | [optional] 
**releaseMethod** | **String** | Method used to deploy release | [optional] 
**releasedByUserId** | **String** | User ID that triggered most recent release | [optional] 
**rollout** | **Number** | Percentage (out of 100) that release is deployed to | [optional] 
**size** | **Number** | Size of release package | [optional] 
**uploadTime** | **Number** | Release upload time as epoch Unix timestamp | [optional] 


