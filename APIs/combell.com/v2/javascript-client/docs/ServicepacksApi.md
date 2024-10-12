# PublicApi.ServicepacksApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicepacks**](ServicepacksApi.md#servicepacks) | **GET** /servicepacks | Overview of service packs



## servicepacks

> [Servicepack] servicepacks()

Overview of service packs

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.ServicepacksApi();
apiInstance.servicepacks((error, data, response) => {
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

[**[Servicepack]**](Servicepack.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

