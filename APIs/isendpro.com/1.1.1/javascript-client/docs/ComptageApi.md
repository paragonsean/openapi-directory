# ApiISendPro.ComptageApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comptage**](ComptageApi.md#comptage) | **POST** /comptage | Compter le nombre de caractère 



## comptage

> ComptageReponse comptage(comptageRequest)

Compter le nombre de caractère 

Compte le nombre de SMS necessaire à un envoi

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.ComptageApi();
let comptageRequest = new ApiISendPro.ComptageRequest(); // ComptageRequest | sms request
apiInstance.comptage(comptageRequest, (error, data, response) => {
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
 **comptageRequest** | [**ComptageRequest**](ComptageRequest.md)| sms request | 

### Return type

[**ComptageReponse**](ComptageReponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, etat

