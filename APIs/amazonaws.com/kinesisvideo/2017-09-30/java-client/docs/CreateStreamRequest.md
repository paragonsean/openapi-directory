

# CreateStreamRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceName** | **String** | &lt;p&gt;The name of the device that is writing to the stream. &lt;/p&gt; &lt;note&gt; &lt;p&gt;In the current implementation, Kinesis Video Streams does not use this name.&lt;/p&gt; &lt;/note&gt; |  [optional] |
|**streamName** | **String** | &lt;p&gt;A name for the stream that you are creating.&lt;/p&gt; &lt;p&gt;The stream name is an identifier for the stream, and must be unique for each account and region.&lt;/p&gt; |  |
|**mediaType** | **String** | &lt;p&gt;The media type of the stream. Consumers of the stream can use this information when processing the stream. For more information about media types, see &lt;a href&#x3D;\&quot;http://www.iana.org/assignments/media-types/media-types.xhtml\&quot;&gt;Media Types&lt;/a&gt;. If you choose to specify the &lt;code&gt;MediaType&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc6838#section-4.2\&quot;&gt;Naming Requirements&lt;/a&gt; for guidelines.&lt;/p&gt; &lt;p&gt;Example valid values include \&quot;video/h264\&quot; and \&quot;video/h264,audio/aac\&quot;.&lt;/p&gt; &lt;p&gt;This parameter is optional; the default value is &lt;code&gt;null&lt;/code&gt; (or empty in JSON).&lt;/p&gt; |  [optional] |
|**kmsKeyId** | **String** | &lt;p&gt;The ID of the Key Management Service (KMS) key that you want Kinesis Video Streams to use to encrypt stream data.&lt;/p&gt; &lt;p&gt;If no key ID is specified, the default, Kinesis Video-managed key (&lt;code&gt;Amazon Web Services/kinesisvideo&lt;/code&gt;) is used.&lt;/p&gt; &lt;p&gt; For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters\&quot;&gt;DescribeKey&lt;/a&gt;. &lt;/p&gt; |  [optional] |
|**dataRetentionInHours** | **Integer** | &lt;p&gt;The number of hours that you want to retain the data in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.&lt;/p&gt; &lt;p&gt;The default value is 0, indicating that the stream does not persist data.&lt;/p&gt; &lt;p&gt;When the &lt;code&gt;DataRetentionInHours&lt;/code&gt; value is 0, consumers can still consume the fragments that remain in the service host buffer, which has a retention time limit of 5 minutes and a retention memory limit of 200 MB. Fragments are removed from the buffer when either limit is reached.&lt;/p&gt; |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A list of tags to associate with the specified stream. Each tag is a key-value pair (the value is optional). |  [optional] |



