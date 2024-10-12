# HybridDataManagementClient.DataStoreProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerSecrets** | [**[CustomerSecret]**](CustomerSecret.md) | List of customer secrets containing a key identifier and key value. The key identifier is a way for the specific data source to understand the key. Value contains customer secret encrypted by the encryptionKeys. | [optional] 
**dataStoreTypeId** | **String** | The arm id of the data store type. | 
**extendedProperties** | **Object** | A generic json used differently by each data source type. | [optional] 
**repositoryId** | **String** | Arm Id for the manager resource to which the data source is associated. This is optional. | [optional] 
**state** | **String** | State of the data source. | 



## Enum: StateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)

* `Supported` (value: `"Supported"`)




