# ServiceControlApi.ExplicitBuckets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounds** | **[Number]** | &#39;bound&#39; is a list of strictly increasing boundaries between buckets. Note that a list of length N-1 defines N buckets because of fenceposting. See comments on &#x60;bucket_options&#x60; for details. The i&#39;th finite bucket covers the interval [bound[i-1], bound[i]) where i ranges from 1 to bound_size() - 1. Note that there are no finite buckets at all if &#39;bound&#39; only contains a single element; in that special case the single bound defines the boundary between the underflow and overflow buckets. bucket number lower bound upper bound i &#x3D;&#x3D; 0 (underflow) -inf bound[i] 0 &lt; i &lt; bound_size() bound[i-1] bound[i] i &#x3D;&#x3D; bound_size() (overflow) bound[i-1] +inf | [optional] 


