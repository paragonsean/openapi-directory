# GiphyApi.Gif

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitlyUrl** | **String** | The unique bit.ly URL for this GIF | [optional] 
**contentUrl** | **String** | Currently unused | [optional] 
**createDatetime** | **Date** | The date this GIF was added to the GIPHY database. | [optional] 
**embdedUrl** | **String** | A URL used for embedding this GIF | [optional] 
**featuredTags** | **[String]** | An array of featured tags for this GIF (Note: Not available when using the Public Beta Key)  | [optional] 
**id** | **String** | This GIF&#39;s unique ID | [optional] 
**images** | [**GifImages**](GifImages.md) |  | [optional] 
**importDatetime** | **Date** | The creation or upload date from this GIF&#39;s source. | [optional] 
**rating** | **String** | The MPAA-style rating for this content. Examples include Y, G, PG, PG-13 and R | [optional] 
**slug** | **String** | The unique slug used in this GIF&#39;s URL | [optional] 
**source** | **String** | The page on which this GIF was found | [optional] 
**sourcePostUrl** | **String** | The URL of the webpage on which this GIF was found. | [optional] 
**sourceTld** | **String** | The top level domain of the source URL. | [optional] 
**tags** | **[String]** | An array of tags for this GIF (Note: Not available when using the Public Beta Key)  | [optional] 
**trendingDatetime** | **Date** | The date on which this gif was marked trending, if applicable. | [optional] 
**type** | **String** | Type of the gif. By default, this is almost always gif | [optional] [default to &#39;gif&#39;]
**updateDatetime** | **Date** | The date on which this GIF was last updated. | [optional] 
**url** | **String** | The unique URL for this GIF | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**username** | **String** | The username this GIF is attached to, if applicable | [optional] 



## Enum: TypeEnum


* `gif` (value: `"gif"`)




