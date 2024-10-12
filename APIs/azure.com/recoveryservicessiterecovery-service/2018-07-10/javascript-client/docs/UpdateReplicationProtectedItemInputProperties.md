# SiteRecoveryManagementClient.UpdateReplicationProtectedItemInputProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableRdpOnTargetOption** | **String** | The selected option to enable RDP\\SSH on target vm after failover. String value of {SrsDataContract.EnableRDPOnTargetOption} enum. | [optional] 
**licenseType** | **String** | License type. | [optional] 
**providerSpecificDetails** | [**UpdateReplicationProtectedItemProviderInput**](UpdateReplicationProtectedItemProviderInput.md) |  | [optional] 
**recoveryAvailabilitySetId** | **String** | The target availability set id. | [optional] 
**recoveryAzureVMName** | **String** | Target azure VM name given by the user. | [optional] 
**recoveryAzureVMSize** | **String** | Target Azure Vm size. | [optional] 
**selectedRecoveryAzureNetworkId** | **String** | Target Azure Network Id. | [optional] 
**selectedSourceNicId** | **String** | The selected source nic Id which will be used as the primary nic during failover. | [optional] 
**selectedTfoAzureNetworkId** | **String** | The Azure Network Id for test failover. | [optional] 
**vmNics** | [**[VMNicInputDetails]**](VMNicInputDetails.md) | The list of vm nic details. | [optional] 



## Enum: LicenseTypeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `NoLicenseType` (value: `"NoLicenseType"`)

* `WindowsServer` (value: `"WindowsServer"`)




