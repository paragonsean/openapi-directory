

# GetOrganizationSensorReadingsLatest200ResponseInnerReadingsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**battery** | [**GetOrganizationSensorReadingsHistory200ResponseInnerBattery**](GetOrganizationSensorReadingsHistory200ResponseInnerBattery.md) |  |  [optional] |
|**button** | [**GetOrganizationSensorReadingsHistory200ResponseInnerButton**](GetOrganizationSensorReadingsHistory200ResponseInnerButton.md) |  |  [optional] |
|**door** | [**GetOrganizationSensorReadingsHistory200ResponseInnerDoor**](GetOrganizationSensorReadingsHistory200ResponseInnerDoor.md) |  |  [optional] |
|**humidity** | [**GetOrganizationSensorReadingsHistory200ResponseInnerHumidity**](GetOrganizationSensorReadingsHistory200ResponseInnerHumidity.md) |  |  [optional] |
|**indoorAirQuality** | [**GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality**](GetOrganizationSensorReadingsHistory200ResponseInnerIndoorAirQuality.md) |  |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) | Type of sensor reading. |  [optional] |
|**noise** | [**GetOrganizationSensorReadingsHistory200ResponseInnerNoise**](GetOrganizationSensorReadingsHistory200ResponseInnerNoise.md) |  |  [optional] |
|**pm25** | [**GetOrganizationSensorReadingsHistory200ResponseInnerPm25**](GetOrganizationSensorReadingsHistory200ResponseInnerPm25.md) |  |  [optional] |
|**temperature** | [**GetOrganizationSensorReadingsHistory200ResponseInnerTemperature**](GetOrganizationSensorReadingsHistory200ResponseInnerTemperature.md) |  |  [optional] |
|**ts** | **String** | Time at which the reading occurred, in ISO8601 format. |  [optional] |
|**tvoc** | [**GetOrganizationSensorReadingsHistory200ResponseInnerTvoc**](GetOrganizationSensorReadingsHistory200ResponseInnerTvoc.md) |  |  [optional] |
|**water** | [**GetOrganizationSensorReadingsHistory200ResponseInnerWater**](GetOrganizationSensorReadingsHistory200ResponseInnerWater.md) |  |  [optional] |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| BATTERY | &quot;battery&quot; |
| BUTTON | &quot;button&quot; |
| DOOR | &quot;door&quot; |
| HUMIDITY | &quot;humidity&quot; |
| INDOOR_AIR_QUALITY | &quot;indoorAirQuality&quot; |
| NOISE | &quot;noise&quot; |
| PM25 | &quot;pm25&quot; |
| TEMPERATURE | &quot;temperature&quot; |
| TVOC | &quot;tvoc&quot; |
| WATER | &quot;water&quot; |



