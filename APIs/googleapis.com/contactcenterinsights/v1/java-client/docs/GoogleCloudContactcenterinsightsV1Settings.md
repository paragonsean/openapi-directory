

# GoogleCloudContactcenterinsightsV1Settings

The settings resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisConfig** | [**GoogleCloudContactcenterinsightsV1SettingsAnalysisConfig**](GoogleCloudContactcenterinsightsV1SettingsAnalysisConfig.md) |  |  [optional] |
|**conversationTtl** | **String** | The default TTL for newly-created conversations. If a conversation has a specified expiration, that value will be used instead. Changing this value will not change the expiration of existing conversations. Conversations with no expire time persist until they are deleted. |  [optional] |
|**createTime** | **String** | Output only. The time at which the settings was created. |  [optional] [readonly] |
|**languageCode** | **String** | A language code to be applied to each transcript segment unless the segment already specifies a language code. Language code defaults to \&quot;en-US\&quot; if it is neither specified on the segment nor here. |  [optional] |
|**name** | **String** | Immutable. The resource name of the settings resource. Format: projects/{project}/locations/{location}/settings |  [optional] |
|**pubsubNotificationSettings** | **Map&lt;String, String&gt;** | A map that maps a notification trigger to a Pub/Sub topic. Each time a specified trigger occurs, Insights will notify the corresponding Pub/Sub topic. Keys are notification triggers. Supported keys are: * \&quot;all-triggers\&quot;: Notify each time any of the supported triggers occurs. * \&quot;create-analysis\&quot;: Notify each time an analysis is created. * \&quot;create-conversation\&quot;: Notify each time a conversation is created. * \&quot;export-insights-data\&quot;: Notify each time an export is complete. * \&quot;update-conversation\&quot;: Notify each time a conversation is updated via UpdateConversation. * \&quot;upload-conversation\&quot;: Notify when an UploadConversation LRO completes. Values are Pub/Sub topics. The format of each Pub/Sub topic is: projects/{project}/topics/{topic} |  [optional] |
|**redactionConfig** | [**GoogleCloudContactcenterinsightsV1RedactionConfig**](GoogleCloudContactcenterinsightsV1RedactionConfig.md) |  |  [optional] |
|**speechConfig** | [**GoogleCloudContactcenterinsightsV1SpeechConfig**](GoogleCloudContactcenterinsightsV1SpeechConfig.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time at which the settings were last updated. |  [optional] [readonly] |



