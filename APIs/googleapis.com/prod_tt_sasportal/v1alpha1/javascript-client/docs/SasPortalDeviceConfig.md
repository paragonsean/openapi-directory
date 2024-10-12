# SasPortalApiTesting.SasPortalDeviceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airInterface** | [**SasPortalDeviceAirInterface**](SasPortalDeviceAirInterface.md) |  | [optional] 
**callSign** | **String** | The call sign of the device operator. | [optional] 
**category** | **String** | FCC category of the device. | [optional] 
**installationParams** | [**SasPortalInstallationParams**](SasPortalInstallationParams.md) |  | [optional] 
**isSigned** | **Boolean** | Output only. Whether the configuration has been signed by a CPI. | [optional] 
**measurementCapabilities** | **[String]** | Measurement reporting capabilities of the device. | [optional] 
**model** | [**SasPortalDeviceModel**](SasPortalDeviceModel.md) |  | [optional] 
**state** | **String** | State of the configuration. | [optional] 
**updateTime** | **String** | Output only. The last time the device configuration was edited. | [optional] 
**userId** | **String** | The identifier of a device user. | [optional] 



## Enum: CategoryEnum


* `UNSPECIFIED` (value: `"DEVICE_CATEGORY_UNSPECIFIED"`)

* `A` (value: `"DEVICE_CATEGORY_A"`)

* `B` (value: `"DEVICE_CATEGORY_B"`)





## Enum: [MeasurementCapabilitiesEnum]


* `UNSPECIFIED` (value: `"MEASUREMENT_CAPABILITY_UNSPECIFIED"`)

* `RECEIVED_POWER_WITH_GRANT` (value: `"MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITH_GRANT"`)

* `RECEIVED_POWER_WITHOUT_GRANT` (value: `"MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITHOUT_GRANT"`)





## Enum: StateEnum


* `DEVICE_CONFIG_STATE_UNSPECIFIED` (value: `"DEVICE_CONFIG_STATE_UNSPECIFIED"`)

* `DRAFT` (value: `"DRAFT"`)

* `FINAL` (value: `"FINAL"`)




