# VertexAiApi.GoogleCloudAiplatformV1Feature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was created. | [optional] [readonly] 
**description** | **String** | Description of the Feature. | [optional] 
**disableMonitoring** | **Boolean** | Optional. Only applicable for Vertex AI Feature Store (Legacy). If not set, use the monitoring_config defined for the EntityType this Feature belongs to. Only Features with type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 can enable monitoring. If set to true, all types of data monitoring are disabled despite the config on EntityType. | [optional] 
**etag** | **String** | Used to perform a consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. | [optional] 
**monitoringStatsAnomalies** | [**[GoogleCloudAiplatformV1FeatureMonitoringStatsAnomaly]**](GoogleCloudAiplatformV1FeatureMonitoringStatsAnomaly.md) | Output only. Only applicable for Vertex AI Feature Store (Legacy). The list of historical stats and anomalies with specified objectives. | [optional] [readonly] 
**name** | **String** | Immutable. Name of the Feature. Format: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}&#x60; &#x60;projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}&#x60; The last part feature is assigned by the client. The feature can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given an entity type. | [optional] 
**pointOfContact** | **String** | Entity responsible for maintaining this feature. Can be comma separated list of email addresses or URIs. | [optional] 
**updateTime** | **String** | Output only. Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was most recently updated. | [optional] [readonly] 
**valueType** | **String** | Immutable. Only applicable for Vertex AI Feature Store (Legacy). Type of Feature value. | [optional] 
**versionColumnName** | **String** | Only applicable for Vertex AI Feature Store. The name of the BigQuery Table/View column hosting data for this version. If no value is provided, will use feature_id. | [optional] 



## Enum: ValueTypeEnum


* `VALUE_TYPE_UNSPECIFIED` (value: `"VALUE_TYPE_UNSPECIFIED"`)

* `BOOL` (value: `"BOOL"`)

* `BOOL_ARRAY` (value: `"BOOL_ARRAY"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `DOUBLE_ARRAY` (value: `"DOUBLE_ARRAY"`)

* `INT64` (value: `"INT64"`)

* `INT64_ARRAY` (value: `"INT64_ARRAY"`)

* `STRING` (value: `"STRING"`)

* `STRING_ARRAY` (value: `"STRING_ARRAY"`)

* `BYTES` (value: `"BYTES"`)




