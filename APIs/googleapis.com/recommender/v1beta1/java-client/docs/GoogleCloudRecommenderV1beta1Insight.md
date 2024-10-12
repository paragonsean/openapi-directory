

# GoogleCloudRecommenderV1beta1Insight

An insight along with the information used to derive the insight. The insight may have associated recommendations as well.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associatedRecommendations** | [**List&lt;GoogleCloudRecommenderV1beta1InsightRecommendationReference&gt;**](GoogleCloudRecommenderV1beta1InsightRecommendationReference.md) | Recommendations derived from this insight. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | Category being targeted by the insight. |  [optional] |
|**content** | **Map&lt;String, Object&gt;** | A struct of custom fields to explain the insight. Example: \&quot;grantedPermissionsCount\&quot;: \&quot;1000\&quot; |  [optional] |
|**description** | **String** | Free-form human readable summary in English. The maximum length is 500 characters. |  [optional] |
|**etag** | **String** | Fingerprint of the Insight. Provides optimistic locking when updating states. |  [optional] |
|**insightSubtype** | **String** | Insight subtype. Insight content schema will be stable for a given subtype. |  [optional] |
|**lastRefreshTime** | **String** | Timestamp of the latest data used to generate the insight. |  [optional] |
|**name** | **String** | Name of the insight. |  [optional] |
|**observationPeriod** | **String** | Observation period that led to the insight. The source data used to generate the insight ends at last_refresh_time and begins at (last_refresh_time - observation_period). |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Insight&#39;s severity. |  [optional] |
|**stateInfo** | [**GoogleCloudRecommenderV1beta1InsightStateInfo**](GoogleCloudRecommenderV1beta1InsightStateInfo.md) |  |  [optional] |
|**targetResources** | **List&lt;String&gt;** | Fully qualified resource names that this insight is targeting. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| CATEGORY_UNSPECIFIED | &quot;CATEGORY_UNSPECIFIED&quot; |
| COST | &quot;COST&quot; |
| SECURITY | &quot;SECURITY&quot; |
| PERFORMANCE | &quot;PERFORMANCE&quot; |
| MANAGEABILITY | &quot;MANAGEABILITY&quot; |
| SUSTAINABILITY | &quot;SUSTAINABILITY&quot; |
| RELIABILITY | &quot;RELIABILITY&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| CRITICAL | &quot;CRITICAL&quot; |



