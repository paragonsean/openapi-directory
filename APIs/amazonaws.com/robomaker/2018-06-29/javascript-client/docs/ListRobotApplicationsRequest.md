# AwsRoboMaker.ListRobotApplicationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versionQualifier** | **String** | The version qualifier of the robot application. | [optional] 
**nextToken** | **String** | If the previous paginated request did not return all of the remaining results, the response object&#39;s &lt;code&gt;nextToken&lt;/code&gt; parameter value is set to a token. To retrieve the next set of results, call &lt;code&gt;ListRobotApplications&lt;/code&gt; again and assign that token to the request object&#39;s &lt;code&gt;nextToken&lt;/code&gt; parameter. If there are no remaining results, the previous response object&#39;s NextToken parameter is set to null.  | [optional] 
**maxResults** | **Number** | When this parameter is used, &lt;code&gt;ListRobotApplications&lt;/code&gt; only returns &lt;code&gt;maxResults&lt;/code&gt; results in a single page along with a &lt;code&gt;nextToken&lt;/code&gt; response element. The remaining results of the initial request can be seen by sending another &lt;code&gt;ListRobotApplications&lt;/code&gt; request with the returned &lt;code&gt;nextToken&lt;/code&gt; value. This value can be between 1 and 100. If this parameter is not used, then &lt;code&gt;ListRobotApplications&lt;/code&gt; returns up to 100 results and a &lt;code&gt;nextToken&lt;/code&gt; value if applicable.  | [optional] 
**filters** | [**[Filter]**](Filter.md) | &lt;p&gt;Optional filters to limit results.&lt;/p&gt; &lt;p&gt;The filter name &lt;code&gt;name&lt;/code&gt; is supported. When filtering, you must use the complete value of the filtered item. You can use up to three filters.&lt;/p&gt; | [optional] 


