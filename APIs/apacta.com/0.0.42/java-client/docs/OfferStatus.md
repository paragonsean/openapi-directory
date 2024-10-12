

# OfferStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** |  |  [optional] [readonly] |
|**createdById** | **UUID** |  |  [optional] |
|**deleted** | **String** | Only present if it&#39;s a deleted object |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**id** | **UUID** |  |  [optional] |
|**identifier** | [**IdentifierEnum**](#IdentifierEnum) | One of 6 values |  [optional] |
|**isCustom** | **Boolean** |  |  [optional] |
|**modified** | **String** |  |  [optional] [readonly] |
|**modifiedById** | **UUID** |  |  [optional] |
|**name** | **String** |  |  [optional] |



## Enum: IdentifierEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| REJECTED | &quot;rejected&quot; |
| DRAFT | &quot;draft&quot; |
| SENT | &quot;sent&quot; |
| SENT_AND_SEEN | &quot;sent_and_seen&quot; |
| DECLINED | &quot;declined&quot; |



