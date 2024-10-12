

# Trigger

Specifies how many time series must fail a predicate to trigger a condition. If not specified, then a {count: 1} trigger is used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | The absolute number of time series that must fail the predicate for the condition to be triggered. |  [optional] |
|**percent** | **Double** | The percentage of time series that must fail the predicate for the condition to be triggered. |  [optional] |



