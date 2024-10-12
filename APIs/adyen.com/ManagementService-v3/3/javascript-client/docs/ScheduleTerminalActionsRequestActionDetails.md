# ManagementApi.ScheduleTerminalActionsRequestActionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The unique identifier of the app to be uninstalled. | [optional] 
**type** | **String** | Type of terminal action: Install an Android app. | [optional] [default to &#39;InstallAndroidApp&#39;]
**certificateId** | **String** | The unique identifier of the certificate to be uninstalled. | [optional] 
**updateAtFirstMaintenanceCall** | **Boolean** | Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will update on its configured reboot time. | [optional] 



## Enum: TypeEnum


* `InstallAndroidApp` (value: `"InstallAndroidApp"`)

* `InstallAndroidCertificate` (value: `"InstallAndroidCertificate"`)

* `ReleaseUpdate` (value: `"ReleaseUpdate"`)

* `UninstallAndroidApp` (value: `"UninstallAndroidApp"`)

* `UninstallAndroidCertificate` (value: `"UninstallAndroidCertificate"`)




