

# PointPointHourlyData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cape** | **BigDecimal** | Convective available potential energy. Unit: J/kg |  [optional] |
|**cloudCover** | [**PointPointHourlyCloudCoverData**](PointPointHourlyCloudCoverData.md) |  |  |
|**date** | **OffsetDateTime** | Datetime in YYYY-MM-DDTHH:MM:SS format. |  [optional] |
|**dewPoint** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**evaporation** | **BigDecimal** | Evaporation of liquid water into water vapor. Unit: mm/h |  [optional] |
|**feelsLike** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**humidity** | **Integer** | Relative humidity. Unit: \\% |  [optional] |
|**icon** | **Integer** | Numeric identifier of the weather icon. The following values can appear:  * 1 - Not available * 2 - Sunny * 3 - Mostly sunny * 4 - Partly sunny * 5 - Mostly cloudy * 6 - Cloudy * 7 - Overcast * 8 - Overcast with low clouds * 9 - Fog * 10 - Light rain * 11 - Rain * 12 - Possible rain * 13 - Rain shower * 14 - Thunderstorm * 15 - Local thunderstorms * 16 - Light snow * 17 - Snow * 18 - Possible snow * 19 - Snow shower * 20 - Rain and snow * 21 - Possible rain and snow * 22 - Rain and snow * 23 - Freezing rain * 24 - Possible freezing rain * 25 - Hail * 26 - Clear (night) * 27 - Mostly clear (night) * 28 - Partly clear (night) * 29 - Mostly cloudy (night) * 30 - Cloudy (night) * 31 - Overcast with low clouds (night) * 32 - Rain shower (night) * 33 - Local thunderstorms (night) * 34 - Snow shower (night) * 35 - Rain and snow (night) * 36 - Possible freezing rain (night)  Unit: weather_ico0_36 |  [optional] |
|**irradiance** | **BigDecimal** | Global downward short-wave radiation flux. Unit: W/m2 |  [optional] |
|**lftx** | **BigDecimal** | Surface lifted index. Unit: K |  [optional] |
|**ozone** | **BigDecimal** | Total column of ozone. Unit: Dobson |  [optional] |
|**precipitation** | [**PointPointHourlyPrecipitationData**](PointPointHourlyPrecipitationData.md) |  |  |
|**pressure** | **BigDecimal** | Atmospheric pressure at mean sea level. Units: metric &#x3D; hPa, us &#x3D; Hg, uk &#x3D; hPa, ca &#x3D; kPa |  [optional] |
|**probability** | [**PointPointHourlyProbData**](PointPointHourlyProbData.md) |  |  |
|**snowDepth** | **BigDecimal** | Snow depth. Units: metric &#x3D; cm, us &#x3D; inch, uk &#x3D; cm, ca &#x3D; cm |  [optional] |
|**soilTemperature** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**summary** | **String** | Short text summary of the weather, e.g. &#x60;Light rain&#x60;. |  [optional] |
|**sunshineDuration** | **BigDecimal** | Sunshine duration since start of previous hour. Unit: s |  [optional] |
|**surfaceTemperature** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**temperature** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |
|**uvIndex** | **BigDecimal** | UV index, values from zero (low risk of harm) to 11+ (extreme risk of harm). Unit: uv_index |  [optional] |
|**visibility** | **BigDecimal** | Visibility. Units: metric &#x3D; km, us &#x3D; mi, uk &#x3D; mi, ca &#x3D; km |  [optional] |
|**weather** | **String** | String identifier of the weather icon, e.g. &#x60;light_rain&#x60;. |  [optional] |
|**wind** | [**PointPointHourlyWindData**](PointPointHourlyWindData.md) |  |  |
|**windChill** | **BigDecimal** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C |  [optional] |



