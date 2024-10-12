

# Channel

Each Channel is owned by a Platform and owns a collection of versions. Possible Channels are listed in the Channel enum below. Not all Channels are available for every Platform (e.g. CANARY does not exist for LINUX).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelType** | [**ChannelTypeEnum**](#ChannelTypeEnum) | Type of channel. |  [optional] |
|**name** | **String** | Channel name. Format is \&quot;{product}/platforms/{platform}/channels/{channel}\&quot; |  [optional] |



## Enum: ChannelTypeEnum

| Name | Value |
|---- | -----|
| CHANNEL_TYPE_UNSPECIFIED | &quot;CHANNEL_TYPE_UNSPECIFIED&quot; |
| STABLE | &quot;STABLE&quot; |
| BETA | &quot;BETA&quot; |
| DEV | &quot;DEV&quot; |
| CANARY | &quot;CANARY&quot; |
| CANARY_ASAN | &quot;CANARY_ASAN&quot; |
| ALL | &quot;ALL&quot; |
| EXTENDED | &quot;EXTENDED&quot; |
| LTS | &quot;LTS&quot; |
| LTC | &quot;LTC&quot; |



