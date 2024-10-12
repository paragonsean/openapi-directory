

# Page


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | [**PageAuthor**](PageAuthor.md) |  |  [optional] |
|**blog** | [**PageBlog**](PageBlog.md) |  |  [optional] |
|**content** | **String** | The body content of this Page, in HTML. |  [optional] |
|**etag** | **String** | Etag of the resource. |  [optional] |
|**id** | **String** | The identifier for this resource. |  [optional] |
|**kind** | **String** | The kind of this entity. Always blogger#page. |  [optional] |
|**published** | **String** | RFC 3339 date-time when this Page was published. |  [optional] |
|**selfLink** | **String** | The API REST URL to fetch this resource from. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the page for admin resources (either LIVE or DRAFT). |  [optional] |
|**title** | **String** | The title of this entity. This is the name displayed in the Admin user interface. |  [optional] |
|**trashed** | **String** | RFC 3339 date-time when this Page was trashed. |  [optional] |
|**updated** | **String** | RFC 3339 date-time when this Page was last updated. |  [optional] |
|**url** | **String** | The URL that this Page is displayed at. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;LIVE&quot; |
| DRAFT | &quot;DRAFT&quot; |
| SOFT_TRASHED | &quot;SOFT_TRASHED&quot; |



