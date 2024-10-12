# ApiISendPro.AddShortlinkApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addShortlink**](AddShortlinkApi.md#addShortlink) | **POST** /shortlink | add a shortlink



## addShortlink

> ShortlinkResponse addShortlink(shortlinkRequest)

add a shortlink

add a shortlink

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.AddShortlinkApi();
let shortlinkRequest = new ApiISendPro.ShortlinkRequest(); // ShortlinkRequest | add sub account request
apiInstance.addShortlink(shortlinkRequest, (error, data, response) => {
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
 **shortlinkRequest** | [**ShortlinkRequest**](ShortlinkRequest.md)| add sub account request | 

### Return type

[**ShortlinkResponse**](ShortlinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, exemple1

