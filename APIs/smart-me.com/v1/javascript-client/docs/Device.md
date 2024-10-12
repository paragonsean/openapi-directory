# SmartMe.Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activePower** | **Number** | The Actvie Power or current flow rate | [optional] 
**activePowerL1** | **Number** | The Actvie Power Phase L1 | [optional] 
**activePowerL2** | **Number** | The Actvie Power Phase L2 | [optional] 
**activePowerL3** | **Number** | The Actvie Power Phase L3 | [optional] 
**activePowerUnit** | **String** | The Unit of the Active Power Value | [optional] 
**activeTariff** | **Number** | The Number of the Active Tariff | [optional] 
**additionalMeterSerialNumber** | **String** | An additional Meter serial number. e.g. the number of a meter a smart-me device is connected to. | [optional] 
**analogOutput1** | **Number** | The analog output number 1 (PWM signal) (0 - 32183) | [optional] 
**analogOutput2** | **Number** | The analog output number 2 (PWM signal) (0 - 32183) | [optional] 
**chargingStationState** | **String** | The state of a pico charging station. (Only available for pico charging stations) | [optional] 
**counterReading** | **Number** | The Meter Counter Reading (Total Energy used) | [optional] 
**counterReadingExport** | **Number** | The Meter Counter Reading only export | [optional] 
**counterReadingImport** | **Number** | The Meter Counter Reading only import | [optional] 
**counterReadingT1** | **Number** | The Meter Counter Reading Tariff 1 | [optional] 
**counterReadingT2** | **Number** | The Meter Counter Reading Tariff 2 | [optional] 
**counterReadingT3** | **Number** | The Meter Counter Reading Tariff 3 | [optional] 
**counterReadingT4** | **Number** | The Meter Counter Reading Tariff 4 | [optional] 
**counterReadingUnit** | **String** | The Unit of the Counter Reading | [optional] 
**current** | **Number** | The Current (in A) | [optional] 
**currentL1** | **Number** | The Current Phase L1 (in A) | [optional] 
**currentL2** | **Number** | The Current Phase L2 (in A) | [optional] 
**currentL3** | **Number** | The Current Phase L3 (in A) | [optional] 
**deviceEnergyType** | **String** | The Energy Type of this device | [optional] 
**digitalInput1** | **Boolean** | The digital input number 1 | [optional] 
**digitalInput2** | **Boolean** | The digital input number 2 | [optional] 
**digitalOutput1** | **Boolean** | The digital output number 1 | [optional] 
**digitalOutput2** | **Boolean** | The digital output number 2 | [optional] 
**familyType** | **String** | The Family Type of the device. | [optional] 
**flowRate** | **Number** | The current flow rate (e.g. m3/h) | [optional] 
**id** | **String** | The ID of the device | [optional] 
**meterSubType** | **String** | The sub meter type (e.g. warmwater or coldwater) | [optional] 
**name** | **String** | The Name of the Device | [optional] 
**powerFactor** | **Number** | The Power Factor (cos phi). Range: 0 - 1 | [optional] 
**powerFactorL1** | **Number** | The Power Factor (cos phi) Phase L1. Range: 0 - 1 | [optional] 
**powerFactorL2** | **Number** | The Power Factor (cos phi) Phase L2. Range: 0 - 1 | [optional] 
**powerFactorL3** | **Number** | The Power Factor (cos phi) Phase L3. Range: 0 - 1 | [optional] 
**serial** | **Number** | The Serial number | [optional] 
**switchOn** | **Boolean** | Flag if the Switch is on on this device. | [optional] 
**switchPhaseL1On** | **Boolean** | Flag if the Phase L1 is on on this device. | [optional] 
**switchPhaseL2On** | **Boolean** | Flag if the Phase L2 is on on this device. | [optional] 
**switchPhaseL3On** | **Boolean** | Flag if the Phase L3 is on on this device. | [optional] 
**temperature** | **Number** | The Temperature (in degree celsius) | [optional] 
**valueDate** | **Date** | Time of last successful connection the the smart-me Cloud. | [optional] 
**voltage** | **Number** | The Voltage (in V) | [optional] 
**voltageL1** | **Number** | The Voltage Phase L1 (in V) | [optional] 
**voltageL2** | **Number** | The Voltage Phase L2 (in V) | [optional] 
**voltageL3** | **Number** | The Voltage Phase L3 (in V) | [optional] 



## Enum: ChargingStationStateEnum


* `Booting` (value: `"Booting"`)

* `ReadyNoCarConnected` (value: `"ReadyNoCarConnected"`)

* `ReadyCarConnected` (value: `"ReadyCarConnected"`)

* `StartedWaitForCar` (value: `"StartedWaitForCar"`)

* `Charging` (value: `"Charging"`)

* `Installation` (value: `"Installation"`)

* `Authorize` (value: `"Authorize"`)

* `Offline` (value: `"Offline"`)





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





## Enum: FamilyTypeEnum


* `MeterFamilyTypeUnknown` (value: `"MeterFamilyTypeUnknown"`)

* `MeterFamilyTypeSmartMeConnectV1` (value: `"MeterFamilyTypeSmartMeConnectV1"`)

* `MeterFamiliyTypeSmartMeMeter` (value: `"MeterFamiliyTypeSmartMeMeter"`)

* `MeterFamiliyTypeSmartMeMeterWithSwitch` (value: `"MeterFamiliyTypeSmartMeMeterWithSwitch"`)

* `MeterFamilyTypeMBusGatewayV1` (value: `"MeterFamilyTypeMBusGatewayV1"`)

* `MeterFamilyTypeRS485GatewayV1` (value: `"MeterFamilyTypeRS485GatewayV1"`)

* `MeterFamilyTypeKamstrupModule` (value: `"MeterFamilyTypeKamstrupModule"`)

* `MeterFamilyTypeSmartMe3PhaseMeter80A` (value: `"MeterFamilyTypeSmartMe3PhaseMeter80A"`)

* `MeterFamilyTypeSmartMe3PhaseMeter32A` (value: `"MeterFamilyTypeSmartMe3PhaseMeter32A"`)

* `MeterFamilyTypeSmartMe3PhaseTelstarTransformer` (value: `"MeterFamilyTypeSmartMe3PhaseTelstarTransformer"`)

* `MeterFamilyTypeLandisGyrModule` (value: `"MeterFamilyTypeLandisGyrModule"`)

* `MeterFamilyTypeFnnOpticalModule` (value: `"MeterFamilyTypeFnnOpticalModule"`)

* `MeterFamilyTypeSmartMe3PhaseTelstar80AWiFi` (value: `"MeterFamilyTypeSmartMe3PhaseTelstar80AWiFi"`)

* `MeterFamilyTypeSmartMe3PhaseTelstar80AMobile` (value: `"MeterFamilyTypeSmartMe3PhaseTelstar80AMobile"`)

* `MeterFamilyTypeSmartMe1PhaseMeter80AV2WiFi` (value: `"MeterFamilyTypeSmartMe1PhaseMeter80AV2WiFi"`)

* `MeterFamilyTypeSmartMe1PhaseMeter32AV2WiFi` (value: `"MeterFamilyTypeSmartMe1PhaseMeter32AV2WiFi"`)

* `MeterFamilyTypeSmartMe1PhaseMeter80AGprs` (value: `"MeterFamilyTypeSmartMe1PhaseMeter80AGprs"`)

* `MeterFamilyTypeSmartMe1PhaseMeter32AGprs` (value: `"MeterFamilyTypeSmartMe1PhaseMeter32AGprs"`)

* `MeterFamilyTypeWMBusGatewayV1` (value: `"MeterFamilyTypeWMBusGatewayV1"`)

* `MeterFamilyTypeSmartMe3PhaseTelstarTransformerMobile` (value: `"MeterFamilyTypeSmartMe3PhaseTelstarTransformerMobile"`)

* `MeterFamilyTypeMithralHallV1` (value: `"MeterFamilyTypeMithralHallV1"`)

* `MeterFamilyTypeRestApiMeter` (value: `"MeterFamilyTypeRestApiMeter"`)

* `MeterFamilyTypeVirtualBillingMeter` (value: `"MeterFamilyTypeVirtualBillingMeter"`)





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




