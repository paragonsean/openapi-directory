# AzureMediaServices.StreamingLocatorProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternativeMediaId** | **String** | Alternative Media ID of this Streaming Locator | [optional] 
**assetName** | **String** | Asset Name | 
**contentKeys** | [**[StreamingLocatorContentKey]**](StreamingLocatorContentKey.md) | The ContentKeys used by this Streaming Locator. | [optional] 
**created** | **Date** | The creation time of the Streaming Locator. | [optional] [readonly] 
**defaultContentKeyPolicyName** | **String** | Name of the default ContentKeyPolicy used by this Streaming Locator. | [optional] 
**endTime** | **Date** | The end time of the Streaming Locator. | [optional] 
**filters** | **[String]** | A list of asset or account filters which apply to this streaming locator | [optional] 
**startTime** | **Date** | The start time of the Streaming Locator. | [optional] 
**streamingLocatorId** | **String** | The StreamingLocatorId of the Streaming Locator. | [optional] 
**streamingPolicyName** | **String** | Name of the Streaming Policy used by this Streaming Locator. Either specify the name of Streaming Policy you created or use one of the predefined Streaming Policies. The predefined Streaming Policies available are: &#39;Predefined_DownloadOnly&#39;, &#39;Predefined_ClearStreamingOnly&#39;, &#39;Predefined_DownloadAndClearStreaming&#39;, &#39;Predefined_ClearKey&#39;, &#39;Predefined_MultiDrmCencStreaming&#39; and &#39;Predefined_MultiDrmStreaming&#39; | 


