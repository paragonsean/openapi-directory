# VirtualMachineImageTemplate.ImageTemplatePowerShellCustomizer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline** | **[String]** | Array of PowerShell commands to execute | [optional] 
**script** | **String** | The PowerShell script to be run for customizing. It can be a github link, SAS URI for Azure Storage, etc | [optional] 
**validExitCodes** | **[Number]** | Valid exit codes for the PowerShell script. [Default: 0] | [optional] 


