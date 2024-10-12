# VtexHeadlessCms.PagesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllContentTypes**](PagesApi.md#getAllContentTypes) | **GET** /_v/cms/api/{builderId}/ | Get all Content Types
[**getCMSpage**](PagesApi.md#getCMSpage) | **GET** /_v/cms/api/{builderId}/{content-type}/{document-id}/ | Get CMS page
[**getPagesbyContentType**](PagesApi.md#getPagesbyContentType) | **GET** /_v/cms/api/{builderId}/{content-type} | Get all CMS pages by Content Type



## getAllContentTypes

> GetAllContentTypes200Response getAllContentTypes(builderId)

Get all Content Types

Gets data from all Content Types.

### Example

```javascript
import VtexHeadlessCms from 'vtex_headless_cms';

let apiInstance = new VtexHeadlessCms.PagesApi();
let builderId = "faststore"; // String | Builder ID specified in the settings of the CMS app.
apiInstance.getAllContentTypes(builderId, (error, data, response) => {
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
 **builderId** | **String**| Builder ID specified in the settings of the CMS app. | 

### Return type

[**GetAllContentTypes200Response**](GetAllContentTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCMSpage

> GetCMSpage200Response getCMSpage(builderId, contentType, documentId, opts)

Get CMS page

Gets all data from a given page.

### Example

```javascript
import VtexHeadlessCms from 'vtex_headless_cms';

let apiInstance = new VtexHeadlessCms.PagesApi();
let builderId = "faststore"; // String | Builder ID specified in the settings of the CMS app.
let contentType = "plp"; // String | Content Type ID defined in the FastStore project.
let documentId = "5af643b5-9a6d-48f2-9b34-919dd762c908"; // String | Document ID presented in the URL path of a CMS preview.
let opts = {
  'versionId': "e7263fc8-bc68-4052-9e25-dd5a2572d3bb", // String | Version ID presented in the URL path of a CMS preview.
  'releaseId': "6196c277c6dce15f9709a2a7" // String | Release ID presented in the URL path of a CMS preview.
};
apiInstance.getCMSpage(builderId, contentType, documentId, opts, (error, data, response) => {
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
 **builderId** | **String**| Builder ID specified in the settings of the CMS app. | 
 **contentType** | **String**| Content Type ID defined in the FastStore project. | 
 **documentId** | **String**| Document ID presented in the URL path of a CMS preview. | 
 **versionId** | **String**| Version ID presented in the URL path of a CMS preview. | [optional] 
 **releaseId** | **String**| Release ID presented in the URL path of a CMS preview. | [optional] 

### Return type

[**GetCMSpage200Response**](GetCMSpage200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPagesbyContentType

> GetPagesbyContentType200Response getPagesbyContentType(builderId, contentType, opts)

Get all CMS pages by Content Type

Gets data from all pages of a given Content Type.

### Example

```javascript
import VtexHeadlessCms from 'vtex_headless_cms';

let apiInstance = new VtexHeadlessCms.PagesApi();
let builderId = "faststore"; // String | Builder ID specified in the settings of the CMS app.
let contentType = "plp"; // String | Content Type identifier defined in the FastStore project.
let opts = {
  'versionId': "e7263fc8-bc68-4052-9e25-dd5a2572d3bb", // String | Version ID presented in the URL path of a CMS preview.
  'releaseId': "6196c277c6dce15f9709a2a7", // String | Release ID presented in the URL path of a CMS preview.
  'filtersField': "published" // String | Filter results by a property of the page (e.g., `filters[status]`) or by a nested custom field of the `parameters` object (e.g., `filters[parameters.collection.sort]`). *Replace {field} with the desired property.*
};
apiInstance.getPagesbyContentType(builderId, contentType, opts, (error, data, response) => {
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
 **builderId** | **String**| Builder ID specified in the settings of the CMS app. | 
 **contentType** | **String**| Content Type identifier defined in the FastStore project. | 
 **versionId** | **String**| Version ID presented in the URL path of a CMS preview. | [optional] 
 **releaseId** | **String**| Release ID presented in the URL path of a CMS preview. | [optional] 
 **filtersField** | **String**| Filter results by a property of the page (e.g., &#x60;filters[status]&#x60;) or by a nested custom field of the &#x60;parameters&#x60; object (e.g., &#x60;filters[parameters.collection.sort]&#x60;). *Replace {field} with the desired property.* | [optional] 

### Return type

[**GetPagesbyContentType200Response**](GetPagesbyContentType200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

