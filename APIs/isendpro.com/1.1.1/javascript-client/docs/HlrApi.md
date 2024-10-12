# ApiISendPro.HlrApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHlr**](HlrApi.md#getHlr) | **POST** /hlr | Vérifier la validité d&#39;un numéro



## getHlr

> HLRReponse getHlr(hLRrequest)

Vérifier la validité d&#39;un numéro

Réalise un lookup HLR sur les numéros  

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.HlrApi();
let hLRrequest = new ApiISendPro.HLRrequest(); // HLRrequest | 
apiInstance.getHlr(hLRrequest, (error, data, response) => {
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
 **hLRrequest** | [**HLRrequest**](HLRrequest.md)|  | 

### Return type

[**HLRReponse**](HLRReponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

