

# AdditionalUnattendContent

Specifies additional XML formatted information that can be included in the Unattend.xml file, which is used by Windows Setup. Contents are defined by setting name, component name, and the pass in which the content is applied.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**componentName** | [**ComponentNameEnum**](#ComponentNameEnum) | The component name. Currently, the only allowable value is Microsoft-Windows-Shell-Setup. |  [optional] |
|**content** | **String** | Specifies the XML formatted content that is added to the unattend.xml file for the specified path and component. The XML must be less than 4KB and must include the root element for the setting or feature that is being inserted. |  [optional] |
|**passName** | [**PassNameEnum**](#PassNameEnum) | The pass name. Currently, the only allowable value is OobeSystem. |  [optional] |
|**settingName** | [**SettingNameEnum**](#SettingNameEnum) | Specifies the name of the setting to which the content applies. Possible values are: FirstLogonCommands and AutoLogon. |  [optional] |



## Enum: ComponentNameEnum

| Name | Value |
|---- | -----|
| MICROSOFT_WINDOWS_SHELL_SETUP | &quot;Microsoft-Windows-Shell-Setup&quot; |



## Enum: PassNameEnum

| Name | Value |
|---- | -----|
| OOBE_SYSTEM | &quot;OobeSystem&quot; |



## Enum: SettingNameEnum

| Name | Value |
|---- | -----|
| AUTO_LOGON | &quot;AutoLogon&quot; |
| FIRST_LOGON_COMMANDS | &quot;FirstLogonCommands&quot; |



