

# AutoInstallPolicy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoInstallConstraint** | [**List&lt;AutoInstallConstraint&gt;**](AutoInstallConstraint.md) | The constraints for auto-installing the app. You can specify a maximum of one constraint. |  [optional] |
|**autoInstallMode** | [**AutoInstallModeEnum**](#AutoInstallModeEnum) | The auto-install mode. If unset, defaults to \&quot;doNotAutoInstall\&quot;. An app is automatically installed regardless of a set maintenance window. |  [optional] |
|**autoInstallPriority** | **Integer** | The priority of the install, as an unsigned integer. A lower number means higher priority. |  [optional] |
|**minimumVersionCode** | **Integer** | The minimum version of the app. If a lower version of the app is installed, then the app will be auto-updated according to the auto-install constraints, instead of waiting for the regular auto-update. You can set a minimum version code for at most 20 apps per device. |  [optional] |



## Enum: AutoInstallModeEnum

| Name | Value |
|---- | -----|
| AUTO_INSTALL_MODE_UNSPECIFIED | &quot;autoInstallModeUnspecified&quot; |
| DO_NOT_AUTO_INSTALL | &quot;doNotAutoInstall&quot; |
| AUTO_INSTALL_ONCE | &quot;autoInstallOnce&quot; |
| FORCE_AUTO_INSTALL | &quot;forceAutoInstall&quot; |



