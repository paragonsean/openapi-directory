# BeezUpMerchantApi.PublicationFeedReporting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **Boolean** | Indicates if the publication is completed or not | [optional] 
**endUtcDate** | **Date** | The feed publication end time (UTC timezone) | [optional] 
**errorMessage** | **String** | The error message | [optional] 
**exportedProducts** | **Number** | The product count downloaded from BeezUP Export | [optional] 
**failedItems** | **Number** | The item count (products or offers) the marketplace flagged as failed | [optional] 
**feedType** | [**FeedType**](FeedType.md) |  | 
**htmlReportGenerationErrorMessage** | **String** | The error message if the Html Report generation failed | [optional] 
**htmlReportUrl** | **String** | The Url for the Html Report generated | [optional] 
**processingStatus** | **String** | The processing status | 
**publishedItems** | **Number** | The item count (products or offers) the marketplace flagged as successful | [optional] 
**publishedItemsWithWarning** | **Number** | The item count (products or offers) the marketplace flagged as successful with warnings | [optional] 
**startUtcDate** | **Date** | The feed publication start time (UTC timezone) | 
**transmittedItems** | **Number** | The item count (products or offers) sent to the marketplace | [optional] 


