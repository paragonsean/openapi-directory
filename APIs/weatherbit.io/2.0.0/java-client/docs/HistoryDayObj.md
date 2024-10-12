

# HistoryDayObj


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datetime** | **String** | Date in format \&quot;YYYY-MM-DD\&quot;. All datetime is in (UTC) |  [optional] |
|**dewpt** | **BigDecimal** | Average dewpoint - Default (C) |  [optional] |
|**dhi** | **Integer** | Average hourly diffuse horizontal solar irradiance (W/m^2) |  [optional] |
|**dni** | **Integer** | Average direct normal solar irradiance (W/m^2) |  [optional] |
|**ghi** | **Integer** | Average hourly global horizontal solar irradiance (W/m^2) |  [optional] |
|**maxTemp** | **BigDecimal** | Max temperature - Default (C) |  [optional] |
|**maxTempTs** | **BigDecimal** | Time of max memperature - Unix Timestamp |  [optional] |
|**maxUv** | **BigDecimal** | Max UV Index (1-11+) |  [optional] |
|**maxWindDir** | **Integer** | Direction of wind at time of max 2min wind (degrees) |  [optional] |
|**maxWindSpd** | **BigDecimal** | Max 2min Wind Speed - default (m/s) |  [optional] |
|**maxWindSpdTs** | **BigDecimal** | Time of max 2min wind - unix timestamp |  [optional] |
|**minTemp** | **BigDecimal** | Min temperature - Default (C) |  [optional] |
|**minTempTs** | **BigDecimal** | Time of max temperature - unix timestamp |  [optional] |
|**precip** | **BigDecimal** | Liquid equivalent precipitation - default (mm) |  [optional] |
|**precipGpm** | **BigDecimal** | Satellite estimated liquid equivalent precipitation - default (mm) |  [optional] |
|**pres** | **BigDecimal** | Average pressure (mb) |  [optional] |
|**revisionStatus** | **String** | Data revision status (interim or final) |  [optional] |
|**rh** | **Integer** | Average relative humidity as a percentage (%) |  [optional] |
|**slp** | **BigDecimal** | Average sea level pressure (mb) |  [optional] |
|**snow** | **BigDecimal** | Snowfall - default (mm) |  [optional] |
|**snowDepth** | **BigDecimal** | Snow Depth - default (mm) |  [optional] |
|**tDhi** | **Integer** | Total diffuse horizontal solar irradiance (W/m^2) |  [optional] |
|**tDni** | **Integer** | Total direct normal solar irradiance (W/m^2) |  [optional] |
|**tGhi** | **Integer** | Total global horizontal solar irradiance (W/m^2) |  [optional] |
|**temp** | **BigDecimal** | Average temperature - Default (C) |  [optional] |
|**ts** | **Integer** | Unix timestamp of datetime (Midnight UTC) |  [optional] |
|**windDir** | **Integer** | Average wind direction (degrees) |  [optional] |
|**windGustSpd** | **BigDecimal** | Wind gust speed - default (m/s) |  [optional] |
|**windSpd** | **BigDecimal** | Average wind speed - default (m/s) |  [optional] |



