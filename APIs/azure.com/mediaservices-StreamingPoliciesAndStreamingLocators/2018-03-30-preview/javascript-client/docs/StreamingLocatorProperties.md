# AzureMediaServices.StreamingLocatorProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetName** | **String** | Asset Name | 
**contentKeys** | [**[StreamingLocatorUserDefinedContentKey]**](StreamingLocatorUserDefinedContentKey.md) | ContentKeys used by this Streaming Locator | [optional] 
**created** | **Date** | Creation time of Streaming Locator | [optional] [readonly] 
**defaultContentKeyPolicyName** | **String** | Default ContentKeyPolicy used by this Streaming Locator | [optional] 
**endTime** | **Date** | EndTime of Streaming Locator | [optional] 
**startTime** | **Date** | StartTime of Streaming Locator | [optional] 
**streamingLocatorId** | **String** | StreamingLocatorId of Streaming Locator | [optional] 
**streamingPolicyName** | **String** | Streaming policy name used by this streaming locator. Either specify the name of streaming policy you created or use one of the predefined streaming polices. The predefined streaming policies available are: &#39;Predefined_DownloadOnly&#39;, &#39;Predefined_ClearStreamingOnly&#39;, &#39;Predefined_DownloadAndClearStreaming&#39;, &#39;Predefined_ClearKey&#39;, &#39;Predefined_SecureStreaming&#39; and &#39;Predefined_SecureStreamingWithFairPlay&#39; | 


