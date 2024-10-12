# BloggerApi.Post

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**PostAuthor**](PostAuthor.md) |  | [optional] 
**blog** | [**PostBlog**](PostBlog.md) |  | [optional] 
**content** | **String** | The content of the Post. May contain HTML markup. | [optional] 
**customMetaData** | **String** | The JSON meta-data for the Post. | [optional] 
**etag** | **String** | Etag of the resource. | [optional] 
**id** | **String** | The identifier of this Post. | [optional] 
**images** | [**[PostImagesInner]**](PostImagesInner.md) | Display image for the Post. | [optional] 
**kind** | **String** | The kind of this entity. Always blogger#post. | [optional] 
**labels** | **[String]** | The list of labels this Post was tagged with. | [optional] 
**location** | [**PostLocation**](PostLocation.md) |  | [optional] 
**published** | **String** | RFC 3339 date-time when this Post was published. | [optional] 
**readerComments** | **String** | Comment control and display setting for readers of this post. | [optional] 
**replies** | [**PostReplies**](PostReplies.md) |  | [optional] 
**selfLink** | **String** | The API REST URL to fetch this resource from. | [optional] 
**status** | **String** | Status of the post. Only set for admin-level requests. | [optional] 
**title** | **String** | The title of the Post. | [optional] 
**titleLink** | **String** | The title link URL, similar to atom&#39;s related link. | [optional] 
**trashed** | **String** | RFC 3339 date-time when this Post was last trashed. | [optional] 
**updated** | **String** | RFC 3339 date-time when this Post was last updated. | [optional] 
**url** | **String** | The URL where this Post is displayed. | [optional] 



## Enum: ReaderCommentsEnum


* `ALLOW` (value: `"ALLOW"`)

* `DONT_ALLOW_SHOW_EXISTING` (value: `"DONT_ALLOW_SHOW_EXISTING"`)

* `DONT_ALLOW_HIDE_EXISTING` (value: `"DONT_ALLOW_HIDE_EXISTING"`)





## Enum: StatusEnum


* `LIVE` (value: `"LIVE"`)

* `DRAFT` (value: `"DRAFT"`)

* `SCHEDULED` (value: `"SCHEDULED"`)

* `SOFT_TRASHED` (value: `"SOFT_TRASHED"`)




