# ContainerServiceClient.ContainerServiceMasterProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The default value is 1. | [optional] [default to CountEnum.1]
**dnsPrefix** | **String** | DNS prefix to be used to create the FQDN for the master pool. | 
**firstConsecutiveStaticIP** | **String** | FirstConsecutiveStaticIP used to specify the first static ip of masters. | [optional] [default to &#39;10.240.255.5&#39;]
**fqdn** | **String** | FQDN for the master pool. | [optional] [readonly] 
**osDiskSizeGB** | **Number** | OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified. | [optional] 
**storageProfile** | [**ContainerServiceStorageProfile**](ContainerServiceStorageProfile.md) |  | [optional] 
**vmSize** | [**ContainerServiceVMSize**](ContainerServiceVMSize.md) |  | 
**vnetSubnetID** | **String** | VNet SubnetID specifies the VNet&#39;s subnet identifier. | [optional] 



## Enum: CountEnum


* `1` (value: `1`)

* `3` (value: `3`)

* `5` (value: `5`)




