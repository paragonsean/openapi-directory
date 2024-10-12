

# DistributionGroupsGetApps200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the app |  [optional] |
|**displayName** | **String** | The display name of the app |  |
|**iconSource** | **String** | The string representation of the source of the app&#39;s icon |  [optional] |
|**iconUrl** | **String** | The string representation of the URL pointing to the app&#39;s icon |  [optional] |
|**id** | **UUID** | The unique ID (UUID) of the app |  |
|**name** | **String** | The name of the app used in URLs |  |
|**os** | [**OsEnum**](#OsEnum) | The OS the app will be running on |  |
|**owner** | [**AppsList200ResponseInnerAllOfOwner**](AppsList200ResponseInnerAllOfOwner.md) |  |  |
|**releaseType** | **String** | A one-word descriptive release-type value that starts with a capital letter but is otherwise lowercase |  [optional] |
|**origin** | **String** | The creation origin of this app |  [optional] |
|**platform** | **String** | The platform of the app |  [optional] |



## Enum: OsEnum

| Name | Value |
|---- | -----|
| ANDROID | &quot;Android&quot; |
| I_OS | &quot;iOS&quot; |
| MAC_OS | &quot;macOS&quot; |
| TIZEN | &quot;Tizen&quot; |
| TV_OS | &quot;tvOS&quot; |
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |
| CUSTOM | &quot;Custom&quot; |



