# DeedApi.DefaultApi

All URIs are relative to *https://api.landregistry.gov.uk/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addDeed**](DefaultApi.md#addDeed) | **POST** /deed/ | Deed



## addDeed

> String addDeed(body)

Deed

The post Deed endpoint creates a new deed based on the JSON provided.  The reponse will return a URL that can retrieve the created deed.   &gt; REQUIRED: Land Registry system requests Conveyancer to confirm that the Borrowers identity has been established in accordance with Section 111 of the Network Access Agreement.

### Example

```javascript
import DeedApi from 'deed_api';

let apiInstance = new DeedApi.DefaultApi();
let body = new DeedApi.DeedApplication(); // DeedApplication | 
apiInstance.addDeed(body, (error, data, response) => {
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
 **body** | [**DeedApplication**](DeedApplication.md)|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain

