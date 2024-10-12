# RecommenderApi.GoogleCloudRecommenderV1beta1Insight

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associatedRecommendations** | [**[GoogleCloudRecommenderV1beta1InsightRecommendationReference]**](GoogleCloudRecommenderV1beta1InsightRecommendationReference.md) | Recommendations derived from this insight. | [optional] 
**category** | **String** | Category being targeted by the insight. | [optional] 
**content** | **{String: Object}** | A struct of custom fields to explain the insight. Example: \&quot;grantedPermissionsCount\&quot;: \&quot;1000\&quot; | [optional] 
**description** | **String** | Free-form human readable summary in English. The maximum length is 500 characters. | [optional] 
**etag** | **String** | Fingerprint of the Insight. Provides optimistic locking when updating states. | [optional] 
**insightSubtype** | **String** | Insight subtype. Insight content schema will be stable for a given subtype. | [optional] 
**lastRefreshTime** | **String** | Timestamp of the latest data used to generate the insight. | [optional] 
**name** | **String** | Name of the insight. | [optional] 
**observationPeriod** | **String** | Observation period that led to the insight. The source data used to generate the insight ends at last_refresh_time and begins at (last_refresh_time - observation_period). | [optional] 
**severity** | **String** | Insight&#39;s severity. | [optional] 
**stateInfo** | [**GoogleCloudRecommenderV1beta1InsightStateInfo**](GoogleCloudRecommenderV1beta1InsightStateInfo.md) |  | [optional] 
**targetResources** | **[String]** | Fully qualified resource names that this insight is targeting. | [optional] 



## Enum: CategoryEnum


* `CATEGORY_UNSPECIFIED` (value: `"CATEGORY_UNSPECIFIED"`)

* `COST` (value: `"COST"`)

* `SECURITY` (value: `"SECURITY"`)

* `PERFORMANCE` (value: `"PERFORMANCE"`)

* `MANAGEABILITY` (value: `"MANAGEABILITY"`)

* `SUSTAINABILITY` (value: `"SUSTAINABILITY"`)

* `RELIABILITY` (value: `"RELIABILITY"`)





## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `LOW` (value: `"LOW"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HIGH` (value: `"HIGH"`)

* `CRITICAL` (value: `"CRITICAL"`)




