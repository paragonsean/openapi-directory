

# HttpRouteFaultInjectionPolicyAbort

Specification of how client requests are aborted as part of fault injection before being sent to a destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**httpStatus** | **Integer** | The HTTP status code used to abort the request. The value must be between 200 and 599 inclusive. |  [optional] |
|**percentage** | **Integer** | The percentage of traffic which will be aborted. The value must be between [0, 100] |  [optional] |



