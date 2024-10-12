# VertexAiApi.GoogleCloudAiplatformV1FeatureOnlineStore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigtable** | [**GoogleCloudAiplatformV1FeatureOnlineStoreBigtable**](GoogleCloudAiplatformV1FeatureOnlineStoreBigtable.md) |  | [optional] 
**createTime** | **String** | Output only. Timestamp when this FeatureOnlineStore was created. | [optional] [readonly] 
**etag** | **String** | Optional. Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | Optional. The labels with user-defined metadata to organize your FeatureOnlineStore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded).\&quot; System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. | [optional] 
**name** | **String** | Identifier. Name of the FeatureOnlineStore. Format: &#x60;projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}&#x60; | [optional] 
**state** | **String** | Output only. State of the featureOnlineStore. | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when this FeatureOnlineStore was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `STABLE` (value: `"STABLE"`)

* `UPDATING` (value: `"UPDATING"`)




