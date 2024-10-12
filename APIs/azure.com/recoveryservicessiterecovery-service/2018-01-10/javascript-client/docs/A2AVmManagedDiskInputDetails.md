# SiteRecoveryManagementClient.A2AVmManagedDiskInputDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskId** | **String** | The disk Id. | [optional] 
**primaryStagingAzureStorageAccountId** | **String** | The primary staging storage account Arm Id. | [optional] 
**recoveryReplicaDiskAccountType** | **String** | The replica disk type. Its an optional value and will be same as source disk type if not user provided. | [optional] 
**recoveryResourceGroupId** | **String** | The target resource group Arm Id. | [optional] 
**recoveryTargetDiskAccountType** | **String** | The target disk type after failover. Its an optional value and will be same as source disk type if not user provided. | [optional] 


