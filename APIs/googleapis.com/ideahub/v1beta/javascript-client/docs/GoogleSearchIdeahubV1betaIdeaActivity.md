# IdeaHubApi.GoogleSearchIdeahubV1betaIdeaActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ideas** | **[String]** | The Idea IDs for this entry. If empty, topics should be set. | [optional] 
**name** | **String** | Unique identifier for the idea activity. The name is ignored when creating an idea activity. Format: platforms/{platform}/properties/{property}/ideaActivities/{idea_activity} | [optional] 
**topics** | **[String]** | The Topic IDs for this entry. If empty, ideas should be set. | [optional] 
**type** | **String** | The type of activity performed. | [optional] 
**uri** | **String** | The uri the activity relates to. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `POST_DRAFTED` (value: `"POST_DRAFTED"`)

* `POST_PUBLISHED` (value: `"POST_PUBLISHED"`)

* `POST_DELETED` (value: `"POST_DELETED"`)

* `POST_UNPUBLISHED` (value: `"POST_UNPUBLISHED"`)




