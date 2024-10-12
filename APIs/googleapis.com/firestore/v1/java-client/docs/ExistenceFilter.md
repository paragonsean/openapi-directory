

# ExistenceFilter

A digest of all the documents that match a given target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | The total count of documents that match target_id. If different from the count of documents in the client that match, the client must manually determine which documents no longer match the target. The client can use the &#x60;unchanged_names&#x60; bloom filter to assist with this determination by testing ALL the document names against the filter; if the document name is NOT in the filter, it means the document no longer matches the target. |  [optional] |
|**targetId** | **Integer** | The target ID to which this filter applies. |  [optional] |
|**unchangedNames** | [**BloomFilter**](BloomFilter.md) |  |  [optional] |



