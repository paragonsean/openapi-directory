

# CurrentObs


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appTemp** | **BigDecimal** | Apparent temperature - Default (C) |  [optional] |
|**aqi** | **BigDecimal** | Air quality index (US EPA standard 0 to +500) |  [optional] |
|**cityName** | **String** | City name (closest) |  [optional] |
|**clouds** | **Integer** | Cloud cover (%) |  [optional] |
|**countryCode** | **String** | Country abbreviation |  [optional] |
|**datetime** | **String** | Cycle Hour (UTC) of observation |  [optional] |
|**dewpt** | **BigDecimal** | Dew point temperature - default (C) |  [optional] |
|**dhi** | **BigDecimal** | Diffuse horizontal irradiance (W/m^2) |  [optional] |
|**dni** | **BigDecimal** | Direct normal irradiance (W/m^2) |  [optional] |
|**elevAngle** | **BigDecimal** | Current solar elevation angle (Degrees) |  [optional] |
|**ghi** | **BigDecimal** | Global horizontal irradiance (W/m^2) |  [optional] |
|**gust** | **BigDecimal** | Wind gust speed - Default (m/s) |  [optional] |
|**hourAngle** | **BigDecimal** | Current solar hour angle (Degrees) |  [optional] |
|**lat** | **BigDecimal** | Latitude |  [optional] |
|**lon** | **BigDecimal** | Longitude |  [optional] |
|**obTime** | **String** | Full time (UTC) of observation (YYYY-MM-DD HH:MM) |  [optional] |
|**pod** | **String** | Part of the day (d &#x3D; day, n &#x3D; night) |  [optional] |
|**precip** | **BigDecimal** | Precipitation in last hour - Default (mm) |  [optional] |
|**pres** | **BigDecimal** | Pressure (mb) |  [optional] |
|**rh** | **Integer** | Relative humidity (%) |  [optional] |
|**slp** | **BigDecimal** | Mean sea level pressure in millibars (mb) |  [optional] |
|**snow** | **BigDecimal** | Snowfall in last hour - Default (mm) |  [optional] |
|**solarRad** | **BigDecimal** | Estimated solar radiation (W/m^2) |  [optional] |
|**sources** | **List&lt;String&gt;** | List of data sources used in response |  [optional] |
|**stateCode** | **String** | State abbreviation |  [optional] |
|**station** | **String** | Source Station ID |  [optional] |
|**sunrise** | **String** | Time (UTC) of Sunrise (HH:MM) |  [optional] |
|**sunset** | **String** | Time (UTC) of Sunset (HH:MM) |  [optional] |
|**temp** | **BigDecimal** | Temperature - Default (C) |  [optional] |
|**timezone** | **String** | Local IANA time zone |  [optional] |
|**ts** | **BigDecimal** | Unix Timestamp |  [optional] |
|**uv** | **BigDecimal** | UV Index |  [optional] |
|**vis** | **Integer** | Visibility - default (M) |  [optional] |
|**weather** | [**CurrentObsWeather**](CurrentObsWeather.md) |  |  [optional] |
|**windCdir** | **String** | Cardinal wind direction |  [optional] |
|**windCdirFull** | **String** | Cardinal wind direction (text) |  [optional] |
|**windDir** | **Integer** | Wind direction (degrees) |  [optional] |
|**windSpeed** | **BigDecimal** | Wind speed - Default (m/s) |  [optional] |



