# Miataru.GetVisitorHistoryApi

All URIs are relative to *http://service.miataru.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVisitorHistory**](GetVisitorHistoryApi.md#getVisitorHistory) | **POST** /GetVisitorHistory | 



## getVisitorHistory

> MiataruGetVisitorHistoryResponse getVisitorHistory(body)



Visitor History is stored on the server with every request to the location or location history information of a device. There is a server-side setting that controls up to how many Visitors the server is storing in the Visitor History before it removes the oldest one. To request the Visitor History of a particular device the client sends the following POST request to the GetVisitorHistory service URL.

### Example

```javascript
import Miataru from 'miataru';

let apiInstance = new Miataru.GetVisitorHistoryApi();
let body = new Miataru.MiataruGetVisitorHistoryRequest(); // MiataruGetVisitorHistoryRequest | the complex JSON formatted datastructure to get the visitor history of one device
apiInstance.getVisitorHistory(body, (error, data, response) => {
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
 **body** | [**MiataruGetVisitorHistoryRequest**](MiataruGetVisitorHistoryRequest.md)| the complex JSON formatted datastructure to get the visitor history of one device | 

### Return type

[**MiataruGetVisitorHistoryResponse**](MiataruGetVisitorHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

