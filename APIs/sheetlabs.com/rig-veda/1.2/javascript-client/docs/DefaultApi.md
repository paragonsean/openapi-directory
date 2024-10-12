# RvApi.DefaultApi

All URIs are relative to *https://api-rv.herokuapp.com/rv/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesGet**](DefaultApi.md#resourcesGet) | **GET** /resources | Fetch all verses sung for a specific category of god, person, or object



## resourcesGet

> resourcesGet(sungforcategory)

Fetch all verses sung for a specific category of god, person, or object

### Example

```javascript
import RvApi from 'rv_api';

let apiInstance = new RvApi.DefaultApi();
let sungforcategory = "sungforcategory_example"; // String | Click to select one of these available values.
apiInstance.resourcesGet(sungforcategory, (error, data, response) => {
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
 **sungforcategory** | **String**| Click to select one of these available values. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

