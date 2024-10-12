

# QueueingPolicy

Defines the policy of the QueuedRequest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**validAfterDuration** | **String** | A relative time after which resources may be created. |  [optional] |
|**validAfterTime** | **String** | An absolute time at which resources may be created. |  [optional] |
|**validInterval** | [**Interval**](Interval.md) |  |  [optional] |
|**validUntilDuration** | **String** | A relative time after which resources should not be created. If the request cannot be fulfilled by this time the request will be failed. |  [optional] |
|**validUntilTime** | **String** | An absolute time after which resources should not be created. If the request cannot be fulfilled by this time the request will be failed. |  [optional] |



