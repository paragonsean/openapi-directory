# VocaDbWeb.ResourcesApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiResourcesCultureCodeGet**](ResourcesApiApi.md#apiResourcesCultureCodeGet) | **GET** /api/resources/{cultureCode} | 



## apiResourcesCultureCodeGet

> {String: {String: String}} apiResourcesCultureCodeGet(cultureCode, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ResourcesApiApi();
let cultureCode = "cultureCode_example"; // String | 
let opts = {
  'setNames': ["null"] // [String] | 
};
apiInstance.apiResourcesCultureCodeGet(cultureCode, opts, (error, data, response) => {
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
 **cultureCode** | **String**|  | 
 **setNames** | [**[String]**](String.md)|  | [optional] 

### Return type

**{String: {String: String}}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

