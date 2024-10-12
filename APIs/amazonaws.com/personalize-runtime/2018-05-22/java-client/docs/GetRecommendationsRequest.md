

# GetRecommendationsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignArn** | **String** | The Amazon Resource Name (ARN) of the campaign to use for getting recommendations. |  [optional] |
|**itemId** | **String** | &lt;p&gt;The item ID to provide recommendations for.&lt;/p&gt; &lt;p&gt;Required for &lt;code&gt;RELATED_ITEMS&lt;/code&gt; recipe type.&lt;/p&gt; |  [optional] |
|**userId** | **String** | &lt;p&gt;The user ID to provide recommendations for.&lt;/p&gt; &lt;p&gt;Required for &lt;code&gt;USER_PERSONALIZATION&lt;/code&gt; recipe type.&lt;/p&gt; |  [optional] |
|**numResults** | **Integer** | The number of results to return. The default is 25. The maximum is 500. |  [optional] |
|**context** | **Map&lt;String, String&gt;** | The contextual metadata to use when getting recommendations. Contextual metadata includes any interaction information that might be relevant when getting a user&#39;s recommendations, such as the user&#39;s current location or device type. |  [optional] |
|**filterArn** | **String** | &lt;p&gt;The ARN of the filter to apply to the returned recommendations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/personalize/latest/dg/filter.html\&quot;&gt;Filtering Recommendations&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;When using this parameter, be sure the filter resource is &lt;code&gt;ACTIVE&lt;/code&gt;.&lt;/p&gt; |  [optional] |
|**filterValues** | **Map&lt;String, String&gt;** | &lt;p&gt;The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. &lt;/p&gt; &lt;p&gt;For filter expressions that use an &lt;code&gt;INCLUDE&lt;/code&gt; element to include items, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an &lt;code&gt;EXCLUDE&lt;/code&gt; element to exclude items, you can omit the &lt;code&gt;filter-values&lt;/code&gt;.In this case, Amazon Personalize doesn&#39;t use that portion of the expression to filter recommendations.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/personalize/latest/dg/filter.html\&quot;&gt;Filtering recommendations and user segments&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**recommenderArn** | **String** | The Amazon Resource Name (ARN) of the recommender to use to get recommendations. Provide a recommender ARN if you created a Domain dataset group with a recommender for a domain use case. |  [optional] |
|**promotions** | [**List&lt;Promotion&gt;**](Promotion.md) | The promotions to apply to the recommendation request. A promotion defines additional business rules that apply to a configurable subset of recommended items. |  [optional] |



