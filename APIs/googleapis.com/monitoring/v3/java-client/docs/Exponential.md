

# Exponential

Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.There are num_finite_buckets + 2 (= N) buckets. Bucket i has the following boundaries:Upper bound (0 <= i < N-1): scale * (growth_factor ^ i).Lower bound (1 <= i < N): scale * (growth_factor ^ (i - 1)).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**growthFactor** | **Double** | Must be greater than 1. |  [optional] |
|**numFiniteBuckets** | **Integer** | Must be greater than 0. |  [optional] |
|**scale** | **Double** | Must be greater than 0. |  [optional] |



