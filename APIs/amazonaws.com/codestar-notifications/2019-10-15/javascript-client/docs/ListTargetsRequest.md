# AwsCodeStarNotifications.ListTargetsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**[ListTargetsFilter]**](ListTargetsFilter.md) | &lt;p&gt;The filters to use to return information by service or resource type. Valid filters include target type, target address, and target status.&lt;/p&gt; &lt;note&gt; &lt;p&gt;A filter with the same name can appear more than once when used with OR statements. Filters with different names should be applied with AND statements.&lt;/p&gt; &lt;/note&gt; | [optional] 
**nextToken** | **String** | An enumeration token that, when provided in a request, returns the next batch of the results. | [optional] 
**maxResults** | **Number** | A non-negative integer used to limit the number of returned results. The maximum number of results that can be returned is 100. | [optional] 


