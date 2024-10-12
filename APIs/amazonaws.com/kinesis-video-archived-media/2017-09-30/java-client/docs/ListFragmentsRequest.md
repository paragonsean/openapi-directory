

# ListFragmentsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**streamName** | **String** | The name of the stream from which to retrieve a fragment list. Specify either this parameter or the &lt;code&gt;StreamARN&lt;/code&gt; parameter. |  [optional] |
|**streamARN** | **String** | The Amazon Resource Name (ARN) of the stream from which to retrieve a fragment list. Specify either this parameter or the &lt;code&gt;StreamName&lt;/code&gt; parameter. |  [optional] |
|**maxResults** | **Integer** | The total number of fragments to return. If the total number of fragments available is more than the value specified in &lt;code&gt;max-results&lt;/code&gt;, then a &lt;a&gt;ListFragmentsOutput$NextToken&lt;/a&gt; is provided in the output that you can use to resume pagination. |  [optional] |
|**nextToken** | **String** | A token to specify where to start paginating. This is the &lt;a&gt;ListFragmentsOutput$NextToken&lt;/a&gt; from a previously truncated response. |  [optional] |
|**fragmentSelector** | [**ListFragmentsRequestFragmentSelector**](ListFragmentsRequestFragmentSelector.md) |  |  [optional] |



