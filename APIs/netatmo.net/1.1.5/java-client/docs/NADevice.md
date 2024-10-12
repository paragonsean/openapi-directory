

# NADevice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**behavior** | **Integer** |  |  [optional] |
|**cipherId** | **String** |  |  [optional] |
|**dashboardData** | [**NADashboardData**](NADashboardData.md) |  |  [optional] |
|**dataType** | **List&lt;String&gt;** |  |  [optional] |
|**dateSetup** | [**NADate**](NADate.md) |  |  [optional] |
|**firmware** | **Integer** |  |  [optional] |
|**firstPidAvail** | **Boolean** |  |  [optional] |
|**heatingSystem** | [**NAHeatingSystem**](NAHeatingSystem.md) |  |  [optional] |
|**houseModel** | [**NAHouseModel**](NAHouseModel.md) |  |  [optional] |
|**hwVersion** | **Integer** |  |  [optional] |
|**ip** | **String** |  |  [optional] |
|**lastFwUpdate** | **Integer** |  |  [optional] |
|**lastRadioStore** | **Integer** |  |  [optional] |
|**lastStatusStore** | **Integer** |  |  [optional] |
|**lastUpgrade** | **Integer** |  |  [optional] |
|**moduleName** | **String** |  |  [optional] |
|**modules** | **List&lt;String&gt;** | It lists which modules are linked with this device |  [optional] |
|**newFeatureAvail** | **Boolean** |  |  [optional] |
|**place** | [**NAPlace**](NAPlace.md) |  |  [optional] |
|**publicExtData** | **Boolean** |  |  [optional] |
|**setpoint** | **Object** |  |  [optional] |
|**setpointDefaultDuration** | **Integer** |  |  [optional] |
|**setpointOrder** | **Map&lt;String, List&lt;NAObject&gt;&gt;** |  |  [optional] |
|**stationName** | **String** |  |  [optional] |
|**thermProgram** | [**Map&lt;String, NAThermProgram&gt;**](NAThermProgram.md) |  |  [optional] |
|**thermProgramBackup** | **Map&lt;String, List&lt;NAThermProgram&gt;&gt;** |  |  [optional] |
|**thermProgramOrder** | **Map&lt;String, List&lt;NAObject&gt;&gt;** |  |  [optional] |
|**type** | **String** | Included in every device or module. It defines the type of the device/module. Its values are among : NAMain : for the base station NAModule1 : for the outdoor module NAModule4 : for the additionnal indoor module NAModule3 : for the rain gauge module NAPlug : for the thermostat relay/plug NATherm1 : for the thermostat module  |  [optional] |
|**udpConn** | **Boolean** |  |  [optional] |
|**userOwner** | **List&lt;String&gt;** |  |  [optional] |
|**wifiStatus** | **Integer** | It contains the current wifi status. The different thresholds to take into account are RSSI_THRESHOLD_0 &#x3D; 86 bad signal RSSI_THRESHOLD_1 &#x3D; 71 middle quality signal RSSI_THRESHOLD_2 &#x3D; 56 good signal  |  [optional] |



