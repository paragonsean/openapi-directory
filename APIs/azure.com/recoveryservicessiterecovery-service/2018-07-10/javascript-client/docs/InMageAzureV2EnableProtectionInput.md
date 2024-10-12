# SiteRecoveryManagementClient.InMageAzureV2EnableProtectionInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskEncryptionSetId** | **String** | The DiskEncryptionSet ARM ID. | [optional] 
**diskType** | **String** | The DiskType. | [optional] 
**disksToInclude** | [**[InMageAzureV2DiskInputDetails]**](InMageAzureV2DiskInputDetails.md) | The disks to include list. | [optional] 
**enableRdpOnTargetOption** | **String** | The selected option to enable RDP\\SSH on target vm after failover. String value of {SrsDataContract.EnableRDPOnTargetOption} enum. | [optional] 
**logStorageAccountId** | **String** | The storage account to be used for logging during replication. | [optional] 
**masterTargetId** | **String** | The Master target Id. | [optional] 
**multiVmGroupId** | **String** | The multi vm group Id. | [optional] 
**multiVmGroupName** | **String** | The multi vm group name. | [optional] 
**processServerId** | **String** | The Process Server Id. | [optional] 
**runAsAccountId** | **String** | The CS account Id. | [optional] 
**storageAccountId** | **String** | The storage account name. | [optional] 
**targetAzureNetworkId** | **String** | The selected target Azure network Id. | [optional] 
**targetAzureSubnetId** | **String** | The selected target Azure subnet Id. | [optional] 
**targetAzureV1ResourceGroupId** | **String** | The Id of the target resource group (for classic deployment) in which the failover VM is to be created. | [optional] 
**targetAzureV2ResourceGroupId** | **String** | The Id of the target resource group (for resource manager deployment) in which the failover VM is to be created. | [optional] 
**targetAzureVmName** | **String** | The target azure Vm Name. | [optional] 



## Enum: DiskTypeEnum


* `Standard_LRS` (value: `"Standard_LRS"`)

* `Premium_LRS` (value: `"Premium_LRS"`)

* `StandardSSD_LRS` (value: `"StandardSSD_LRS"`)




