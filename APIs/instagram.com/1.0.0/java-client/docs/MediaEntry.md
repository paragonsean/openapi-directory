

# MediaEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attribution** | **String** | ??? Unknown ??? |  [optional] |
|**caption** | [**CaptionData**](CaptionData.md) |  |  [optional] |
|**comments** | [**CommentsCollection**](CommentsCollection.md) |  |  [optional] |
|**createdTime** | **String** | Media creation UNIX timestamp |  [optional] |
|**filter** | **String** | Filter of this media entry |  [optional] |
|**id** | **String** | ID of a media entry |  [optional] |
|**images** | [**ImagesData**](ImagesData.md) |  |  [optional] |
|**likes** | [**LikesCollection**](LikesCollection.md) |  |  [optional] |
|**link** | **String** | Fixed URL of this media entry |  [optional] |
|**location** | [**LocationInfo**](LocationInfo.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** | List of tags assigned to this media |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this media entry |  [optional] |
|**user** | [**UserShortInfo**](UserShortInfo.md) |  |  [optional] |
|**userHasLiked** | **Boolean** | Indicates whether authenticated user has liked this media or not |  [optional] |
|**usersInPhoto** | [**List&lt;UserInPhoto&gt;**](UserInPhoto.md) | Users located on this media entry |  [optional] |
|**videos** | [**VideosData**](VideosData.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| VIDEO | &quot;video&quot; |



