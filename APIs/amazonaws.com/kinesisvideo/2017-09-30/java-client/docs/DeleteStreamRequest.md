

# DeleteStreamRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**streamARN** | **String** | The Amazon Resource Name (ARN) of the stream that you want to delete.  |  |
|**currentVersion** | **String** | &lt;p&gt;Optional: The version of the stream that you want to delete. &lt;/p&gt; &lt;p&gt;Specify the version as a safeguard to ensure that your are deleting the correct stream. To get the stream version, use the &lt;code&gt;DescribeStream&lt;/code&gt; API.&lt;/p&gt; &lt;p&gt;If not specified, only the &lt;code&gt;CreationTime&lt;/code&gt; is checked before deleting the stream.&lt;/p&gt; |  [optional] |



