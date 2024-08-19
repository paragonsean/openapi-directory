# VertexAiApi.GoogleCloudAiplatformV1Featurestore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this Featurestore was created. | [optional] [readonly] 
**encryptionSpec** | [**GoogleCloudAiplatformV1EncryptionSpec**](GoogleCloudAiplatformV1EncryptionSpec.md) |  | [optional] 
**etag** | **String** | Optional. Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | Optional. The labels with user-defined metadata to organize your Featurestore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Featurestore(System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. | [optional] 
**name** | **String** | Output only. Name of the Featurestore. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}&#x60; | [optional] [readonly] 
**onlineServingConfig** | [**GoogleCloudAiplatformV1FeaturestoreOnlineServingConfig**](GoogleCloudAiplatformV1FeaturestoreOnlineServingConfig.md) |  | [optional] 
**onlineStorageTtlDays** | **Number** | Optional. TTL in days for feature values that will be stored in online serving storage. The Feature Store online storage periodically removes obsolete feature values older than &#x60;online_storage_ttl_days&#x60; since the feature generation time. Note that &#x60;online_storage_ttl_days&#x60; should be less than or equal to &#x60;offline_storage_ttl_days&#x60; for each EntityType under a featurestore. If not set, default to 4000 days | [optional] 
**state** | **String** | Output only. State of the featurestore. | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when this Featurestore was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `STABLE` (value: `"STABLE"`)

* `UPDATING` (value: `"UPDATING"`)




