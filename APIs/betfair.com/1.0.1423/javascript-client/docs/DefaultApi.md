# BetfairExchangeStreamingApi.DefaultApi

All URIs are relative to *http://stream-api.betfair.com:443/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestPost**](DefaultApi.md#requestPost) | **POST** /request | 



## requestPost

> AllResponseTypesExample requestPost(allRequestTypesExample)



This is a socket protocol delimited by CRLF (not http)

### Example

```javascript
import BetfairExchangeStreamingApi from 'betfair_exchange_streaming_api';

let apiInstance = new BetfairExchangeStreamingApi.DefaultApi();
let allRequestTypesExample = new BetfairExchangeStreamingApi.AllRequestTypesExample(); // AllRequestTypesExample | Requests are sent to socket
apiInstance.requestPost(allRequestTypesExample, (error, data, response) => {
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
 **allRequestTypesExample** | [**AllRequestTypesExample**](AllRequestTypesExample.md)| Requests are sent to socket | 

### Return type

[**AllResponseTypesExample**](AllResponseTypesExample.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

