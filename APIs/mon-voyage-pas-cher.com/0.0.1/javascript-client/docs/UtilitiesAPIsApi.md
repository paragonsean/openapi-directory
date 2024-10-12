# MonVoyagePasCherComPublicApi.UtilitiesAPIsApi

All URIs are relative to *https://api.mon-voyage-pas-cher.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPing**](UtilitiesAPIsApi.md#getPing) | **GET** /pong | 



## getPing

> PongResponse getPing()



Returns a ping. In case you need a health check in your system. Cannot be called /ping as AWS is using this route for their health check. This webservice doesn&#39;t have CORS enable, as it&#39;s supposed to be call server to server and not from a webpage ( it won&#39;t work over the tester)

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.UtilitiesAPIsApi();
apiInstance.getPing((error, data, response) => {
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

[**PongResponse**](PongResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

