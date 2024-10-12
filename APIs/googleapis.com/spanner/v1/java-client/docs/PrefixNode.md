

# PrefixNode

A message representing a key prefix node in the key prefix hierarchy. for eg. Bigtable keyspaces are lexicographically ordered mappings of keys to values. Keys often have a shared prefix structure where users use the keys to organize data. Eg ///employee In this case Keysight will possibly use one node for a company and reuse it for all employees that fall under the company. Doing so improves legibility in the UI.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceNode** | **Boolean** | Whether this corresponds to a data_source name. |  [optional] |
|**depth** | **Integer** | The depth in the prefix hierarchy. |  [optional] |
|**endIndex** | **Integer** | The index of the end key bucket of the range that this node spans. |  [optional] |
|**startIndex** | **Integer** | The index of the start key bucket of the range that this node spans. |  [optional] |
|**word** | **String** | The string represented by the prefix node. |  [optional] |



