

# StreamingLocatorProperties

Class to specify properties of Streaming Locator

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternativeMediaId** | **String** | An Alternative Media Identifier associated with the StreamingLocator.  This identifier can be used to distinguish different StreamingLocators for the same Asset for authorization purposes in the CustomLicenseAcquisitionUrlTemplate or the CustomKeyAcquisitionUrlTemplate of the StreamingPolicy specified in the StreamingPolicyName field. |  [optional] |
|**assetName** | **String** | Asset Name |  |
|**contentKeys** | [**List&lt;StreamingLocatorContentKey&gt;**](StreamingLocatorContentKey.md) | ContentKeys used by this Streaming Locator |  [optional] |
|**created** | **OffsetDateTime** | Creation time of Streaming Locator |  [optional] [readonly] |
|**defaultContentKeyPolicyName** | **String** | Default ContentKeyPolicy used by this Streaming Locator |  [optional] |
|**endTime** | **OffsetDateTime** | EndTime of Streaming Locator |  [optional] |
|**startTime** | **OffsetDateTime** | StartTime of Streaming Locator |  [optional] |
|**streamingLocatorId** | **UUID** | StreamingLocatorId of Streaming Locator |  [optional] |
|**streamingPolicyName** | **String** | Streaming policy name used by this streaming locator. Either specify the name of streaming policy you created or use one of the predefined streaming polices. The predefined streaming policies available are: &#39;Predefined_DownloadOnly&#39;, &#39;Predefined_ClearStreamingOnly&#39;, &#39;Predefined_DownloadAndClearStreaming&#39;, &#39;Predefined_ClearKey&#39;, &#39;Predefined_SecureStreaming&#39; and &#39;Predefined_SecureStreamingWithFairPlay&#39; |  |



