# SendPersonToMerchant.DigitalAccountReferenceNumberApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDigitalAccntRefNum**](DigitalAccountReferenceNumberApi.md#createDigitalAccntRefNum) | **POST** /send/v1/{partnerId}/digital-account | Used to create a digital account reference number from Incontrol 



## createDigitalAccntRefNum

> DigitalAccount87Wrapper createDigitalAccntRefNum(partnerId, opts)

Used to create a digital account reference number from Incontrol 

Used to create a digital account reference number from Incontrol 

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.DigitalAccountReferenceNumberApi();
let partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32
let opts = {
  'digitalAccount': new SendPersonToMerchant.DigitalAccount86Wrapper() // DigitalAccount86Wrapper | Contains the details of the request message.
};
apiInstance.createDigitalAccntRefNum(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32 | 
 **digitalAccount** | [**DigitalAccount86Wrapper**](DigitalAccount86Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**DigitalAccount87Wrapper**](DigitalAccount87Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

