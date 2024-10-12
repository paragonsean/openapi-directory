# SmartMe.DeviceToPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activePower** | **Number** | The Active Power or current flow rate. In kW or m3/h | [optional] 
**counterReading** | **Number** | The Meter Counter Reading (Total Energy used) in kWh or m3. | [optional] 
**counterReadingExport** | **Number** | The Meter Counter Reading only export | [optional] 
**counterReadingExportT1** | **Number** | The Meter Counter Reading only export (Tariff 1) | [optional] 
**counterReadingExportT2** | **Number** | The Meter Counter Reading only export (Tariff 2) | [optional] 
**counterReadingT1** | **Number** | The Meter Counter Reading Tariff 1 in kWh or m3. | [optional] 
**counterReadingT2** | **Number** | The Meter Counter Reading Tariff 2 in kWh or m3. | [optional] 
**current** | **Number** | The Current (in A) | [optional] 
**currentL1** | **Number** | The Current Phase L1 (in A) | [optional] 
**currentL2** | **Number** | The Current Phase L2 (in A) | [optional] 
**currentL3** | **Number** | The Current Phase L3 (in A) | [optional] 
**deviceEnergyType** | **String** | The Energy Type of this device | [optional] 
**digitalInput1** | **Boolean** | The digital input number 1 | [optional] 
**id** | **String** | The ID of the device | [optional] 
**meterSubType** | **String** | The Sub Type of this Meter. | [optional] 
**name** | **String** | The Name of the Device | [optional] 
**powerFactor** | **Number** | The Power Factor (cos phi). Range: 0 - 1 | [optional] 
**powerFactorL1** | **Number** | The Power Factor (cos phi) Phase L1. Range: 0 - 1 | [optional] 
**powerFactorL2** | **Number** | The Power Factor (cos phi) Phase L2. Range: 0 - 1 | [optional] 
**powerFactorL3** | **Number** | The Power Factor (cos phi) Phase L3. Range: 0 - 1 | [optional] 
**serial** | **Number** | The Serial number | [optional] 
**temperature** | **Number** | The Temperature (in degree celsius) | [optional] 
**valueDate** | **Date** | The Date of the Value (in UTC). If this is null the Server Time is used. | [optional] 
**voltage** | **Number** | The Voltage (in V) | [optional] 
**voltageL1** | **Number** | The Voltage Phase L1 (in V) | [optional] 
**voltageL2** | **Number** | The Voltage Phase L2 (in V) | [optional] 
**voltageL3** | **Number** | The Voltage Phase L3 (in V) | [optional] 



## Enum: DeviceEnergyTypeEnum


* `MeterTypeUnknown` (value: `"MeterTypeUnknown"`)

* `MeterTypeElectricity` (value: `"MeterTypeElectricity"`)

* `MeterTypeWater` (value: `"MeterTypeWater"`)

* `MeterTypeGas` (value: `"MeterTypeGas"`)

* `MeterTypeHeat` (value: `"MeterTypeHeat"`)

* `MeterTypeHCA` (value: `"MeterTypeHCA"`)

* `MeterTypeAllMeters` (value: `"MeterTypeAllMeters"`)

* `MeterTypeTemperature` (value: `"MeterTypeTemperature"`)

* `MeterTypeMBusGateway` (value: `"MeterTypeMBusGateway"`)

* `MeterTypeRS485Gateway` (value: `"MeterTypeRS485Gateway"`)

* `MeterTypeCustomDevice` (value: `"MeterTypeCustomDevice"`)

* `MeterTypeCompressedAir` (value: `"MeterTypeCompressedAir"`)

* `MeterTypeSolarLog` (value: `"MeterTypeSolarLog"`)

* `MeterTypeVirtualMeter` (value: `"MeterTypeVirtualMeter"`)

* `MeterTypeWMBusGateway` (value: `"MeterTypeWMBusGateway"`)





## Enum: MeterSubTypeEnum


* `MeterSubTypeUnknown` (value: `"MeterSubTypeUnknown"`)

* `MeterSubTypeCold` (value: `"MeterSubTypeCold"`)

* `MeterSubTypeHeat` (value: `"MeterSubTypeHeat"`)

* `MeterSubTypeChargingStation` (value: `"MeterSubTypeChargingStation"`)

* `MeterSubTypeElectricity` (value: `"MeterSubTypeElectricity"`)

* `MeterSubTypeWater` (value: `"MeterSubTypeWater"`)

* `MeterSubTypeGas` (value: `"MeterSubTypeGas"`)

* `MeterSubTypeElectricityHeat` (value: `"MeterSubTypeElectricityHeat"`)

* `MeterSubTypeTemperature` (value: `"MeterSubTypeTemperature"`)

* `MeterSubTypeVirtualBattery` (value: `"MeterSubTypeVirtualBattery"`)




