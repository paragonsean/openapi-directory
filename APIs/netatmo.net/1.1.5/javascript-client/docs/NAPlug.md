# Netatmo.NAPlug

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**firmware** | **Number** |  | [optional] 
**lastBilan** | [**NAYearMonth**](NAYearMonth.md) |  | [optional] 
**lastPlugSeen** | **Number** |  | [optional] 
**lastStatusStore** | **Number** |  | [optional] 
**modules** | [**[NAThermostat]**](NAThermostat.md) |  | [optional] 
**place** | [**NAPlace**](NAPlace.md) |  | [optional] 
**plugConnectedBoiler** | **Number** |  | [optional] 
**stationName** | **String** |  | [optional] 
**syncing** | **Boolean** |  | [optional] 
**type** | **String** | Included in every device or module. It defines the type of the device/module. Its values are among : NAMain : for the base station NAModule1 : for the outdoor module NAModule4 : for the additionnal indoor module NAModule3 : for the rain gauge module NAPlug : for the thermostat relay/plug NATherm1 : for the thermostat module  | [optional] 
**udpConn** | **Boolean** |  | [optional] 
**wifiStatus** | **Number** | It contains the current wifi status. The different thresholds to take into account are RSSI_THRESHOLD_0 &#x3D; 86 bad signal RSSI_THRESHOLD_1 &#x3D; 71 middle quality signal RSSI_THRESHOLD_2 &#x3D; 56 good signal  | [optional] 


