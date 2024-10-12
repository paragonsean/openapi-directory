

# VisualizationData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceEndToken** | **String** | The token signifying the end of a data_source. |  [optional] |
|**dataSourceSeparatorToken** | **String** | The token delimiting a datasource name from the rest of a key in a data_source. |  [optional] |
|**diagnosticMessages** | [**List&lt;DiagnosticMessage&gt;**](DiagnosticMessage.md) | The list of messages (info, alerts, ...) |  [optional] |
|**endKeyStrings** | **List&lt;String&gt;** | We discretize the entire keyspace into buckets. Assuming each bucket has an inclusive keyrange and covers keys from k(i) ... k(n). In this case k(n) would be an end key for a given range. end_key_string is the collection of all such end keys |  [optional] |
|**hasPii** | **Boolean** | Whether this scan contains PII. |  [optional] |
|**indexedKeys** | **List&lt;String&gt;** | Keys of key ranges that contribute significantly to a given metric Can be thought of as heavy hitters. |  [optional] |
|**keySeparator** | **String** | The token delimiting the key prefixes. |  [optional] |
|**keyUnit** | [**KeyUnitEnum**](#KeyUnitEnum) | The unit for the key: e.g. &#39;key&#39; or &#39;chunk&#39;. |  [optional] |
|**metrics** | [**List&lt;Metric&gt;**](Metric.md) | The list of data objects for each metric. |  [optional] |
|**prefixNodes** | [**List&lt;PrefixNode&gt;**](PrefixNode.md) | The list of extracted key prefix nodes used in the key prefix hierarchy. |  [optional] |



## Enum: KeyUnitEnum

| Name | Value |
|---- | -----|
| KEY_UNIT_UNSPECIFIED | &quot;KEY_UNIT_UNSPECIFIED&quot; |
| KEY | &quot;KEY&quot; |
| CHUNK | &quot;CHUNK&quot; |



