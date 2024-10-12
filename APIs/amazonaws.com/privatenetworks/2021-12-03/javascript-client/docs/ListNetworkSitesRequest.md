# AwsPrivate5G.ListNetworkSitesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | **{String: Array}** | &lt;p&gt;The filters. Add filters to your request to return a more specific list of results. Use filters to match the status of the network sites.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;STATUS&lt;/code&gt; - The status (&lt;code&gt;AVAILABLE&lt;/code&gt; | &lt;code&gt;CREATED&lt;/code&gt; | &lt;code&gt;DELETED&lt;/code&gt; | &lt;code&gt;DEPROVISIONING&lt;/code&gt; | &lt;code&gt;PROVISIONING&lt;/code&gt;).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Filter values are case sensitive. If you specify multiple values for a filter, the values are joined with an &lt;code&gt;OR&lt;/code&gt;, and the request returns all results that match any of the specified values.&lt;/p&gt; | [optional] 
**maxResults** | **Number** | The maximum number of results to return. | [optional] 
**networkArn** | **String** | The Amazon Resource Name (ARN) of the network. | 
**startToken** | **String** | The token for the next page of results. | [optional] 


