# UpdateManagement.UpdateConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureVirtualMachines** | **[String]** | List of azure resource Ids for azure virtual machines targeted by the software update configuration. | [optional] 
**duration** | **String** | Maximum time allowed for the software update configuration run. Duration needs to be specified using the format PT[n]H[n]M[n]S as per ISO8601 | [optional] 
**linux** | [**LinuxProperties**](LinuxProperties.md) |  | [optional] 
**nonAzureComputerNames** | **[String]** | List of names of non-azure machines targeted by the software update configuration. | [optional] 
**operatingSystem** | [**OperatingSystemType**](OperatingSystemType.md) |  | 
**targets** | [**TargetProperties**](TargetProperties.md) |  | [optional] 
**windows** | [**WindowsProperties**](WindowsProperties.md) |  | [optional] 


