

# DeletedStorageAccountItem

The deleted storage account item containing metadata about the deleted storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedDate** | **Integer** | The time when the storage account was deleted, in UTC |  [optional] [readonly] |
|**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted storage account. |  [optional] |
|**scheduledPurgeDate** | **Integer** | The time when the storage account is scheduled to be purged, in UTC |  [optional] [readonly] |
|**attributes** | [**StorageAccountAttributes**](StorageAccountAttributes.md) |  |  [optional] |
|**id** | **String** | Storage identifier. |  [optional] [readonly] |
|**resourceId** | **String** | Storage account resource Id. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] [readonly] |



