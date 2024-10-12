# AppCenterClient.DeploymentInternalAllOfLatestRelease

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** |  | [optional] 
**isDisabled** | **Boolean** |  | [optional] 
**isMandatory** | **Boolean** |  | [optional] 
**rollout** | **Number** |  | [optional] 
**targetBinaryRange** | **String** |  | [optional] 
**blobUrl** | **String** |  | [optional] 
**diffPackageMap** | [**{String: CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue}**](CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue.md) |  | [optional] 
**label** | **String** |  | [optional] 
**originalDeployment** | **String** | Set on &#39;Promote&#39; | [optional] 
**originalLabel** | **String** | Set on &#39;Promote&#39; and &#39;Rollback&#39; | [optional] 
**packageHash** | **String** |  | [optional] 
**releaseMethod** | **String** | The release method is unknown if unspecified | [optional] 
**releasedBy** | **String** |  | [optional] 
**size** | **Number** |  | [optional] 
**uploadTime** | **Number** |  | [optional] 



## Enum: ReleaseMethodEnum


* `Upload` (value: `"Upload"`)

* `Promote` (value: `"Promote"`)

* `Rollback` (value: `"Rollback"`)




