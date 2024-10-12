

# PropertyQuota

Current state of all quotas for this Analytics Property. If any quota for a property is exhausted, all requests to that property will return Resource Exhausted errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**concurrentRequests** | [**QuotaStatus**](QuotaStatus.md) |  |  [optional] |
|**potentiallyThresholdedRequestsPerHour** | [**QuotaStatus**](QuotaStatus.md) |  |  [optional] |
|**serverErrorsPerProjectPerHour** | [**QuotaStatus**](QuotaStatus.md) |  |  [optional] |
|**tokensPerDay** | [**QuotaStatus**](QuotaStatus.md) |  |  [optional] |
|**tokensPerHour** | [**QuotaStatus**](QuotaStatus.md) |  |  [optional] |
|**tokensPerProjectPerHour** | [**QuotaStatus**](QuotaStatus.md) |  |  [optional] |



