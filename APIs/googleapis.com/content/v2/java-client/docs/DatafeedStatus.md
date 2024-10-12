

# DatafeedStatus

The status of a datafeed, i.e., the result of the last retrieval of the datafeed computed asynchronously when the feed processing is finished.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | The country for which the status is reported, represented as a CLDR territory code. |  [optional] |
|**datafeedId** | **String** | The ID of the feed for which the status is reported. |  [optional] |
|**errors** | [**List&lt;DatafeedStatusError&gt;**](DatafeedStatusError.md) | The list of errors occurring in the feed. |  [optional] |
|**itemsTotal** | **String** | The number of items in the feed that were processed. |  [optional] |
|**itemsValid** | **String** | The number of items in the feed that were valid. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#datafeedStatus&#x60;\&quot; |  [optional] |
|**language** | **String** | The two-letter ISO 639-1 language for which the status is reported. |  [optional] |
|**lastUploadDate** | **String** | The last date at which the feed was uploaded. |  [optional] |
|**processingStatus** | **String** | The processing status of the feed. Acceptable values are: - \&quot;&#x60;\&quot;&#x60;failure&#x60;\&quot;: The feed could not be processed or all items had errors.&#x60;\&quot; - \&quot;&#x60;in progress&#x60;\&quot;: The feed is being processed. - \&quot;&#x60;none&#x60;\&quot;: The feed has not yet been processed. For example, a feed that has never been uploaded will have this processing status. - \&quot;&#x60;success&#x60;\&quot;: The feed was processed successfully, though some items might have had errors.  |  [optional] |
|**warnings** | [**List&lt;DatafeedStatusError&gt;**](DatafeedStatusError.md) | The list of errors occurring in the feed. |  [optional] |



