

# GoogleSearchIdeahubV1alphaIdeaActivity

An idea activity entry.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ideas** | **List&lt;String&gt;** | The Idea IDs for this entry. If empty, topics should be set. |  [optional] |
|**name** | **String** | Unique identifier for the idea activity. The name is ignored when creating an idea activity. Format: platforms/{platform}/properties/{property}/ideaActivities/{idea_activity} |  [optional] |
|**topics** | **List&lt;String&gt;** | The Topic IDs for this entry. If empty, ideas should be set. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of activity performed. |  [optional] |
|**uri** | **String** | The uri the activity relates to. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| POST_DRAFTED | &quot;POST_DRAFTED&quot; |
| POST_PUBLISHED | &quot;POST_PUBLISHED&quot; |
| POST_DELETED | &quot;POST_DELETED&quot; |
| POST_UNPUBLISHED | &quot;POST_UNPUBLISHED&quot; |



