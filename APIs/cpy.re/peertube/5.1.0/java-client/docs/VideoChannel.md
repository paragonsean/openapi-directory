

# VideoChannel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**followersCount** | **Integer** | number of followers of this actor, as seen by this instance |  [optional] |
|**followingCount** | **Integer** | number of actors subscribed to by this actor, as seen by this instance |  [optional] |
|**host** | **String** | server on which the actor is resident |  [optional] |
|**hostRedundancyAllowed** | **Boolean** | whether this actor&#39;s host allows redundancy of its videos |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**name** | **String** | immutable name of the actor, used to find or mention it |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**url** | **String** |  |  [optional] |
|**banners** | [**List&lt;ActorImage&gt;**](ActorImage.md) |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**displayName** | **String** | editable name of the channel, displayed in its representations |  [optional] |
|**isLocal** | **Boolean** |  |  [optional] [readonly] |
|**ownerAccount** | [**VideoChannelAllOfOwnerAccount**](VideoChannelAllOfOwnerAccount.md) |  |  [optional] |
|**support** | **String** | text shown by default on all videos of this channel, to tell the audience how to support it |  [optional] |



