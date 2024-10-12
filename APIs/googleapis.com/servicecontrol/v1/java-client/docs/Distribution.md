

# Distribution

Distribution represents a frequency distribution of double-valued sample points. It contains the size of the population of sample points plus additional optional information: * the arithmetic mean of the samples * the minimum and maximum of the samples * the sum-squared-deviation of the samples, used to compute variance * a histogram of the values of the sample points

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketCounts** | **List&lt;String&gt;** | The number of samples in each histogram bucket. &#x60;bucket_counts&#x60; are optional. If present, they must sum to the &#x60;count&#x60; value. The buckets are defined below in &#x60;bucket_option&#x60;. There are N buckets. &#x60;bucket_counts[0]&#x60; is the number of samples in the underflow bucket. &#x60;bucket_counts[1]&#x60; to &#x60;bucket_counts[N-1]&#x60; are the numbers of samples in each of the finite buckets. And &#x60;bucket_counts[N] is the number of samples in the overflow bucket. See the comments of &#x60;bucket_option&#x60; below for more details. Any suffix of trailing zeros may be omitted. |  [optional] |
|**count** | **String** | The total number of samples in the distribution. Must be &gt;&#x3D; 0. |  [optional] |
|**exemplars** | [**List&lt;Exemplar&gt;**](Exemplar.md) | Example points. Must be in increasing order of &#x60;value&#x60; field. |  [optional] |
|**explicitBuckets** | [**ExplicitBuckets**](ExplicitBuckets.md) |  |  [optional] |
|**exponentialBuckets** | [**ExponentialBuckets**](ExponentialBuckets.md) |  |  [optional] |
|**linearBuckets** | [**LinearBuckets**](LinearBuckets.md) |  |  [optional] |
|**maximum** | **Double** | The maximum of the population of values. Ignored if &#x60;count&#x60; is zero. |  [optional] |
|**mean** | **Double** | The arithmetic mean of the samples in the distribution. If &#x60;count&#x60; is zero then this field must be zero. |  [optional] |
|**minimum** | **Double** | The minimum of the population of values. Ignored if &#x60;count&#x60; is zero. |  [optional] |
|**sumOfSquaredDeviation** | **Double** | The sum of squared deviations from the mean: Sum[i&#x3D;1..count]((x_i - mean)^2) where each x_i is a sample values. If &#x60;count&#x60; is zero then this field must be zero, otherwise validation of the request fails. |  [optional] |



