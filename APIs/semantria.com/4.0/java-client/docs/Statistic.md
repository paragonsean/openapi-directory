

# Statistic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callsData** | **Integer** | Total number of data API calls made. These affect you API balance |  |
|**callsPolling** | **Integer** | Total number of polling API calls made. These do not affect API balance |  |
|**callsSettings** | **Integer** | Total number of settings API calls made. These do not affect API balance |  |
|**collsDocuments** | **Integer** | Total number of documents that have been queued into collections |  |
|**collsFailed** | **Integer** | Total number of collections that have failed to be processed |  |
|**collsProcessed** | **Integer** | Total numbers of collections that have been successfully processed |  |
|**collsResponded** | **Integer** | Total number of successfully processed collections that have been returned |  |
|**configurations** | [**List&lt;StatisticConfiguration&gt;**](StatisticConfiguration.md) | Includes statistics per specific configuration |  |
|**docsFailed** | **Integer** | Total number of documents that have failed to be processed |  |
|**docsProcessed** | **Integer** | Total number of documents that have been successfully processed |  |
|**docsResponded** | **Integer** | Total number of successfully processed documents that have been returned |  |
|**latestUsedApp** | **String** | The latest application that used the API on this account |  |
|**name** | **String** | Semantria subscriber name. Usually email |  |
|**overallBatches** | **Integer** | Total number of queued batches of texts processed |  |
|**overallCalls** | **Integer** | Total number of API calls made |  |
|**overallDocs** | **Integer** | Total number of documents that have been queued |  |
|**overallExceeded** | **Integer** | Total number of documents that have exceeded the favorable (suggested) limit |  |
|**overallTexts** | **Integer** | Total number of texts processed |  |
|**overcallColls** | **Integer** | Total numbers of collections that have been queued |  |
|**status** | **String** | Semantria subscriber status. Can be active, expired, disabled, etc |  |
|**usedApps** | **String** | A list of all the applications that have used the API on this account |  |



