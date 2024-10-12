

# TypesRequestBatchGetOrDelete

Request to get or delete time series types by IDs or type names. Exactly one of \"typeIds\" or \"names\" must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**names** | **List&lt;String&gt;** | List of names of time series types to return or delete. |  [optional] |
|**typeIds** | **List&lt;UUID&gt;** | List of IDs of time series types to return or delete. |  [optional] |



