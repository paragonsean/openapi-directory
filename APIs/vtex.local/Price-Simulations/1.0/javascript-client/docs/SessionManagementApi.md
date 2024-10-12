# PriceSimulationsApi.SessionManagementApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sessionsPost**](SessionManagementApi.md#sessionsPost) | **POST** /sessions/ | Update Order Configuration



## sessionsPost

> Object sessionsPost(contentType, accept, opts)

Update Order Configuration

Updates the Order Configuration. You should use this route every time you edit a configuration value

### Example

```javascript
import PriceSimulationsApi from 'price_simulations_api';

let apiInstance = new PriceSimulationsApi.SessionManagementApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
let opts = {
  'requestBody': new PriceSimulationsApi.RequestBody() // RequestBody | 
};
apiInstance.sessionsPost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

