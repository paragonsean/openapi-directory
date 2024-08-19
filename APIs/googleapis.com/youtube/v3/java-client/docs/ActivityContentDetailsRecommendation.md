

# ActivityContentDetailsRecommendation

Information that identifies the recommended resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason that the resource is recommended to the user. |  [optional] |
|**resourceId** | [**ResourceId**](ResourceId.md) |  |  [optional] |
|**seedResourceId** | [**ResourceId**](ResourceId.md) |  |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| REASON_UNSPECIFIED | &quot;reasonUnspecified&quot; |
| VIDEO_FAVORITED | &quot;videoFavorited&quot; |
| VIDEO_LIKED | &quot;videoLiked&quot; |
| VIDEO_WATCHED | &quot;videoWatched&quot; |



