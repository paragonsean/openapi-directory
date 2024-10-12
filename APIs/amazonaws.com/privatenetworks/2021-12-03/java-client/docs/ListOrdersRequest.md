

# ListOrdersRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filters** | **Map&lt;String, List&lt;String&gt;&gt;** | &lt;p&gt;The filters.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NETWORK_SITE&lt;/code&gt; - The Amazon Resource Name (ARN) of the network site.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;STATUS&lt;/code&gt; - The status (&lt;code&gt;ACKNOWLEDGING&lt;/code&gt; | &lt;code&gt;ACKNOWLEDGED&lt;/code&gt; | &lt;code&gt;UNACKNOWLEDGED&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Filter values are case sensitive. If you specify multiple values for a filter, the values are joined with an &lt;code&gt;OR&lt;/code&gt;, and the request returns all results that match any of the specified values.&lt;/p&gt; |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return. |  [optional] |
|**networkArn** | **String** | The Amazon Resource Name (ARN) of the network. |  |
|**startToken** | **String** | The token for the next page of results. |  [optional] |



