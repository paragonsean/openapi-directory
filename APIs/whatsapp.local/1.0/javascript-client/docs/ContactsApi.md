# WhatsAppBusinessApi.ContactsApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkContact**](ContactsApi.md#checkContact) | **POST** /contacts | Check-Contact



## checkContact

> CheckContactResponse checkContact(checkContactRequestBody)

Check-Contact

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.ContactsApi();
let checkContactRequestBody = {"blocking":"wait","contacts":["{{Recipient-WA-ID}}"]}; // CheckContactRequestBody | 
apiInstance.checkContact(checkContactRequestBody, (error, data, response) => {
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
 **checkContactRequestBody** | [**CheckContactRequestBody**](CheckContactRequestBody.md)|  | 

### Return type

[**CheckContactResponse**](CheckContactResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

