# NicAtDomainfinderApiDocumentation.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1SuggestGet**](DefaultApi.md#apiV1SuggestGet) | **GET** /api/v1/suggest | Get .at domain name suggestions



## apiV1SuggestGet

> ApiV1SuggestGet200Response apiV1SuggestGet(term)

Get .at domain name suggestions

Provides a list of available .at domain names related to the given input term or domain

### Example

```javascript
import NicAtDomainfinderApiDocumentation from 'nic_at_domainfinder_api_documentation';

let apiInstance = new NicAtDomainfinderApiDocumentation.DefaultApi();
let term = "mydomain"; // String | Domainname/term to obtain suggestions for
apiInstance.apiV1SuggestGet(term, (error, data, response) => {
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
 **term** | **String**| Domainname/term to obtain suggestions for | 

### Return type

[**ApiV1SuggestGet200Response**](ApiV1SuggestGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

