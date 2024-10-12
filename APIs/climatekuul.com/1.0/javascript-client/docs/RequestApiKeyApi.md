# ClimateKuulLive.RequestApiKeyApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestApiKey**](RequestApiKeyApi.md#requestApiKey) | **POST** /requestApiKey | requestApiKey



## requestApiKey

> requestApiKey(apiKeyL1, apiKeyL2, email, password, userFirstName, userLastName)

requestApiKey

### Example

```javascript
import ClimateKuulLive from 'climate_kuul_live';

let apiInstance = new ClimateKuulLive.RequestApiKeyApi();
let apiKeyL1 = "apiKeyL1_example"; // String | Api Key for client
let apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
let email = "email_example"; // String | User email
let password = 56; // Number | User password
let userFirstName = "userFirstName_example"; // String | User first name
let userLastName = "userLastName_example"; // String | User last name
apiInstance.requestApiKey(apiKeyL1, apiKeyL2, email, password, userFirstName, userLastName, (error, data, response) => {
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
 **apiKeyL1** | **String**| Api Key for client | 
 **apiKeyL2** | **String**| Integration Partner Api Key | 
 **email** | **String**| User email | 
 **password** | **Number**| User password | 
 **userFirstName** | **String**| User first name | 
 **userLastName** | **String**| User last name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

