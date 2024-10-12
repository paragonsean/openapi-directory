# MagentoB2B.DirectoryCurrencyApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet**](DirectoryCurrencyApi.md#directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet) | **GET** /V1/directory/currency | directory/currency



## directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet

> DirectoryDataCurrencyInformationInterface directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet()

directory/currency

Get currency information for the store.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.DirectoryCurrencyApi();
apiInstance.directoryCurrencyInformationAcquirerV1GetCurrencyInfoGet((error, data, response) => {
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

[**DirectoryDataCurrencyInformationInterface**](DirectoryDataCurrencyInformationInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

