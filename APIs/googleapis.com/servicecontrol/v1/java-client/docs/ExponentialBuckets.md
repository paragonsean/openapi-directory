

# ExponentialBuckets

Describing buckets with exponentially growing width.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**growthFactor** | **Double** | The i&#39;th exponential bucket covers the interval [scale * growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to num_finite_buckets inclusive. Must be larger than 1.0. |  [optional] |
|**numFiniteBuckets** | **Integer** | The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is &#x60;num_finite_buckets&#x60; + 2. See comments on &#x60;bucket_options&#x60; for details. |  [optional] |
|**scale** | **Double** | The i&#39;th exponential bucket covers the interval [scale * growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to num_finite_buckets inclusive. Must be &gt; 0. |  [optional] |



