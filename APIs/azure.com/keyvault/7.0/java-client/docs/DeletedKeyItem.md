

# DeletedKeyItem

The deleted key item containing the deleted key metadata and information about deletion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deletedDate** | **Integer** | The time when the key was deleted, in UTC |  [optional] [readonly] |
|**recoveryId** | **String** | The url of the recovery object, used to identify and recover the deleted key. |  [optional] |
|**scheduledPurgeDate** | **Integer** | The time when the key is scheduled to be purged, in UTC |  [optional] [readonly] |
|**attributes** | [**KeyAttributes**](KeyAttributes.md) |  |  [optional] |
|**kid** | **String** | Key identifier. |  [optional] |
|**managed** | **Boolean** | True if the key&#39;s lifetime is managed by key vault. If this is a key backing a certificate, then managed will be true. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] |



