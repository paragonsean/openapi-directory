# HhsMediaServicesApi.ResourcesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesJsonGet**](ResourcesApi.md#resourcesJsonGet) | **GET** /resources.json | Get Resources by search query



## resourcesJsonGet

> [Object] resourcesJsonGet(q)

Get Resources by search query

Global search

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.ResourcesApi();
let q = "q_example"; // String | The search query supplied by the user
apiInstance.resourcesJsonGet(q, (error, data, response) => {
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

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

