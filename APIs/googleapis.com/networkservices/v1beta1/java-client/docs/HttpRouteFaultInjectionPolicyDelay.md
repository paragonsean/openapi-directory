

# HttpRouteFaultInjectionPolicyDelay

Specification of how client requests are delayed as part of fault injection before being sent to a destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fixedDelay** | **String** | Specify a fixed delay before forwarding the request. |  [optional] |
|**percentage** | **Integer** | The percentage of traffic on which delay will be injected. The value must be between [0, 100] |  [optional] |



