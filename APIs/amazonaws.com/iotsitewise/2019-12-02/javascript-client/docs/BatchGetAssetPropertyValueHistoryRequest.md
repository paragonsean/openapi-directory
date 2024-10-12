# AwsIoTSiteWise.BatchGetAssetPropertyValueHistoryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**[BatchGetAssetPropertyValueHistoryEntry]**](BatchGetAssetPropertyValueHistoryEntry.md) | The list of asset property historical value entries for the batch get request. You can specify up to 16 entries per request. | 
**nextToken** | **String** | The token to be used for the next set of paginated results. | [optional] 
**maxResults** | **Number** | &lt;p&gt;The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The size of the result set is equal to 4 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of data points in the result set is equal to the value of &lt;code&gt;maxResults&lt;/code&gt;. The maximum value of &lt;code&gt;maxResults&lt;/code&gt; is 20000.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 


