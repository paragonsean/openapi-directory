

# Policy

The device policy for a given managed device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoUpdatePolicy** | [**AutoUpdatePolicyEnum**](#AutoUpdatePolicyEnum) | Controls when automatic app updates on the device can be applied. Recommended alternative: autoUpdateMode which is set per app, provides greater flexibility around update frequency. When autoUpdateMode is set to AUTO_UPDATE_POSTPONED or AUTO_UPDATE_HIGH_PRIORITY, autoUpdatePolicy has no effect. \&quot;choiceToTheUser\&quot; allows the device&#39;s user to configure the app update policy. \&quot;always\&quot; enables auto updates. \&quot;never\&quot; disables auto updates. \&quot;wifiOnly\&quot; enables auto updates only when the device is connected to wifi. |  [optional] |
|**deviceReportPolicy** | [**DeviceReportPolicyEnum**](#DeviceReportPolicyEnum) | Whether the device reports app states to the EMM. The default value is \&quot;deviceReportDisabled\&quot;. |  [optional] |
|**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  |  [optional] |
|**productAvailabilityPolicy** | [**ProductAvailabilityPolicyEnum**](#ProductAvailabilityPolicyEnum) | The availability granted to the device for the specified products. \&quot;all\&quot; gives the device access to all products, regardless of approval status. \&quot;all\&quot; does not enable automatic visibility of \&quot;alpha\&quot; or \&quot;beta\&quot; tracks. \&quot;whitelist\&quot; grants the device access the products specified in productPolicy[]. Only products that are approved or products that were previously approved (products with revoked approval) by the enterprise can be whitelisted. If no value is provided, the availability set at the user level is applied by default. |  [optional] |
|**productPolicy** | [**List&lt;ProductPolicy&gt;**](ProductPolicy.md) | The list of product policies. The productAvailabilityPolicy needs to be set to WHITELIST or ALL for the product policies to be applied. |  [optional] |



## Enum: AutoUpdatePolicyEnum

| Name | Value |
|---- | -----|
| AUTO_UPDATE_POLICY_UNSPECIFIED | &quot;autoUpdatePolicyUnspecified&quot; |
| CHOICE_TO_THE_USER | &quot;choiceToTheUser&quot; |
| NEVER | &quot;never&quot; |
| WIFI_ONLY | &quot;wifiOnly&quot; |
| ALWAYS | &quot;always&quot; |



## Enum: DeviceReportPolicyEnum

| Name | Value |
|---- | -----|
| DEVICE_REPORT_POLICY_UNSPECIFIED | &quot;deviceReportPolicyUnspecified&quot; |
| DEVICE_REPORT_DISABLED | &quot;deviceReportDisabled&quot; |
| DEVICE_REPORT_ENABLED | &quot;deviceReportEnabled&quot; |



## Enum: ProductAvailabilityPolicyEnum

| Name | Value |
|---- | -----|
| PRODUCT_AVAILABILITY_POLICY_UNSPECIFIED | &quot;productAvailabilityPolicyUnspecified&quot; |
| WHITELIST | &quot;whitelist&quot; |
| ALL | &quot;all&quot; |



