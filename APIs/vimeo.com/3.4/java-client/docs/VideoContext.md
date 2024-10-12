

# VideoContext

The context of the video's subscription, if this video is part of a subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The contextual action:  Option descriptions:  * &#x60;Added to&#x60; - An Added To action.  * &#x60;Appearance by&#x60; - An Appearance By action.  * &#x60;Liked by&#x60; - A Liked By action.  * &#x60;Uploaded by&#x60; - An Unloaded By action.  |  |
|**resource** | **Object** | The contextual resource: a user, group, or channel representation, or an object of a tag. |  |
|**resourceType** | **String** | The contextual resource type. |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ADDED_TO | &quot;Added to&quot; |
| APPEARANCE_BY | &quot;Appearance by&quot; |
| LIKED_BY | &quot;Liked by&quot; |
| UPLOADED_BY | &quot;Uploaded by&quot; |



