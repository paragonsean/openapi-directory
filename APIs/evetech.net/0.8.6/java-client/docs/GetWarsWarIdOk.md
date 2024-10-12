

# GetWarsWarIdOk

200 ok object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggressor** | [**GetWarsWarIdAggressor**](GetWarsWarIdAggressor.md) |  |  |
|**allies** | [**List&lt;GetWarsWarIdAlly&gt;**](GetWarsWarIdAlly.md) | allied corporations or alliances, each object contains either corporation_id or alliance_id |  [optional] |
|**declared** | **OffsetDateTime** | Time that the war was declared |  |
|**defender** | [**GetWarsWarIdDefender**](GetWarsWarIdDefender.md) |  |  |
|**finished** | **OffsetDateTime** | Time the war ended and shooting was no longer allowed |  [optional] |
|**id** | **Integer** | ID of the specified war |  |
|**mutual** | **Boolean** | Was the war declared mutual by both parties |  |
|**openForAllies** | **Boolean** | Is the war currently open for allies or not |  |
|**retracted** | **OffsetDateTime** | Time the war was retracted but both sides could still shoot each other |  [optional] |
|**started** | **OffsetDateTime** | Time when the war started and both sides could shoot each other |  [optional] |



