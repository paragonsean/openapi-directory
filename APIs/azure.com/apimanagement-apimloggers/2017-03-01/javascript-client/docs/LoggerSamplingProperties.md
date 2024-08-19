# ApiManagementClient.LoggerSamplingProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluationInterval** | **String** | Rate re-evaluation interval in ISO8601 format. | [optional] 
**initialPercentage** | **Number** | Initial sampling rate. | [optional] 
**maxPercentage** | **Number** | Maximum allowed rate of sampling. | [optional] 
**maxTelemetryItemsPerSecond** | **Number** | Target rate of telemetry items per second. | [optional] 
**minPercentage** | **Number** | Minimum allowed rate of sampling. | [optional] 
**movingAverageRatio** | **Number** | Moving average ration assigned to most recent value. | [optional] 
**percentage** | **Number** | Rate of sampling for fixed-rate sampling. | [optional] 
**percentageDecreaseTimeout** | **String** | Duration in ISO8601 format after which it&#39;s allowed to lower the sampling rate. | [optional] 
**percentageIncreaseTimeout** | **String** | Duration in ISO8601 format after which it&#39;s allowed to increase the sampling rate. | [optional] 
**samplingType** | **String** | Sampling type. | [optional] 



## Enum: SamplingTypeEnum


* `fixed` (value: `"fixed"`)

* `adaptive` (value: `"adaptive"`)




