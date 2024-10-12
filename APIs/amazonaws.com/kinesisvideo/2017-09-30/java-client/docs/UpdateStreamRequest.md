

# UpdateStreamRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**streamName** | **String** | &lt;p&gt;The name of the stream whose metadata you want to update.&lt;/p&gt; &lt;p&gt;The stream name is an identifier for the stream, and must be unique for each account and region.&lt;/p&gt; |  [optional] |
|**streamARN** | **String** | The ARN of the stream whose metadata you want to update. |  [optional] |
|**currentVersion** | **String** | The version of the stream whose metadata you want to update. |  |
|**deviceName** | **String** | &lt;p&gt;The name of the device that is writing to the stream. &lt;/p&gt; &lt;note&gt; &lt;p&gt; In the current implementation, Kinesis Video Streams does not use this name. &lt;/p&gt; &lt;/note&gt; |  [optional] |
|**mediaType** | **String** | &lt;p&gt;The stream&#39;s media type. Use &lt;code&gt;MediaType&lt;/code&gt; to specify the type of content that the stream contains to the consumers of the stream. For more information about media types, see &lt;a href&#x3D;\&quot;http://www.iana.org/assignments/media-types/media-types.xhtml\&quot;&gt;Media Types&lt;/a&gt;. If you choose to specify the &lt;code&gt;MediaType&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc6838#section-4.2\&quot;&gt;Naming Requirements&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To play video on the console, you must specify the correct video type. For example, if the video in the stream is H.264, specify &lt;code&gt;video/h264&lt;/code&gt; as the &lt;code&gt;MediaType&lt;/code&gt;.&lt;/p&gt; |  [optional] |



