

# CodePushDeploymentsList200ResponseInnerLatestRelease


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  [optional] |
|**isDisabled** | **Boolean** |  |  [optional] |
|**isMandatory** | **Boolean** |  |  [optional] |
|**rollout** | **Integer** |  |  [optional] |
|**targetBinaryRange** | **String** |  |  [optional] |
|**blobUrl** | **String** |  |  [optional] |
|**diffPackageMap** | [**Map&lt;String, CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue&gt;**](CodePushDeploymentsList200ResponseInnerLatestReleaseAllOfDiffPackageMapValue.md) |  |  [optional] |
|**label** | **String** |  |  [optional] |
|**originalDeployment** | **String** | Set on &#39;Promote&#39; |  [optional] |
|**originalLabel** | **String** | Set on &#39;Promote&#39; and &#39;Rollback&#39; |  [optional] |
|**packageHash** | **String** |  |  [optional] |
|**releaseMethod** | [**ReleaseMethodEnum**](#ReleaseMethodEnum) | The release method is unknown if unspecified |  [optional] |
|**releasedBy** | **String** |  |  [optional] |
|**size** | **BigDecimal** |  |  [optional] |
|**uploadTime** | **Integer** |  |  [optional] |



## Enum: ReleaseMethodEnum

| Name | Value |
|---- | -----|
| UPLOAD | &quot;Upload&quot; |
| PROMOTE | &quot;Promote&quot; |
| ROLLBACK | &quot;Rollback&quot; |



