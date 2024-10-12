# Netatmo.NADevice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**behavior** | **Number** |  | [optional] 
**cipherId** | **String** |  | [optional] 
**dashboardData** | [**NADashboardData**](NADashboardData.md) |  | [optional] 
**dataType** | **[String]** |  | [optional] 
**dateSetup** | [**NADate**](NADate.md) |  | [optional] 
**firmware** | **Number** |  | [optional] 
**firstPidAvail** | **Boolean** |  | [optional] 
**heatingSystem** | [**NAHeatingSystem**](NAHeatingSystem.md) |  | [optional] 
**houseModel** | [**NAHouseModel**](NAHouseModel.md) |  | [optional] 
**hwVersion** | **Number** |  | [optional] 
**ip** | **String** |  | [optional] 
**lastFwUpdate** | **Number** |  | [optional] 
**lastRadioStore** | **Number** |  | [optional] 
**lastStatusStore** | **Number** |  | [optional] 
**lastUpgrade** | **Number** |  | [optional] 
**moduleName** | **String** |  | [optional] 
**modules** | **[String]** | It lists which modules are linked with this device | [optional] 
**newFeatureAvail** | **Boolean** |  | [optional] 
**place** | [**NAPlace**](NAPlace.md) |  | [optional] 
**publicExtData** | **Boolean** |  | [optional] 
**setpoint** | **Object** |  | [optional] 
**setpointDefaultDuration** | **Number** |  | [optional] 
**setpointOrder** | **{String: [NAObject]}** |  | [optional] 
**stationName** | **String** |  | [optional] 
**thermProgram** | [**{String: NAThermProgram}**](NAThermProgram.md) |  | [optional] 
**thermProgramBackup** | **{String: [NAThermProgram]}** |  | [optional] 
**thermProgramOrder** | **{String: [NAObject]}** |  | [optional] 
**type** | **String** | Included in every device or module. It defines the type of the device/module. Its values are among : NAMain : for the base station NAModule1 : for the outdoor module NAModule4 : for the additionnal indoor module NAModule3 : for the rain gauge module NAPlug : for the thermostat relay/plug NATherm1 : for the thermostat module  | [optional] 
**udpConn** | **Boolean** |  | [optional] 
**userOwner** | **[String]** |  | [optional] 
**wifiStatus** | **Number** | It contains the current wifi status. The different thresholds to take into account are RSSI_THRESHOLD_0 &#x3D; 86 bad signal RSSI_THRESHOLD_1 &#x3D; 71 middle quality signal RSSI_THRESHOLD_2 &#x3D; 56 good signal  | [optional] 


