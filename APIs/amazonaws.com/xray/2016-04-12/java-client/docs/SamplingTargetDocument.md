

# SamplingTargetDocument

Temporary changes to a sampling rule configuration. To meet the global sampling target for a rule, X-Ray calculates a new reservoir for each service based on the recent sampling results of all services that called <a href=\"https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html\">GetSamplingTargets</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ruleName** | [**String**](String.md) |  |  [optional] |
|**fixedRate** | [**Double**](Double.md) |  |  [optional] |
|**reservoirQuota** | [**Integer**](Integer.md) |  |  [optional] |
|**reservoirQuotaTTL** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**interval** | [**Integer**](Integer.md) |  |  [optional] |



