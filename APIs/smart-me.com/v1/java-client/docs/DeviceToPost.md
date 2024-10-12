

# DeviceToPost

Container Class for the Web API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activePower** | **Double** | The Active Power or current flow rate. In kW or m3/h |  [optional] |
|**counterReading** | **Double** | The Meter Counter Reading (Total Energy used) in kWh or m3. |  [optional] |
|**counterReadingExport** | **Double** | The Meter Counter Reading only export |  [optional] |
|**counterReadingExportT1** | **Double** | The Meter Counter Reading only export (Tariff 1) |  [optional] |
|**counterReadingExportT2** | **Double** | The Meter Counter Reading only export (Tariff 2) |  [optional] |
|**counterReadingT1** | **Double** | The Meter Counter Reading Tariff 1 in kWh or m3. |  [optional] |
|**counterReadingT2** | **Double** | The Meter Counter Reading Tariff 2 in kWh or m3. |  [optional] |
|**current** | **Double** | The Current (in A) |  [optional] |
|**currentL1** | **Double** | The Current Phase L1 (in A) |  [optional] |
|**currentL2** | **Double** | The Current Phase L2 (in A) |  [optional] |
|**currentL3** | **Double** | The Current Phase L3 (in A) |  [optional] |
|**deviceEnergyType** | [**DeviceEnergyTypeEnum**](#DeviceEnergyTypeEnum) | The Energy Type of this device |  [optional] |
|**digitalInput1** | **Boolean** | The digital input number 1 |  [optional] |
|**id** | **String** | The ID of the device |  [optional] |
|**meterSubType** | [**MeterSubTypeEnum**](#MeterSubTypeEnum) | The Sub Type of this Meter. |  [optional] |
|**name** | **String** | The Name of the Device |  [optional] |
|**powerFactor** | **Double** | The Power Factor (cos phi). Range: 0 - 1 |  [optional] |
|**powerFactorL1** | **Double** | The Power Factor (cos phi) Phase L1. Range: 0 - 1 |  [optional] |
|**powerFactorL2** | **Double** | The Power Factor (cos phi) Phase L2. Range: 0 - 1 |  [optional] |
|**powerFactorL3** | **Double** | The Power Factor (cos phi) Phase L3. Range: 0 - 1 |  [optional] |
|**serial** | **Long** | The Serial number |  [optional] |
|**temperature** | **Double** | The Temperature (in degree celsius) |  [optional] |
|**valueDate** | **OffsetDateTime** | The Date of the Value (in UTC). If this is null the Server Time is used. |  [optional] |
|**voltage** | **Double** | The Voltage (in V) |  [optional] |
|**voltageL1** | **Double** | The Voltage Phase L1 (in V) |  [optional] |
|**voltageL2** | **Double** | The Voltage Phase L2 (in V) |  [optional] |
|**voltageL3** | **Double** | The Voltage Phase L3 (in V) |  [optional] |



## Enum: DeviceEnergyTypeEnum

| Name | Value |
|---- | -----|
| METER_TYPE_UNKNOWN | &quot;MeterTypeUnknown&quot; |
| METER_TYPE_ELECTRICITY | &quot;MeterTypeElectricity&quot; |
| METER_TYPE_WATER | &quot;MeterTypeWater&quot; |
| METER_TYPE_GAS | &quot;MeterTypeGas&quot; |
| METER_TYPE_HEAT | &quot;MeterTypeHeat&quot; |
| METER_TYPE_HCA | &quot;MeterTypeHCA&quot; |
| METER_TYPE_ALL_METERS | &quot;MeterTypeAllMeters&quot; |
| METER_TYPE_TEMPERATURE | &quot;MeterTypeTemperature&quot; |
| METER_TYPE_M_BUS_GATEWAY | &quot;MeterTypeMBusGateway&quot; |
| METER_TYPE_RS485_GATEWAY | &quot;MeterTypeRS485Gateway&quot; |
| METER_TYPE_CUSTOM_DEVICE | &quot;MeterTypeCustomDevice&quot; |
| METER_TYPE_COMPRESSED_AIR | &quot;MeterTypeCompressedAir&quot; |
| METER_TYPE_SOLAR_LOG | &quot;MeterTypeSolarLog&quot; |
| METER_TYPE_VIRTUAL_METER | &quot;MeterTypeVirtualMeter&quot; |
| METER_TYPE_WM_BUS_GATEWAY | &quot;MeterTypeWMBusGateway&quot; |



## Enum: MeterSubTypeEnum

| Name | Value |
|---- | -----|
| METER_SUB_TYPE_UNKNOWN | &quot;MeterSubTypeUnknown&quot; |
| METER_SUB_TYPE_COLD | &quot;MeterSubTypeCold&quot; |
| METER_SUB_TYPE_HEAT | &quot;MeterSubTypeHeat&quot; |
| METER_SUB_TYPE_CHARGING_STATION | &quot;MeterSubTypeChargingStation&quot; |
| METER_SUB_TYPE_ELECTRICITY | &quot;MeterSubTypeElectricity&quot; |
| METER_SUB_TYPE_WATER | &quot;MeterSubTypeWater&quot; |
| METER_SUB_TYPE_GAS | &quot;MeterSubTypeGas&quot; |
| METER_SUB_TYPE_ELECTRICITY_HEAT | &quot;MeterSubTypeElectricityHeat&quot; |
| METER_SUB_TYPE_TEMPERATURE | &quot;MeterSubTypeTemperature&quot; |
| METER_SUB_TYPE_VIRTUAL_BATTERY | &quot;MeterSubTypeVirtualBattery&quot; |



