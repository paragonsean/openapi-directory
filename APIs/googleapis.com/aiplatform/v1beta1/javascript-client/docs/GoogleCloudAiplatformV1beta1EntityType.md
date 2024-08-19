# VertexAiApi.GoogleCloudAiplatformV1beta1EntityType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this EntityType was created. | [optional] [readonly] 
**description** | **String** | Optional. Description of the EntityType. | [optional] 
**etag** | **String** | Optional. Used to perform a consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | Optional. The labels with user-defined metadata to organize your EntityTypes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one EntityType (System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. | [optional] 
**monitoringConfig** | [**GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig**](GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfig.md) |  | [optional] 
**name** | **String** | Immutable. Name of the EntityType. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; The last part entity_type is assigned by the client. The entity_type can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z and underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given a featurestore. | [optional] 
**offlineStorageTtlDays** | **Number** | Optional. Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than &#x60;offline_storage_ttl_days&#x60; since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL. | [optional] 
**updateTime** | **String** | Output only. Timestamp when this EntityType was most recently updated. | [optional] [readonly] 


