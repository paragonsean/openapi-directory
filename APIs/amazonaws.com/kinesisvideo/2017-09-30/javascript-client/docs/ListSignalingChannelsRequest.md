# AmazonKinesisVideoStreams.ListSignalingChannelsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxResults** | **Number** | The maximum number of channels to return in the response. The default is 500. | [optional] 
**nextToken** | **String** | If you specify this parameter, when the result of a &lt;code&gt;ListSignalingChannels&lt;/code&gt; operation is truncated, the call returns the &lt;code&gt;NextToken&lt;/code&gt; in the response. To get another batch of channels, provide this token in your next request. | [optional] 
**channelNameCondition** | [**ListSignalingChannelsRequestChannelNameCondition**](ListSignalingChannelsRequestChannelNameCondition.md) |  | [optional] 


