# AmazonSimpleEmailService.ListRecommendationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **{String: String}** | An object that contains mapping between &lt;code&gt;ListRecommendationsFilterKey&lt;/code&gt; and &lt;code&gt;ListRecommendationFilterValue&lt;/code&gt; to filter by. | [optional] 
**nextToken** | **String** | A token returned from a previous call to &lt;code&gt;ListRecommendations&lt;/code&gt; to indicate the position in the list of recommendations. | [optional] 
**pageSize** | **Number** | &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListRecommendations&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 1, and can be no more than 100.&lt;/p&gt; | [optional] 


