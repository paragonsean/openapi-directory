

# Platform

Each Platform is owned by a Product and owns a collection of channels. Available platforms are listed in Platform enum below. Not all Channels are available for every Platform (e.g. CANARY does not exist for LINUX).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Platform name. Format is \&quot;{product}/platforms/{platform}\&quot; |  [optional] |
|**platformType** | [**PlatformTypeEnum**](#PlatformTypeEnum) | Type of platform. |  [optional] |



## Enum: PlatformTypeEnum

| Name | Value |
|---- | -----|
| PLATFORM_TYPE_UNSPECIFIED | &quot;PLATFORM_TYPE_UNSPECIFIED&quot; |
| WIN | &quot;WIN&quot; |
| WIN64 | &quot;WIN64&quot; |
| MAC | &quot;MAC&quot; |
| LINUX | &quot;LINUX&quot; |
| ANDROID | &quot;ANDROID&quot; |
| WEBVIEW | &quot;WEBVIEW&quot; |
| IOS | &quot;IOS&quot; |
| ALL | &quot;ALL&quot; |
| MAC_ARM64 | &quot;MAC_ARM64&quot; |
| LACROS | &quot;LACROS&quot; |
| LACROS_ARM32 | &quot;LACROS_ARM32&quot; |
| CHROMEOS | &quot;CHROMEOS&quot; |
| LACROS_ARM64 | &quot;LACROS_ARM64&quot; |
| FUCHSIA | &quot;FUCHSIA&quot; |



