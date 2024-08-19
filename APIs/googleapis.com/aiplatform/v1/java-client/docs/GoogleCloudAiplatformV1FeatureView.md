

# GoogleCloudAiplatformV1FeatureView

FeatureView is representation of values that the FeatureOnlineStore will serve based on its syncConfig.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigQuerySource** | [**GoogleCloudAiplatformV1FeatureViewBigQuerySource**](GoogleCloudAiplatformV1FeatureViewBigQuerySource.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp when this FeatureView was created. |  [optional] [readonly] |
|**etag** | **String** | Optional. Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**featureRegistrySource** | [**GoogleCloudAiplatformV1FeatureViewFeatureRegistrySource**](GoogleCloudAiplatformV1FeatureViewFeatureRegistrySource.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata to organize your FeatureViews. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. |  [optional] |
|**name** | **String** | Identifier. Name of the FeatureView. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}&#x60; |  [optional] |
|**syncConfig** | [**GoogleCloudAiplatformV1FeatureViewSyncConfig**](GoogleCloudAiplatformV1FeatureViewSyncConfig.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Timestamp when this FeatureView was last updated. |  [optional] [readonly] |



