# SmartMe.AccessTokenApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accessTokenPut**](AccessTokenApi.md#accessTokenPut) | **PUT** /api/AccessToken | Creates a Access Token to write on a Card (e.g. NFC)



## accessTokenPut

> String accessTokenPut(accessTokenToPut)

Creates a Access Token to write on a Card (e.g. NFC)

Creates a Access Token to write on a Card (e.g. NFC)

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.AccessTokenApi();
let accessTokenToPut = new SmartMe.AccessTokenToPut(); // AccessTokenToPut | 
apiInstance.accessTokenPut(accessTokenToPut, (error, data, response) => {
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
 **accessTokenToPut** | [**AccessTokenToPut**](AccessTokenToPut.md)|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

