

# NADashboardData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absolutePressure** | **Float** | Real measured pressure @ time_utc (in mb) |  [optional] |
|**boilerOff** | **Integer** |  |  [optional] |
|**boilerOn** | **Integer** |  |  [optional] |
|**CO2** | **Float** | Last Co2 measured @ time_utc (in ppm) |  [optional] |
|**gustAngle** | **Integer** | Direction of the last 5 min highest gust wind |  [optional] |
|**gustStrength** | **Integer** | Speed of the last 5 min highest gust wind |  [optional] |
|**humidity** | **Float** | Last humidity measured @ time_utc (in %) |  [optional] |
|**noise** | **Float** | Last noise measured @ time_utc (in db) |  [optional] |
|**pressure** | **Float** | Last Sea level pressure measured @ time_utc (in mb) |  [optional] |
|**rain** | **Float** | Last rain measured (in mm) |  [optional] |
|**temperature** | **Float** | Last temperature measure @ time_utc (in °C) |  [optional] |
|**windAngle** | **Integer** | Current 5 min average wind direction measured @ time_utc (in °) |  [optional] |
|**windStrength** | **Integer** | Current 5 min average wind speed measured @ time_utc (in km/h) |  [optional] |
|**dateMaxTemp** | **Integer** | Timestamp when max temperature was measured |  [optional] |
|**dateMaxWindStr** | **Integer** | Timestamp when max wind strength was measured |  [optional] |
|**dateMinTemp** | **Integer** | Timestamp when min temperature was measured |  [optional] |
|**deviceId** | **Float** |  |  [optional] |
|**healthIdx** | **Integer** | Current health index: 0 &#x3D; Healthy, 1 &#x3D; Fine, 2 &#x3D; Fair, 3 &#x3D; Poor, 4 &#x3D; Unhealthy |  [optional] |
|**maxTemp** | **Float** | Min temperature of the day (measured @ date_min_temp) |  [optional] |
|**maxWindStr** | **Integer** |  |  [optional] |
|**minTemp** | **Float** | Max temperature of the day (measured @ date_max_temp) |  [optional] |
|**pressureTrend** | **String** | Pressure evolution trend |  [optional] |
|**sumRain1** | **Float** | Amount of rain in last hour |  [optional] |
|**sumRain24** | **Float** | Amount of rain today |  [optional] |
|**tempTrend** | **String** | Temperature evolution trend |  [optional] |
|**timeUtc** | **Integer** |  |  [optional] |



