# UebermapsApiEndpoints.AccountApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountPatch**](AccountApi.md#accountPatch) | **PATCH** /account | Update account



## accountPatch

> User accountPatch(opts)

Update account

Update account. Wrap map parameters in [user].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.AccountApi();
let opts = {
  'user': new UebermapsApiEndpoints.UserEditable() // UserEditable | user attributes
};
apiInstance.accountPatch(opts, (error, data, response) => {
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
 **user** | [**UserEditable**](UserEditable.md)| user attributes | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

