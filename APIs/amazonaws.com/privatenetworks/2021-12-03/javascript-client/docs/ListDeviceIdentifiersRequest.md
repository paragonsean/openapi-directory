# AwsPrivate5G.ListDeviceIdentifiersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **{String: Array}** | &lt;p&gt;The filters.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ORDER&lt;/code&gt; - The Amazon Resource Name (ARN) of the order.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;STATUS&lt;/code&gt; - The status (&lt;code&gt;ACTIVE&lt;/code&gt; | &lt;code&gt;INACTIVE&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TRAFFIC_GROUP&lt;/code&gt; - The Amazon Resource Name (ARN) of the traffic group.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Filter values are case sensitive. If you specify multiple values for a filter, the values are joined with an &lt;code&gt;OR&lt;/code&gt;, and the request returns all results that match any of the specified values.&lt;/p&gt; | [optional] 
**maxResults** | **Number** | The maximum number of results to return. | [optional] 
**networkArn** | **String** | The Amazon Resource Name (ARN) of the network. | 
**startToken** | **String** | The token for the next page of results. | [optional] 


