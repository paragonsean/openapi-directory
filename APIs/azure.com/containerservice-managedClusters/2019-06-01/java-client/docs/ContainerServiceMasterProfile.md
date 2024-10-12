

# ContainerServiceMasterProfile

Profile for the container service master.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | [**CountEnum**](#CountEnum) | Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The default value is 1. |  [optional] |
|**dnsPrefix** | **String** | DNS prefix to be used to create the FQDN for the master pool. |  |
|**firstConsecutiveStaticIP** | **String** | FirstConsecutiveStaticIP used to specify the first static ip of masters. |  [optional] |
|**fqdn** | **String** | FQDN for the master pool. |  [optional] [readonly] |
|**osDiskSizeGB** | **Integer** | OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified. |  [optional] |
|**storageProfile** | **ContainerServiceStorageProfile** |  |  [optional] |
|**vmSize** | **ContainerServiceVMSize** |  |  |
|**vnetSubnetID** | **String** | VNet SubnetID specifies the VNet&#39;s subnet identifier. |  [optional] |



## Enum: CountEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_3 | 3 |
| NUMBER_5 | 5 |



