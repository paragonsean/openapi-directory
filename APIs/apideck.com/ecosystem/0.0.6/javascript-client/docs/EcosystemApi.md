# EcosystemApi.EcosystemApi

All URIs are relative to *https://api.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ecosystemsOne**](EcosystemApi.md#ecosystemsOne) | **GET** /ecosystems/{ecosystem_id} | Get ecosystem



## ecosystemsOne

> GetEcosystemResponse ecosystemsOne(ecosystemId)

Get ecosystem

Get ecosystem

### Example

```javascript
import EcosystemApi from 'ecosystem_api';

let apiInstance = new EcosystemApi.EcosystemApi();
let ecosystemId = "ecosystemId_example"; // String | 
apiInstance.ecosystemsOne(ecosystemId, (error, data, response) => {
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
 **ecosystemId** | **String**|  | 

### Return type

[**GetEcosystemResponse**](GetEcosystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

