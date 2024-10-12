# MediaApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesMediaFeaturedJsonGet**](MediaApi.md#resourcesMediaFeaturedJsonGet) | **GET** /resources/media/featured.json | Get the list of featured content in the syndication system |
| [**resourcesMediaIdContentGet**](MediaApi.md#resourcesMediaIdContentGet) | **GET** /resources/media/{id}/content | Get content for MediaItem |
| [**resourcesMediaIdEmbedJsonGet**](MediaApi.md#resourcesMediaIdEmbedJsonGet) | **GET** /resources/media/{id}/embed.json | Get embed code for MediaItem |
| [**resourcesMediaIdJsonGet**](MediaApi.md#resourcesMediaIdJsonGet) | **GET** /resources/media/{id}.json | Get MediaItem by ID |
| [**resourcesMediaIdPreviewJpgGet**](MediaApi.md#resourcesMediaIdPreviewJpgGet) | **GET** /resources/media/{id}/preview.jpg | Get Tag by ID |
| [**resourcesMediaIdRelatedMediaFormatGet**](MediaApi.md#resourcesMediaIdRelatedMediaFormatGet) | **GET** /resources/media/{id}/relatedMedia.{format} | Get related MediaItems by ID |
| [**resourcesMediaIdSyndicateFormatGet**](MediaApi.md#resourcesMediaIdSyndicateFormatGet) | **GET** /resources/media/{id}/syndicate.{format} | Get syndicated content for MediaItem |
| [**resourcesMediaIdThumbnailJpgGet**](MediaApi.md#resourcesMediaIdThumbnailJpgGet) | **GET** /resources/media/{id}/thumbnail.jpg | Get JPG thumbnail for MediaItem |
| [**resourcesMediaIdYoutubeMetaDataJsonGet**](MediaApi.md#resourcesMediaIdYoutubeMetaDataJsonGet) | **GET** /resources/media/{id}/youtubeMetaData.json | Get Youtube metadata for MediaItem |
| [**resourcesMediaJsonGet**](MediaApi.md#resourcesMediaJsonGet) | **GET** /resources/media.json | Get MediaItems |
| [**resourcesMediaMostPopularMediaFormatGet**](MediaApi.md#resourcesMediaMostPopularMediaFormatGet) | **GET** /resources/media/mostPopularMedia.{format} | Get MediaItems by popularity |
| [**resourcesMediaSearchResultsJsonGet**](MediaApi.md#resourcesMediaSearchResultsJsonGet) | **GET** /resources/media/searchResults.json | Get MediaItems by search query |


<a id="resourcesMediaFeaturedJsonGet"></a>
# **resourcesMediaFeaturedJsonGet**
> List&lt;MediaItem&gt; resourcesMediaFeaturedJsonGet(sort, max, offset)

Get the list of featured content in the syndication system

Get the list of featured content in the syndication system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | Return records starting at the offset index.
    try {
      List<MediaItem> result = apiInstance.resourcesMediaFeaturedJsonGet(sort, max, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaFeaturedJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| Return records starting at the offset index. | [optional] |

### Return type

[**List&lt;MediaItem&gt;**](MediaItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get the list of featured content in the syndication system |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdContentGet"></a>
# **resourcesMediaIdContentGet**
> String resourcesMediaIdContentGet(id, calledByBuild)

Get content for MediaItem

The actual media content (html, image, etc...)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the media to show content for.
    Boolean calledByBuild = true; // Boolean | The method that called this method
    try {
      String result = apiInstance.resourcesMediaIdContentGet(id, calledByBuild);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdContentGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the media to show content for. | |
| **calledByBuild** | **Boolean**| The method that called this method | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the raw content (html, image, etc...) for the MediaItem identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdEmbedJsonGet"></a>
# **resourcesMediaIdEmbedJsonGet**
> String resourcesMediaIdEmbedJsonGet(id, flavor, width, height, iframeName, excludeJquery, excludeDiv, divId, displayMethod)

Get embed code for MediaItem

Get the javascript or iframe embed code for this item (to embed it on a web page).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the media to get embed code for.
    String flavor = "flavor_example"; // String | Currently supports 'iframe', defaults to 'javascript'.
    Integer width = 56; // Integer | The width of the generated iframe.
    Integer height = 56; // Integer | The height of the generated iframe.
    String iframeName = "iframeName_example"; // String | The name of the iframe element
    Boolean excludeJquery = false; // Boolean | Should a reference to the JQuery Library be omitted?
    Boolean excludeDiv = false; // Boolean | Should the div to insert content into be omitted?
    String divId = "divId_example"; // String | Should the div to insert content into have a specific name?
    String displayMethod = "displayMethod_example"; // String | Method used to render an html request. Accepts one: [mv, list, feed]
    try {
      String result = apiInstance.resourcesMediaIdEmbedJsonGet(id, flavor, width, height, iframeName, excludeJquery, excludeDiv, divId, displayMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdEmbedJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the media to get embed code for. | |
| **flavor** | **String**| Currently supports &#39;iframe&#39;, defaults to &#39;javascript&#39;. | [optional] |
| **width** | **Integer**| The width of the generated iframe. | [optional] |
| **height** | **Integer**| The height of the generated iframe. | [optional] |
| **iframeName** | **String**| The name of the iframe element | [optional] |
| **excludeJquery** | **Boolean**| Should a reference to the JQuery Library be omitted? | [optional] [default to false] |
| **excludeDiv** | **Boolean**| Should the div to insert content into be omitted? | [optional] [default to false] |
| **divId** | **String**| Should the div to insert content into have a specific name? | [optional] |
| **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the javascript or iframe embed code for the MediaItem identified by &#39;id&#39;. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdJsonGet"></a>
# **resourcesMediaIdJsonGet**
> List&lt;MediaItemWrapped&gt; resourcesMediaIdJsonGet(id)

Get MediaItem by ID

Information about a specific media item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the record to look up
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesMediaIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the record to look up | |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the MediaItem identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdPreviewJpgGet"></a>
# **resourcesMediaIdPreviewJpgGet**
> Object resourcesMediaIdPreviewJpgGet(id)

Get Tag by ID

Get the jpg preview of the content item where applicable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the media to get a preview for.
    try {
      Object result = apiInstance.resourcesMediaIdPreviewJpgGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdPreviewJpgGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the media to get a preview for. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the JPG preview, where applicable, for the MediaItem identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdRelatedMediaFormatGet"></a>
# **resourcesMediaIdRelatedMediaFormatGet**
> List&lt;MediaItemWrapped&gt; resourcesMediaIdRelatedMediaFormatGet(id, format, max, offset, sort)

Get related MediaItems by ID

Get the media related to the current media item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the media item to get related media for
    String format = "format_example"; // String | Automatically added
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | Return records starting at the offset index.
    String sort = "sort_example"; // String | The name of the property to which sorting will be applied
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesMediaIdRelatedMediaFormatGet(id, format, max, offset, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdRelatedMediaFormatGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the media item to get related media for | |
| **format** | **String**| Automatically added | |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| Return records starting at the offset index. | [optional] |
| **sort** | **String**| The name of the property to which sorting will be applied | [optional] |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of MediaItems related to the MediaItem identified by the &#39;id&#39;. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdSyndicateFormatGet"></a>
# **resourcesMediaIdSyndicateFormatGet**
> SyndicateMarshallerWrapped resourcesMediaIdSyndicateFormatGet(id, format, cssClass, stripStyles, stripScripts, stripImages, stripBreaks, stripClasses, fontSize, imageFloat, imageMargin, autoplay, rel)

Get syndicated content for MediaItem

Get syndicated content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the media to show embed code for.
    String format = "format_example"; // String | Automatically added
    String cssClass = "syndicate"; // String | The css class to target for extraction.
    Boolean stripStyles = false; // Boolean | Remove in-line styles from content.
    Boolean stripScripts = false; // Boolean | Remove script tags from content.
    Boolean stripImages = false; // Boolean | Remove image tags from content.
    Boolean stripBreaks = false; // Boolean | Remove break tags from content.
    Boolean stripClasses = false; // Boolean | Remove class attributes from content (except 'syndicate').
    Integer fontSize = 56; // Integer | Set font size (in points) of p, div, and span tags.
    String imageFloat = "imageFloat_example"; // String | Accepts valid CSS float options, such as 'left' or 'right'. Will inject a style into the content before rendering.
    String imageMargin = "imageMargin_example"; // String | Accepts 4 CSV values representing pixel sizes of margin similar to CSS. Default format is 'north,east,south,west' - for example '0,10,10,0' would put a 10 pixel margin on the right and bottom sides of an image. Will inject a style into the content before rendering.
    Boolean autoplay = true; // Boolean | If content is a video, the embeded video will auto play when loaded.
    Boolean rel = false; // Boolean | If content is a video, related items will be shown at the end of playback.
    try {
      SyndicateMarshallerWrapped result = apiInstance.resourcesMediaIdSyndicateFormatGet(id, format, cssClass, stripStyles, stripScripts, stripImages, stripBreaks, stripClasses, fontSize, imageFloat, imageMargin, autoplay, rel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdSyndicateFormatGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the media to show embed code for. | |
| **format** | **String**| Automatically added | |
| **cssClass** | **String**| The css class to target for extraction. | [optional] [default to syndicate] |
| **stripStyles** | **Boolean**| Remove in-line styles from content. | [optional] [default to false] |
| **stripScripts** | **Boolean**| Remove script tags from content. | [optional] [default to false] |
| **stripImages** | **Boolean**| Remove image tags from content. | [optional] [default to false] |
| **stripBreaks** | **Boolean**| Remove break tags from content. | [optional] [default to false] |
| **stripClasses** | **Boolean**| Remove class attributes from content (except &#39;syndicate&#39;). | [optional] [default to false] |
| **fontSize** | **Integer**| Set font size (in points) of p, div, and span tags. | [optional] |
| **imageFloat** | **String**| Accepts valid CSS float options, such as &#39;left&#39; or &#39;right&#39;. Will inject a style into the content before rendering. | [optional] |
| **imageMargin** | **String**| Accepts 4 CSV values representing pixel sizes of margin similar to CSS. Default format is &#39;north,east,south,west&#39; - for example &#39;0,10,10,0&#39; would put a 10 pixel margin on the right and bottom sides of an image. Will inject a style into the content before rendering. | [optional] |
| **autoplay** | **Boolean**| If content is a video, the embeded video will auto play when loaded. | [optional] [default to true] |
| **rel** | **Boolean**| If content is a video, related items will be shown at the end of playback. | [optional] [default to false] |

### Return type

[**SyndicateMarshallerWrapped**](SyndicateMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the syndicated content for a given MediaItem in the specified &#39;format&#39; (HTML or JSON). |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdThumbnailJpgGet"></a>
# **resourcesMediaIdThumbnailJpgGet**
> Object resourcesMediaIdThumbnailJpgGet(id)

Get JPG thumbnail for MediaItem

Get the jpg thumbnail of the content item where applicable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the media to get a thumbnail for.
    try {
      Object result = apiInstance.resourcesMediaIdThumbnailJpgGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdThumbnailJpgGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the media to get a thumbnail for. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the JPG thumbnail, where applicable, for the MediaItem identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaIdYoutubeMetaDataJsonGet"></a>
# **resourcesMediaIdYoutubeMetaDataJsonGet**
> ResourcesMediaIdYoutubeMetaDataJsonGet200Response resourcesMediaIdYoutubeMetaDataJsonGet(id)

Get Youtube metadata for MediaItem

Youtube meta-data for a video item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Long id = 56L; // Long | The id of the video to show meta data for.
    try {
      ResourcesMediaIdYoutubeMetaDataJsonGet200Response result = apiInstance.resourcesMediaIdYoutubeMetaDataJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaIdYoutubeMetaDataJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Long**| The id of the video to show meta data for. | |

### Return type

[**ResourcesMediaIdYoutubeMetaDataJsonGet200Response**](ResourcesMediaIdYoutubeMetaDataJsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the Youtube metadata, where applicable, for the MediaItem identified by the &#39;id&#39;. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaJsonGet"></a>
# **resourcesMediaJsonGet**
> List&lt;MediaItemWrapped&gt; resourcesMediaJsonGet(max, offset, sort, order, mediaTypes, name, collectionId, nameContains, descriptionContains, sourceUrl, sourceUrlContains, customThumbnailUrl, customThumbnailUrlContains, dateContentAuthored, dateContentUpdated, dateContentPublished, dateContentReviewed, dateSyndicationCaptured, dateSyndicationUpdated, contentAuthoredSinceDate, contentAuthoredBeforeDate, contentAuthoredInRange, contentUpdatedSinceDate, contentUpdatedBeforeDate, contentUpdatedInRange, contentPublishedSinceDate, contentPublishedBeforeDate, contentPublishedInRange, contentReviewedSinceDate, contentReviewedBeforeDate, contentReviewedInRange, syndicationCapturedSinceDate, syndicationCapturedBeforeDate, syndicationCapturedInRange, syndicationUpdatedSinceDate, syndicationUpdatedBeforeDate, syndicationUpdatedInRange, syndicationVisibleSinceDate, syndicationVisibleBeforeDate, syndicationVisibleInRange, languageId, languageName, languageIsoCode, hash, hashContains, sourceId, sourceName, sourceNameContains, sourceAcronym, sourceAcronymContains, tagIds, restrictToSet, createdBy)

Get MediaItems

Media Items Listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | The offset of the records set to return for pagination.
    String sort = "sort_example"; // String | * Set of fields to sort the records by.
    String order = "order_example"; // String | * The ascending or descending order.
    String mediaTypes = "mediaTypes_example"; // String | Find all media items belonging to the specified media type[s].
    String name = "name_example"; // String | Find all media items containing the provided name, case insensitive.
    Integer collectionId = 56; // Integer | Restrict filtering to media items in a specific collection.
    String nameContains = "nameContains_example"; // String | Find all media items containing the partial name, case insensitive.
    String descriptionContains = "descriptionContains_example"; // String | Find all media items containing the provided partial description, case insensitive.
    String sourceUrl = "sourceUrl_example"; // String | Find all media items which have the provided sourceUrl, case insensitive.
    String sourceUrlContains = "sourceUrlContains_example"; // String | Find all media items which contain the provided partial sourceUrl, case insensitive.
    String customThumbnailUrl = "customThumbnailUrl_example"; // String | Find all media items which have the provided customThumbnailUrl, case insensitive.
    String customThumbnailUrlContains = "customThumbnailUrlContains_example"; // String | Find all media items which contain the provided partial customThumbnailUrl, case insensitive.
    LocalDate dateContentAuthored = LocalDate.now(); // LocalDate | Find all media items authored on the provided day (RFC 3339, time ignored).
    LocalDate dateContentUpdated = LocalDate.now(); // LocalDate | Find all media items updated on the provided day (RFC 3339, time ignored).
    LocalDate dateContentPublished = LocalDate.now(); // LocalDate | Find all media items published on the provided day (RFC 3339, time ignored).
    LocalDate dateContentReviewed = LocalDate.now(); // LocalDate | Find all media items reviewed on the provided day (RFC 3339, time ignored).
    LocalDate dateSyndicationCaptured = LocalDate.now(); // LocalDate | Find all media items syndicated on the provided day (RFC 3339, time ignored).
    LocalDate dateSyndicationUpdated = LocalDate.now(); // LocalDate | Find all media items updated through the syndication system on the provided day, (RFC 3339, time ignored).
    LocalDate contentAuthoredSinceDate = LocalDate.now(); // LocalDate | Find all media items authored since the provided day (RFC 3339, time ignored).
    LocalDate contentAuthoredBeforeDate = LocalDate.now(); // LocalDate | Find all media items authored before the provided day (RFC 3339, time ignored).
    String contentAuthoredInRange = "contentAuthoredInRange_example"; // String | Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored).
    LocalDate contentUpdatedSinceDate = LocalDate.now(); // LocalDate | Find all media items updated since the provided day (RFC 3339, time ignored).
    LocalDate contentUpdatedBeforeDate = LocalDate.now(); // LocalDate | Find all media items updated before the provided day (RFC 3339, time ignored).
    String contentUpdatedInRange = "contentUpdatedInRange_example"; // String | Find all media items updated between the provided start and end days (RFC 3339, comma separated, time ignored).
    LocalDate contentPublishedSinceDate = LocalDate.now(); // LocalDate | Find all media items updated since the provided day (RFC 3339, time ignored).
    LocalDate contentPublishedBeforeDate = LocalDate.now(); // LocalDate | Find all media items published before the provided day (RFC 3339, time ignored).
    String contentPublishedInRange = "contentPublishedInRange_example"; // String | Find all media items published between the provided start and end days (RFC 3339, comma separated, time ignored).
    LocalDate contentReviewedSinceDate = LocalDate.now(); // LocalDate | Find all media items reviewed since the provided day (RFC 3339, time ignored).
    LocalDate contentReviewedBeforeDate = LocalDate.now(); // LocalDate | Find all media items reviewed before the provided day (RFC 3339, time ignored).
    String contentReviewedInRange = "contentReviewedInRange_example"; // String | Find all media items reviewed between the provided start and end days (RFC 3339, comma separated, time ignored).
    LocalDate syndicationCapturedSinceDate = LocalDate.now(); // LocalDate | Find all media items authored since the provided day (RFC 3339, time ignored).
    LocalDate syndicationCapturedBeforeDate = LocalDate.now(); // LocalDate | Find all media items authored before the provided day (RFC 3339, time ignored).
    String syndicationCapturedInRange = "syndicationCapturedInRange_example"; // String | Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored).
    LocalDate syndicationUpdatedSinceDate = LocalDate.now(); // LocalDate | Find all media items updated since the provided day, (RFC 3339, time ignored).
    LocalDate syndicationUpdatedBeforeDate = LocalDate.now(); // LocalDate | Find all media items updated before the provided day, (RFC 3339, time ignored).
    String syndicationUpdatedInRange = "syndicationUpdatedInRange_example"; // String | Find all media items updated between the provided start and end days, (RFC 3339, comma separated, time ignored).
    LocalDate syndicationVisibleSinceDate = LocalDate.now(); // LocalDate | Find all media items visible since the provided day, (RFC 3339, time ignored).
    LocalDate syndicationVisibleBeforeDate = LocalDate.now(); // LocalDate | Find all media items visible before the provided day, (RFC 3339, time ignored).
    LocalDate syndicationVisibleInRange = LocalDate.now(); // LocalDate | Find all media items visible between the provided start and end days, (RFC 3339, comma separated, time ignored).
    Long languageId = 56L; // Long | Find all media items written in the language specified by Id.
    String languageName = "languageName_example"; // String | Find all media items written in the language specified by name, case insensitive.
    String languageIsoCode = "languageIsoCode_example"; // String | Find all media items written in the language specified by 639-2 isoCode , case insensitive.
    String hash = "hash_example"; // String | Find all media items which match the provided hash, case insensitive.
    String hashContains = "hashContains_example"; // String | Find all media items which match the provided partial hash, case insensitive.
    Long sourceId = 56L; // Long | Find all media items that belong to the source specified by Id.
    String sourceName = "sourceName_example"; // String | Find all media items that belong to the source specified by name, case insensitive.
    String sourceNameContains = "sourceNameContains_example"; // String | Find all media items that belong to the source specified by partial name, case insensitive.
    String sourceAcronym = "sourceAcronym_example"; // String | Find all media items that belong to the source specified by acronym, case insensitive.
    String sourceAcronymContains = "sourceAcronymContains_example"; // String | Find all media items that belong to the source specified by partial acronym, case insensitive.
    String tagIds = "tagIds_example"; // String | Find only media items tagged with the specified tag Ids.
    String restrictToSet = "restrictToSet_example"; // String | Find only media from within the supplied list of Ids.
    String createdBy = "createdBy_example"; // String | Find all media items containing the createdBy value.
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesMediaJsonGet(max, offset, sort, order, mediaTypes, name, collectionId, nameContains, descriptionContains, sourceUrl, sourceUrlContains, customThumbnailUrl, customThumbnailUrlContains, dateContentAuthored, dateContentUpdated, dateContentPublished, dateContentReviewed, dateSyndicationCaptured, dateSyndicationUpdated, contentAuthoredSinceDate, contentAuthoredBeforeDate, contentAuthoredInRange, contentUpdatedSinceDate, contentUpdatedBeforeDate, contentUpdatedInRange, contentPublishedSinceDate, contentPublishedBeforeDate, contentPublishedInRange, contentReviewedSinceDate, contentReviewedBeforeDate, contentReviewedInRange, syndicationCapturedSinceDate, syndicationCapturedBeforeDate, syndicationCapturedInRange, syndicationUpdatedSinceDate, syndicationUpdatedBeforeDate, syndicationUpdatedInRange, syndicationVisibleSinceDate, syndicationVisibleBeforeDate, syndicationVisibleInRange, languageId, languageName, languageIsoCode, hash, hashContains, sourceId, sourceName, sourceNameContains, sourceAcronym, sourceAcronymContains, tagIds, restrictToSet, createdBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| The offset of the records set to return for pagination. | [optional] |
| **sort** | **String**| * Set of fields to sort the records by. | [optional] |
| **order** | **String**| * The ascending or descending order. | [optional] |
| **mediaTypes** | **String**| Find all media items belonging to the specified media type[s]. | [optional] |
| **name** | **String**| Find all media items containing the provided name, case insensitive. | [optional] |
| **collectionId** | **Integer**| Restrict filtering to media items in a specific collection. | [optional] |
| **nameContains** | **String**| Find all media items containing the partial name, case insensitive. | [optional] |
| **descriptionContains** | **String**| Find all media items containing the provided partial description, case insensitive. | [optional] |
| **sourceUrl** | **String**| Find all media items which have the provided sourceUrl, case insensitive. | [optional] |
| **sourceUrlContains** | **String**| Find all media items which contain the provided partial sourceUrl, case insensitive. | [optional] |
| **customThumbnailUrl** | **String**| Find all media items which have the provided customThumbnailUrl, case insensitive. | [optional] |
| **customThumbnailUrlContains** | **String**| Find all media items which contain the provided partial customThumbnailUrl, case insensitive. | [optional] |
| **dateContentAuthored** | **LocalDate**| Find all media items authored on the provided day (RFC 3339, time ignored). | [optional] |
| **dateContentUpdated** | **LocalDate**| Find all media items updated on the provided day (RFC 3339, time ignored). | [optional] |
| **dateContentPublished** | **LocalDate**| Find all media items published on the provided day (RFC 3339, time ignored). | [optional] |
| **dateContentReviewed** | **LocalDate**| Find all media items reviewed on the provided day (RFC 3339, time ignored). | [optional] |
| **dateSyndicationCaptured** | **LocalDate**| Find all media items syndicated on the provided day (RFC 3339, time ignored). | [optional] |
| **dateSyndicationUpdated** | **LocalDate**| Find all media items updated through the syndication system on the provided day, (RFC 3339, time ignored). | [optional] |
| **contentAuthoredSinceDate** | **LocalDate**| Find all media items authored since the provided day (RFC 3339, time ignored). | [optional] |
| **contentAuthoredBeforeDate** | **LocalDate**| Find all media items authored before the provided day (RFC 3339, time ignored). | [optional] |
| **contentAuthoredInRange** | **String**| Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] |
| **contentUpdatedSinceDate** | **LocalDate**| Find all media items updated since the provided day (RFC 3339, time ignored). | [optional] |
| **contentUpdatedBeforeDate** | **LocalDate**| Find all media items updated before the provided day (RFC 3339, time ignored). | [optional] |
| **contentUpdatedInRange** | **String**| Find all media items updated between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] |
| **contentPublishedSinceDate** | **LocalDate**| Find all media items updated since the provided day (RFC 3339, time ignored). | [optional] |
| **contentPublishedBeforeDate** | **LocalDate**| Find all media items published before the provided day (RFC 3339, time ignored). | [optional] |
| **contentPublishedInRange** | **String**| Find all media items published between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] |
| **contentReviewedSinceDate** | **LocalDate**| Find all media items reviewed since the provided day (RFC 3339, time ignored). | [optional] |
| **contentReviewedBeforeDate** | **LocalDate**| Find all media items reviewed before the provided day (RFC 3339, time ignored). | [optional] |
| **contentReviewedInRange** | **String**| Find all media items reviewed between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] |
| **syndicationCapturedSinceDate** | **LocalDate**| Find all media items authored since the provided day (RFC 3339, time ignored). | [optional] |
| **syndicationCapturedBeforeDate** | **LocalDate**| Find all media items authored before the provided day (RFC 3339, time ignored). | [optional] |
| **syndicationCapturedInRange** | **String**| Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] |
| **syndicationUpdatedSinceDate** | **LocalDate**| Find all media items updated since the provided day, (RFC 3339, time ignored). | [optional] |
| **syndicationUpdatedBeforeDate** | **LocalDate**| Find all media items updated before the provided day, (RFC 3339, time ignored). | [optional] |
| **syndicationUpdatedInRange** | **String**| Find all media items updated between the provided start and end days, (RFC 3339, comma separated, time ignored). | [optional] |
| **syndicationVisibleSinceDate** | **LocalDate**| Find all media items visible since the provided day, (RFC 3339, time ignored). | [optional] |
| **syndicationVisibleBeforeDate** | **LocalDate**| Find all media items visible before the provided day, (RFC 3339, time ignored). | [optional] |
| **syndicationVisibleInRange** | **LocalDate**| Find all media items visible between the provided start and end days, (RFC 3339, comma separated, time ignored). | [optional] |
| **languageId** | **Long**| Find all media items written in the language specified by Id. | [optional] |
| **languageName** | **String**| Find all media items written in the language specified by name, case insensitive. | [optional] |
| **languageIsoCode** | **String**| Find all media items written in the language specified by 639-2 isoCode , case insensitive. | [optional] |
| **hash** | **String**| Find all media items which match the provided hash, case insensitive. | [optional] |
| **hashContains** | **String**| Find all media items which match the provided partial hash, case insensitive. | [optional] |
| **sourceId** | **Long**| Find all media items that belong to the source specified by Id. | [optional] |
| **sourceName** | **String**| Find all media items that belong to the source specified by name, case insensitive. | [optional] |
| **sourceNameContains** | **String**| Find all media items that belong to the source specified by partial name, case insensitive. | [optional] |
| **sourceAcronym** | **String**| Find all media items that belong to the source specified by acronym, case insensitive. | [optional] |
| **sourceAcronymContains** | **String**| Find all media items that belong to the source specified by partial acronym, case insensitive. | [optional] |
| **tagIds** | **String**| Find only media items tagged with the specified tag Ids. | [optional] |
| **restrictToSet** | **String**| Find only media from within the supplied list of Ids. | [optional] |
| **createdBy** | **String**| Find all media items containing the createdBy value. | [optional] |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of MediaItems matching the specified query parameters. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaMostPopularMediaFormatGet"></a>
# **resourcesMediaMostPopularMediaFormatGet**
> List&lt;MediaItemWrapped&gt; resourcesMediaMostPopularMediaFormatGet(format, max, offset)

Get MediaItems by popularity

Get the media with the highest ratings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    String format = "format_example"; // String | Automatically added
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | The offset of the records set to return for pagination.
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesMediaMostPopularMediaFormatGet(format, max, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaMostPopularMediaFormatGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **format** | **String**| Automatically added | |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| The offset of the records set to return for pagination. | [optional] |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of MediaItems with the highest ratings. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="resourcesMediaSearchResultsJsonGet"></a>
# **resourcesMediaSearchResultsJsonGet**
> List&lt;MediaItemWrapped&gt; resourcesMediaSearchResultsJsonGet(q, max, offset)

Get MediaItems by search query

Full search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaApi apiInstance = new MediaApi(defaultClient);
    String q = "q_example"; // String | The search query supplied by the user
    Integer max = 56; // Integer | The maximum number of records to return
    Integer offset = 56; // Integer | The offset of the records set to return for pagination.
    try {
      List<MediaItemWrapped> result = apiInstance.resourcesMediaSearchResultsJsonGet(q, max, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#resourcesMediaSearchResultsJsonGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q** | **String**| The search query supplied by the user | |
| **max** | **Integer**| The maximum number of records to return | [optional] |
| **offset** | **Integer**| The offset of the records set to return for pagination. | [optional] |

### Return type

[**List&lt;MediaItemWrapped&gt;**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of MediaItems matching the search query &#39;q&#39;.&lt;p&gt;Please enter keyword or URL in search query &#39;q&#39;. |  -  |
| **400** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

