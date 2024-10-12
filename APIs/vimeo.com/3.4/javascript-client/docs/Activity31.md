# Vimeo.Activity31

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**Category**](Category.md) | The category that this event occurred for. This will be preset for only \&quot;category\&quot; activity types. | [optional] 
**channel** | [**Channel**](Channel.md) | The channel that this event occurred for. This will be present for only \&quot;channel\&quot; activity types. | [optional] 
**clip** | [**Video**](Video.md) | Video associated with ths activity. | 
**group** | [**Group**](Group.md) | The group that this event occurred for. This will be present for only \&quot;group\&quot; activity types. | [optional] 
**metadata** | [**Activity31Metadata**](Activity31Metadata.md) |  | 
**tag** | [**Tag**](Tag.md) | The tag that this event occurred for. This will be present for only \&quot;tag\&quot; activity types. | [optional] 
**time** | **String** | Time that the event occurred. | 
**type** | **String** | Activity type | 
**user** | [**User**](User.md) | The user that this event occurred for. This will be present for \&quot;like\&quot;, \&quot;appearance\&quot;, and \&quot;share\&quot; activity types. | [optional] 



## Enum: TypeEnum


* `appearance` (value: `"appearance"`)

* `category` (value: `"category"`)

* `channel` (value: `"channel"`)

* `facebook_feed` (value: `"facebook_feed"`)

* `group` (value: `"group"`)

* `like` (value: `"like"`)

* `ondemand` (value: `"ondemand"`)

* `share` (value: `"share"`)

* `tag` (value: `"tag"`)

* `twitter_timeline` (value: `"twitter_timeline"`)

* `upload` (value: `"upload"`)




