# SendPersonToMerchant.DigitalAccountReferenceNumberRetrievalApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveDigitalAccntRefNumList**](DigitalAccountReferenceNumberRetrievalApi.md#retrieveDigitalAccntRefNumList) | **POST** /send/v1/{partnerId}/digital-account/search | Used to retreive a digital account reference list from Incontrol 



## retrieveDigitalAccntRefNumList

> DigitalAccount90Wrapper retrieveDigitalAccntRefNumList(partnerId, opts)

Used to retreive a digital account reference list from Incontrol 

Used to retreive a digital account reference list from Incontrol 

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.DigitalAccountReferenceNumberRetrievalApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let opts = {
  'digitalAccount': new SendPersonToMerchant.DigitalAccount89Wrapper() // DigitalAccount89Wrapper | Contains the details of the request message.
};
apiInstance.retrieveDigitalAccntRefNumList(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | 
 **digitalAccount** | [**DigitalAccount89Wrapper**](DigitalAccount89Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**DigitalAccount90Wrapper**](DigitalAccount90Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

