# HhsMediaServicesApi.LanguagesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesLanguagesIdJsonGet**](LanguagesApi.md#resourcesLanguagesIdJsonGet) | **GET** /resources/languages/{id}.json | Get Language by ID
[**resourcesLanguagesJsonGet**](LanguagesApi.md#resourcesLanguagesJsonGet) | **GET** /resources/languages.json | Get Languages



## resourcesLanguagesIdJsonGet

> [LanguageWrapped] resourcesLanguagesIdJsonGet(id)

Get Language by ID

Information about a specific language

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.LanguagesApi();
let id = 789; // Number | The id of the language to look up
apiInstance.resourcesLanguagesIdJsonGet(id, (error, data, response) => {
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
 **id** | **Number**| The id of the language to look up | 

### Return type

[**[LanguageWrapped]**](LanguageWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesLanguagesJsonGet

> [LanguageWrapped] resourcesLanguagesJsonGet(opts)

Get Languages

Language Listings

### Example

```javascript
import HhsMediaServicesApi from 'hhs_media_services_api';

let apiInstance = new HhsMediaServicesApi.LanguagesApi();
let opts = {
  'max': 56, // Number | The maximum number of records to return
  'offset': 56, // Number | Return records starting at the offset index.
  'sort': "sort_example" // String | The name of the property to which sorting will be applied
};
apiInstance.resourcesLanguagesJsonGet(opts, (error, data, response) => {
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

[**[LanguageWrapped]**](LanguageWrapped.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

