# TurbineLabsApi.CohortSeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the cookie, the header field, or the query argument to be checked for a cohort seed value.  | [optional] 
**type** | **String** | Where a request&#39;s cohort seed will be drawn from. | [optional] 
**useZeroValueSeed** | **Boolean** | If true, requests with a seed source which resolves to an empty value will still be grouped and routed consistently. This means a misspelled or missing seed source on a request will sort all such traffic into a single backend. This could result in all traffic being assigned to a backend intended for only a small percentage of traffic. Use with caution.  | [optional] 



## Enum: TypeEnum


* `header` (value: `"header"`)

* `cookie` (value: `"cookie"`)

* `query` (value: `"query"`)




