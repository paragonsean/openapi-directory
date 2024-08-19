

# NAThermostat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**batteryPercent** | **Integer** | It contains the current battery level in percentage. |  [optional] |
|**batteryVp** | **Integer** | It contains the current battery status. The threshold depends on the kind of module, below is the list of the different threshold to take into account according the module type. \&quot;Indoor module Battery range: 6000 ... 4200\&quot; | INDOOR_BATTERY_LEVEL_FULL &#x3D; 5640 INDOOR_BATTERY_LEVEL_HIGH &#x3D; 5280 INDOOR_BATTERY_LEVEL_MEDIUM &#x3D; 4920 INDOOR_BATTERY_LEVEL_LOW &#x3D; 4560 \&quot;Below 4560: very low\&quot; |      \&quot;Raingauge and outdoor module Battery range: 6000 ... 3600\&quot; | BATTERY_LEVEL_FULL &#x3D; 5500 BATTERY_LEVEL_HIGH &#x3D; 5000 BATTERY_LEVEL_MEDIUM &#x3D; 4500 BATTERY_LEVEL_LOW &#x3D; 4000 \&quot;Below 4000: very low\&quot; |      \&quot;Thermostat Battery range: 4500 ... 3000\&quot; | THERMOSTAT_BATTERY_LEVEL_FULL &#x3D; 4100 THERMOSTAT_BATTERY_LEVEL_HIGH &#x3D; 3600 THERMOSTAT_BATTERY_LEVEL_MEDIUM &#x3D; 3300 THERMOSTAT_BATTERY_LEVEL_LOW &#x3D; 3000 \&quot;Below 3000: very low\&quot;  |  [optional] |
|**firmware** | **Integer** |  |  [optional] |
|**lastMessage** | **Integer** |  |  [optional] |
|**lastThermSeen** | **Integer** |  |  [optional] |
|**measured** | [**NAThermMeasure**](NAThermMeasure.md) |  |  [optional] |
|**moduleName** | **String** |  |  [optional] |
|**rfStatus** | **Integer** | \&quot;It contains the current radio status. The different thresholds to take into account are :\&quot; | RADIO_THRESHOLD_SIGNAL_LOW &#x3D; 90  RADIO_THRESHOLD_SIGNAL_MEDIUM &#x3D; 80 RADIO_THRESHOLD_SIGNAL_HIGH &#x3D; 70 RADIO_THRESHOLD_SIGNAL_FULL &#x3D; 60  |  [optional] |
|**setpoint** | [**NASetpoint**](NASetpoint.md) |  |  [optional] |
|**setpointHistory** | [**List&lt;NASetpointLog&gt;**](NASetpointLog.md) | The last 20 setpoints (mode, endtime, and timestamp) the thermostats has entered. |  [optional] |
|**setpointOrder** | [**NASetpoint**](NASetpoint.md) |  |  [optional] |
|**thermOrientation** | **Integer** |  |  [optional] |
|**thermProgramList** | [**List&lt;NAThermProgram&gt;**](NAThermProgram.md) | List of the weekly heating planning used by the thermostat |  [optional] |
|**thermRelayCmd** | **Integer** |  |  [optional] |
|**type** | **String** | Included in every device or module. It defines the type of the device/module. Its values are among : NAMain : for the base station NAModule1 : for the outdoor module NAModule4 : for the additionnal indoor module NAModule3 : for the rain gauge module NAPlug : for the thermostat relay/plug NATherm1 : for the thermostat module  |  [optional] |



