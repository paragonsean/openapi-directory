

# Blog


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customMetaData** | **String** | The JSON custom meta-data for the Blog. |  [optional] |
|**description** | **String** | The description of this blog. This is displayed underneath the title. |  [optional] |
|**id** | **String** | The identifier for this resource. |  [optional] |
|**kind** | **String** | The kind of this entry. Always blogger#blog. |  [optional] |
|**locale** | [**BlogLocale**](BlogLocale.md) |  |  [optional] |
|**name** | **String** | The name of this blog. This is displayed as the title. |  [optional] |
|**pages** | [**BlogPages**](BlogPages.md) |  |  [optional] |
|**posts** | [**BlogPosts**](BlogPosts.md) |  |  [optional] |
|**published** | **String** | RFC 3339 date-time when this blog was published. |  [optional] |
|**selfLink** | **String** | The API REST URL to fetch this resource from. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the blog. |  [optional] |
|**updated** | **String** | RFC 3339 date-time when this blog was last updated. |  [optional] |
|**url** | **String** | The URL where this blog is published. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| LIVE | &quot;LIVE&quot; |
| DELETED | &quot;DELETED&quot; |



