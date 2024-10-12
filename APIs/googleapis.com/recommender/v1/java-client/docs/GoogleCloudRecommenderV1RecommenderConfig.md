

# GoogleCloudRecommenderV1RecommenderConfig

Configuration for a Recommender.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Allows clients to store small amounts of arbitrary data. Annotations must follow the Kubernetes syntax. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |  [optional] |
|**displayName** | **String** | A user-settable field to provide a human-readable name to be used in user interfaces. |  [optional] |
|**etag** | **String** | Fingerprint of the RecommenderConfig. Provides optimistic locking when updating. |  [optional] |
|**name** | **String** | Name of recommender config. Eg, projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/config |  [optional] |
|**recommenderGenerationConfig** | [**GoogleCloudRecommenderV1RecommenderGenerationConfig**](GoogleCloudRecommenderV1RecommenderGenerationConfig.md) |  |  [optional] |
|**revisionId** | **String** | Output only. Immutable. The revision ID of the config. A new revision is committed whenever the config is changed in any way. The format is an 8-character hexadecimal string. |  [optional] [readonly] |
|**updateTime** | **String** | Last time when the config was updated. |  [optional] |



