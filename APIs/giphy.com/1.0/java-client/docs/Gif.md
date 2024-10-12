

# Gif


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bitlyUrl** | **String** | The unique bit.ly URL for this GIF |  [optional] |
|**contentUrl** | **String** | Currently unused |  [optional] |
|**createDatetime** | **OffsetDateTime** | The date this GIF was added to the GIPHY database. |  [optional] |
|**embdedUrl** | **String** | A URL used for embedding this GIF |  [optional] |
|**featuredTags** | **List&lt;String&gt;** | An array of featured tags for this GIF (Note: Not available when using the Public Beta Key)  |  [optional] |
|**id** | **String** | This GIF&#39;s unique ID |  [optional] |
|**images** | [**GifImages**](GifImages.md) |  |  [optional] |
|**importDatetime** | **OffsetDateTime** | The creation or upload date from this GIF&#39;s source. |  [optional] |
|**rating** | **String** | The MPAA-style rating for this content. Examples include Y, G, PG, PG-13 and R |  [optional] |
|**slug** | **String** | The unique slug used in this GIF&#39;s URL |  [optional] |
|**source** | **String** | The page on which this GIF was found |  [optional] |
|**sourcePostUrl** | **String** | The URL of the webpage on which this GIF was found. |  [optional] |
|**sourceTld** | **String** | The top level domain of the source URL. |  [optional] |
|**tags** | **List&lt;String&gt;** | An array of tags for this GIF (Note: Not available when using the Public Beta Key)  |  [optional] |
|**trendingDatetime** | **OffsetDateTime** | The date on which this gif was marked trending, if applicable. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the gif. By default, this is almost always gif |  [optional] |
|**updateDatetime** | **OffsetDateTime** | The date on which this GIF was last updated. |  [optional] |
|**url** | **String** | The unique URL for this GIF |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |
|**username** | **String** | The username this GIF is attached to, if applicable |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GIF | &quot;gif&quot; |



