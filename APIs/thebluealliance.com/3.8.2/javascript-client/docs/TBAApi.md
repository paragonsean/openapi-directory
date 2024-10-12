# TheBlueAllianceApiV3.TBAApi

All URIs are relative to *https://www.thebluealliance.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatus**](TBAApi.md#getStatus) | **GET** /status | 



## getStatus

> APIStatus getStatus(opts)



Returns API status, and TBA status information.

### Example

```javascript
import TheBlueAllianceApiV3 from 'the_blue_alliance_api_v3';
let defaultClient = TheBlueAllianceApiV3.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new TheBlueAllianceApiV3.TBAApi();
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | Value of the `ETag` header in the most recently cached response by the client.
};
apiInstance.getStatus(opts, (error, data, response) => {
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
 **ifNoneMatch** | **String**| Value of the &#x60;ETag&#x60; header in the most recently cached response by the client. | [optional] 

### Return type

[**APIStatus**](APIStatus.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

