

# CreateSignalingChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelName** | **String** | A name for the signaling channel that you are creating. It must be unique for each Amazon Web Services account and Amazon Web Services Region. |  |
|**channelType** | [**ChannelTypeEnum**](#ChannelTypeEnum) | A type of the signaling channel that you are creating. Currently, &lt;code&gt;SINGLE_MASTER&lt;/code&gt; is the only supported channel type.  |  [optional] |
|**singleMasterConfiguration** | [**CreateSignalingChannelRequestSingleMasterConfiguration**](CreateSignalingChannelRequestSingleMasterConfiguration.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | A set of tags (key-value pairs) that you want to associate with this channel. |  [optional] |



## Enum: ChannelTypeEnum

| Name | Value |
|---- | -----|
| SINGLE_MASTER | &quot;SINGLE_MASTER&quot; |
| FULL_MESH | &quot;FULL_MESH&quot; |



