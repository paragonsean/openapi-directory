# MerakiDashboardApi.GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **String** | If &#39;above&#39;, an alert will be sent when a sensor reads above the threshold. If &#39;below&#39;, an alert will be sent when a sensor reads below the threshold. Only applicable for temperature and humidity thresholds. | [optional] 
**duration** | **Number** | Length of time in seconds that the triggering state must persist before an alert is sent. Available options are 0 seconds, 1 minute, 2 minutes, 3 minutes, 4 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, and 1 hour. Default is 0. | [optional] [default to DurationEnum.0]
**metric** | **String** | The type of sensor metric that will be monitored for changes. Available metrics are door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. | 
**threshold** | [**GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold**](GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThreshold.md) |  | 



## Enum: DirectionEnum


* `above` (value: `"above"`)

* `below` (value: `"below"`)





## Enum: DurationEnum


* `0` (value: `0`)

* `60` (value: `60`)

* `120` (value: `120`)

* `180` (value: `180`)

* `240` (value: `240`)

* `300` (value: `300`)

* `600` (value: `600`)

* `900` (value: `900`)

* `1800` (value: `1800`)

* `3600` (value: `3600`)




