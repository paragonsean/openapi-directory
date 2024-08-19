

# Forecast


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appMaxTemp** | **BigDecimal** | Apparent Maximum daily Temperature - default (C) |  [optional] |
|**appMinTemp** | **BigDecimal** | Apparent Minimum daily Temperature - default (C) |  [optional] |
|**clouds** | **Integer** | Cloud cover as a percentage (%) |  [optional] |
|**datetime** | **String** | Date in format \&quot;YYYY-MM-DD:HH\&quot;. All datetime is in (UTC) |  [optional] |
|**dewpt** | **BigDecimal** | Dewpoint (Average) - default (C) |  [optional] |
|**maxDhi** | **BigDecimal** | [Deprecated] Max direct component of solar insolation (W/m^2) |  [optional] |
|**maxTemp** | **BigDecimal** | Maximum daily Temperature - default (C) |  [optional] |
|**minTemp** | **BigDecimal** | Minimum daily Temperature - default (C) |  [optional] |
|**moonPhase** | **BigDecimal** | Moon phase |  [optional] |
|**moonriseTs** | **Integer** | Moonrise unix timestamp |  [optional] |
|**moonsetTs** | **Integer** | Moonset unix timestamp |  [optional] |
|**pod** | **String** | Part of the day (d &#x3D; day, n &#x3D; night) |  [optional] |
|**pop** | **BigDecimal** | Chance of Precipitation as a percentage (%) |  [optional] |
|**precip** | **BigDecimal** | Accumulated precipitation since last forecast point - default (mm) |  [optional] |
|**pres** | **BigDecimal** | Pressure (mb) |  [optional] |
|**rh** | **Integer** | Relative Humidity as a percentage (%) |  [optional] |
|**slp** | **BigDecimal** | Mean Sea level pressure (mb) |  [optional] |
|**snow** | **BigDecimal** | Accumulated snowfall since last forecast point - default (mm) |  [optional] |
|**snowDepth** | **BigDecimal** | Snow Depth - default (mm) |  [optional] |
|**sunriseTs** | **Integer** | Sunrise unix timestamp |  [optional] |
|**sunsetTs** | **Integer** | Sunset unix timestamp |  [optional] |
|**temp** | **BigDecimal** | Temperature (Average) - default (C) |  [optional] |
|**timestampLocal** | **String** | Timestamp in local time |  [optional] |
|**timestampUtc** | **String** | Timestamp UTC |  [optional] |
|**ts** | **BigDecimal** | Unix Timestamp |  [optional] |
|**uv** | **BigDecimal** | UV Index |  [optional] |
|**vis** | **BigDecimal** | Average Visibility default (KM) |  [optional] |
|**weather** | [**ForecastWeather**](ForecastWeather.md) |  |  [optional] |
|**windCdir** | **String** | Cardinal wind direction |  [optional] |
|**windCdirFull** | **String** | Cardinal wind direction (text) |  [optional] |
|**windDir** | **Integer** | Wind direction |  [optional] |
|**windSpd** | **BigDecimal** | Wind Speed (default m/s) |  [optional] |



