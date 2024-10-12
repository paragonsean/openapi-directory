

# Insight

When fault rates go outside of the expected range, X-Ray creates an insight. Insights tracks emergent issues within your applications.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**insightId** | [**String**](String.md) |  |  [optional] |
|**groupARN** | [**String**](String.md) |  |  [optional] |
|**groupName** | [**String**](String.md) |  |  [optional] |
|**rootCauseServiceId** | [**ServiceId**](ServiceId.md) |  |  [optional] |
|**categories** | [**List**](List.md) |  |  [optional] |
|**state** | [**InsightState**](InsightState.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**summary** | [**String**](String.md) |  |  [optional] |
|**clientRequestImpactStatistics** | [**InsightClientRequestImpactStatistics**](InsightClientRequestImpactStatistics.md) |  |  [optional] |
|**rootCauseServiceRequestImpactStatistics** | [**InsightRootCauseServiceRequestImpactStatistics**](InsightRootCauseServiceRequestImpactStatistics.md) |  |  [optional] |
|**topAnomalousServices** | [**List**](List.md) |  |  [optional] |



