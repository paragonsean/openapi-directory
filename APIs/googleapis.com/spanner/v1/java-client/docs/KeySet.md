

# KeySet

`KeySet` defines a collection of Cloud Spanner keys and/or key ranges. All the keys are expected to be in the same table or index. The keys need not be sorted in any particular way. If the same key is specified multiple times in the set (for example if two ranges, two keys, or a key and a range overlap), Cloud Spanner behaves as if the key were only specified once.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**all** | **Boolean** | For convenience &#x60;all&#x60; can be set to &#x60;true&#x60; to indicate that this &#x60;KeySet&#x60; matches all keys in the table or index. Note that any keys specified in &#x60;keys&#x60; or &#x60;ranges&#x60; are only yielded once. |  [optional] |
|**keys** | **List&lt;List&lt;Object&gt;&gt;** | A list of specific keys. Entries in &#x60;keys&#x60; should have exactly as many elements as there are columns in the primary or index key with which this &#x60;KeySet&#x60; is used. Individual key values are encoded as described here. |  [optional] |
|**ranges** | [**List&lt;KeyRange&gt;**](KeyRange.md) | A list of key ranges. See KeyRange for more information about key range specifications. |  [optional] |



