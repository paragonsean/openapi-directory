# AgcoApi.TranslationRequestsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translationRequestsCreateTranslationRequest**](TranslationRequestsApi.md#translationRequestsCreateTranslationRequest) | **POST** /api/v2/TranslationRequests | Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’.
[**translationRequestsGetTranslationRequest**](TranslationRequestsApi.md#translationRequestsGetTranslationRequest) | **GET** /api/v2/TranslationRequests/{Id} | Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids.
[**translationRequestsGetTranslationRequests**](TranslationRequestsApi.md#translationRequestsGetTranslationRequests) | **GET** /api/v2/TranslationRequests | Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids.
[**translationRequestsUpdateTranslationRequest**](TranslationRequestsApi.md#translationRequestsUpdateTranslationRequest) | **PUT** /api/v2/TranslationRequests/{Id} | Update a TranslationRequest object by id. Accepts a TranslationRequest object.
[**translationRequestsUpdateTranslationRequestStrings**](TranslationRequestsApi.md#translationRequestsUpdateTranslationRequestStrings) | **PUT** /api/v2/TranslationRequests/{Id}/Strings | No Documentation Found.



## translationRequestsCreateTranslationRequest

> Number translationRequestsCreateTranslationRequest(globalResourcesSharedModelsTranslationRequest)

Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationRequestsApi();
let globalResourcesSharedModelsTranslationRequest = new AgcoApi.GlobalResourcesSharedModelsTranslationRequest(); // GlobalResourcesSharedModelsTranslationRequest | 
apiInstance.translationRequestsCreateTranslationRequest(globalResourcesSharedModelsTranslationRequest, (error, data, response) => {
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
 **globalResourcesSharedModelsTranslationRequest** | [**GlobalResourcesSharedModelsTranslationRequest**](GlobalResourcesSharedModelsTranslationRequest.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## translationRequestsGetTranslationRequest

> GlobalResourcesSharedModelsTranslationRequest translationRequestsGetTranslationRequest(id)

Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationRequestsApi();
let id = 56; // Number | 
apiInstance.translationRequestsGetTranslationRequest(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**GlobalResourcesSharedModelsTranslationRequest**](GlobalResourcesSharedModelsTranslationRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationRequestsGetTranslationRequests

> APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest translationRequestsGetTranslationRequests(opts)

Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationRequestsApi();
let opts = {
  'limit': 56, // Number | 
  'offset': 56 // Number | 
};
apiInstance.translationRequestsGetTranslationRequests(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 

### Return type

[**APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest**](APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## translationRequestsUpdateTranslationRequest

> translationRequestsUpdateTranslationRequest(id, globalResourcesSharedModelsTranslationRequest, opts)

Update a TranslationRequest object by id. Accepts a TranslationRequest object.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationRequestsApi();
let id = 56; // Number | 
let globalResourcesSharedModelsTranslationRequest = new AgcoApi.GlobalResourcesSharedModelsTranslationRequest(); // GlobalResourcesSharedModelsTranslationRequest | 
let opts = {
  'doResendRequest': true // Boolean | 
};
apiInstance.translationRequestsUpdateTranslationRequest(id, globalResourcesSharedModelsTranslationRequest, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **globalResourcesSharedModelsTranslationRequest** | [**GlobalResourcesSharedModelsTranslationRequest**](GlobalResourcesSharedModelsTranslationRequest.md)|  | 
 **doResendRequest** | **Boolean**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## translationRequestsUpdateTranslationRequestStrings

> translationRequestsUpdateTranslationRequestStrings(id, requestBody)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.TranslationRequestsApi();
let id = 56; // Number | 
let requestBody = ["null"]; // [String] | 
apiInstance.translationRequestsUpdateTranslationRequestStrings(id, requestBody, (error, data, response) => {
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
 **id** | **Number**|  | 
 **requestBody** | [**[String]**](String.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

