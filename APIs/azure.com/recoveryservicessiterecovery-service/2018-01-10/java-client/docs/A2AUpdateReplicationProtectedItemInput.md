

# A2AUpdateReplicationProtectedItemInput

InMage Azure V2 input to update replication protected item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskEncryptionInfo** | [**DiskEncryptionInfo**](DiskEncryptionInfo.md) |  |  [optional] |
|**managedDiskUpdateDetails** | [**List&lt;A2AVmManagedDiskUpdateDetails&gt;**](A2AVmManagedDiskUpdateDetails.md) | Managed disk update details. |  [optional] |
|**recoveryBootDiagStorageAccountId** | **String** | The boot diagnostic storage account. |  [optional] |
|**recoveryCloudServiceId** | **String** | The target cloud service ARM Id (for V1). |  [optional] |
|**recoveryResourceGroupId** | **String** | The target resource group ARM Id (for V2). |  [optional] |



