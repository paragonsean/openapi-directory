

# GoogleCloudRecommenderV1MarkRecommendationClaimedRequest

Request for the `MarkRecommendationClaimed` Method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | Required. Fingerprint of the Recommendation. Provides optimistic locking. |  [optional] |
|**stateMetadata** | **Map&lt;String, String&gt;** | State properties to include with this state. Overwrites any existing &#x60;state_metadata&#x60;. Keys must match the regex &#x60;/^a-z0-9{0,62}$/&#x60;. Values must match the regex &#x60;/^[a-zA-Z0-9_./-]{0,255}$/&#x60;. |  [optional] |



