# TextAnalyticsClient.SentimentBatchResultItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique, non-empty document identifier. | [optional] 
**score** | **Number** | A decimal number between 0 and 1 denoting the sentiment of the document. A score above 0.7 usually refers to a positive document while a score below 0.3 normally has a negative connotation. Mid values refer to neutral text. | [optional] 
**statistics** | [**DocumentStatistics**](DocumentStatistics.md) |  | [optional] 


