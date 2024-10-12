# DataflowApi.Histogram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketCounts** | **[String]** | Counts of values in each bucket. For efficiency, prefix and trailing buckets with count &#x3D; 0 are elided. Buckets can store the full range of values of an unsigned long, with ULLONG_MAX falling into the 59th bucket with range [1e19, 2e19). | [optional] 
**firstBucketOffset** | **Number** | Starting index of first stored bucket. The non-inclusive upper-bound of the ith bucket is given by: pow(10,(i-first_bucket_offset)/3) * (1,2,5)[(i-first_bucket_offset)%3] | [optional] 


