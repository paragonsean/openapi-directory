

# SplitInt64

A representation of an int64, n, that is immune to precision loss when encoded in JSON.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**highBits** | **Integer** | The high order bits, including the sign: n &gt;&gt; 32. |  [optional] |
|**lowBits** | **Integer** | The low order bits: n &amp; 0xffffffff. |  [optional] |



