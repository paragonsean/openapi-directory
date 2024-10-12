# AmazonKinesisVideoStreams.CreateSignalingChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelName** | **String** | A name for the signaling channel that you are creating. It must be unique for each Amazon Web Services account and Amazon Web Services Region. | 
**channelType** | **String** | A type of the signaling channel that you are creating. Currently, &lt;code&gt;SINGLE_MASTER&lt;/code&gt; is the only supported channel type.  | [optional] 
**singleMasterConfiguration** | [**CreateSignalingChannelRequestSingleMasterConfiguration**](CreateSignalingChannelRequestSingleMasterConfiguration.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | A set of tags (key-value pairs) that you want to associate with this channel. | [optional] 



## Enum: ChannelTypeEnum


* `SINGLE_MASTER` (value: `"SINGLE_MASTER"`)

* `FULL_MESH` (value: `"FULL_MESH"`)




