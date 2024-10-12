

# BloomFilter

A bloom filter (https://en.wikipedia.org/wiki/Bloom_filter). The bloom filter hashes the entries with MD5 and treats the resulting 128-bit hash as 2 distinct 64-bit hash values, interpreted as unsigned integers using 2's complement encoding. These two hash values, named `h1` and `h2`, are then used to compute the `hash_count` hash values using the formula, starting at `i=0`: h(i) = h1 + (i * h2) These resulting values are then taken modulo the number of bits in the bloom filter to get the bits of the bloom filter to test for the given entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bits** | [**BitSequence**](BitSequence.md) |  |  [optional] |
|**hashCount** | **Integer** | The number of hashes used by the algorithm. |  [optional] |



