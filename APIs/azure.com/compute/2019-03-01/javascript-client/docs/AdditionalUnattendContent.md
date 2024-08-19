# ComputeManagementClient.AdditionalUnattendContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**componentName** | **String** | The component name. Currently, the only allowable value is Microsoft-Windows-Shell-Setup. | [optional] 
**content** | **String** | Specifies the XML formatted content that is added to the unattend.xml file for the specified path and component. The XML must be less than 4KB and must include the root element for the setting or feature that is being inserted. | [optional] 
**passName** | **String** | The pass name. Currently, the only allowable value is OobeSystem. | [optional] 
**settingName** | **String** | Specifies the name of the setting to which the content applies. Possible values are: FirstLogonCommands and AutoLogon. | [optional] 



## Enum: ComponentNameEnum


* `Microsoft-Windows-Shell-Setup` (value: `"Microsoft-Windows-Shell-Setup"`)





## Enum: PassNameEnum


* `OobeSystem` (value: `"OobeSystem"`)





## Enum: SettingNameEnum


* `AutoLogon` (value: `"AutoLogon"`)

* `FirstLogonCommands` (value: `"FirstLogonCommands"`)




