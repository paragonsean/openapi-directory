# AmazonKinesisVideoStreams.ListStreamsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxResults** | **Number** | The maximum number of streams to return in the response. The default is 10,000. | [optional] 
**nextToken** | **String** | If you specify this parameter, when the result of a &lt;code&gt;ListStreams&lt;/code&gt; operation is truncated, the call returns the &lt;code&gt;NextToken&lt;/code&gt; in the response. To get another batch of streams, provide this token in your next request. | [optional] 
**streamNameCondition** | [**ListStreamsRequestStreamNameCondition**](ListStreamsRequestStreamNameCondition.md) |  | [optional] 


