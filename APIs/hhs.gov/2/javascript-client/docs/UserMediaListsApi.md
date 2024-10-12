# HhsMediaServicesApi.UserMediaListsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesUserMediaListsIdJsonGet**](UserMediaListsApi.md#resourcesUserMediaListsIdJsonGet) | **GET** /resources/userMediaLists/{id}.json | Get UserMediaList by ID



## resourcesUserMediaListsIdJsonGet

> [MediaItemWrapped] resourcesUserMediaListsIdJsonGet(id, opts)

Get UserMediaList by ID

Get a specific user media list.

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.UserMediaListsApi();
let id = 789; // Number | The id of the record to look up
let opts = {
  'displayMethod': "displayMethod_example" // String | Method used to render an html request. Accepts one: [mv, list, feed]
};
apiInstance.resourcesUserMediaListsIdJsonGet(id, opts, (error, data, response) => {
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
 **displayMethod** | **String**| Method used to render an html request. Accepts one: [mv, list, feed] | [optional] 

### Return type

[**[MediaItemWrapped]**](MediaItemWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

