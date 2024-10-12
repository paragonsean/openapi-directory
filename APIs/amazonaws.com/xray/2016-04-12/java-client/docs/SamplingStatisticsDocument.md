

# SamplingStatisticsDocument

Request sampling results for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to <a href=\"https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html\">GetSamplingTargets</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ruleName** | [**String**](String.md) |  |  |
|**clientID** | [**String**](String.md) |  |  |
|**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**requestCount** | [**Integer**](Integer.md) |  |  |
|**sampledCount** | [**Integer**](Integer.md) |  |  |
|**borrowCount** | [**Integer**](Integer.md) |  |  [optional] |



