# AwsLicenseManagerLinuxSubscriptions.ListLinuxSubscriptionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**[Filter]**](Filter.md) | &lt;p&gt;An array of structures that you can use to filter the results to those that match one or more sets of key-value pairs that you specify. For example, you can filter by the name of &lt;code&gt;Subscription&lt;/code&gt; with an optional operator to see subscriptions that match, partially match, or don&#39;t match a certain subscription&#39;s name.&lt;/p&gt; &lt;p&gt;The valid names for this filter are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Subscription&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The valid Operators for this filter are:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;contains&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;equals&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Notequal&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**maxResults** | **Number** | Maximum number of results to return in a single call. | [optional] 
**nextToken** | **String** | Token for the next set of results. | [optional] 


