

# InstancesRequestBatchGetOrDelete

Request to get or delete instances by time series IDs or time series names. Exactly one of \"timeSeriesIds\" or \"names\" must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**names** | **List&lt;String&gt;** | List of names of the time series instances to return or delete. |  [optional] |
|**timeSeriesIds** | **List&lt;List&lt;Object&gt;&gt;** | List of time series IDs of the time series instances to return or delete. |  [optional] |



