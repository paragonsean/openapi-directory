# RandommerApi.CardApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCardGet**](CardApi.md#apiCardGet) | **GET** /api/Card | Get Card
[**apiCardTypesGet**](CardApi.md#apiCardTypesGet) | **GET** /api/Card/Types | Get available card types



## apiCardGet

> apiCardGet(opts)

Get Card

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.CardApi();
let opts = {
  'type': "type_example", // String | 
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiCardGet(opts, (error, data, response) => {
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
 **type** | **String**|  | [optional] 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCardTypesGet

> apiCardTypesGet(opts)

Get available card types

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.CardApi();
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiCardTypesGet(opts, (error, data, response) => {
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
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

