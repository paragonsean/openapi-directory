# ServiceControlApi.LinearBuckets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numFiniteBuckets** | **Number** | The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is &#x60;num_finite_buckets&#x60; + 2. See comments on &#x60;bucket_options&#x60; for details. | [optional] 
**offset** | **Number** | The i&#39;th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive. | [optional] 
**width** | **Number** | The i&#39;th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive. Must be strictly positive. | [optional] 


