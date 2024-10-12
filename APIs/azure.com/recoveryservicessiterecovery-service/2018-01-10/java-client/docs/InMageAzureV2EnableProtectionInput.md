

# InMageAzureV2EnableProtectionInput

VMware Azure specific enable protection input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disksToInclude** | **List&lt;String&gt;** | The disks to include list. |  [optional] |
|**enableRdpOnTargetOption** | **String** | The selected option to enable RDP\\SSH on target vm after failover. String value of {SrsDataContract.EnableRDPOnTargetOption} enum. |  [optional] |
|**logStorageAccountId** | **String** | The storage account to be used for logging during replication. |  [optional] |
|**masterTargetId** | **String** | The Master target Id. |  [optional] |
|**multiVmGroupId** | **String** | The multi vm group Id. |  [optional] |
|**multiVmGroupName** | **String** | The multi vm group name. |  [optional] |
|**processServerId** | **String** | The Process Server Id. |  [optional] |
|**runAsAccountId** | **String** | The CS account Id. |  [optional] |
|**storageAccountId** | **String** | The storage account name. |  |
|**targetAzureNetworkId** | **String** | The selected target Azure network Id. |  [optional] |
|**targetAzureSubnetId** | **String** | The selected target Azure subnet Id. |  [optional] |
|**targetAzureV1ResourceGroupId** | **String** | The Id of the target resource group (for classic deployment) in which the failover VM is to be created. |  [optional] |
|**targetAzureV2ResourceGroupId** | **String** | The Id of the target resource group (for resource manager deployment) in which the failover VM is to be created. |  [optional] |
|**targetAzureVmName** | **String** | The target azure Vm Name. |  [optional] |
|**useManagedDisks** | **String** | A value indicating whether managed disks should be used during failover. |  [optional] |



