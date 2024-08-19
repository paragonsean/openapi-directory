

# GoogleChromeManagementV1NetworkDevice

Details about the network device. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportNetworkDeviceConfiguration](https://chromeenterprise.google/policies/#ReportNetworkDeviceConfiguration) * Data Collection Frequency: At device startup * Default Data Reporting Frequency: At device startup - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: Yes * Reported for affiliated users only: N/A

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**iccid** | **String** | Output only. The integrated circuit card ID associated with the device&#39;s sim card. |  [optional] [readonly] |
|**imei** | **String** | Output only. IMEI (if applicable) of the corresponding network device. |  [optional] [readonly] |
|**macAddress** | **String** | Output only. MAC address (if applicable) of the corresponding network device. |  [optional] [readonly] |
|**mdn** | **String** | Output only. The mobile directory number associated with the device&#39;s sim card. |  [optional] [readonly] |
|**meid** | **String** | Output only. MEID (if applicable) of the corresponding network device. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Network device type. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NETWORK_DEVICE_TYPE_UNSPECIFIED | &quot;NETWORK_DEVICE_TYPE_UNSPECIFIED&quot; |
| CELLULAR_DEVICE | &quot;CELLULAR_DEVICE&quot; |
| ETHERNET_DEVICE | &quot;ETHERNET_DEVICE&quot; |
| WIFI_DEVICE | &quot;WIFI_DEVICE&quot; |



