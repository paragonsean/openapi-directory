# CloudDatastoreApi.Count

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upTo** | **String** | Optional. Optional constraint on the maximum number of entities to count. This provides a way to set an upper bound on the number of entities to scan, limiting latency, and cost. Unspecified is interpreted as no bound. If a zero value is provided, a count result of zero should always be expected. High-Level Example: &#x60;&#x60;&#x60; AGGREGATE COUNT_UP_TO(1000) OVER ( SELECT * FROM k ); &#x60;&#x60;&#x60; Requires: * Must be non-negative when present. | [optional] 


