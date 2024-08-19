# Netatmo.NAMain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**cipherId** | **String** |  | [optional] 
**co2Calibrating** | **Boolean** |  | [optional] 
**dashboardData** | [**NADashboardData**](NADashboardData.md) |  | [optional] 
**dataType** | **[String]** |  | [optional] 
**dateSetup** | **Number** |  | [optional] 
**favorite** | **Boolean** | true when the device is a user favorite and not owned by them | [optional] 
**firmware** | **Number** |  | [optional] 
**lastSetup** | **Number** |  | [optional] 
**lastStatusStore** | **Number** |  | [optional] 
**lastUpgrade** | **Number** |  | [optional] 
**moduleName** | **String** |  | [optional] 
**modules** | [**[NAStationModule]**](NAStationModule.md) |  | [optional] 
**place** | [**NAPlace**](NAPlace.md) |  | [optional] 
**reachable** | **Boolean** | true when the station was seen by the Netatmo cloud within the last 4 hours | [optional] 
**readOnly** | **Boolean** | true when the user was invited to (or has favorited) a station, false when the user owns it | [optional] 
**stationName** | **String** |  | [optional] 
**type** | **String** | Included in every device or module. It defines the type of the device/module. Its values are among : NAMain : for the base station NAModule1 : for the outdoor module NAModule4 : for the additionnal indoor module NAModule3 : for the rain gauge module NAPlug : for the thermostat relay/plug NATherm1 : for the thermostat module  | [optional] 
**wifiStatus** | **Number** | It contains the current wifi status. The different thresholds to take into account are RSSI_THRESHOLD_0 &#x3D; 86 bad signal RSSI_THRESHOLD_1 &#x3D; 71 middle quality signal RSSI_THRESHOLD_2 &#x3D; 56 good signal  | [optional] 


