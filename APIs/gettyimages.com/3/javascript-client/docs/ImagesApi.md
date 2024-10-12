# GettyImages.ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3ImagesGet**](ImagesApi.md#v3ImagesGet) | **GET** /v3/images | Get metadata for multiple images by supplying multiple image ids
[**v3ImagesIdDownloadhistoryGet**](ImagesApi.md#v3ImagesIdDownloadhistoryGet) | **GET** /v3/images/{id}/downloadhistory | Returns information about a customer&#39;s download history for a specific asset
[**v3ImagesIdGet**](ImagesApi.md#v3ImagesIdGet) | **GET** /v3/images/{id} | Get metadata for a single image by supplying one image id
[**v3ImagesIdSameSeriesGet**](ImagesApi.md#v3ImagesIdSameSeriesGet) | **GET** /v3/images/{id}/same-series | Retrieve creative images from the same series
[**v3ImagesIdSimilarGet**](ImagesApi.md#v3ImagesIdSimilarGet) | **GET** /v3/images/{id}/similar | Retrieve similar images



## v3ImagesGet

> ImagesDetailResults v3ImagesGet(opts)

Get metadata for multiple images by supplying multiple image ids

This endpoint returns the detailed image metadata for all specified images.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build  search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,          \&quot;artist_title\&quot;,          \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;city\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,          \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,          \&quot;copyright\&quot;,          \&quot;country\&quot;,          \&quot;credit_line\&quot;,          \&quot;date_created\&quot;,          \&quot;date_submitted\&quot;,         \&quot;download_sizes\&quot;,          \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;state_province\&quot;,          \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image  in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary. 

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

let apiInstance = new GettyImages.ImagesApi();
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'ids': ["null"], // [String] | Specifies one or more image ids to return. Use comma delimiter when requesting multiple ids.  Maximum of 100 ids.
  'fields': [new GettyImages.ImageDetailFieldValues()] // [ImageDetailFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
};
apiInstance.v3ImagesGet(opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| Specifies one or more image ids to return. Use comma delimiter when requesting multiple ids.  Maximum of 100 ids. | [optional] 
 **fields** | [**[ImageDetailFieldValues]**](ImageDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] 

### Return type

[**ImagesDetailResults**](ImagesDetailResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3ImagesIdDownloadhistoryGet

> AssetDownloadHistoryResults v3ImagesIdDownloadhistoryGet(id, opts)

Returns information about a customer&#39;s download history for a specific asset



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

let apiInstance = new GettyImages.ImagesApi();
let id = "id_example"; // String | An image id.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'companyDownloads': true // Boolean | If specified, returns the list of previously downloaded images for all users in your company.              Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false.
};
apiInstance.v3ImagesIdDownloadhistoryGet(id, opts, (error, data, response) => {
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
 **id** | **String**| An image id. | 
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **companyDownloads** | **Boolean**| If specified, returns the list of previously downloaded images for all users in your company.              Your account must be enabled for this functionality. Contact your Getty Images account rep for more information. Default is false. | [optional] 

### Return type

[**AssetDownloadHistoryResults**](AssetDownloadHistoryResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3ImagesIdGet

> ImagesDetailResults v3ImagesIdGet(id, opts)

Get metadata for a single image by supplying one image id

This endpoint returns the detailed image metadata for a specified image.  You&#39;ll need an API key and access token to use this resource.    ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are  often used to build a detailed view of images. The following fields are provided for every image in your  result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,          \&quot;artist_title\&quot;,          \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,          \&quot;city\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,          \&quot;collection_name\&quot;,         \&quot;color_type\&quot;,          \&quot;copyright\&quot;,          \&quot;country\&quot;,          \&quot;credit_line\&quot;,          \&quot;date_created\&quot;,          \&quot;date_submitted\&quot;,         \&quot;download_sizes\&quot;,          \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;state_province\&quot;,          \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60;  ## Request Usage Considerations  - Specifying the \&quot;entity_details\&quot; response field can have significant performance implications. The field should be used only when necessary.              \&quot;name\&quot;: \&quot;string\&quot;,           \&quot;uri\&quot;: \&quot;string\&quot;

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

let apiInstance = new GettyImages.ImagesApi();
let id = "id_example"; // String | An image id. For more than one image please use the /v3/images endpoint.
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'fields': [new GettyImages.ImageDetailFieldValues()] // [ImageDetailFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
};
apiInstance.v3ImagesIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| An image id. For more than one image please use the /v3/images endpoint. | 
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **fields** | [**[ImageDetailFieldValues]**](ImageDetailFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] 

### Return type

[**ImagesDetailResults**](ImagesDetailResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3ImagesIdSameSeriesGet

> ImageSearchItemSearchResults v3ImagesIdSameSeriesGet(id, opts)

Retrieve creative images from the same series

This endpoint will provide the list of images, if any exist, from the same series as the specified creative asset id. These images are typically from the same photo shoot. This functionality will not work for editorial assets.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ]         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files  that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.  The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60; 

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

let apiInstance = new GettyImages.ImagesApi();
let id = "id_example"; // String | Identifies an existing image
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'fields': [new GettyImages.ImagesFieldValues()], // [ImagesFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
  'page': 1, // Number | Identifies page to return. Default is 1.
  'pageSize': 30 // Number | Specifies page size. Default is 30, maximum page_size is 100.
};
apiInstance.v3ImagesIdSameSeriesGet(id, opts, (error, data, response) => {
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
 **id** | **String**| Identifies an existing image | 
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **fields** | [**[ImagesFieldValues]**](ImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] 
 **page** | **Number**| Identifies page to return. Default is 1. | [optional] [default to 1]
 **pageSize** | **Number**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30]

### Return type

[**ImageSearchItemSearchResults**](ImageSearchItemSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v3ImagesIdSimilarGet

> ImageSearchItemSearchResults v3ImagesIdSimilarGet(id, opts)

Retrieve similar images

This endpoint will provide a list of images that are similar to the specified asset id.  You&#39;ll need an API key and access token to use this resource.  ## Working with Fields Sets  Fields sets are used in the **fields** request parameter to receive a suite of metadata fields. The following fields sets are available:  #### Summary Fields Set  The **summary_set** query string parameter fields value represents a small batch of metadata fields that are often used to build search response results. The following fields are provided for every image in your result set when you include **summary_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;asset_family\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ]         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Detail Fields Set  The **detail_set** query string parameter fields value represents a large batch of metadata fields that are often used to build a  detailed view of images. The following fields are provided for every image in your result set when you include **detail_set** in your request.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;allowed_use\&quot;,         \&quot;artist\&quot;,         \&quot;asset_family\&quot;,         \&quot;call_for_image\&quot;,         \&quot;caption\&quot;,         \&quot;collection_code\&quot;,         \&quot;collection_id\&quot;,         \&quot;collection_name\&quot;,         \&quot;copyright\&quot;,         \&quot;date_created\&quot;,         \&quot;display_sizes\&quot;:          [             {                 \&quot;name\&quot;: \&quot;comp\&quot;             },             {                 \&quot;name\&quot;: \&quot;preview\&quot;             },             {                 \&quot;name\&quot;: \&quot;thumb\&quot;             }         ],         \&quot;editorial_segments\&quot;,         \&quot;event_ids\&quot;,         \&quot;graphical_style\&quot;,         \&quot;license_model\&quot;,         \&quot;max_dimensions\&quot;,         \&quot;orientation\&quot;,         \&quot;product_types\&quot;,         \&quot;quality_rank\&quot;,         \&quot;referral_destinations\&quot;,         \&quot;title\&quot;     ] } &#x60;&#x60;&#x60;  #### Display Fields Set  The **display_set** query string parameter fields value represents the fields that provide you with URLs for the low resolution files  that are most frequently used to build a UI displaying search results. The following fields are provided for every image in your result set when you include **display_set** in your request.   The URI provided is subject to change at any time and must be used as-is with no modification.  &#x60;&#x60;&#x60; {     \&quot;images\&quot;:     [         \&quot;display_sizes\&quot;:          [             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;comp\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;preview\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             },             {                 \&quot;is_watermarked\&quot;: &lt;boolean&gt;,                 \&quot;name\&quot;: \&quot;thumb\&quot;,                 \&quot;uri\&quot;: \&quot;&lt;link&gt;\&quot;             }         ]     ] } &#x60;&#x60;&#x60; 

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

let apiInstance = new GettyImages.ImagesApi();
let id = "id_example"; // String | Identifies an existing image
let opts = {
  'acceptLanguage': "acceptLanguage_example", // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
  'fields': [new GettyImages.ImagesFieldValues()], // [ImagesFieldValues] | Specifies fields to return. Defaults to 'summary_set'. NOTE: Bytes, height, and width returned by 'download_sizes' field are estimates.
  'page': 1, // Number | Identifies page to return. Default is 1.
  'pageSize': 30 // Number | Specifies page size. Default is 30, maximum page_size is 100.
};
apiInstance.v3ImagesIdSimilarGet(id, opts, (error, data, response) => {
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
 **id** | **String**| Identifies an existing image | 
 **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] 
 **fields** | [**[ImagesFieldValues]**](ImagesFieldValues.md)| Specifies fields to return. Defaults to &#39;summary_set&#39;. NOTE: Bytes, height, and width returned by &#39;download_sizes&#39; field are estimates. | [optional] 
 **page** | **Number**| Identifies page to return. Default is 1. | [optional] [default to 1]
 **pageSize** | **Number**| Specifies page size. Default is 30, maximum page_size is 100. | [optional] [default to 30]

### Return type

[**ImageSearchItemSearchResults**](ImageSearchItemSearchResults.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

