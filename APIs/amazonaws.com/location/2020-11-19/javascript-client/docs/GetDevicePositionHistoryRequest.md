# AmazonLocationService.GetDevicePositionHistoryRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTimeExclusive** | **Date** | &lt;p&gt;Specify the end time for the position history in &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html\&quot;&gt; ISO 8601&lt;/a&gt; format: &lt;code&gt;YYYY-MM-DDThh:mm:ss.sssZ&lt;/code&gt;. By default, the value will be the time that the request is made.&lt;/p&gt; &lt;p&gt;Requirement:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The time specified for &lt;code&gt;EndTimeExclusive&lt;/code&gt; must be after the time for &lt;code&gt;StartTimeInclusive&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 
**maxResults** | **Number** | &lt;p&gt;An optional limit for the number of device positions returned in a single call.&lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;100&lt;/code&gt; &lt;/p&gt; | [optional] 
**nextToken** | **String** | &lt;p&gt;The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. &lt;/p&gt; &lt;p&gt;Default value: &lt;code&gt;null&lt;/code&gt; &lt;/p&gt; | [optional] 
**startTimeInclusive** | **Date** | &lt;p&gt;Specify the start time for the position history in &lt;a href&#x3D;\&quot;https://www.iso.org/iso-8601-date-and-time-format.html\&quot;&gt; ISO 8601&lt;/a&gt; format: &lt;code&gt;YYYY-MM-DDThh:mm:ss.sssZ&lt;/code&gt;. By default, the value will be 24 hours prior to the time that the request is made.&lt;/p&gt; &lt;p&gt;Requirement:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The time specified for &lt;code&gt;StartTimeInclusive&lt;/code&gt; must be before &lt;code&gt;EndTimeExclusive&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 


