

# DataflowHistogramValue

Summary statistics for a population of values. HistogramValue contains a sequence of buckets and gives a count of values that fall into each bucket. Bucket boundares are defined by a formula and bucket widths are either fixed or exponentially increasing.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketCounts** | **List&lt;String&gt;** | Optional. The number of values in each bucket of the histogram, as described in &#x60;bucket_options&#x60;. &#x60;bucket_counts&#x60; should contain N values, where N is the number of buckets specified in &#x60;bucket_options&#x60;. If &#x60;bucket_counts&#x60; has fewer than N values, the remaining values are assumed to be 0. |  [optional] |
|**bucketOptions** | [**BucketOptions**](BucketOptions.md) |  |  [optional] |
|**count** | **String** | Number of values recorded in this histogram. |  [optional] |
|**outlierStats** | [**OutlierStats**](OutlierStats.md) |  |  [optional] |



