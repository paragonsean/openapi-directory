# GoogleHome.StaticFilesApi

All URIs are relative to *http://example.com/setup*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chromecastIcon**](StaticFilesApi.md#chromecastIcon) | **GET** /icon.png | Chromecast Icon
[**legalNotice**](StaticFilesApi.md#legalNotice) | **GET** /NOTICE.html.gz | Legal Notice



## chromecastIcon

> chromecastIcon()

Chromecast Icon

**Update:** This no longer exists. It&#39;s not useful, anyway.  A redirect to &#x60;http://www.gstatic.com/eureka/images/eureka_device.png&#x60;

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.StaticFilesApi();
apiInstance.chromecastIcon((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## legalNotice

> String legalNotice()

Legal Notice

All licenses of programs used by Home.

### Example

```javascript
import GoogleHome from 'google_home';
let defaultClient = GoogleHome.ApiClient.instance;
// Configure API key authorization: cast-local-authorization-token
let cast-local-authorization-token = defaultClient.authentications['cast-local-authorization-token'];
cast-local-authorization-token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cast-local-authorization-token.apiKeyPrefix = 'Token';

let apiInstance = new GoogleHome.StaticFilesApi();
apiInstance.legalNotice((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

