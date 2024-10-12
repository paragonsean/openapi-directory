

# SasPortalDeviceConfig

Information about the device configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airInterface** | [**SasPortalDeviceAirInterface**](SasPortalDeviceAirInterface.md) |  |  [optional] |
|**callSign** | **String** | The call sign of the device operator. |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | FCC category of the device. |  [optional] |
|**installationParams** | [**SasPortalInstallationParams**](SasPortalInstallationParams.md) |  |  [optional] |
|**isSigned** | **Boolean** | Output only. Whether the configuration has been signed by a CPI. |  [optional] |
|**measurementCapabilities** | [**List&lt;MeasurementCapabilitiesEnum&gt;**](#List&lt;MeasurementCapabilitiesEnum&gt;) | Measurement reporting capabilities of the device. |  [optional] |
|**model** | [**SasPortalDeviceModel**](SasPortalDeviceModel.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the configuration. |  [optional] |
|**updateTime** | **String** | Output only. The last time the device configuration was edited. |  [optional] |
|**userId** | **String** | The identifier of a device user. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DEVICE_CATEGORY_UNSPECIFIED&quot; |
| A | &quot;DEVICE_CATEGORY_A&quot; |
| B | &quot;DEVICE_CATEGORY_B&quot; |



## Enum: List&lt;MeasurementCapabilitiesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MEASUREMENT_CAPABILITY_UNSPECIFIED&quot; |
| RECEIVED_POWER_WITH_GRANT | &quot;MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITH_GRANT&quot; |
| RECEIVED_POWER_WITHOUT_GRANT | &quot;MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITHOUT_GRANT&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DEVICE_CONFIG_STATE_UNSPECIFIED | &quot;DEVICE_CONFIG_STATE_UNSPECIFIED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| FINAL | &quot;FINAL&quot; |



