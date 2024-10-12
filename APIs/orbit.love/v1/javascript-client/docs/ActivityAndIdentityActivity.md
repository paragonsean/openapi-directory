# OrbitApi.ActivityAndIdentityActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityType** | **String** |  | 
**activityTypeKey** | **String** | The key for a custom activity type for the workspace. Will create a new activity type if it does not exist. | [optional] 
**description** | **String** | A description of the activity; displayed in the timeline | [optional] 
**key** | **String** | Supply a key that must be unique or leave blank to have one generated. | [optional] 
**link** | **String** | A URL for the activity; displayed in the timeline | [optional] 
**linkText** | **String** | The text for the timeline link | [optional] 
**occurredAt** | **String** | The date and time at which the content was published; defaults to now | [optional] 
**properties** | **Object** | Key-value pairs to provide contextual metadata about an activity. | [optional] 
**title** | **String** | A title for the activity; displayed in the timeline | 
**weight** | **String** | A custom weight to be used in filters and reports; defaults to 1. | [optional] 
**member** | [**Member**](Member.md) |  | [optional] 
**url** | **String** | The url representing the post | 



## Enum: ActivityTypeEnum


* `content` (value: `"content"`)




