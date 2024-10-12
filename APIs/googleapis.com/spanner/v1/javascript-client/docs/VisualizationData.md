# CloudSpannerApi.VisualizationData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSourceEndToken** | **String** | The token signifying the end of a data_source. | [optional] 
**dataSourceSeparatorToken** | **String** | The token delimiting a datasource name from the rest of a key in a data_source. | [optional] 
**diagnosticMessages** | [**[DiagnosticMessage]**](DiagnosticMessage.md) | The list of messages (info, alerts, ...) | [optional] 
**endKeyStrings** | **[String]** | We discretize the entire keyspace into buckets. Assuming each bucket has an inclusive keyrange and covers keys from k(i) ... k(n). In this case k(n) would be an end key for a given range. end_key_string is the collection of all such end keys | [optional] 
**hasPii** | **Boolean** | Whether this scan contains PII. | [optional] 
**indexedKeys** | **[String]** | Keys of key ranges that contribute significantly to a given metric Can be thought of as heavy hitters. | [optional] 
**keySeparator** | **String** | The token delimiting the key prefixes. | [optional] 
**keyUnit** | **String** | The unit for the key: e.g. &#39;key&#39; or &#39;chunk&#39;. | [optional] 
**metrics** | [**[Metric]**](Metric.md) | The list of data objects for each metric. | [optional] 
**prefixNodes** | [**[PrefixNode]**](PrefixNode.md) | The list of extracted key prefix nodes used in the key prefix hierarchy. | [optional] 



## Enum: KeyUnitEnum


* `KEY_UNIT_UNSPECIFIED` (value: `"KEY_UNIT_UNSPECIFIED"`)

* `KEY` (value: `"KEY"`)

* `CHUNK` (value: `"CHUNK"`)




