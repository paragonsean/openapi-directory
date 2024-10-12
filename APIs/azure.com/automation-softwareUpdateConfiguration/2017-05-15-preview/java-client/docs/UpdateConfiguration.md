

# UpdateConfiguration

Update specific properties of the software update configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureVirtualMachines** | **List&lt;String&gt;** | List of azure resource Ids for azure virtual machines targeted by the software update configuration. |  [optional] |
|**duration** | **String** | Maximum time allowed for the software update configuration run. Duration needs to be specified using the format PT[n]H[n]M[n]S as per ISO8601 |  [optional] |
|**linux** | [**LinuxProperties**](LinuxProperties.md) |  |  [optional] |
|**nonAzureComputerNames** | **List&lt;String&gt;** | List of names of non-azure machines targeted by the software update configuration. |  [optional] |
|**operatingSystem** | **OperatingSystemType** |  |  |
|**targets** | [**TargetProperties**](TargetProperties.md) |  |  [optional] |
|**windows** | [**WindowsProperties**](WindowsProperties.md) |  |  [optional] |



