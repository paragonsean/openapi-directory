

# GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**direction** | [**DirectionEnum**](#DirectionEnum) | If &#39;above&#39;, an alert will be sent when a sensor reads above the threshold. If &#39;below&#39;, an alert will be sent when a sensor reads below the threshold. Only applicable for temperature and humidity thresholds. |  [optional] |
|**duration** | [**DurationEnum**](#DurationEnum) | Length of time in seconds that the triggering state must persist before an alert is sent. Available options are 0 seconds, 1 minute, 2 minutes, 3 minutes, 4 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, and 1 hour. Default is 0. |  [optional] |
|**metric** | **String** | The type of sensor metric that will be monitored for changes. Available metrics are door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. |  |
|**threshold** | [**GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold**](GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.md) |  |  |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| ABOVE | &quot;above&quot; |
| BELOW | &quot;below&quot; |



## Enum: DurationEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_60 | 60 |
| NUMBER_120 | 120 |
| NUMBER_180 | 180 |
| NUMBER_240 | 240 |
| NUMBER_300 | 300 |
| NUMBER_600 | 600 |
| NUMBER_900 | 900 |
| NUMBER_1800 | 1800 |
| NUMBER_3600 | 3600 |



