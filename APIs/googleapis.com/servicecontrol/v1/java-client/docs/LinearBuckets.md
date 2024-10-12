

# LinearBuckets

Describing buckets with constant width.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numFiniteBuckets** | **Integer** | The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is &#x60;num_finite_buckets&#x60; + 2. See comments on &#x60;bucket_options&#x60; for details. |  [optional] |
|**offset** | **Double** | The i&#39;th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive. |  [optional] |
|**width** | **Double** | The i&#39;th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive. Must be strictly positive. |  [optional] |



