

# Release

 A `Release` is a particular [collection of configurations and files](sites.versions) that is set to be public at a particular time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The deploy description when the release was created. The value can be up to 512 characters. |  [optional] |
|**name** | **String** | Output only. The unique identifier for the release, in either of the following formats: - sites/SITE_ID/releases/RELEASE_ID - sites/SITE_ID/channels/CHANNEL_ID/releases/RELEASE_ID This name is provided in the response body when you call [&#x60;releases.create&#x60;](sites.releases/create) or [&#x60;channels.releases.create&#x60;](sites.channels.releases/create). |  [optional] |
|**releaseTime** | **String** | Output only. The time at which the version is set to be public. |  [optional] |
|**releaseUser** | [**ActingUser**](ActingUser.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Explains the reason for the release. Specify a value for this field only when creating a &#x60;SITE_DISABLE&#x60; type release. |  [optional] |
|**version** | [**Version**](Version.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| DEPLOY | &quot;DEPLOY&quot; |
| ROLLBACK | &quot;ROLLBACK&quot; |
| SITE_DISABLE | &quot;SITE_DISABLE&quot; |



