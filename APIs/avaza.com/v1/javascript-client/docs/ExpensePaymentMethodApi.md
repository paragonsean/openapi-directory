# AvazaApiDocumentation.ExpensePaymentMethodApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expensePaymentMethodLookup**](ExpensePaymentMethodApi.md#expensePaymentMethodLookup) | **GET** /api/ExpensePaymentMethod/Lookup | Gets minimal list of Expense Payment Methods.



## expensePaymentMethodLookup

> ExpensePaymentMethodDropdownList expensePaymentMethodLookup()

Gets minimal list of Expense Payment Methods.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpensePaymentMethodApi();
apiInstance.expensePaymentMethodLookup((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ExpensePaymentMethodDropdownList**](ExpensePaymentMethodDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

