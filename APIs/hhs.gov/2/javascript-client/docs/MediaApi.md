# HhsMediaServicesApi.MediaApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesMediaFeaturedJsonGet**](MediaApi.md#resourcesMediaFeaturedJsonGet) | **GET** /resources/media/featured.json | Get the list of featured content in the syndication system
[**resourcesMediaIdContentGet**](MediaApi.md#resourcesMediaIdContentGet) | **GET** /resources/media/{id}/content | Get content for MediaItem
[**resourcesMediaIdEmbedJsonGet**](MediaApi.md#resourcesMediaIdEmbedJsonGet) | **GET** /resources/media/{id}/embed.json | Get embed code for MediaItem
[**resourcesMediaIdJsonGet**](MediaApi.md#resourcesMediaIdJsonGet) | **GET** /resources/media/{id}.json | Get MediaItem by ID
[**resourcesMediaIdPreviewJpgGet**](MediaApi.md#resourcesMediaIdPreviewJpgGet) | **GET** /resources/media/{id}/preview.jpg | Get Tag by ID
[**resourcesMediaIdRelatedMediaFormatGet**](MediaApi.md#resourcesMediaIdRelatedMediaFormatGet) | **GET** /resources/media/{id}/relatedMedia.{format} | Get related MediaItems by ID
[**resourcesMediaIdSyndicateFormatGet**](MediaApi.md#resourcesMediaIdSyndicateFormatGet) | **GET** /resources/media/{id}/syndicate.{format} | Get syndicated content for MediaItem
[**resourcesMediaIdThumbnailJpgGet**](MediaApi.md#resourcesMediaIdThumbnailJpgGet) | **GET** /resources/media/{id}/thumbnail.jpg | Get JPG thumbnail for MediaItem
[**resourcesMediaIdYoutubeMetaDataJsonGet**](MediaApi.md#resourcesMediaIdYoutubeMetaDataJsonGet) | **GET** /resources/media/{id}/youtubeMetaData.json | Get Youtube metadata for MediaItem
[**resourcesMediaJsonGet**](MediaApi.md#resourcesMediaJsonGet) | **GET** /resources/media.json | Get MediaItems
[**resourcesMediaMostPopularMediaFormatGet**](MediaApi.md#resourcesMediaMostPopularMediaFormatGet) | **GET** /resources/media/mostPopularMedia.{format} | Get MediaItems by popularity
[**resourcesMediaSearchResultsJsonGet**](MediaApi.md#resourcesMediaSearchResultsJsonGet) | **GET** /resources/media/searchResults.json | Get MediaItems by search query



## resourcesMediaFeaturedJsonGet

> [MediaItem] resourcesMediaFeaturedJsonGet(opts)

Get the list of featured content in the syndication system

Get the list of featured content in the syndication system

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let opts = {
  'sort': "sort_example", // String | The name of the property to which sorting will be applied
  'max': 56, // Number | The maximum number of records to return
  'offset': 56 // Number | Return records starting at the offset index.
};
apiInstance.resourcesMediaFeaturedJsonGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **String**| The name of the property to which sorting will be applied | [optional] 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| Return records starting at the offset index. | [optional] 

### Return type

[**[MediaItem]**](MediaItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdContentGet

> String resourcesMediaIdContentGet(id, opts)

Get content for MediaItem

The actual media content (html, image, etc...)

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the media to show content for.
let opts = {
  'calledByBuild': true // Boolean | The method that called this method
};
apiInstance.resourcesMediaIdContentGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the media to show content for. | 
 **calledByBuild** | **Boolean**| The method that called this method | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdEmbedJsonGet

> String resourcesMediaIdEmbedJsonGet(id, opts)

Get embed code for MediaItem

Get the javascript or iframe embed code for this item (to embed it on a web page).

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the media to get embed code for.
let opts = {
  'flavor': "flavor_example", // String | Currently supports 'iframe', defaults to 'javascript'.
  'width': 56, // Number | The width of the generated iframe.
  'height': 56, // Number | The height of the generated iframe.
  'iframeName': "iframeName_example", // String | The name of the iframe element
  'excludeJquery': false, // Boolean | Should a reference to the JQuery Library be omitted?
  'excludeDiv': false, // Boolean | Should the div to insert content into be omitted?
  'divId': "divId_example", // String | Should the div to insert content into have a specific name?
  'displayMethod': "displayMethod_example" // String | Method used to render an html request. Accepts one: [mv, list, feed]
};
apiInstance.resourcesMediaIdEmbedJsonGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the media to get embed code for. | 
 **flavor** | **String**| Currently supports &#39;iframe&#39;, defaults to &#39;javascript&#39;. | [optional] 
 **width** | **Number**| The width of the generated iframe. | [optional] 
 **height** | **Number**| The height of the generated iframe. | [optional] 
 **iframeName** | **String**| The name of the iframe element | [optional] 
 **excludeJquery** | **Boolean**| Should a reference to the JQuery Library be omitted? | [optional] [default to false]
 **excludeDiv** | **Boolean**| Should the div to insert content into be omitted? | [optional] [default to false]
 **divId** | **String**| Should the div to insert content into have a specific name? | [optional] 
 **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdJsonGet

> [MediaItemWrapped] resourcesMediaIdJsonGet(id)

Get MediaItem by ID

Information about a specific media item

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the record to look up
apiInstance.resourcesMediaIdJsonGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the record to look up | 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdPreviewJpgGet

> Object resourcesMediaIdPreviewJpgGet(id)

Get Tag by ID

Get the jpg preview of the content item where applicable.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the media to get a preview for.
apiInstance.resourcesMediaIdPreviewJpgGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the media to get a preview for. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdRelatedMediaFormatGet

> [MediaItemWrapped] resourcesMediaIdRelatedMediaFormatGet(id, format, opts)

Get related MediaItems by ID

Get the media related to the current media item.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the media item to get related media for
let format = "format_example"; // String | Automatically added
let opts = {
  'max': 56, // Number | The maximum number of records to return
  'offset': 56, // Number | Return records starting at the offset index.
  'sort': "sort_example" // String | The name of the property to which sorting will be applied
};
apiInstance.resourcesMediaIdRelatedMediaFormatGet(id, format, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the media item to get related media for | 
 **format** | **String**| Automatically added | 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| Return records starting at the offset index. | [optional] 
 **sort** | **String**| The name of the property to which sorting will be applied | [optional] 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdSyndicateFormatGet

> SyndicateMarshallerWrapped resourcesMediaIdSyndicateFormatGet(id, format, opts)

Get syndicated content for MediaItem

Get syndicated content.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the media to show embed code for.
let format = "format_example"; // String | Automatically added
let opts = {
  'cssClass': "'syndicate'", // String | The css class to target for extraction.
  'stripStyles': false, // Boolean | Remove in-line styles from content.
  'stripScripts': false, // Boolean | Remove script tags from content.
  'stripImages': false, // Boolean | Remove image tags from content.
  'stripBreaks': false, // Boolean | Remove break tags from content.
  'stripClasses': false, // Boolean | Remove class attributes from content (except 'syndicate').
  'fontSize': 56, // Number | Set font size (in points) of p, div, and span tags.
  'imageFloat': "imageFloat_example", // String | Accepts valid CSS float options, such as 'left' or 'right'. Will inject a style into the content before rendering.
  'imageMargin': "imageMargin_example", // String | Accepts 4 CSV values representing pixel sizes of margin similar to CSS. Default format is 'north,east,south,west' - for example '0,10,10,0' would put a 10 pixel margin on the right and bottom sides of an image. Will inject a style into the content before rendering.
  'autoplay': true, // Boolean | If content is a video, the embeded video will auto play when loaded.
  'rel': false // Boolean | If content is a video, related items will be shown at the end of playback.
};
apiInstance.resourcesMediaIdSyndicateFormatGet(id, format, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the media to show embed code for. | 
 **format** | **String**| Automatically added | 
 **cssClass** | **String**| The css class to target for extraction. | [optional] [default to &#39;syndicate&#39;]
 **stripStyles** | **Boolean**| Remove in-line styles from content. | [optional] [default to false]
 **stripScripts** | **Boolean**| Remove script tags from content. | [optional] [default to false]
 **stripImages** | **Boolean**| Remove image tags from content. | [optional] [default to false]
 **stripBreaks** | **Boolean**| Remove break tags from content. | [optional] [default to false]
 **stripClasses** | **Boolean**| Remove class attributes from content (except &#39;syndicate&#39;). | [optional] [default to false]
 **fontSize** | **Number**| Set font size (in points) of p, div, and span tags. | [optional] 
 **imageFloat** | **String**| Accepts valid CSS float options, such as &#39;left&#39; or &#39;right&#39;. Will inject a style into the content before rendering. | [optional] 
 **imageMargin** | **String**| Accepts 4 CSV values representing pixel sizes of margin similar to CSS. Default format is &#39;north,east,south,west&#39; - for example &#39;0,10,10,0&#39; would put a 10 pixel margin on the right and bottom sides of an image. Will inject a style into the content before rendering. | [optional] 
 **autoplay** | **Boolean**| If content is a video, the embeded video will auto play when loaded. | [optional] [default to true]
 **rel** | **Boolean**| If content is a video, related items will be shown at the end of playback. | [optional] [default to false]

### Return type

[**SyndicateMarshallerWrapped**](SyndicateMarshallerWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdThumbnailJpgGet

> Object resourcesMediaIdThumbnailJpgGet(id)

Get JPG thumbnail for MediaItem

Get the jpg thumbnail of the content item where applicable.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the media to get a thumbnail for.
apiInstance.resourcesMediaIdThumbnailJpgGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the media to get a thumbnail for. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaIdYoutubeMetaDataJsonGet

> ResourcesMediaIdYoutubeMetaDataJsonGet200Response resourcesMediaIdYoutubeMetaDataJsonGet(id)

Get Youtube metadata for MediaItem

Youtube meta-data for a video item.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let id = 789; // Number | The id of the video to show meta data for.
apiInstance.resourcesMediaIdYoutubeMetaDataJsonGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| The id of the video to show meta data for. | 

### Return type

[**ResourcesMediaIdYoutubeMetaDataJsonGet200Response**](ResourcesMediaIdYoutubeMetaDataJsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaJsonGet

> [MediaItemWrapped] resourcesMediaJsonGet(opts)

Get MediaItems

Media Items Listings

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let opts = {
  'max': 56, // Number | The maximum number of records to return
  'offset': 56, // Number | The offset of the records set to return for pagination.
  'sort': "sort_example", // String | * Set of fields to sort the records by.
  'order': "order_example", // String | * The ascending or descending order.
  'mediaTypes': "mediaTypes_example", // String | Find all media items belonging to the specified media type[s].
  'name': "name_example", // String | Find all media items containing the provided name, case insensitive.
  'collectionId': 56, // Number | Restrict filtering to media items in a specific collection.
  'nameContains': "nameContains_example", // String | Find all media items containing the partial name, case insensitive.
  'descriptionContains': "descriptionContains_example", // String | Find all media items containing the provided partial description, case insensitive.
  'sourceUrl': "sourceUrl_example", // String | Find all media items which have the provided sourceUrl, case insensitive.
  'sourceUrlContains': "sourceUrlContains_example", // String | Find all media items which contain the provided partial sourceUrl, case insensitive.
  'customThumbnailUrl': "customThumbnailUrl_example", // String | Find all media items which have the provided customThumbnailUrl, case insensitive.
  'customThumbnailUrlContains': "customThumbnailUrlContains_example", // String | Find all media items which contain the provided partial customThumbnailUrl, case insensitive.
  'dateContentAuthored': new Date("2013-10-20"), // Date | Find all media items authored on the provided day (RFC 3339, time ignored).
  'dateContentUpdated': new Date("2013-10-20"), // Date | Find all media items updated on the provided day (RFC 3339, time ignored).
  'dateContentPublished': new Date("2013-10-20"), // Date | Find all media items published on the provided day (RFC 3339, time ignored).
  'dateContentReviewed': new Date("2013-10-20"), // Date | Find all media items reviewed on the provided day (RFC 3339, time ignored).
  'dateSyndicationCaptured': new Date("2013-10-20"), // Date | Find all media items syndicated on the provided day (RFC 3339, time ignored).
  'dateSyndicationUpdated': new Date("2013-10-20"), // Date | Find all media items updated through the syndication system on the provided day, (RFC 3339, time ignored).
  'contentAuthoredSinceDate': new Date("2013-10-20"), // Date | Find all media items authored since the provided day (RFC 3339, time ignored).
  'contentAuthoredBeforeDate': new Date("2013-10-20"), // Date | Find all media items authored before the provided day (RFC 3339, time ignored).
  'contentAuthoredInRange': "contentAuthoredInRange_example", // String | Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored).
  'contentUpdatedSinceDate': new Date("2013-10-20"), // Date | Find all media items updated since the provided day (RFC 3339, time ignored).
  'contentUpdatedBeforeDate': new Date("2013-10-20"), // Date | Find all media items updated before the provided day (RFC 3339, time ignored).
  'contentUpdatedInRange': "contentUpdatedInRange_example", // String | Find all media items updated between the provided start and end days (RFC 3339, comma separated, time ignored).
  'contentPublishedSinceDate': new Date("2013-10-20"), // Date | Find all media items updated since the provided day (RFC 3339, time ignored).
  'contentPublishedBeforeDate': new Date("2013-10-20"), // Date | Find all media items published before the provided day (RFC 3339, time ignored).
  'contentPublishedInRange': "contentPublishedInRange_example", // String | Find all media items published between the provided start and end days (RFC 3339, comma separated, time ignored).
  'contentReviewedSinceDate': new Date("2013-10-20"), // Date | Find all media items reviewed since the provided day (RFC 3339, time ignored).
  'contentReviewedBeforeDate': new Date("2013-10-20"), // Date | Find all media items reviewed before the provided day (RFC 3339, time ignored).
  'contentReviewedInRange': "contentReviewedInRange_example", // String | Find all media items reviewed between the provided start and end days (RFC 3339, comma separated, time ignored).
  'syndicationCapturedSinceDate': new Date("2013-10-20"), // Date | Find all media items authored since the provided day (RFC 3339, time ignored).
  'syndicationCapturedBeforeDate': new Date("2013-10-20"), // Date | Find all media items authored before the provided day (RFC 3339, time ignored).
  'syndicationCapturedInRange': "syndicationCapturedInRange_example", // String | Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored).
  'syndicationUpdatedSinceDate': new Date("2013-10-20"), // Date | Find all media items updated since the provided day, (RFC 3339, time ignored).
  'syndicationUpdatedBeforeDate': new Date("2013-10-20"), // Date | Find all media items updated before the provided day, (RFC 3339, time ignored).
  'syndicationUpdatedInRange': "syndicationUpdatedInRange_example", // String | Find all media items updated between the provided start and end days, (RFC 3339, comma separated, time ignored).
  'syndicationVisibleSinceDate': new Date("2013-10-20"), // Date | Find all media items visible since the provided day, (RFC 3339, time ignored).
  'syndicationVisibleBeforeDate': new Date("2013-10-20"), // Date | Find all media items visible before the provided day, (RFC 3339, time ignored).
  'syndicationVisibleInRange': new Date("2013-10-20"), // Date | Find all media items visible between the provided start and end days, (RFC 3339, comma separated, time ignored).
  'languageId': 789, // Number | Find all media items written in the language specified by Id.
  'languageName': "languageName_example", // String | Find all media items written in the language specified by name, case insensitive.
  'languageIsoCode': "languageIsoCode_example", // String | Find all media items written in the language specified by 639-2 isoCode , case insensitive.
  'hash': "hash_example", // String | Find all media items which match the provided hash, case insensitive.
  'hashContains': "hashContains_example", // String | Find all media items which match the provided partial hash, case insensitive.
  'sourceId': 789, // Number | Find all media items that belong to the source specified by Id.
  'sourceName': "sourceName_example", // String | Find all media items that belong to the source specified by name, case insensitive.
  'sourceNameContains': "sourceNameContains_example", // String | Find all media items that belong to the source specified by partial name, case insensitive.
  'sourceAcronym': "sourceAcronym_example", // String | Find all media items that belong to the source specified by acronym, case insensitive.
  'sourceAcronymContains': "sourceAcronymContains_example", // String | Find all media items that belong to the source specified by partial acronym, case insensitive.
  'tagIds': "tagIds_example", // String | Find only media items tagged with the specified tag Ids.
  'restrictToSet': "restrictToSet_example", // String | Find only media from within the supplied list of Ids.
  'createdBy': "createdBy_example" // String | Find all media items containing the createdBy value.
};
apiInstance.resourcesMediaJsonGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| The offset of the records set to return for pagination. | [optional] 
 **sort** | **String**| * Set of fields to sort the records by. | [optional] 
 **order** | **String**| * The ascending or descending order. | [optional] 
 **mediaTypes** | **String**| Find all media items belonging to the specified media type[s]. | [optional] 
 **name** | **String**| Find all media items containing the provided name, case insensitive. | [optional] 
 **collectionId** | **Number**| Restrict filtering to media items in a specific collection. | [optional] 
 **nameContains** | **String**| Find all media items containing the partial name, case insensitive. | [optional] 
 **descriptionContains** | **String**| Find all media items containing the provided partial description, case insensitive. | [optional] 
 **sourceUrl** | **String**| Find all media items which have the provided sourceUrl, case insensitive. | [optional] 
 **sourceUrlContains** | **String**| Find all media items which contain the provided partial sourceUrl, case insensitive. | [optional] 
 **customThumbnailUrl** | **String**| Find all media items which have the provided customThumbnailUrl, case insensitive. | [optional] 
 **customThumbnailUrlContains** | **String**| Find all media items which contain the provided partial customThumbnailUrl, case insensitive. | [optional] 
 **dateContentAuthored** | **Date**| Find all media items authored on the provided day (RFC 3339, time ignored). | [optional] 
 **dateContentUpdated** | **Date**| Find all media items updated on the provided day (RFC 3339, time ignored). | [optional] 
 **dateContentPublished** | **Date**| Find all media items published on the provided day (RFC 3339, time ignored). | [optional] 
 **dateContentReviewed** | **Date**| Find all media items reviewed on the provided day (RFC 3339, time ignored). | [optional] 
 **dateSyndicationCaptured** | **Date**| Find all media items syndicated on the provided day (RFC 3339, time ignored). | [optional] 
 **dateSyndicationUpdated** | **Date**| Find all media items updated through the syndication system on the provided day, (RFC 3339, time ignored). | [optional] 
 **contentAuthoredSinceDate** | **Date**| Find all media items authored since the provided day (RFC 3339, time ignored). | [optional] 
 **contentAuthoredBeforeDate** | **Date**| Find all media items authored before the provided day (RFC 3339, time ignored). | [optional] 
 **contentAuthoredInRange** | **String**| Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] 
 **contentUpdatedSinceDate** | **Date**| Find all media items updated since the provided day (RFC 3339, time ignored). | [optional] 
 **contentUpdatedBeforeDate** | **Date**| Find all media items updated before the provided day (RFC 3339, time ignored). | [optional] 
 **contentUpdatedInRange** | **String**| Find all media items updated between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] 
 **contentPublishedSinceDate** | **Date**| Find all media items updated since the provided day (RFC 3339, time ignored). | [optional] 
 **contentPublishedBeforeDate** | **Date**| Find all media items published before the provided day (RFC 3339, time ignored). | [optional] 
 **contentPublishedInRange** | **String**| Find all media items published between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] 
 **contentReviewedSinceDate** | **Date**| Find all media items reviewed since the provided day (RFC 3339, time ignored). | [optional] 
 **contentReviewedBeforeDate** | **Date**| Find all media items reviewed before the provided day (RFC 3339, time ignored). | [optional] 
 **contentReviewedInRange** | **String**| Find all media items reviewed between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] 
 **syndicationCapturedSinceDate** | **Date**| Find all media items authored since the provided day (RFC 3339, time ignored). | [optional] 
 **syndicationCapturedBeforeDate** | **Date**| Find all media items authored before the provided day (RFC 3339, time ignored). | [optional] 
 **syndicationCapturedInRange** | **String**| Find all media items authored between the provided start and end days (RFC 3339, comma separated, time ignored). | [optional] 
 **syndicationUpdatedSinceDate** | **Date**| Find all media items updated since the provided day, (RFC 3339, time ignored). | [optional] 
 **syndicationUpdatedBeforeDate** | **Date**| Find all media items updated before the provided day, (RFC 3339, time ignored). | [optional] 
 **syndicationUpdatedInRange** | **String**| Find all media items updated between the provided start and end days, (RFC 3339, comma separated, time ignored). | [optional] 
 **syndicationVisibleSinceDate** | **Date**| Find all media items visible since the provided day, (RFC 3339, time ignored). | [optional] 
 **syndicationVisibleBeforeDate** | **Date**| Find all media items visible before the provided day, (RFC 3339, time ignored). | [optional] 
 **syndicationVisibleInRange** | **Date**| Find all media items visible between the provided start and end days, (RFC 3339, comma separated, time ignored). | [optional] 
 **languageId** | **Number**| Find all media items written in the language specified by Id. | [optional] 
 **languageName** | **String**| Find all media items written in the language specified by name, case insensitive. | [optional] 
 **languageIsoCode** | **String**| Find all media items written in the language specified by 639-2 isoCode , case insensitive. | [optional] 
 **hash** | **String**| Find all media items which match the provided hash, case insensitive. | [optional] 
 **hashContains** | **String**| Find all media items which match the provided partial hash, case insensitive. | [optional] 
 **sourceId** | **Number**| Find all media items that belong to the source specified by Id. | [optional] 
 **sourceName** | **String**| Find all media items that belong to the source specified by name, case insensitive. | [optional] 
 **sourceNameContains** | **String**| Find all media items that belong to the source specified by partial name, case insensitive. | [optional] 
 **sourceAcronym** | **String**| Find all media items that belong to the source specified by acronym, case insensitive. | [optional] 
 **sourceAcronymContains** | **String**| Find all media items that belong to the source specified by partial acronym, case insensitive. | [optional] 
 **tagIds** | **String**| Find only media items tagged with the specified tag Ids. | [optional] 
 **restrictToSet** | **String**| Find only media from within the supplied list of Ids. | [optional] 
 **createdBy** | **String**| Find all media items containing the createdBy value. | [optional] 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaMostPopularMediaFormatGet

> [MediaItemWrapped] resourcesMediaMostPopularMediaFormatGet(format, opts)

Get MediaItems by popularity

Get the media with the highest ratings.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let format = "format_example"; // String | Automatically added
let opts = {
  'max': 56, // Number | The maximum number of records to return
  'offset': 56 // Number | The offset of the records set to return for pagination.
};
apiInstance.resourcesMediaMostPopularMediaFormatGet(format, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **String**| Automatically added | 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| The offset of the records set to return for pagination. | [optional] 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMediaSearchResultsJsonGet

> [MediaItemWrapped] resourcesMediaSearchResultsJsonGet(q, opts)

Get MediaItems by search query

Full search

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.MediaApi();
let q = "q_example"; // String | The search query supplied by the user
let opts = {
  'max': 56, // Number | The maximum number of records to return
  'offset': 56 // Number | The offset of the records set to return for pagination.
};
apiInstance.resourcesMediaSearchResultsJsonGet(q, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**| The search query supplied by the user | 
 **max** | **Number**| The maximum number of records to return | [optional] 
 **offset** | **Number**| The offset of the records set to return for pagination. | [optional] 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

