

# DynamicThresholdFailingPeriods

The minimum number of violations required within the selected lookback time window required to raise an alert.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**minFailingPeriodsToAlert** | **BigDecimal** | The number of violations to trigger an alert. Should be smaller or equal to numberOfEvaluationPeriods. |  |
|**numberOfEvaluationPeriods** | **BigDecimal** | The number of aggregated lookback points. The lookback time window is calculated based on the aggregation granularity (windowSize) and the selected number of aggregated points. |  |



