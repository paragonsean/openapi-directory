# GoogleAnalyticsDataApi.SamplingMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samplesReadCount** | **String** | The total number of events read in this sampled report for a date range. This is the size of the subset this property&#39;s data that was analyzed in this report. | [optional] 
**samplingSpaceSize** | **String** | The total number of events present in this property&#39;s data that could have been analyzed in this report for a date range. Sampling uncovers the meaningful information about the larger data set, and this is the size of the larger data set. To calculate the percentage of available data that was used in this report, compute &#x60;samplesReadCount/samplingSpaceSize&#x60;. | [optional] 


