# Semantria.Statistic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callsData** | **Number** | Total number of data API calls made. These affect you API balance | 
**callsPolling** | **Number** | Total number of polling API calls made. These do not affect API balance | 
**callsSettings** | **Number** | Total number of settings API calls made. These do not affect API balance | 
**collsDocuments** | **Number** | Total number of documents that have been queued into collections | 
**collsFailed** | **Number** | Total number of collections that have failed to be processed | 
**collsProcessed** | **Number** | Total numbers of collections that have been successfully processed | 
**collsResponded** | **Number** | Total number of successfully processed collections that have been returned | 
**configurations** | [**[StatisticConfiguration]**](StatisticConfiguration.md) | Includes statistics per specific configuration | 
**docsFailed** | **Number** | Total number of documents that have failed to be processed | 
**docsProcessed** | **Number** | Total number of documents that have been successfully processed | 
**docsResponded** | **Number** | Total number of successfully processed documents that have been returned | 
**latestUsedApp** | **String** | The latest application that used the API on this account | 
**name** | **String** | Semantria subscriber name. Usually email | 
**overallBatches** | **Number** | Total number of queued batches of texts processed | 
**overallCalls** | **Number** | Total number of API calls made | 
**overallDocs** | **Number** | Total number of documents that have been queued | 
**overallExceeded** | **Number** | Total number of documents that have exceeded the favorable (suggested) limit | 
**overallTexts** | **Number** | Total number of texts processed | 
**overcallColls** | **Number** | Total numbers of collections that have been queued | 
**status** | **String** | Semantria subscriber status. Can be active, expired, disabled, etc | 
**usedApps** | **String** | A list of all the applications that have used the API on this account | 


