

# SyncRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelCids** | **List&lt;String&gt;** | List of channel CIDs to sync |  [optional] |
|**clientId** | **String** |  |  [optional] |
|**connectionId** | **String** |  |  [optional] |
|**lastSyncAt** | **OffsetDateTime** | Date from which synchronization should happen |  |
|**user** | **UserObjectRequest** |  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**watch** | **Boolean** | If set to true this will start watching requested and newly added channels that user has access to. If error occurred with this option enabled and it is not an input error - channels will still be watched. |  [optional] |
|**withInaccessibleCids** | **Boolean** | If set to true this will add &#39;inaccessible_cids&#39; to response type |  [optional] |



