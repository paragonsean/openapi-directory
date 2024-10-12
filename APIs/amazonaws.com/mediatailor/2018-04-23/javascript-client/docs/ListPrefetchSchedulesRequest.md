# AwsMediaTailor.ListPrefetchSchedulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxResults** | **Number** | The maximum number of prefetch schedules that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; prefetch schedules, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
**nextToken** | **String** | &lt;p&gt;(Optional) If the playback configuration has more than &lt;code&gt;MaxResults&lt;/code&gt; prefetch schedules, use &lt;code&gt;NextToken&lt;/code&gt; to get the second and subsequent pages of results.&lt;/p&gt; &lt;p&gt; For the first &lt;code&gt;ListPrefetchSchedulesRequest&lt;/code&gt; request, omit this value.&lt;/p&gt; &lt;p&gt; For the second and subsequent requests, get the value of &lt;code&gt;NextToken&lt;/code&gt; from the previous response and specify that value for &lt;code&gt;NextToken&lt;/code&gt; in the request.&lt;/p&gt; &lt;p&gt; If the previous response didn&#39;t include a &lt;code&gt;NextToken&lt;/code&gt; element, there are no more prefetch schedules to get.&lt;/p&gt; | [optional] 
**streamId** | **String** | An optional filtering parameter whereby MediaTailor filters the prefetch schedules to include only specific streams. | [optional] 


