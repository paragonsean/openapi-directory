# SensitiveDataProtectionDlp.GooglePrivacyDlpV2HybridInspectStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abortedCount** | **String** | The number of hybrid inspection requests aborted because the job ran out of quota or was ended before they could be processed. | [optional] 
**pendingCount** | **String** | The number of hybrid requests currently being processed. Only populated when called via method &#x60;getDlpJob&#x60;. A burst of traffic may cause hybrid inspect requests to be enqueued. Processing will take place as quickly as possible, but resource limitations may impact how long a request is enqueued for. | [optional] 
**processedCount** | **String** | The number of hybrid inspection requests processed within this job. | [optional] 


