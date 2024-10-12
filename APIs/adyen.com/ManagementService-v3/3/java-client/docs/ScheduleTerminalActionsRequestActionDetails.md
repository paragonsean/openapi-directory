

# ScheduleTerminalActionsRequestActionDetails

Information about the action to take.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | The unique identifier of the app to be uninstalled. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of terminal action: Install an Android app. |  [optional] |
|**certificateId** | **String** | The unique identifier of the certificate to be uninstalled. |  [optional] |
|**updateAtFirstMaintenanceCall** | **Boolean** | Boolean flag that tells if the terminal should update at the first next maintenance call. If false, terminal will update on its configured reboot time. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INSTALL_ANDROID_APP | &quot;InstallAndroidApp&quot; |
| INSTALL_ANDROID_CERTIFICATE | &quot;InstallAndroidCertificate&quot; |
| RELEASE_UPDATE | &quot;ReleaseUpdate&quot; |
| UNINSTALL_ANDROID_APP | &quot;UninstallAndroidApp&quot; |
| UNINSTALL_ANDROID_CERTIFICATE | &quot;UninstallAndroidCertificate&quot; |



