

# HyperVReplicaAzureEnableProtectionInput

Azure specific enable protection input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disksToInclude** | **List&lt;String&gt;** | The list of VHD IDs of disks to be protected. |  [optional] |
|**enableRdpOnTargetOption** | **String** | The selected option to enable RDP\\SSH on target vm after failover. String value of {SrsDataContract.EnableRDPOnTargetOption} enum. |  [optional] |
|**hvHostVmId** | **String** | The Hyper-V host Vm Id. |  [optional] |
|**logStorageAccountId** | **String** | The storage account to be used for logging during replication. |  [optional] |
|**osType** | **String** | The OS type associated with vm. |  [optional] |
|**targetAzureNetworkId** | **String** | The selected target Azure network Id. |  [optional] |
|**targetAzureSubnetId** | **String** | The selected target Azure subnet Id. |  [optional] |
|**targetAzureV1ResourceGroupId** | **String** | The Id of the target resource group (for classic deployment) in which the failover VM is to be created. |  [optional] |
|**targetAzureV2ResourceGroupId** | **String** | The Id of the target resource group (for resource manager deployment) in which the failover VM is to be created. |  [optional] |
|**targetAzureVmName** | **String** | The target azure Vm Name. |  [optional] |
|**targetStorageAccountId** | **String** | The storage account name. |  [optional] |
|**useManagedDisks** | **String** | A value indicating whether managed disks should be used during failover. |  [optional] |
|**vhdId** | **String** | The OS disk VHD id associated with vm. |  [optional] |
|**vmName** | **String** | The Vm Name. |  [optional] |



