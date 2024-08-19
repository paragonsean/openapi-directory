# VirtualMachineImageTemplate.ImageTemplatePowerShellCustomizer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline** | **[String]** | Array of PowerShell commands to execute | [optional] 
**runElevated** | **Boolean** | If specified, the PowerShell script will be run with elevated privileges | [optional] 
**scriptUri** | **String** | URI of the PowerShell script to be run for customizing. It can be a github link, SAS URI for Azure Storage, etc | [optional] 
**sha256Checksum** | **String** | SHA256 checksum of the power shell script provided in the scriptUri field above | [optional] 
**validExitCodes** | **[Number]** | Valid exit codes for the PowerShell script. [Default: 0] | [optional] 


