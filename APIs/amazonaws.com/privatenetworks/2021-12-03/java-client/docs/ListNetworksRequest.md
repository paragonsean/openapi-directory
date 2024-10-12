

# ListNetworksRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filters** | **Map&lt;String, List&lt;String&gt;&gt;** | &lt;p&gt;The filters.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;STATUS&lt;/code&gt; - The status (&lt;code&gt;AVAILABLE&lt;/code&gt; | &lt;code&gt;CREATED&lt;/code&gt; | &lt;code&gt;DELETED&lt;/code&gt; | &lt;code&gt;DEPROVISIONING&lt;/code&gt; | &lt;code&gt;PROVISIONING&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Filter values are case sensitive. If you specify multiple values for a filter, the values are joined with an &lt;code&gt;OR&lt;/code&gt;, and the request returns all results that match any of the specified values.&lt;/p&gt; |  [optional] |
|**maxResults** | **Integer** | The maximum number of results to return. |  [optional] |
|**startToken** | **String** | The token for the next page of results. |  [optional] |



