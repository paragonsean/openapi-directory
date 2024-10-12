

# Device

Container Class for the Web API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activePower** | **Double** | The Actvie Power or current flow rate |  [optional] |
|**activePowerL1** | **Double** | The Actvie Power Phase L1 |  [optional] |
|**activePowerL2** | **Double** | The Actvie Power Phase L2 |  [optional] |
|**activePowerL3** | **Double** | The Actvie Power Phase L3 |  [optional] |
|**activePowerUnit** | **String** | The Unit of the Active Power Value |  [optional] |
|**activeTariff** | **Integer** | The Number of the Active Tariff |  [optional] |
|**additionalMeterSerialNumber** | **String** | An additional Meter serial number. e.g. the number of a meter a smart-me device is connected to. |  [optional] |
|**analogOutput1** | **Integer** | The analog output number 1 (PWM signal) (0 - 32183) |  [optional] |
|**analogOutput2** | **Integer** | The analog output number 2 (PWM signal) (0 - 32183) |  [optional] |
|**chargingStationState** | [**ChargingStationStateEnum**](#ChargingStationStateEnum) | The state of a pico charging station. (Only available for pico charging stations) |  [optional] |
|**counterReading** | **Double** | The Meter Counter Reading (Total Energy used) |  [optional] |
|**counterReadingExport** | **Double** | The Meter Counter Reading only export |  [optional] |
|**counterReadingImport** | **Double** | The Meter Counter Reading only import |  [optional] |
|**counterReadingT1** | **Double** | The Meter Counter Reading Tariff 1 |  [optional] |
|**counterReadingT2** | **Double** | The Meter Counter Reading Tariff 2 |  [optional] |
|**counterReadingT3** | **Double** | The Meter Counter Reading Tariff 3 |  [optional] |
|**counterReadingT4** | **Double** | The Meter Counter Reading Tariff 4 |  [optional] |
|**counterReadingUnit** | **String** | The Unit of the Counter Reading |  [optional] |
|**current** | **Double** | The Current (in A) |  [optional] |
|**currentL1** | **Double** | The Current Phase L1 (in A) |  [optional] |
|**currentL2** | **Double** | The Current Phase L2 (in A) |  [optional] |
|**currentL3** | **Double** | The Current Phase L3 (in A) |  [optional] |
|**deviceEnergyType** | [**DeviceEnergyTypeEnum**](#DeviceEnergyTypeEnum) | The Energy Type of this device |  [optional] |
|**digitalInput1** | **Boolean** | The digital input number 1 |  [optional] |
|**digitalInput2** | **Boolean** | The digital input number 2 |  [optional] |
|**digitalOutput1** | **Boolean** | The digital output number 1 |  [optional] |
|**digitalOutput2** | **Boolean** | The digital output number 2 |  [optional] |
|**familyType** | [**FamilyTypeEnum**](#FamilyTypeEnum) | The Family Type of the device. |  [optional] |
|**flowRate** | **Double** | The current flow rate (e.g. m3/h) |  [optional] |
|**id** | **String** | The ID of the device |  [optional] |
|**meterSubType** | [**MeterSubTypeEnum**](#MeterSubTypeEnum) | The sub meter type (e.g. warmwater or coldwater) |  [optional] |
|**name** | **String** | The Name of the Device |  [optional] |
|**powerFactor** | **Double** | The Power Factor (cos phi). Range: 0 - 1 |  [optional] |
|**powerFactorL1** | **Double** | The Power Factor (cos phi) Phase L1. Range: 0 - 1 |  [optional] |
|**powerFactorL2** | **Double** | The Power Factor (cos phi) Phase L2. Range: 0 - 1 |  [optional] |
|**powerFactorL3** | **Double** | The Power Factor (cos phi) Phase L3. Range: 0 - 1 |  [optional] |
|**serial** | **Long** | The Serial number |  [optional] |
|**switchOn** | **Boolean** | Flag if the Switch is on on this device. |  [optional] |
|**switchPhaseL1On** | **Boolean** | Flag if the Phase L1 is on on this device. |  [optional] |
|**switchPhaseL2On** | **Boolean** | Flag if the Phase L2 is on on this device. |  [optional] |
|**switchPhaseL3On** | **Boolean** | Flag if the Phase L3 is on on this device. |  [optional] |
|**temperature** | **Double** | The Temperature (in degree celsius) |  [optional] |
|**valueDate** | **OffsetDateTime** | Time of last successful connection the the smart-me Cloud. |  [optional] |
|**voltage** | **Double** | The Voltage (in V) |  [optional] |
|**voltageL1** | **Double** | The Voltage Phase L1 (in V) |  [optional] |
|**voltageL2** | **Double** | The Voltage Phase L2 (in V) |  [optional] |
|**voltageL3** | **Double** | The Voltage Phase L3 (in V) |  [optional] |



## Enum: ChargingStationStateEnum

| Name | Value |
|---- | -----|
| BOOTING | &quot;Booting&quot; |
| READY_NO_CAR_CONNECTED | &quot;ReadyNoCarConnected&quot; |
| READY_CAR_CONNECTED | &quot;ReadyCarConnected&quot; |
| STARTED_WAIT_FOR_CAR | &quot;StartedWaitForCar&quot; |
| CHARGING | &quot;Charging&quot; |
| INSTALLATION | &quot;Installation&quot; |
| AUTHORIZE | &quot;Authorize&quot; |
| OFFLINE | &quot;Offline&quot; |



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



## Enum: FamilyTypeEnum

| Name | Value |
|---- | -----|
| METER_FAMILY_TYPE_UNKNOWN | &quot;MeterFamilyTypeUnknown&quot; |
| METER_FAMILY_TYPE_SMART_ME_CONNECT_V1 | &quot;MeterFamilyTypeSmartMeConnectV1&quot; |
| METER_FAMILIY_TYPE_SMART_ME_METER | &quot;MeterFamiliyTypeSmartMeMeter&quot; |
| METER_FAMILIY_TYPE_SMART_ME_METER_WITH_SWITCH | &quot;MeterFamiliyTypeSmartMeMeterWithSwitch&quot; |
| METER_FAMILY_TYPE_M_BUS_GATEWAY_V1 | &quot;MeterFamilyTypeMBusGatewayV1&quot; |
| METER_FAMILY_TYPE_RS485_GATEWAY_V1 | &quot;MeterFamilyTypeRS485GatewayV1&quot; |
| METER_FAMILY_TYPE_KAMSTRUP_MODULE | &quot;MeterFamilyTypeKamstrupModule&quot; |
| METER_FAMILY_TYPE_SMART_ME3_PHASE_METER80_A | &quot;MeterFamilyTypeSmartMe3PhaseMeter80A&quot; |
| METER_FAMILY_TYPE_SMART_ME3_PHASE_METER32_A | &quot;MeterFamilyTypeSmartMe3PhaseMeter32A&quot; |
| METER_FAMILY_TYPE_SMART_ME3_PHASE_TELSTAR_TRANSFORMER | &quot;MeterFamilyTypeSmartMe3PhaseTelstarTransformer&quot; |
| METER_FAMILY_TYPE_LANDIS_GYR_MODULE | &quot;MeterFamilyTypeLandisGyrModule&quot; |
| METER_FAMILY_TYPE_FNN_OPTICAL_MODULE | &quot;MeterFamilyTypeFnnOpticalModule&quot; |
| METER_FAMILY_TYPE_SMART_ME3_PHASE_TELSTAR80_AWI_FI | &quot;MeterFamilyTypeSmartMe3PhaseTelstar80AWiFi&quot; |
| METER_FAMILY_TYPE_SMART_ME3_PHASE_TELSTAR80_A_MOBILE | &quot;MeterFamilyTypeSmartMe3PhaseTelstar80AMobile&quot; |
| METER_FAMILY_TYPE_SMART_ME1_PHASE_METER80_AV2_WI_FI | &quot;MeterFamilyTypeSmartMe1PhaseMeter80AV2WiFi&quot; |
| METER_FAMILY_TYPE_SMART_ME1_PHASE_METER32_AV2_WI_FI | &quot;MeterFamilyTypeSmartMe1PhaseMeter32AV2WiFi&quot; |
| METER_FAMILY_TYPE_SMART_ME1_PHASE_METER80_A_GPRS | &quot;MeterFamilyTypeSmartMe1PhaseMeter80AGprs&quot; |
| METER_FAMILY_TYPE_SMART_ME1_PHASE_METER32_A_GPRS | &quot;MeterFamilyTypeSmartMe1PhaseMeter32AGprs&quot; |
| METER_FAMILY_TYPE_WM_BUS_GATEWAY_V1 | &quot;MeterFamilyTypeWMBusGatewayV1&quot; |
| METER_FAMILY_TYPE_SMART_ME3_PHASE_TELSTAR_TRANSFORMER_MOBILE | &quot;MeterFamilyTypeSmartMe3PhaseTelstarTransformerMobile&quot; |
| METER_FAMILY_TYPE_MITHRAL_HALL_V1 | &quot;MeterFamilyTypeMithralHallV1&quot; |
| METER_FAMILY_TYPE_REST_API_METER | &quot;MeterFamilyTypeRestApiMeter&quot; |
| METER_FAMILY_TYPE_VIRTUAL_BILLING_METER | &quot;MeterFamilyTypeVirtualBillingMeter&quot; |



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



