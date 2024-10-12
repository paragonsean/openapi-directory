# MessageCenterApi.DKIMConfigurationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDKIM**](DKIMConfigurationApi.md#createDKIM) | **POST** /api/mail-service/pvt/providers/{EmailProvider}/dkim | Generate DKIM keys



## createDKIM

> Model200OK createDKIM(emailProvider)

Generate DKIM keys

Create DKIM keys for sender that was setup in VTEX mail servers

### Example

```javascript
import MessageCenterApi from 'message_center_api';
let defaultClient = MessageCenterApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new MessageCenterApi.DKIMConfigurationApi();
let emailProvider = "'help@valdie.co'"; // String | E-mail address for sender that was setup in VTEX mail servers
apiInstance.createDKIM(emailProvider, (error, data, response) => {
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
 **emailProvider** | **String**| E-mail address for sender that was setup in VTEX mail servers | [default to &#39;help@valdie.co&#39;]

### Return type

[**Model200OK**](Model200OK.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

