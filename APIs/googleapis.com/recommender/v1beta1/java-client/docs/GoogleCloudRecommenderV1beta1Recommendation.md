

# GoogleCloudRecommenderV1beta1Recommendation

A recommendation along with a suggested action. E.g., a rightsizing recommendation for an underutilized VM, IAM role recommendations, etc

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalImpact** | [**List&lt;GoogleCloudRecommenderV1beta1Impact&gt;**](GoogleCloudRecommenderV1beta1Impact.md) | Optional set of additional impact that this recommendation may have when trying to optimize for the primary category. These may be positive or negative. |  [optional] |
|**associatedInsights** | [**List&lt;GoogleCloudRecommenderV1beta1RecommendationInsightReference&gt;**](GoogleCloudRecommenderV1beta1RecommendationInsightReference.md) | Insights that led to this recommendation. |  [optional] |
|**content** | [**GoogleCloudRecommenderV1beta1RecommendationContent**](GoogleCloudRecommenderV1beta1RecommendationContent.md) |  |  [optional] |
|**description** | **String** | Free-form human readable summary in English. The maximum length is 500 characters. |  [optional] |
|**etag** | **String** | Fingerprint of the Recommendation. Provides optimistic locking when updating states. |  [optional] |
|**lastRefreshTime** | **String** | Last time this recommendation was refreshed by the system that created it in the first place. |  [optional] |
|**name** | **String** | Name of recommendation. |  [optional] |
|**primaryImpact** | [**GoogleCloudRecommenderV1beta1Impact**](GoogleCloudRecommenderV1beta1Impact.md) |  |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | Recommendation&#39;s priority. |  [optional] |
|**recommenderSubtype** | **String** | Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to &#x60;content&#x60; or &#x60;primary_impact.category&#x60; are introduced. See the Recommenders section to see a list of subtypes for a given Recommender. Examples: For recommender &#x3D; \&quot;google.iam.policy.Recommender\&quot;, recommender_subtype can be one of \&quot;REMOVE_ROLE\&quot;/\&quot;REPLACE_ROLE\&quot; |  [optional] |
|**stateInfo** | [**GoogleCloudRecommenderV1beta1RecommendationStateInfo**](GoogleCloudRecommenderV1beta1RecommendationStateInfo.md) |  |  [optional] |
|**targetResources** | **List&lt;String&gt;** | Fully qualified resource names that this recommendation is targeting. |  [optional] |
|**xorGroupId** | **String** | Corresponds to a mutually exclusive group ID within a recommender. A non-empty ID indicates that the recommendation belongs to a mutually exclusive group. This means that only one recommendation within the group is suggested to be applied. |  [optional] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| PRIORITY_UNSPECIFIED | &quot;PRIORITY_UNSPECIFIED&quot; |
| P4 | &quot;P4&quot; |
| P3 | &quot;P3&quot; |
| P2 | &quot;P2&quot; |
| P1 | &quot;P1&quot; |



