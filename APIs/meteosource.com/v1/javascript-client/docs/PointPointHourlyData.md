# InteractiveDocumentationForYourPremiumPlan.PointPointHourlyData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cape** | **Number** | Convective available potential energy. Unit: J/kg | [optional] 
**cloudCover** | [**PointPointHourlyCloudCoverData**](PointPointHourlyCloudCoverData.md) |  | 
**date** | **Date** | Datetime in YYYY-MM-DDTHH:MM:SS format. | [optional] 
**dewPoint** | **Number** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C | [optional] 
**evaporation** | **Number** | Evaporation of liquid water into water vapor. Unit: mm/h | [optional] 
**feelsLike** | **Number** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C | [optional] 
**humidity** | **Number** | Relative humidity. Unit: \\% | [optional] 
**icon** | **Number** | Numeric identifier of the weather icon. The following values can appear:  * 1 - Not available * 2 - Sunny * 3 - Mostly sunny * 4 - Partly sunny * 5 - Mostly cloudy * 6 - Cloudy * 7 - Overcast * 8 - Overcast with low clouds * 9 - Fog * 10 - Light rain * 11 - Rain * 12 - Possible rain * 13 - Rain shower * 14 - Thunderstorm * 15 - Local thunderstorms * 16 - Light snow * 17 - Snow * 18 - Possible snow * 19 - Snow shower * 20 - Rain and snow * 21 - Possible rain and snow * 22 - Rain and snow * 23 - Freezing rain * 24 - Possible freezing rain * 25 - Hail * 26 - Clear (night) * 27 - Mostly clear (night) * 28 - Partly clear (night) * 29 - Mostly cloudy (night) * 30 - Cloudy (night) * 31 - Overcast with low clouds (night) * 32 - Rain shower (night) * 33 - Local thunderstorms (night) * 34 - Snow shower (night) * 35 - Rain and snow (night) * 36 - Possible freezing rain (night)  Unit: weather_ico0_36 | [optional] 
**irradiance** | **Number** | Global downward short-wave radiation flux. Unit: W/m2 | [optional] 
**lftx** | **Number** | Surface lifted index. Unit: K | [optional] 
**ozone** | **Number** | Total column of ozone. Unit: Dobson | [optional] 
**precipitation** | [**PointPointHourlyPrecipitationData**](PointPointHourlyPrecipitationData.md) |  | 
**pressure** | **Number** | Atmospheric pressure at mean sea level. Units: metric &#x3D; hPa, us &#x3D; Hg, uk &#x3D; hPa, ca &#x3D; kPa | [optional] 
**probability** | [**PointPointHourlyProbData**](PointPointHourlyProbData.md) |  | 
**snowDepth** | **Number** | Snow depth. Units: metric &#x3D; cm, us &#x3D; inch, uk &#x3D; cm, ca &#x3D; cm | [optional] 
**soilTemperature** | **Number** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C | [optional] 
**summary** | **String** | Short text summary of the weather, e.g. &#x60;Light rain&#x60;. | [optional] 
**sunshineDuration** | **Number** | Sunshine duration since start of previous hour. Unit: s | [optional] 
**surfaceTemperature** | **Number** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C | [optional] 
**temperature** | **Number** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C | [optional] 
**uvIndex** | **Number** | UV index, values from zero (low risk of harm) to 11+ (extreme risk of harm). Unit: uv_index | [optional] 
**visibility** | **Number** | Visibility. Units: metric &#x3D; km, us &#x3D; mi, uk &#x3D; mi, ca &#x3D; km | [optional] 
**weather** | **String** | String identifier of the weather icon, e.g. &#x60;light_rain&#x60;. | [optional] 
**wind** | [**PointPointHourlyWindData**](PointPointHourlyWindData.md) |  | 
**windChill** | **Number** | Units: metric &#x3D; °C, us &#x3D; °F, uk &#x3D; °C, ca &#x3D; °C | [optional] 


