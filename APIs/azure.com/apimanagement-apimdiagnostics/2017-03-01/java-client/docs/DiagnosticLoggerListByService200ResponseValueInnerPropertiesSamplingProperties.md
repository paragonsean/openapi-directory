

# DiagnosticLoggerListByService200ResponseValueInnerPropertiesSamplingProperties

Sampling settings for an ApplicationInsights logger.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluationInterval** | **String** | Rate re-evaluation interval in ISO8601 format. |  [optional] |
|**initialPercentage** | **Double** | Initial sampling rate. |  [optional] |
|**maxPercentage** | **Double** | Maximum allowed rate of sampling. |  [optional] |
|**maxTelemetryItemsPerSecond** | **Integer** | Target rate of telemetry items per second. |  [optional] |
|**minPercentage** | **Double** | Minimum allowed rate of sampling. |  [optional] |
|**movingAverageRatio** | **Double** | Moving average ration assigned to most recent value. |  [optional] |
|**percentage** | **Double** | Rate of sampling for fixed-rate sampling. |  [optional] |
|**percentageDecreaseTimeout** | **String** | Duration in ISO8601 format after which it&#39;s allowed to lower the sampling rate. |  [optional] |
|**percentageIncreaseTimeout** | **String** | Duration in ISO8601 format after which it&#39;s allowed to increase the sampling rate. |  [optional] |
|**samplingType** | [**SamplingTypeEnum**](#SamplingTypeEnum) | Sampling type. |  [optional] |



## Enum: SamplingTypeEnum

| Name | Value |
|---- | -----|
| FIXED | &quot;fixed&quot; |
| ADAPTIVE | &quot;adaptive&quot; |



