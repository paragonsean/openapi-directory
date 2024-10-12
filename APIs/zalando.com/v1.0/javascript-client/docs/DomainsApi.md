# ZalandoShop.DomainsApi

All URIs are relative to *https://api.zalando.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domainsGet**](DomainsApi.md#domainsGet) | **GET** /domains | Shop Domains



## domainsGet

> [Domain] domainsGet()

Shop Domains

Zalando API Domains Schema

### Example

```javascript
import ZalandoShop from 'zalando_shop';

let apiInstance = new ZalandoShop.DomainsApi();
apiInstance.domainsGet((error, data, response) => {
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

[**[Domain]**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

