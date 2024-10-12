

# ReleaseChannelConfig

ReleaseChannelConfig exposes configuration for a release channel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableVersions** | [**List&lt;AvailableVersion&gt;**](AvailableVersion.md) | Deprecated. This field has been deprecated and replaced with the valid_versions field. |  [optional] |
|**channel** | [**ChannelEnum**](#ChannelEnum) | The release channel this configuration applies to. |  [optional] |
|**defaultVersion** | **String** | The default version for newly created clusters on the channel. |  [optional] |
|**validVersions** | **List&lt;String&gt;** | List of valid versions for the channel. |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| RAPID | &quot;RAPID&quot; |
| REGULAR | &quot;REGULAR&quot; |
| STABLE | &quot;STABLE&quot; |



