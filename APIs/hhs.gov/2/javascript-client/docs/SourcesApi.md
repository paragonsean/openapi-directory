# HhsMediaServicesApi.SourcesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesSourcesIdJsonGet**](SourcesApi.md#resourcesSourcesIdJsonGet) | **GET** /resources/sources/{id}.json | Get Source by ID
[**resourcesSourcesIdSyndicateFormatGet**](SourcesApi.md#resourcesSourcesIdSyndicateFormatGet) | **GET** /resources/sources/{id}/syndicate.{format} | Get MediaItems for Source
[**resourcesSourcesJsonGet**](SourcesApi.md#resourcesSourcesJsonGet) | **GET** /resources/sources.json | Get Sources



## resourcesSourcesIdJsonGet

> [SourceWrapped] resourcesSourcesIdJsonGet(id)

Get Source by ID

Information about a specific source.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.SourcesApi();
let id = 789; // Number | The id of the source to look up
apiInstance.resourcesSourcesIdJsonGet(id, (error, data, response) => {
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
 **id** | **Number**| The id of the source to look up | 

### Return type

[**[SourceWrapped]**](SourceWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesSourcesIdSyndicateFormatGet

> [MediaItemWrapped] resourcesSourcesIdSyndicateFormatGet(id, format, opts)

Get MediaItems for Source

MediaItem

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.SourcesApi();
let id = 789; // Number | The id of the record to look up
let format = "format_example"; // String | Automatically added
let opts = {
  'displayMethod': "displayMethod_example" // String | Method used to render an html request. Accepts one: [mv, list, feed]
};
apiInstance.resourcesSourcesIdSyndicateFormatGet(id, format, opts, (error, data, response) => {
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
 **format** | **String**| Automatically added | 
 **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesSourcesJsonGet

> [SourceWrapped] resourcesSourcesJsonGet(opts)

Get Sources

Source Listings

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.SourcesApi();
let opts = {
  'max': 56, // Number | The maximum number of records to return
  'offset': 56, // Number | Return records starting at the offset index.
  'sort': "sort_example" // String | The name of the property to which sorting will be applied
};
apiInstance.resourcesSourcesJsonGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Return records starting at the offset index. | [optional] 
 **sort** | **String**| The name of the property to which sorting will be applied | [optional] 

### Return type

[**[SourceWrapped]**](SourceWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

