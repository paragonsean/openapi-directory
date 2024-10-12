

# CustomViewabilityMetricConfiguration

The attributes, like playtime and percent onscreen, that define the Custom Viewability Metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audible** | **Boolean** | Whether the video must be audible to count an impression. |  [optional] |
|**timeMillis** | **Integer** | The time in milliseconds the video must play for the Custom Viewability Metric to count an impression. If both this and timePercent are specified, the earlier of the two will be used. |  [optional] |
|**timePercent** | **Integer** | The percentage of video that must play for the Custom Viewability Metric to count an impression. If both this and timeMillis are specified, the earlier of the two will be used. |  [optional] |
|**viewabilityPercent** | **Integer** | The percentage of video that must be on screen for the Custom Viewability Metric to count an impression. |  [optional] |



