

# GoogleChromeManagementV1RuntimeCountersReport

Runtime counters retrieved from CPU. Currently the runtime counters telemetry is only supported by Intel vPro PSR on Gen 14+.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enterHibernationCount** | **String** | Number of times that the device has entered into the hibernation state. Currently obtained via the PSR, count from S0-&gt;S4. |  [optional] |
|**enterPoweroffCount** | **String** | Number of times that the device has entered into the power-off state. Currently obtained via the PSR, count from S0-&gt;S5. |  [optional] |
|**enterSleepCount** | **String** | Number of times that the device has entered into the sleep state. Currently obtained via the PSR, count from S0-&gt;S3. |  [optional] |
|**reportTime** | **String** | Timestamp when the report was collected. |  [optional] |
|**uptimeRuntimeDuration** | **String** | Total lifetime runtime. Currently always S0 runtime from Intel vPro PSR. |  [optional] |



