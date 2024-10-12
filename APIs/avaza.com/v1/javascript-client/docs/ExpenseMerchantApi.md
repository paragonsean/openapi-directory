# AvazaApiDocumentation.ExpenseMerchantApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseMerchangeLookup**](ExpenseMerchantApi.md#expenseMerchangeLookup) | **GET** /api/ExpenseMerchant/Lookup | Gets minimal list of Expense Merchants.



## expenseMerchangeLookup

> ExpenseMerchantDropdownList expenseMerchangeLookup(opts)

Gets minimal list of Expense Merchants.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseMerchantApi();
let opts = {
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'search': "search_example" // String | Search string to match against Expense Group Name
};
apiInstance.expenseMerchangeLookup(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **search** | **String**| Search string to match against Expense Group Name | [optional] 

### Return type

[**ExpenseMerchantDropdownList**](ExpenseMerchantDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

