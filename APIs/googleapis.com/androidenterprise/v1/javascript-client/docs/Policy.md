# GooglePlayEmmApi.Policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoUpdatePolicy** | **String** | Controls when automatic app updates on the device can be applied. Recommended alternative: autoUpdateMode which is set per app, provides greater flexibility around update frequency. When autoUpdateMode is set to AUTO_UPDATE_POSTPONED or AUTO_UPDATE_HIGH_PRIORITY, autoUpdatePolicy has no effect. \&quot;choiceToTheUser\&quot; allows the device&#39;s user to configure the app update policy. \&quot;always\&quot; enables auto updates. \&quot;never\&quot; disables auto updates. \&quot;wifiOnly\&quot; enables auto updates only when the device is connected to wifi. | [optional] 
**deviceReportPolicy** | **String** | Whether the device reports app states to the EMM. The default value is \&quot;deviceReportDisabled\&quot;. | [optional] 
**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 
**productAvailabilityPolicy** | **String** | The availability granted to the device for the specified products. \&quot;all\&quot; gives the device access to all products, regardless of approval status. \&quot;all\&quot; does not enable automatic visibility of \&quot;alpha\&quot; or \&quot;beta\&quot; tracks. \&quot;whitelist\&quot; grants the device access the products specified in productPolicy[]. Only products that are approved or products that were previously approved (products with revoked approval) by the enterprise can be whitelisted. If no value is provided, the availability set at the user level is applied by default. | [optional] 
**productPolicy** | [**[ProductPolicy]**](ProductPolicy.md) | The list of product policies. The productAvailabilityPolicy needs to be set to WHITELIST or ALL for the product policies to be applied. | [optional] 



## Enum: AutoUpdatePolicyEnum


* `autoUpdatePolicyUnspecified` (value: `"autoUpdatePolicyUnspecified"`)

* `choiceToTheUser` (value: `"choiceToTheUser"`)

* `never` (value: `"never"`)

* `wifiOnly` (value: `"wifiOnly"`)

* `always` (value: `"always"`)





## Enum: DeviceReportPolicyEnum


* `deviceReportPolicyUnspecified` (value: `"deviceReportPolicyUnspecified"`)

* `deviceReportDisabled` (value: `"deviceReportDisabled"`)

* `deviceReportEnabled` (value: `"deviceReportEnabled"`)





## Enum: ProductAvailabilityPolicyEnum


* `productAvailabilityPolicyUnspecified` (value: `"productAvailabilityPolicyUnspecified"`)

* `whitelist` (value: `"whitelist"`)

* `all` (value: `"all"`)




