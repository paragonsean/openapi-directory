

# GoogleCloudAiplatformV1beta1FeatureGroup

Vertex AI Feature Group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigQuery** | [**GoogleCloudAiplatformV1beta1FeatureGroupBigQuery**](GoogleCloudAiplatformV1beta1FeatureGroupBigQuery.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp when this FeatureGroup was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the FeatureGroup. |  [optional] |
|**etag** | **String** | Optional. Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels with user-defined metadata to organize your FeatureGroup. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureGroup(System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. |  [optional] |
|**name** | **String** | Identifier. Name of the FeatureGroup. Format: &#x60;projects/{project}/locations/{location}/featureGroups/{featureGroup}&#x60; |  [optional] |
|**updateTime** | **String** | Output only. Timestamp when this FeatureGroup was last updated. |  [optional] [readonly] |



