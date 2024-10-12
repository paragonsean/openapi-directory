

# Base2Exponent

Exponential buckets where the growth factor between buckets is `2**(2**-scale)`. e.g. for `scale=1` growth factor is `2**(2**(-1))=sqrt(2)`. `n` buckets will have the following boundaries. - 0th: [0, gf) - i in [1, n-1]: [gf^(i), gf^(i+1))

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numberOfBuckets** | **Integer** | Must be greater than 0. |  [optional] |
|**scale** | **Integer** | Must be between -3 and 3. This forces the growth factor of the bucket boundaries to be between &#x60;2^(1/8)&#x60; and &#x60;256&#x60;. |  [optional] |



