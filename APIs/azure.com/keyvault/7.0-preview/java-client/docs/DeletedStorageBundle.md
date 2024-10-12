

# DeletedStorageBundle

A deleted storage account bundle consisting of its previous id, attributes and its tags, as well as information on when it will be purged.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedDate** | **Integer** | The time when the storage account was deleted, in UTC |  [optional] [readonly] |
|**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted storage account. |  [optional] |
|**scheduledPurgeDate** | **Integer** | The time when the storage account is scheduled to be purged, in UTC |  [optional] [readonly] |
|**activeKeyName** | **String** | The current active storage account key name. |  [optional] [readonly] |
|**attributes** | [**StorageAccountAttributes**](StorageAccountAttributes.md) |  |  [optional] |
|**autoRegenerateKey** | **Boolean** | whether keyvault should manage the storage account for the user. |  [optional] [readonly] |
|**id** | **String** | The storage account id. |  [optional] [readonly] |
|**regenerationPeriod** | **String** | The key regeneration time duration specified in ISO-8601 format. |  [optional] [readonly] |
|**resourceId** | **String** | The storage account resource id. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs |  [optional] [readonly] |



