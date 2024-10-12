# GooglePlayEmmApi.AutoInstallPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoInstallConstraint** | [**[AutoInstallConstraint]**](AutoInstallConstraint.md) | The constraints for auto-installing the app. You can specify a maximum of one constraint. | [optional] 
**autoInstallMode** | **String** | The auto-install mode. If unset, defaults to \&quot;doNotAutoInstall\&quot;. An app is automatically installed regardless of a set maintenance window. | [optional] 
**autoInstallPriority** | **Number** | The priority of the install, as an unsigned integer. A lower number means higher priority. | [optional] 
**minimumVersionCode** | **Number** | The minimum version of the app. If a lower version of the app is installed, then the app will be auto-updated according to the auto-install constraints, instead of waiting for the regular auto-update. You can set a minimum version code for at most 20 apps per device. | [optional] 



## Enum: AutoInstallModeEnum


* `autoInstallModeUnspecified` (value: `"autoInstallModeUnspecified"`)

* `doNotAutoInstall` (value: `"doNotAutoInstall"`)

* `autoInstallOnce` (value: `"autoInstallOnce"`)

* `forceAutoInstall` (value: `"forceAutoInstall"`)




