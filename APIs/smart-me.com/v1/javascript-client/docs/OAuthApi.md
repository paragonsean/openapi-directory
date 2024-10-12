# SmartMe.OAuthApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiOauthAuthorizePost**](OAuthApi.md#apiOauthAuthorizePost) | **POST** /api/oauth/authorize | 
[**oAuthAuthorize**](OAuthApi.md#oAuthAuthorize) | **GET** /api/oauth/authorize | 



## apiOauthAuthorizePost

> Object apiOauthAuthorizePost(clientId, redirectUri, state, opts)



### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.OAuthApi();
let clientId = "clientId_example"; // String | 
let redirectUri = "redirectUri_example"; // String | 
let state = "state_example"; // String | 
let opts = {
  'scope': "scope_example", // String | 
  'clientSecret': "clientSecret_example" // String | 
};
apiInstance.apiOauthAuthorizePost(clientId, redirectUri, state, opts, (error, data, response) => {
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
 **clientId** | **String**|  | 
 **redirectUri** | **String**|  | 
 **state** | **String**|  | 
 **scope** | **String**|  | [optional] 
 **clientSecret** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## oAuthAuthorize

> Object oAuthAuthorize(clientId, redirectUri, state, opts)



### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.OAuthApi();
let clientId = "clientId_example"; // String | 
let redirectUri = "redirectUri_example"; // String | 
let state = "state_example"; // String | 
let opts = {
  'scope': "scope_example", // String | 
  'clientSecret': "clientSecret_example" // String | 
};
apiInstance.oAuthAuthorize(clientId, redirectUri, state, opts, (error, data, response) => {
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
 **clientId** | **String**|  | 
 **redirectUri** | **String**|  | 
 **state** | **String**|  | 
 **scope** | **String**|  | [optional] 
 **clientSecret** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

