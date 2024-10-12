# CloudAutoMlApi.Float64Stats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**histogramBuckets** | [**[HistogramBucket]**](HistogramBucket.md) | Histogram buckets of the data series. Sorted by the min value of the bucket, ascendingly, and the number of the buckets is dynamically generated. The buckets are non-overlapping and completely cover whole FLOAT64 range with min of first bucket being &#x60;\&quot;-Infinity\&quot;&#x60;, and max of the last one being &#x60;\&quot;Infinity\&quot;&#x60;. | [optional] 
**mean** | **Number** | The mean of the series. | [optional] 
**quantiles** | **[Number]** | Ordered from 0 to k k-quantile values of the data series of n values. The value at index i is, approximately, the i*n/k-th smallest value in the series; for i &#x3D; 0 and i &#x3D; k these are, respectively, the min and max values. | [optional] 
**standardDeviation** | **Number** | The standard deviation of the series. | [optional] 


