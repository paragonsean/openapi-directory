

# GoogleCloudAiplatformV1beta1FeatureView

FeatureView is representation of values that the FeatureOnlineStore will serve based on its syncConfig.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigQuerySource** | [**GoogleCloudAiplatformV1beta1FeatureViewBigQuerySource**](GoogleCloudAiplatformV1beta1FeatureViewBigQuerySource.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp when this FeatureView was created. |  [optional] [readonly] |
|**etag** | **String** | Optional. Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**featureRegistrySource** | [**GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySource**](GoogleCloudAiplatformV1beta1FeatureViewFeatureRegistrySource.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata to organize your FeatureViews. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. |  [optional] |
|**name** | **String** | Identifier. Name of the FeatureView. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}&#x60; |  [optional] |
|**serviceAccountEmail** | **String** | Output only. A Service Account unique to this FeatureView. The role bigquery.dataViewer should be granted to this service account to allow Vertex AI Feature Store to sync data to the online store. |  [optional] [readonly] |
|**serviceAgentType** | [**ServiceAgentTypeEnum**](#ServiceAgentTypeEnum) | Optional. Service agent type used during data sync. By default, the Vertex AI Service Agent is used. When using an IAM Policy to isolate this FeatureView within a project (https://cloud.google.com/vertex-ai/docs/featurestore/latest/resource-policy) a separate service account should be provisioned by setting this field to &#x60;SERVICE_AGENT_TYPE_FEATURE_VIEW&#x60;. This will generate a separate service account to access the BigQuery source table. |  [optional] |
|**syncConfig** | [**GoogleCloudAiplatformV1beta1FeatureViewSyncConfig**](GoogleCloudAiplatformV1beta1FeatureViewSyncConfig.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Timestamp when this FeatureView was last updated. |  [optional] [readonly] |
|**vectorSearchConfig** | [**GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig**](GoogleCloudAiplatformV1beta1FeatureViewVectorSearchConfig.md) |  |  [optional] |



## Enum: ServiceAgentTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SERVICE_AGENT_TYPE_UNSPECIFIED&quot; |
| PROJECT | &quot;SERVICE_AGENT_TYPE_PROJECT&quot; |
| FEATURE_VIEW | &quot;SERVICE_AGENT_TYPE_FEATURE_VIEW&quot; |



