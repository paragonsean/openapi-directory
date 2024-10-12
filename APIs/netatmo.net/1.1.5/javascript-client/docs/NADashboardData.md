# Netatmo.NADashboardData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolutePressure** | **Number** | Real measured pressure @ time_utc (in mb) | [optional] 
**boilerOff** | **Number** |  | [optional] 
**boilerOn** | **Number** |  | [optional] 
**cO2** | **Number** | Last Co2 measured @ time_utc (in ppm) | [optional] 
**gustAngle** | **Number** | Direction of the last 5 min highest gust wind | [optional] 
**gustStrength** | **Number** | Speed of the last 5 min highest gust wind | [optional] 
**humidity** | **Number** | Last humidity measured @ time_utc (in %) | [optional] 
**noise** | **Number** | Last noise measured @ time_utc (in db) | [optional] 
**pressure** | **Number** | Last Sea level pressure measured @ time_utc (in mb) | [optional] 
**rain** | **Number** | Last rain measured (in mm) | [optional] 
**temperature** | **Number** | Last temperature measure @ time_utc (in °C) | [optional] 
**windAngle** | **Number** | Current 5 min average wind direction measured @ time_utc (in °) | [optional] 
**windStrength** | **Number** | Current 5 min average wind speed measured @ time_utc (in km/h) | [optional] 
**dateMaxTemp** | **Number** | Timestamp when max temperature was measured | [optional] 
**dateMaxWindStr** | **Number** | Timestamp when max wind strength was measured | [optional] 
**dateMinTemp** | **Number** | Timestamp when min temperature was measured | [optional] 
**deviceId** | **Number** |  | [optional] 
**healthIdx** | **Number** | Current health index: 0 &#x3D; Healthy, 1 &#x3D; Fine, 2 &#x3D; Fair, 3 &#x3D; Poor, 4 &#x3D; Unhealthy | [optional] 
**maxTemp** | **Number** | Min temperature of the day (measured @ date_min_temp) | [optional] 
**maxWindStr** | **Number** |  | [optional] 
**minTemp** | **Number** | Max temperature of the day (measured @ date_max_temp) | [optional] 
**pressureTrend** | **String** | Pressure evolution trend | [optional] 
**sumRain1** | **Number** | Amount of rain in last hour | [optional] 
**sumRain24** | **Number** | Amount of rain today | [optional] 
**tempTrend** | **String** | Temperature evolution trend | [optional] 
**timeUtc** | **Number** |  | [optional] 


