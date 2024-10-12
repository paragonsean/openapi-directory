# ApiISendPro.CreditApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCredit**](CreditApi.md#getCredit) | **GET** /credit | Interrogation credit



## getCredit

> CreditResponse getCredit(keyid, credit)

Interrogation credit

Retourne le credit existant associe au compte. 

### Example

```javascript
import ApiISendPro from 'api_i_send_pro';

let apiInstance = new ApiISendPro.CreditApi();
let keyid = "keyid_example"; // String | Clé API
let credit = "credit_example"; // String | Type de reponse demandée, 1 pour euro, 2 pour euro + estimation quantité
apiInstance.getCredit(keyid, credit, (error, data, response) => {
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
 **keyid** | **String**| Clé API | 
 **credit** | **String**| Type de reponse demandée, 1 pour euro, 2 pour euro + estimation quantité | 

### Return type

[**CreditResponse**](CreditResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

