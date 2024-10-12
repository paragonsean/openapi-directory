# RecommenderApi.GoogleCloudRecommenderV1beta1InsightTypeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Allows clients to store small amounts of arbitrary data. Annotations must follow the Kubernetes syntax. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. | [optional] 
**displayName** | **String** | A user-settable field to provide a human-readable name to be used in user interfaces. | [optional] 
**etag** | **String** | Fingerprint of the InsightTypeConfig. Provides optimistic locking when updating. | [optional] 
**insightTypeGenerationConfig** | [**GoogleCloudRecommenderV1beta1InsightTypeGenerationConfig**](GoogleCloudRecommenderV1beta1InsightTypeGenerationConfig.md) |  | [optional] 
**name** | **String** | Name of insight type config. Eg, projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config | [optional] 
**revisionId** | **String** | Output only. Immutable. The revision ID of the config. A new revision is committed whenever the config is changed in any way. The format is an 8-character hexadecimal string. | [optional] [readonly] 
**updateTime** | **String** | Last time when the config was updated. | [optional] 


