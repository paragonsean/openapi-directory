# BusinessRegistries.RolesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classificationsRolesGet**](RolesApi.md#classificationsRolesGet) | **GET** /classifications/roles | Retrieve a list of roles



## classificationsRolesGet

> [Role] classificationsRolesGet(apiKey)

Retrieve a list of roles

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.RolesApi();
let apiKey = "apiKey_example"; // String | The API key.
apiInstance.classificationsRolesGet(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 

### Return type

[**[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

