

# GoogleChromeManagementV1BrowserVersion

Describes a browser version and its install count.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) | Output only. The release channel of the installed browser. |  [optional] [readonly] |
|**count** | **String** | Output only. Count grouped by device_system and major version |  [optional] [readonly] |
|**deviceOsVersion** | **String** | Output only. Version of the system-specified operating system. |  [optional] [readonly] |
|**system** | [**SystemEnum**](#SystemEnum) | Output only. The device operating system. |  [optional] [readonly] |
|**version** | **String** | Output only. The full version of the installed browser. |  [optional] [readonly] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| RELEASE_CHANNEL_UNSPECIFIED | &quot;RELEASE_CHANNEL_UNSPECIFIED&quot; |
| CANARY | &quot;CANARY&quot; |
| DEV | &quot;DEV&quot; |
| BETA | &quot;BETA&quot; |
| STABLE | &quot;STABLE&quot; |



## Enum: SystemEnum

| Name | Value |
|---- | -----|
| DEVICE_SYSTEM_UNSPECIFIED | &quot;DEVICE_SYSTEM_UNSPECIFIED&quot; |
| SYSTEM_OTHER | &quot;SYSTEM_OTHER&quot; |
| SYSTEM_ANDROID | &quot;SYSTEM_ANDROID&quot; |
| SYSTEM_IOS | &quot;SYSTEM_IOS&quot; |
| SYSTEM_CROS | &quot;SYSTEM_CROS&quot; |
| SYSTEM_WINDOWS | &quot;SYSTEM_WINDOWS&quot; |
| SYSTEM_MAC | &quot;SYSTEM_MAC&quot; |
| SYSTEM_LINUX | &quot;SYSTEM_LINUX&quot; |



