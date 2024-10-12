# CloudFirestoreApi.Count

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upTo** | **String** | Optional. Optional constraint on the maximum number of documents to count. This provides a way to set an upper bound on the number of documents to scan, limiting latency, and cost. Unspecified is interpreted as no bound. High-Level Example: &#x60;&#x60;&#x60; AGGREGATE COUNT_UP_TO(1000) OVER ( SELECT * FROM k ); &#x60;&#x60;&#x60; Requires: * Must be greater than zero when present. | [optional] 


