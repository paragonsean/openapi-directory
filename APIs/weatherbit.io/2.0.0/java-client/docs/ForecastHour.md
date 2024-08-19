

# ForecastHour


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appTemp** | **BigDecimal** | Apparent Temperature - Default (C) |  [optional] |
|**clouds** | **Integer** | Cloud cover as a percentage (%) |  [optional] |
|**datetime** | **String** | Date in format \&quot;YYYY-MM-DD:HH\&quot;. All datetime is in (UTC) |  [optional] |
|**dewpt** | **BigDecimal** | Dewpoint - Default (C) |  [optional] |
|**dhi** | **BigDecimal** | Diffuse normal solar irradiance (W/m^2) |  [optional] |
|**dni** | **BigDecimal** | Direct normal solar irradiance (W/m^2) |  [optional] |
|**ghi** | **BigDecimal** | Global horizontal solar irradiance (W/m^2) |  [optional] |
|**pod** | **String** | Part of day (d &#x3D; day, n &#x3D; night) |  [optional] |
|**pop** | **BigDecimal** | Chance of Precipitation as a percentage (%) |  [optional] |
|**precip** | **BigDecimal** | Accumulated precipitation since last forecast point. Default (mm) |  [optional] |
|**pres** | **BigDecimal** | Pressure (mb) |  [optional] |
|**rh** | **Integer** | Relative Humidity as a percentage (%) |  [optional] |
|**slp** | **BigDecimal** | Mean Sea level pressure (mb) |  [optional] |
|**snow** | **BigDecimal** | Accumulated snowfall since last forecast point - Default (mm) |  [optional] |
|**snowDepth** | **BigDecimal** | Snow depth - Default (mm) |  [optional] |
|**solarRad** | **BigDecimal** | Estimated solar radiation (W/m^2) |  [optional] |
|**temp** | **BigDecimal** | Temperature - Default (C) |  [optional] |
|**timestampLocal** | **String** | Timestamp in local time |  [optional] |
|**timestampUtc** | **String** | Timestamp UTC |  [optional] |
|**ts** | **BigDecimal** | Unix Timestamp |  [optional] |
|**uv** | **BigDecimal** | UV Index |  [optional] |
|**vis** | **BigDecimal** | Visibility - Default (KM) |  [optional] |
|**weather** | [**ForecastHourWeather**](ForecastHourWeather.md) |  |  [optional] |
|**windCdir** | **String** | Cardinal wind direction |  [optional] |
|**windCdirFull** | **String** | Cardinal wind direction (text) |  [optional] |
|**windDir** | **Integer** | Wind direction |  [optional] |
|**windGustSpd** | **BigDecimal** | Wind Gust Speed - Default (m/s) |  [optional] |
|**windSpd** | **BigDecimal** | Wind Speed - Default (m/s) |  [optional] |



