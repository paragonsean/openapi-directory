# DataflowApi.DataflowHistogramValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketCounts** | **[String]** | Optional. The number of values in each bucket of the histogram, as described in &#x60;bucket_options&#x60;. &#x60;bucket_counts&#x60; should contain N values, where N is the number of buckets specified in &#x60;bucket_options&#x60;. If &#x60;bucket_counts&#x60; has fewer than N values, the remaining values are assumed to be 0. | [optional] 
**bucketOptions** | [**BucketOptions**](BucketOptions.md) |  | [optional] 
**count** | **String** | Number of values recorded in this histogram. | [optional] 
**outlierStats** | [**OutlierStats**](OutlierStats.md) |  | [optional] 


