# AvazaApiDocumentation.ExpenseCategoryApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseCategoryGet**](ExpenseCategoryApi.md#expenseCategoryGet) | **GET** /api/ExpenseCategory | Gets list of Expense Categories



## expenseCategoryGet

> ExpenseCategoryList expenseCategoryGet(opts)

Gets list of Expense Categories

The default sort order is by Name asc

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.ExpenseCategoryApi();
let opts = {
  'isEnabled': true // Boolean | Optional filter on for enabled/disabled categories. Defaults to true.
};
apiInstance.expenseCategoryGet(opts, (error, data, response) => {
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
 **isEnabled** | **Boolean**| Optional filter on for enabled/disabled categories. Defaults to true. | [optional] 

### Return type

[**ExpenseCategoryList**](ExpenseCategoryList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

