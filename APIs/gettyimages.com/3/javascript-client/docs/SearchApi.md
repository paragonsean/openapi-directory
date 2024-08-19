# GettyImages.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3SearchByImageUploadsFileNamePut**](SearchApi.md#v3SearchByImageUploadsFileNamePut) | **PUT** /v3/search/by-image/uploads/{file-name} | Upload image for use by the search creative images/videos operations
[**v3SearchEventsGet**](SearchApi.md#v3SearchEventsGet) | **GET** /v3/search/events | Search for events
[**v3SearchImagesCreativeByImageGet**](SearchApi.md#v3SearchImagesCreativeByImageGet) | **GET** /v3/search/images/creative/by-image | Search for creative images based on url
[**v3SearchImagesCreativeGet**](SearchApi.md#v3SearchImagesCreativeGet) | **GET** /v3/search/images/creative | Search for creative images only
[**v3SearchImagesEditorialGet**](SearchApi.md#v3SearchImagesEditorialGet) | **GET** /v3/search/images/editorial | Search for editorial images only
[**v3SearchImagesGet**](SearchApi.md#v3SearchImagesGet) | **GET** /v3/search/images | Search for both creative and editorial images - *** DEPRECATED ***
[**v3SearchVideosCreativeByImageGet**](SearchApi.md#v3SearchVideosCreativeByImageGet) | **GET** /v3/search/videos/creative/by-image | Search for creative videos based on url
[**v3SearchVideosCreativeGet**](SearchApi.md#v3SearchVideosCreativeGet) | **GET** /v3/search/videos/creative | Search for creative videos
[**v3SearchVideosEditorialGet**](SearchApi.md#v3SearchVideosEditorialGet) | **GET** /v3/search/videos/editorial | Search for editorial videos



## v3SearchByImageUploadsFileNamePut

> v3SearchByImageUploadsFileNamePut(fileName, opts)

Upload image for use by the search creative images/videos operations

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let fileName = "fileName_example"; // String | 
let opts = {
  'body': null // Blob | 
};
apiInstance.v3SearchByImageUploadsFileNamePut(fileName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileName** | **String**|  | 
 **body** | **Blob**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: image/jpeg, image/png
- **Accept**: Not defined


## v3SearchEventsGet

> EventsSearchResult v3SearchEventsGet(opts)

Search for events

Use this endpoint to search Getty Images news, sports and entertainment events. Getty Images photographers and videographers cover editorially relevant events occurring around the world.  All images or video clips produced in association with an event, are assigned the same EventID. EventIDs are part of the meta-data returned in Search Results. Only content produced under a Getty Images brand name (Getty Images News, Getty Images Sports, Getty Images Entertainment, Film Magic, Wire Image) will be consistently assigned an EventID. The Event framework may also be used to group similar content, such as \&quot;Hats from the Royal Wedding\&quot; or \&quot;Odd-ballOffbeat images of the week\&quot;.     You&#39;ll need an API key and access token to use this resource.   You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'editorialSegment': new GettyImages.EditorialSegmentContract(), // EditorialSegmentContract | Filters to events with a matching editorial segment.
  'dateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Filters to events that start on or after this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified.
  'dateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Filters to events that start on or before this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified.
  'fields': [new GettyImages.EventFieldValues()], // [EventFieldValues] | Specifies fields to return. Default set is 'id','name','start_date'.
  'page': 1, // Number | Request results starting at a page number (default is 1, maximum is 50).
  'pageSize': 30, // Number | Request number of events to return in each page. Default is 30, maximum page_size is 100.
  'phrase': "''", // String | Filters to events related to this phrase
  'sortOrder': new GettyImages.EventSearchSortOrder() // EventSearchSortOrder | Specifies the order in which to sort the results. Default is `newest`.
};
apiInstance.v3SearchEventsGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **editorialSegment** | [**EditorialSegmentContract**](.md)| Filters to events with a matching editorial segment. | [optional] 
 **dateFrom** | **Date**| Filters to events that start on or after this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified. | [optional] 
 **dateTo** | **Date**| Filters to events that start on or before this date. Use ISO 8601 format (e.g., 1999-12-31). Defaults to UTC unless otherwise specified. | [optional] 
 **fields** | [**[EventFieldValues]**](EventFieldValues.md)| Specifies fields to return. Default set is &#39;id&#39;,&#39;name&#39;,&#39;start_date&#39;. | [optional] 
 **page** | **Number**| Request results starting at a page number (default is 1, maximum is 50). | [optional] [default to 1]
 **pageSize** | **Number**| Request number of events to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **phrase** | **String**| Filters to events related to this phrase | [optional] [default to &#39;&#39;]
 **sortOrder** | [**EventSearchSortOrder**](.md)| Specifies the order in which to sort the results. Default is &#x60;newest&#x60;. | [optional] 

### Return type

[**EventsSearchResult**](EventsSearchResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3SearchImagesCreativeByImageGet

> SearchByImageResourceResults v3SearchImagesCreativeByImageGet(opts)

Search for creative images based on url

Search for **similar creative images** by passing an &#x60;image_url&#x60; to an uploaded image OR an &#x60;asset_id&#x60; of an asset in our catalog.  All responses will have the &#x60;exclude_nudity&#x60; filter automatically applied.  ## Searching by URL  Before calling the search by image endpoint, an image in JPEG format must be uploaded to &#x60;https://api.gettyimages.com/v3/search/by-image/uploads/{CLIENT_IMAGE.jpg}&#x60;, where the client defines the &#x60;{CLIENT_IMAGE.jpg}&#x60; portion of the URL.  For example, using cURL:  &#x60;&#x60;&#x60; sh curl -i -X PUT https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg -H &#39;Content-Type: image/jpeg&#39; -H &#39;Api-Key: API_KEY&#39; --data-binary \&quot;@testimage.jpg\&quot; &#x60;&#x60;&#x60;  Once the image has been uploaded, use the full URL in the &#x60;image_url&#x60; parameter, e.g. &#x60;image_url&#x3D;https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg&#x60;.  - Uploaded files must be 10MB or smaller. - Uploads to the same URL will overwrite each other, so ensure that the client application is handling naming uniqueness appropriately. - Uploads expire after 24 hours. - Uploads and searches must be performed using the _same_ API Key.  ## Searching by asset id  When searching by &#x60;asset_id&#x60;, any image or video asset id in the Getty/iStock catalog can be used as the source for similar images. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'assetId': "assetId_example", // String | Specifies the Getty image id to use in the search.
  'excludeEditorialUseOnly': true, // Boolean | Exclude images that are only available for editorial (non-commercial) use. Default value is false.
  'facetFields': [new GettyImages.CreateImageSearchFacetsFields()], // [CreateImageSearchFacetsFields] | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \"true\" for facets to be returned.
  'facetMaxCount': 300, // Number | Specifies the maximum number of facets to return per type. Default is 300.
  'fields': [new GettyImages.CreativeImagesFieldValues()], // [CreativeImagesFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
  'imageUrl': "imageUrl_example", // String | Specifies the location of the image to use in the search.
  'includeFacets': true, // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
  'page': 1, // Number | Request results starting at a page number (default is 1).
  'pageSize': 30, // Number | Request number of images to return in each page. Default is 30, maximum page_size is 100.
  'productTypes': ["null"] // [String] | Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
};
apiInstance.v3SearchImagesCreativeByImageGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **assetId** | **String**| Specifies the Getty image id to use in the search. | [optional] 
 **excludeEditorialUseOnly** | **Boolean**| Exclude images that are only available for editorial (non-commercial) use. Default value is false. | [optional] 
 **facetFields** | [**[CreateImageSearchFacetsFields]**](CreateImageSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] 
 **facetMaxCount** | **Number**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300]
 **fields** | [**[CreativeImagesFieldValues]**](CreativeImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] 
 **imageUrl** | **String**| Specifies the location of the image to use in the search. | [optional] 
 **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] 
 **page** | **Number**| Request results starting at a page number (default is 1). | [optional] [default to 1]
 **pageSize** | **Number**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **productTypes** | [**[String]**](String.md)| Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] 

### Return type

[**SearchByImageResourceResults**](SearchByImageResourceResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3SearchImagesCreativeGet

> CreativeImageSearchResults v3SearchImagesCreativeGet(opts)

Search for creative images only

Use this endpoint to search our contemporary stock photos, illustrations and archival images.  You&#39;ll need an API key and access token to use this resource.   You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to  build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to  build a detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image  in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'ageOfPeople': [new GettyImages.AgeOfPeopleFilterType()], // [AgeOfPeopleFilterType] | Filter based on the age of individuals in an image.
  'artists': "artists_example", // String | Search for images by specific artists (free-text, comma-separated list of artists).
  'collectionCodes': ["null"], // [String] | Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type.
  'collectionsFilterType': new GettyImages.CollectionsFilterType(), // CollectionsFilterType | Use to include or exclude collections from search. The default is include
  'color': "color_example", // String | Filter based on predominant color in an image. Use 6 character hexadecimal format (e.g., #002244).
  'compositions': [new GettyImages.CompositionsFilterType()], // [CompositionsFilterType] | Filter based on image composition.
  'downloadProduct': "downloadProduct_example", // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
  'embedContentOnly': false, // Boolean | Restrict search results to embeddable images. The default is false.
  'ethnicity': [new GettyImages.EthnicityFilterType()], // [EthnicityFilterType] | Filter search results based on the ethnicity of individuals in an image.
  'excludeKeywordIds': [null], // [Number] | Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned.
  'excludeNudity': false, // Boolean | Excludes images containing nudity. The default is false.
  'excludeEditorialUseOnly': true, // Boolean | Exclude images that are only available for editorial (non-commercial) use. Default value is false.
  'fields': [new GettyImages.CreativeImagesFieldValues()], // [CreativeImagesFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
  'fileTypes': [new GettyImages.SearchFileType()], // [SearchFileType] | Return only images having a specific file type.
  'graphicalStyles': [new GettyImages.GraphicalStyle()], // [GraphicalStyle] | Filter based on graphical style of the image.
  'graphicalStylesFilterType': new GettyImages.GraphicalStylesFilterType(), // GraphicalStylesFilterType | Provides searching based on specified graphical style(s). The default is include.
  'includeRelatedSearches': false, // Boolean | Specifies whether or not to include related searches in the response. The default is false.
  'keywordIds': [null], // [Number] | Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
  'minimumSize': new GettyImages.TeeShirtSize(), // TeeShirtSize | Filter based on minimum size requested. The default is x-small.
  'numberOfPeople': [new GettyImages.NumberOfPeopleFilterType()], // [NumberOfPeopleFilterType] | Filter based on the number of people in the image.
  'orientations': [new GettyImages.ImageOrientationRequest()], // [ImageOrientationRequest] | Return only images with selected aspect ratios.
  'page': 1, // Number | Request results starting at a page number (default is 1).
  'pageSize': 30, // Number | Request number of images to return in each page. Default is 30, maximum page_size is 100.
  'phrase': "''", // String | Search images using a search phrase.
  'safeSearch': false, // Boolean | Setting safe_search to \"true\" excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it's possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative.
  'sortOrder': new GettyImages.CreativeImageSortOrder(), // CreativeImageSortOrder | Select sort order of results.  The default is best_match
  'facetFields': [new GettyImages.CreateImageSearchFacetsFields()], // [CreateImageSearchFacetsFields] | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
  'includeFacets': true, // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
  'facetMaxCount': 300 // Number | Specifies the maximum number of facets to return per type. Default is 300.
};
apiInstance.v3SearchImagesCreativeGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **ageOfPeople** | [**[AgeOfPeopleFilterType]**](AgeOfPeopleFilterType.md)| Filter based on the age of individuals in an image. | [optional] 
 **artists** | **String**| Search for images by specific artists (free-text, comma-separated list of artists). | [optional] 
 **collectionCodes** | [**[String]**](String.md)| Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type. | [optional] 
 **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] 
 **color** | **String**| Filter based on predominant color in an image. Use 6 character hexadecimal format (e.g., #002244). | [optional] 
 **compositions** | [**[CompositionsFilterType]**](CompositionsFilterType.md)| Filter based on image composition. | [optional] 
 **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] 
 **embedContentOnly** | **Boolean**| Restrict search results to embeddable images. The default is false. | [optional] [default to false]
 **ethnicity** | [**[EthnicityFilterType]**](EthnicityFilterType.md)| Filter search results based on the ethnicity of individuals in an image. | [optional] 
 **excludeKeywordIds** | [**[Number]**](Number.md)| Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned. | [optional] 
 **excludeNudity** | **Boolean**| Excludes images containing nudity. The default is false. | [optional] [default to false]
 **excludeEditorialUseOnly** | **Boolean**| Exclude images that are only available for editorial (non-commercial) use. Default value is false. | [optional] 
 **fields** | [**[CreativeImagesFieldValues]**](CreativeImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] 
 **fileTypes** | [**[SearchFileType]**](SearchFileType.md)| Return only images having a specific file type. | [optional] 
 **graphicalStyles** | [**[GraphicalStyle]**](GraphicalStyle.md)| Filter based on graphical style of the image. | [optional] 
 **graphicalStylesFilterType** | [**GraphicalStylesFilterType**](.md)| Provides searching based on specified graphical style(s). The default is include. | [optional] 
 **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false]
 **keywordIds** | [**[Number]**](Number.md)| Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned. | [optional] 
 **minimumSize** | [**TeeShirtSize**](.md)| Filter based on minimum size requested. The default is x-small. | [optional] 
 **numberOfPeople** | [**[NumberOfPeopleFilterType]**](NumberOfPeopleFilterType.md)| Filter based on the number of people in the image. | [optional] 
 **orientations** | [**[ImageOrientationRequest]**](ImageOrientationRequest.md)| Return only images with selected aspect ratios. | [optional] 
 **page** | **Number**| Request results starting at a page number (default is 1). | [optional] [default to 1]
 **pageSize** | **Number**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **phrase** | **String**| Search images using a search phrase. | [optional] [default to &#39;&#39;]
 **safeSearch** | **Boolean**| Setting safe_search to \&quot;true\&quot; excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it&#39;s possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative. | [optional] [default to false]
 **sortOrder** | [**CreativeImageSortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] 
 **facetFields** | [**[CreateImageSearchFacetsFields]**](CreateImageSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] 
 **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] 
 **facetMaxCount** | **Number**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300]

### Return type

[**CreativeImageSearchResults**](CreativeImageSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3SearchImagesEditorialGet

> EditorialImageSearchResults v3SearchImagesEditorialGet(opts)

Search for editorial images only

Use this endpoint to search our editorial stock photos, illustrations and archival images.  Editorial images represent newsworthy events or illustrate matters of general interest, such as news, sport and entertainment and are generally intended for editorial use.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token. To include your API token in the search request, add it to the headers as a Bearer token (example in curl):   -H \&quot;Authorization: Bearer &lt;your-token&gt;\&quot;  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'ageOfPeople': [new GettyImages.AgeOfPeopleFilterType()], // [AgeOfPeopleFilterType] | Filter based on the age of individuals in an image.
  'artists': "artists_example", // String | Search for images by specific artists (free-text, comma-separated list of artists).
  'collectionCodes': ["null"], // [String] | Filter by collections (comma-separated list of collection codes). Include or exclude based on collections_filter_type.
  'collectionsFilterType': new GettyImages.CollectionsFilterType(), // CollectionsFilterType | Use to include or exclude collections from search. The default is include
  'compositions': [new GettyImages.CompositionsFilterType()], // [CompositionsFilterType] | Filter based on image composition.
  'dateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31).
  'dateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31).
  'downloadProduct': "downloadProduct_example", // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
  'editorialSegments': [new GettyImages.EditorialSegmentContract()], // [EditorialSegmentContract] | Return only events with a matching editorial segment.
  'embedContentOnly': false, // Boolean | Restrict search results to embeddable images. The default is false.
  'ethnicity': [new GettyImages.EthnicityFilterType()], // [EthnicityFilterType] | Filter search results based on the ethnicity of individuals in an image.
  'eventIds': [null], // [Number] | Filter based on specific events
  'excludeKeywordIds': [null], // [Number] | Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned.
  'fields': [new GettyImages.EditorialImagesFieldValues()], // [EditorialImagesFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
  'fileTypes': [new GettyImages.SearchFileType()], // [SearchFileType] | Return only images having a specific file type.
  'graphicalStyles': [new GettyImages.EditorialGraphicalStyle()], // [EditorialGraphicalStyle] | Filter based on graphical style of the image.
  'graphicalStylesFilterType': new GettyImages.GraphicalStylesFilterType(), // GraphicalStylesFilterType | Provides searching based on specified graphical style(s). The default is include.
  'includeRelatedSearches': false, // Boolean | Specifies whether or not to include related searches in the response. The default is false.
  'keywordIds': [null], // [Number] | Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
  'minimumSize': new GettyImages.TeeShirtSize(), // TeeShirtSize | Filter based on minimum size requested. The default is x-small.
  'numberOfPeople': [new GettyImages.NumberOfPeopleFilterType()], // [NumberOfPeopleFilterType] | Filter based on the number of people in the image.
  'orientations': [new GettyImages.ImageOrientationRequest()], // [ImageOrientationRequest] | Return only images with selected aspect ratios.
  'page': 1, // Number | Request results starting at a page number (default is 1).
  'pageSize': 30, // Number | Request number of images to return in each page. Default is 30, maximum page_size is 100.
  'phrase': "phrase_example", // String | Search images using a search phrase.
  'sortOrder': new GettyImages.SortOrder(), // SortOrder | Select sort order of results.  The default is best_match
  'specificPeople': ["null"], // [String] | Return only images associated with specific people (using a comma-delimited list).
  'minimumQualityRank': 56, // Number | Filter search results based on minimum quality ranking. Possible values 1, 2, 3 with 1 being best.
  'facetFields': [new GettyImages.EditorialImageSearchFacetsFields()], // [EditorialImageSearchFacetsFields] | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
  'includeFacets': true, // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
  'facetMaxCount': 300 // Number | Specifies the maximum number of facets to return per type. Default is 300.
};
apiInstance.v3SearchImagesEditorialGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **ageOfPeople** | [**[AgeOfPeopleFilterType]**](AgeOfPeopleFilterType.md)| Filter based on the age of individuals in an image. | [optional] 
 **artists** | **String**| Search for images by specific artists (free-text, comma-separated list of artists). | [optional] 
 **collectionCodes** | [**[String]**](String.md)| Filter by collections (comma-separated list of collection codes). Include or exclude based on collections_filter_type. | [optional] 
 **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] 
 **compositions** | [**[CompositionsFilterType]**](CompositionsFilterType.md)| Filter based on image composition. | [optional] 
 **dateFrom** | **Date**| Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] 
 **dateTo** | **Date**| Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] 
 **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] 
 **editorialSegments** | [**[EditorialSegmentContract]**](EditorialSegmentContract.md)| Return only events with a matching editorial segment. | [optional] 
 **embedContentOnly** | **Boolean**| Restrict search results to embeddable images. The default is false. | [optional] [default to false]
 **ethnicity** | [**[EthnicityFilterType]**](EthnicityFilterType.md)| Filter search results based on the ethnicity of individuals in an image. | [optional] 
 **eventIds** | [**[Number]**](Number.md)| Filter based on specific events | [optional] 
 **excludeKeywordIds** | [**[Number]**](Number.md)| Return only images not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also do not contain the requested keyword(s) are returned. | [optional] 
 **fields** | [**[EditorialImagesFieldValues]**](EditorialImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] 
 **fileTypes** | [**[SearchFileType]**](SearchFileType.md)| Return only images having a specific file type. | [optional] 
 **graphicalStyles** | [**[EditorialGraphicalStyle]**](EditorialGraphicalStyle.md)| Filter based on graphical style of the image. | [optional] 
 **graphicalStylesFilterType** | [**GraphicalStylesFilterType**](.md)| Provides searching based on specified graphical style(s). The default is include. | [optional] 
 **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false]
 **keywordIds** | [**[Number]**](Number.md)| Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned. | [optional] 
 **minimumSize** | [**TeeShirtSize**](.md)| Filter based on minimum size requested. The default is x-small. | [optional] 
 **numberOfPeople** | [**[NumberOfPeopleFilterType]**](NumberOfPeopleFilterType.md)| Filter based on the number of people in the image. | [optional] 
 **orientations** | [**[ImageOrientationRequest]**](ImageOrientationRequest.md)| Return only images with selected aspect ratios. | [optional] 
 **page** | **Number**| Request results starting at a page number (default is 1). | [optional] [default to 1]
 **pageSize** | **Number**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **phrase** | **String**| Search images using a search phrase. | [optional] 
 **sortOrder** | [**SortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] 
 **specificPeople** | [**[String]**](String.md)| Return only images associated with specific people (using a comma-delimited list). | [optional] 
 **minimumQualityRank** | **Number**| Filter search results based on minimum quality ranking. Possible values 1, 2, 3 with 1 being best. | [optional] 
 **facetFields** | [**[EditorialImageSearchFacetsFields]**](EditorialImageSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] 
 **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] 
 **facetMaxCount** | **Number**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300]

### Return type

[**EditorialImageSearchResults**](EditorialImageSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3SearchImagesGet

> ImageSearchItemSearchResults v3SearchImagesGet(opts)

Search for both creative and editorial images - *** DEPRECATED ***

## _This endpoint draws from such a large diversity of content, the results will not be as relevant as when the more specific Creative or Editorial endpoints are used. Additionally, the response time for this endpoint is slower compared to that for Creative and Editorial-specific endpoints. For these reasons,_ _**it is highly recommended that those endpoints are used instead of this blended endpoint.**_    You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.&lt;br&gt; To include your API token in the search request, add it to the headers as a Bearer token (example in curl):   -H \&quot;Authorization: Bearer &lt;your-token&gt;\&quot;  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of images.  The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] ] &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most  frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'ageOfPeople': [new GettyImages.AgeOfPeopleFilterType()], // [AgeOfPeopleFilterType] | Filter based on the age of individuals in an image.
  'artists': "artists_example", // String | Search for images by specific artists (free-text, comma-separated list of artists).
  'collectionCodes': ["null"], // [String] | Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type.
  'collectionsFilterType': new GettyImages.CollectionsFilterType(), // CollectionsFilterType | Provides searching based on specified collection(s). The default is Include
  'color': "color_example", // String | Filter based on predominant color in an image. Use 6 character hexidecimal format (e.g., #002244). Note: when specified, results will not contain editorial images.
  'compositions': [new GettyImages.CompositionsFilterType()], // [CompositionsFilterType] | Filter based on image composition.
  'downloadProduct': "downloadProduct_example", // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
  'embedContentOnly': false, // Boolean | Restrict search results to embeddable images. The default is false.
  'eventIds': [null], // [Number] | Filter based on specific events
  'ethnicity': [new GettyImages.EthnicityFilterType()], // [EthnicityFilterType] | Filter search results based on the ethnicity of individuals in an image.
  'excludeNudity': false, // Boolean | Excludes images containing nudity. The default is false.
  'fields': [new GettyImages.ImagesFieldValues()], // [ImagesFieldValues] | Specifies fields to return. Defaults to 'summary_set'.
  'fileTypes': [new GettyImages.SearchFileType()], // [SearchFileType] | Return only images having a specific file type.
  'graphicalStyles': [new GettyImages.GraphicalStyle()], // [GraphicalStyle] | Filter based on graphical style of the image.
  'graphicalStylesFilterType': new GettyImages.GraphicalStylesFilterType(), // GraphicalStylesFilterType | Provides searching based on specified graphical style(s). The default is Include
  'includeRelatedSearches': false, // Boolean | Specifies whether or not to include related searches in the response. The default is false.
  'keywordIds': [null], // [Number] | Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned.
  'minimumSize': new GettyImages.TeeShirtSize(), // TeeShirtSize | Filter based on minimum size requested. The default is x-small
  'numberOfPeople': [new GettyImages.NumberOfPeopleFilterType()], // [NumberOfPeopleFilterType] | Filter based on the number of people in the image.
  'orientations': [new GettyImages.ImageOrientationRequest()], // [ImageOrientationRequest] | Return only images with selected aspect ratios.
  'page': 1, // Number | Request results starting at a page number (default is 1).
  'pageSize': 30, // Number | Request number of images to return in each page. Default is 30, maximum page_size is 100.
  'phrase': "phrase_example", // String | Search images using a search phrase.
  'sortOrder': new GettyImages.BlendedImageSortOrder(), // BlendedImageSortOrder | Select sort order of results.  The default is best_match
  'specificPeople': ["null"] // [String] | Return only images associated with specific people (using a comma-delimited list).
};
apiInstance.v3SearchImagesGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **ageOfPeople** | [**[AgeOfPeopleFilterType]**](AgeOfPeopleFilterType.md)| Filter based on the age of individuals in an image. | [optional] 
 **artists** | **String**| Search for images by specific artists (free-text, comma-separated list of artists). | [optional] 
 **collectionCodes** | [**[String]**](String.md)| Filter by collection codes (comma-separated list). Include or exclude based on collections_filter_type. | [optional] 
 **collectionsFilterType** | [**CollectionsFilterType**](.md)| Provides searching based on specified collection(s). The default is Include | [optional] 
 **color** | **String**| Filter based on predominant color in an image. Use 6 character hexidecimal format (e.g., #002244). Note: when specified, results will not contain editorial images. | [optional] 
 **compositions** | [**[CompositionsFilterType]**](CompositionsFilterType.md)| Filter based on image composition. | [optional] 
 **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] 
 **embedContentOnly** | **Boolean**| Restrict search results to embeddable images. The default is false. | [optional] [default to false]
 **eventIds** | [**[Number]**](Number.md)| Filter based on specific events | [optional] 
 **ethnicity** | [**[EthnicityFilterType]**](EthnicityFilterType.md)| Filter search results based on the ethnicity of individuals in an image. | [optional] 
 **excludeNudity** | **Boolean**| Excludes images containing nudity. The default is false. | [optional] [default to false]
 **fields** | [**[ImagesFieldValues]**](ImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. | [optional] 
 **fileTypes** | [**[SearchFileType]**](SearchFileType.md)| Return only images having a specific file type. | [optional] 
 **graphicalStyles** | [**[GraphicalStyle]**](GraphicalStyle.md)| Filter based on graphical style of the image. | [optional] 
 **graphicalStylesFilterType** | [**GraphicalStylesFilterType**](.md)| Provides searching based on specified graphical style(s). The default is Include | [optional] 
 **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false]
 **keywordIds** | [**[Number]**](Number.md)| Return only images tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those images matching the query phrase which also contain the requested keyword(s) are returned. | [optional] 
 **minimumSize** | [**TeeShirtSize**](.md)| Filter based on minimum size requested. The default is x-small | [optional] 
 **numberOfPeople** | [**[NumberOfPeopleFilterType]**](NumberOfPeopleFilterType.md)| Filter based on the number of people in the image. | [optional] 
 **orientations** | [**[ImageOrientationRequest]**](ImageOrientationRequest.md)| Return only images with selected aspect ratios. | [optional] 
 **page** | **Number**| Request results starting at a page number (default is 1). | [optional] [default to 1]
 **pageSize** | **Number**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **phrase** | **String**| Search images using a search phrase. | [optional] 
 **sortOrder** | [**BlendedImageSortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] 
 **specificPeople** | [**[String]**](String.md)| Return only images associated with specific people (using a comma-delimited list). | [optional] 

### Return type

[**ImageSearchItemSearchResults**](ImageSearchItemSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3SearchVideosCreativeByImageGet

> CreativeVideoSearchResults v3SearchVideosCreativeByImageGet(opts)

Search for creative videos based on url

Search for **similar creative videos** by passing an &#x60;image_url&#x60; to an uploaded image/frame grab from a video OR an &#x60;asset_id&#x60; of an asset in our catalog.  All responses will have the &#x60;exclude_nudity&#x60; filter automatically applied.  ## Searching by URL  Before calling the search by image endpoint, an image or frame grab in JPEG format must be uploaded to &#x60;https://api.gettyimages.com/v3/search/by-image/uploads/{CLIENT_IMAGE.jpg}&#x60;, where the client defines the &#x60;{CLIENT_IMAGE.jpg}&#x60; portion of the URL.  For example, using cURL:  &#x60;&#x60;&#x60; sh curl -i -X PUT https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg -H &#39;Content-Type: image/jpeg&#39; -H &#39;Api-Key: API_KEY&#39; --data-binary \&quot;@testimage.jpg\&quot; &#x60;&#x60;&#x60;  Once the image has been uploaded, use the full URL in the &#x60;image_url&#x60; parameter, e.g. &#x60;image_url&#x3D;https://api.gettyimages.com/v3/search/by-image/uploads/my-test-image.jpg&#x60;.  - Uploaded files must be 10MB or smaller - Uploads to the same URL will overwrite each other, so ensure that the client application is handling naming uniqueness appropriately. - Uploads expire after 24 hours. - Uploads and searches must be performed using the _same_ API Key.  ## Searching by asset id  When searching by &#x60;asset_id&#x60;, any image or video asset id in the Getty/iStock catalog can be used as the source for similar videos. 

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'assetId': "assetId_example", // String | Specifies the Getty video id to use in the search.
  'excludeEditorialUseOnly': true, // Boolean | Exclude videos that are only available for editorial (non-commercial) use. Default value is false.
  'facetFields': [new GettyImages.CreateVideoSearchFacetsFields()], // [CreateVideoSearchFacetsFields] | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \"true\" for facets to be returned.
  'facetMaxCount': 300, // Number | Specifies the maximum number of facets to return per type. Default is 300.
  'fields': [new GettyImages.CreativeVideosFieldValues()], // [CreativeVideosFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
  'imageUrl': "imageUrl_example", // String | Specifies the location of the image to use in the search.
  'includeFacets': true, // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
  'page': 1, // Number | Request results starting at a page number (default is 1).
  'pageSize': 30, // Number | Request number of images to return in each page. Default is 30, maximum page_size is 100.
  'productTypes': ["null"] // [String] | Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
};
apiInstance.v3SearchVideosCreativeByImageGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **assetId** | **String**| Specifies the Getty video id to use in the search. | [optional] 
 **excludeEditorialUseOnly** | **Boolean**| Exclude videos that are only available for editorial (non-commercial) use. Default value is false. | [optional] 
 **facetFields** | [**[CreateVideoSearchFacetsFields]**](CreateVideoSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                      The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] 
 **facetMaxCount** | **Number**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300]
 **fields** | [**[CreativeVideosFieldValues]**](CreativeVideosFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] 
 **imageUrl** | **String**| Specifies the location of the image to use in the search. | [optional] 
 **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] 
 **page** | **Number**| Request results starting at a page number (default is 1). | [optional] [default to 1]
 **pageSize** | **Number**| Request number of images to return in each page. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **productTypes** | [**[String]**](String.md)| Filter images to those from one of your product types.                       Allowed values are easyaccess, imagepack, premiumaccess and royaltyfreesubscription.                       If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the product_types value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] 

### Return type

[**CreativeVideoSearchResults**](CreativeVideoSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3SearchVideosCreativeGet

> CreativeVideoSearchResults v3SearchVideosCreativeGet(opts)

Search for creative videos

Use this endpoint to search premium stock video, from archival film to contemporary 4K and HD footage.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only  assets that you have a license to use, you need to also include an authorization token in the header of your request. Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,          \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,    \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,          \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;era\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files  that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result  set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'ageOfPeople': [new GettyImages.AgeOfPeopleFilterType()], // [AgeOfPeopleFilterType] | Provides filtering according to the age of individuals in a video.
  'artists': "artists_example", // String | Search for videos by specific artists (free-text, comma-separated list of artists).
  'aspectRatios': [new GettyImages.VideoAspectRatioFilterType()], // [VideoAspectRatioFilterType] | Search for videos by specific aspect ratios.
  'collectionCodes': ["null"], // [String] | Provides filtering by collection code.
  'collectionsFilterType': new GettyImages.CollectionsFilterType(), // CollectionsFilterType | Use to include or exclude collections from search. The default is include
  'compositions': [new GettyImages.CompositionsFilterType()], // [CompositionsFilterType] | Filter based on video composition.
  'downloadProduct': "downloadProduct_example", // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
  'excludeNudity': false, // Boolean | Excludes videos containing nudity. The default is false.
  'excludeEditorialUseOnly': true, // Boolean | Exclude videos that are only available for editorial (non-commercial) use. Default value is false.
  'excludeKeywordIds': [null], // [Number] | Return only videos not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also do not contain the requested keyword(s) are returned.
  'fields': [new GettyImages.CreativeVideosFieldValues()], // [CreativeVideosFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
  'formatAvailable': new GettyImages.VideoFormatsRequest(), // VideoFormatsRequest | Filters according to the digital video format available on a film asset.
  'frameRates': [new GettyImages.VideoFrameRates()], // [VideoFrameRates] | Provides filtering by video frame rate (frames/second).
  'imageTechniques': [new GettyImages.ImageTechniquesFilterType()], // [ImageTechniquesFilterType] | Filter based on image technique.
  'includeRelatedSearches': false, // Boolean | Specifies whether or not to include related searches in the response. The default is false.
  'keywordIds': [null], // [Number] | Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned.
  'licenseModels': [new GettyImages.LicenseModelVideoRequest()], // [LicenseModelVideoRequest] | Specifies the video licensing model(s).
  'orientations': [new GettyImages.VideoOrientationRequest()], // [VideoOrientationRequest] | Return only videos with selected orientations.
  'minClipLength': 0, // Number | Provides filtering by minimum length of video clip, in seconds
  'maxClipLength': 0, // Number | Provides filtering by maximum length of video, in seconds
  'page': 1, // Number | Identifies page to return. Default is 1.
  'pageSize': 30, // Number | Specifies page size. Default is 30, maximum page_size is 100.
  'phrase': "''", // String | Free-text search query.
  'safeSearch': false, // Boolean | Setting safe_search to \"true\" excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it's possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative.
  'sortOrder': new GettyImages.CreativeVideoSortOrder(), // CreativeVideoSortOrder | Select sort order of results.  The default is best_match
  'releaseStatus': new GettyImages.ReleaseStatus(), // ReleaseStatus | Allows filtering by type of model release.
  'facetFields': [new GettyImages.CreateVideoSearchFacetsFields()], // [CreateVideoSearchFacetsFields] | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
  'facetMaxCount': 300, // Number | Specifies the maximum number of facets to return per type. Default is 300.
  'includeFacets': true, // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
  'viewpoints': [new GettyImages.ViewpointsFilterType()] // [ViewpointsFilterType] | Filter based on viewpoint.
};
apiInstance.v3SearchVideosCreativeGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **ageOfPeople** | [**[AgeOfPeopleFilterType]**](AgeOfPeopleFilterType.md)| Provides filtering according to the age of individuals in a video. | [optional] 
 **artists** | **String**| Search for videos by specific artists (free-text, comma-separated list of artists). | [optional] 
 **aspectRatios** | [**[VideoAspectRatioFilterType]**](VideoAspectRatioFilterType.md)| Search for videos by specific aspect ratios. | [optional] 
 **collectionCodes** | [**[String]**](String.md)| Provides filtering by collection code. | [optional] 
 **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] 
 **compositions** | [**[CompositionsFilterType]**](CompositionsFilterType.md)| Filter based on video composition. | [optional] 
 **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] 
 **excludeNudity** | **Boolean**| Excludes videos containing nudity. The default is false. | [optional] [default to false]
 **excludeEditorialUseOnly** | **Boolean**| Exclude videos that are only available for editorial (non-commercial) use. Default value is false. | [optional] 
 **excludeKeywordIds** | [**[Number]**](Number.md)| Return only videos not tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also do not contain the requested keyword(s) are returned. | [optional] 
 **fields** | [**[CreativeVideosFieldValues]**](CreativeVideosFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] 
 **formatAvailable** | [**VideoFormatsRequest**](.md)| Filters according to the digital video format available on a film asset. | [optional] 
 **frameRates** | [**[VideoFrameRates]**](VideoFrameRates.md)| Provides filtering by video frame rate (frames/second). | [optional] 
 **imageTechniques** | [**[ImageTechniquesFilterType]**](ImageTechniquesFilterType.md)| Filter based on image technique. | [optional] 
 **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false]
 **keywordIds** | [**[Number]**](Number.md)| Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned. | [optional] 
 **licenseModels** | [**[LicenseModelVideoRequest]**](LicenseModelVideoRequest.md)| Specifies the video licensing model(s). | [optional] 
 **orientations** | [**[VideoOrientationRequest]**](VideoOrientationRequest.md)| Return only videos with selected orientations. | [optional] 
 **minClipLength** | **Number**| Provides filtering by minimum length of video clip, in seconds | [optional] [default to 0]
 **maxClipLength** | **Number**| Provides filtering by maximum length of video, in seconds | [optional] [default to 0]
 **page** | **Number**| Identifies page to return. Default is 1. | [optional] [default to 1]
 **pageSize** | **Number**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **phrase** | **String**| Free-text search query. | [optional] [default to &#39;&#39;]
 **safeSearch** | **Boolean**| Setting safe_search to \&quot;true\&quot; excludes images containing nudity, death, profanity, drugs and alcohol, suggestive content, and graphic content from the result set. The default is false. Because this is a keyword-based filter, it&#39;s possible that a small number of unsafe images may not be caught by the filter. Please direct feedback to your Getty Images Account or API support representative. | [optional] [default to false]
 **sortOrder** | [**CreativeVideoSortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] 
 **releaseStatus** | [**ReleaseStatus**](.md)| Allows filtering by type of model release. | [optional] 
 **facetFields** | [**[CreateVideoSearchFacetsFields]**](CreateVideoSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] 
 **facetMaxCount** | **Number**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300]
 **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] 
 **viewpoints** | [**[ViewpointsFilterType]**](ViewpointsFilterType.md)| Filter based on viewpoint. | [optional] 

### Return type

[**CreativeVideoSearchResults**](CreativeVideoSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3SearchVideosEditorialGet

> EditorialVideoSearchResults v3SearchVideosEditorialGet(opts)

Search for editorial videos

Use this endpoint to search current and archival video clips of celebrities, newsmakers, and events.  You&#39;ll need an API key and access token to use this resource.  You can show different information in the response by specifying values on the \&quot;fields\&quot; parameter (see details below). You can search with only an API key, and that will give you search results that are equivalent to doing a search on the GettyImages.com site without being logged in (anonymous search).  If you are a Getty Images API customer and would like to ensure that your API searches return only assets that you have a license to use, you need to also include an authorization token in the header of your request.  Please consult our [Authorization FAQ](http://developers.gettyimages.com/en/authorization-faq.html) for more information on authorization tokens, and our [Authorization Workflows](https://github.com/gettyimages/gettyimages-api/blob/master/OAuth2Workflow.md) for code examples of getting a token.  Search requests without a phrase parameter are not supported and may not always work.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every video in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;asset_family\&quot;,          \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;license_model\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a detailed view of videos. The following fields are provided for every video in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:      [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,    \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;clip_length\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,          \&quot;color_type\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:         [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;era\&quot;,         \&quot;event_ids\&quot;,         \&quot;license_model\&quot;,         \&quot;mastered_to\&quot;,         \&quot;originally_shot_on\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;shot_speed\&quot;,         \&quot;source\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every video in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;videos\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import GettyImages from 'getty_images';
let defaultClient = GettyImages.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: Api-Key
let Api-Key = defaultClient.authentications['Api-Key'];
Api-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Api-Key.apiKeyPrefix = 'Token';

let apiInstance = new GettyImages.SearchApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'gICountryCode': "gICountryCode_example", // String | Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes.
  'ageOfPeople': [new GettyImages.AgeOfPeopleFilterType()], // [AgeOfPeopleFilterType] | Provides filtering according to the age of individuals in a video.
  'artists': "artists_example", // String | Search for videos by specific artists (free-text, comma-separated list of artists).
  'aspectRatios': [new GettyImages.VideoAspectRatioFilterType()], // [VideoAspectRatioFilterType] | Search for videos by specific aspect ratios.
  'collectionCodes': ["null"], // [String] | Provides filtering by collection code.
  'collectionsFilterType': new GettyImages.CollectionsFilterType(), // CollectionsFilterType | Use to include or exclude collections from search. The default is include
  'compositions': [new GettyImages.CompositionsFilterType()], // [CompositionsFilterType] | Filter based on video composition.
  'dateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31).
  'dateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31).
  'downloadProduct': "downloadProduct_example", // String | Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response.
  'editorialVideoTypes': [new GettyImages.EditorialVideoType()], // [EditorialVideoType] | Allows filtering by types of video.
  'fields': [new GettyImages.EditorialVideosFieldValues()], // [EditorialVideosFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes returned by 'download_sizes' field is an estimate.
  'formatAvailable': new GettyImages.VideoFormatsRequest(), // VideoFormatsRequest | Filters according to the digital video format available on a film asset.
  'frameRates': [new GettyImages.VideoFrameRates()], // [VideoFrameRates] | Provides filtering by video frame rate (frames/second).
  'imageTechniques': [new GettyImages.ImageTechniquesFilterType()], // [ImageTechniquesFilterType] | Filter based on image technique.
  'includeRelatedSearches': false, // Boolean | Specifies whether or not to include related searches in the response. The default is false.
  'keywordIds': [null], // [Number] | Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned.
  'minClipLength': 0, // Number | Provides filtering by minimum length of video clip, in seconds
  'maxClipLength': 0, // Number | Provides filtering by maximum length of video clip, in seconds
  'orientations': [new GettyImages.VideoOrientationRequest()], // [VideoOrientationRequest] | Return only videos with selected orientations.
  'page': 1, // Number | Identifies page to return. Default is 1.
  'pageSize': 30, // Number | Specifies page size. Default is 30, maximum page_size is 100.
  'phrase': "''", // String | Free-text search query.
  'sortOrder': new GettyImages.SortOrder(), // SortOrder | Select sort order of results.  The default is best_match
  'specificPeople': ["null"], // [String] | Allows filtering by specific peoples' names.
  'releaseStatus': new GettyImages.ReleaseStatus(), // ReleaseStatus | Allows filtering by type of model release.
  'facetFields': [new GettyImages.EditorialVideoSearchFacetsFields()], // [EditorialVideoSearchFacetsFields] | Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \"true\" for facets to be returned.
  'includeFacets': true, // Boolean | Specifies whether or not to include facets in the result set. Default is \"false\".
  'facetMaxCount': 300, // Number | Specifies the maximum number of facets to return per type. Default is 300.
  'viewpoints': [new GettyImages.ViewpointsFilterType()] // [ViewpointsFilterType] | Filter based on viewpoint.
};
apiInstance.v3SearchVideosEditorialGet(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **gICountryCode** | **String**| Receive regionally relevant search results based on the value specified. Accepts only ISO Alpha-3 country codes. The Countries operation can be used to retrieve the codes. | [optional] 
 **ageOfPeople** | [**[AgeOfPeopleFilterType]**](AgeOfPeopleFilterType.md)| Provides filtering according to the age of individuals in a video. | [optional] 
 **artists** | **String**| Search for videos by specific artists (free-text, comma-separated list of artists). | [optional] 
 **aspectRatios** | [**[VideoAspectRatioFilterType]**](VideoAspectRatioFilterType.md)| Search for videos by specific aspect ratios. | [optional] 
 **collectionCodes** | [**[String]**](String.md)| Provides filtering by collection code. | [optional] 
 **collectionsFilterType** | [**CollectionsFilterType**](.md)| Use to include or exclude collections from search. The default is include | [optional] 
 **compositions** | [**[CompositionsFilterType]**](CompositionsFilterType.md)| Filter based on video composition. | [optional] 
 **dateFrom** | **Date**| Return only images that are created on or after this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] 
 **dateTo** | **Date**| Return only images that are created on or before this date. Use ISO 8601 format (e.g., 1999-12-31). | [optional] 
 **downloadProduct** | **String**| Filters based on which product the asset will download against.                      Allowed values are easyaccess, editorialsubscription, imagepack, premiumaccess and royaltyfreesubscription.                      If you have more than one instance of a product, you may also include the ID of the product instance you wish to filter on.                       For example, some users may have more than one premiumaccess product, so the download_product value would be premiumaccess:1234.                       Product ID can be obtained from the GET /products response. | [optional] 
 **editorialVideoTypes** | [**[EditorialVideoType]**](EditorialVideoType.md)| Allows filtering by types of video. | [optional] 
 **fields** | [**[EditorialVideosFieldValues]**](EditorialVideosFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes returned by &#39;download_sizes&#39; field is an estimate. | [optional] 
 **formatAvailable** | [**VideoFormatsRequest**](.md)| Filters according to the digital video format available on a film asset. | [optional] 
 **frameRates** | [**[VideoFrameRates]**](VideoFrameRates.md)| Provides filtering by video frame rate (frames/second). | [optional] 
 **imageTechniques** | [**[ImageTechniquesFilterType]**](ImageTechniquesFilterType.md)| Filter based on image technique. | [optional] 
 **includeRelatedSearches** | **Boolean**| Specifies whether or not to include related searches in the response. The default is false. | [optional] [default to false]
 **keywordIds** | [**[Number]**](Number.md)| Return only videos tagged with specific keyword(s). Specify using a comma-separated list of keyword Ids. If keyword Ids and phrase are both specified, only those videos matching the query phrase which also contain the requested keyword(s) are returned. | [optional] 
 **minClipLength** | **Number**| Provides filtering by minimum length of video clip, in seconds | [optional] [default to 0]
 **maxClipLength** | **Number**| Provides filtering by maximum length of video clip, in seconds | [optional] [default to 0]
 **orientations** | [**[VideoOrientationRequest]**](VideoOrientationRequest.md)| Return only videos with selected orientations. | [optional] 
 **page** | **Number**| Identifies page to return. Default is 1. | [optional] [default to 1]
 **pageSize** | **Number**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30]
 **phrase** | **String**| Free-text search query. | [optional] [default to &#39;&#39;]
 **sortOrder** | [**SortOrder**](.md)| Select sort order of results.  The default is best_match | [optional] 
 **specificPeople** | [**[String]**](String.md)| Allows filtering by specific peoples&#39; names. | [optional] 
 **releaseStatus** | [**ReleaseStatus**](.md)| Allows filtering by type of model release. | [optional] 
 **facetFields** | [**[EditorialVideoSearchFacetsFields]**](EditorialVideoSearchFacetsFields.md)| Specifies the facets to return in the response. Facets provide additional search parameters to refine your results.                     The include_facets parameter must be set to \&quot;true\&quot; for facets to be returned. | [optional] 
 **includeFacets** | **Boolean**| Specifies whether or not to include facets in the result set. Default is \&quot;false\&quot;. | [optional] 
 **facetMaxCount** | **Number**| Specifies the maximum number of facets to return per type. Default is 300. | [optional] [default to 300]
 **viewpoints** | [**[ViewpointsFilterType]**](ViewpointsFilterType.md)| Filter based on viewpoint. | [optional] 

### Return type

[**EditorialVideoSearchResults**](EditorialVideoSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

