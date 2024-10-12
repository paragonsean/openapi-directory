

# InsightEvent

X-Ray reevaluates insights periodically until they are resolved, and records each intermediate state in an event. You can review incident events in the Impact Timeline on the Inspect page in the X-Ray console.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**summary** | [**String**](String.md) |  |  [optional] |
|**eventTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**clientRequestImpactStatistics** | [**InsightClientRequestImpactStatistics**](InsightClientRequestImpactStatistics.md) |  |  [optional] |
|**rootCauseServiceRequestImpactStatistics** | [**InsightRootCauseServiceRequestImpactStatistics**](InsightRootCauseServiceRequestImpactStatistics.md) |  |  [optional] |
|**topAnomalousServices** | [**List**](List.md) |  |  [optional] |



