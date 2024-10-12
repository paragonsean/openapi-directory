# ObonoRksvApi.MonatsbelegeApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMonatsbelege**](MonatsbelegeApi.md#getMonatsbelege) | **GET** /registrierkassen/{registrierkasseUuid}/monatsbelege | 



## getMonatsbelege

> [Monatsbeleg] getMonatsbelege(registrierkasseUuid, opts)



Returns a list of &#x60;Monatsbelege&#x60;.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new ObonoRksvApi.MonatsbelegeApi();
let registrierkasseUuid = "registrierkasseUuid_example"; // String | The `_uuid` of the `Registrierkasse`.
let opts = {
  'year': 56, // Number | 
  'month': 56 // Number | 
};
apiInstance.getMonatsbelege(registrierkasseUuid, opts, (error, data, response) => {
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
 **registrierkasseUuid** | **String**| The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60;. | 
 **year** | **Number**|  | [optional] 
 **month** | **Number**|  | [optional] 

### Return type

[**[Monatsbeleg]**](Monatsbeleg.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

