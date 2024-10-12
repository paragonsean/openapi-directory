

# GoogleCloudAiplatformV1beta1FeatureOnlineStore

Vertex AI Feature Online Store provides a centralized repository for serving ML features and embedding indexes at low latency. The Feature Online Store is a top-level container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigtable** | [**GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtable**](GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtable.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp when this FeatureOnlineStore was created. |  [optional] [readonly] |
|**dedicatedServingEndpoint** | [**GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpoint**](GoogleCloudAiplatformV1beta1FeatureOnlineStoreDedicatedServingEndpoint.md) |  |  [optional] |
|**embeddingManagement** | [**GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagement**](GoogleCloudAiplatformV1beta1FeatureOnlineStoreEmbeddingManagement.md) |  |  [optional] |
|**etag** | **String** | Optional. Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata to organize your FeatureOnlineStore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. |  [optional] |
|**name** | **String** | Identifier. Name of the FeatureOnlineStore. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}&#x60; |  [optional] |
|**optimized** | **Object** | Optimized storage type |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the featureOnlineStore. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when this FeatureOnlineStore was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| STABLE | &quot;STABLE&quot; |
| UPDATING | &quot;UPDATING&quot; |



