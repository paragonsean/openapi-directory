

# TimeMachineTimeMachineHourlyData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cape** | **Integer** | Convective available potential energy. Unit: J/kg |  [optional] |
|**cloudCover** | [**TimeMachineTimeMachineCloudCoverData**](TimeMachineTimeMachineCloudCoverData.md) |  |  |
|**date** | **OffsetDateTime** | Datetime in YYYY-MM-DDTHH:MM:SS format. |  [optional] |
|**dewPoint** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**evaporation** | **Integer** | Evaporation of liquid water into water vapor. Unit: mm/h |  [optional] |
|**feelsLike** | **BigDecimal** | Feels like temperature. Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**humidity** | **Integer** | Relative humidity. Unit: \\% |  [optional] |
|**icon** | **Integer** | Numeric identifier of the weather icon. The following values can appear:  * 1 - Not available * 2 - Sunny * 3 - Mostly sunny * 4 - Partly sunny * 5 - Mostly cloudy * 6 - Cloudy * 7 - Overcast * 8 - Overcast with low clouds * 9 - Fog * 10 - Light rain * 11 - Rain * 12 - Possible rain * 13 - Rain shower * 14 - Thunderstorm * 15 - Local thunderstorms * 16 - Light snow * 17 - Snow * 18 - Possible snow * 19 - Snow shower * 20 - Rain and snow * 21 - Possible rain and snow * 22 - Rain and snow * 23 - Freezing rain * 24 - Possible freezing rain * 25 - Hail * 26 - Clear (night) * 27 - Mostly clear (night) * 28 - Partly clear (night) * 29 - Mostly cloudy (night) * 30 - Cloudy (night) * 31 - Overcast with low clouds (night) * 32 - Rain shower (night) * 33 - Local thunderstorms (night) * 34 - Snow shower (night) * 35 - Rain and snow (night) * 36 - Possible freezing rain (night)  Unit: N/A |  [optional] |
|**irradiance** | **Integer** | Global downward short-wave radiation flux. Unit: W/m2 |  [optional] |
|**ozone** | **Integer** | Total column of ozone. Unit: Dobson |  [optional] |
|**precipitation** | [**TimeMachineTimeMachinePrecipitationData**](TimeMachineTimeMachinePrecipitationData.md) |  |  |
|**pressure** | **BigDecimal** | Atmospheric pressure at mean sea level. Units: metric &#x3D; hPa, us &#x3D; Hg, uk &#x3D; hPa, ca &#x3D; kPa |  [optional] |
|**soilTemperature** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**surfaceTemperature** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**temperature** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**weather** | **String** | String identifier of the weather icon, e.g. &#x60;light_rain&#x60;. |  [optional] |
|**wind** | [**TimeMachineTimeMachineWindData**](TimeMachineTimeMachineWindData.md) |  |  |
|**windChill** | **BigDecimal** | Windchill temperature. Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |



