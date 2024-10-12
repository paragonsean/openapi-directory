# MagentoB2B.TaxRatesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxTaxRateRepositoryV1SavePost**](TaxRatesApi.md#taxTaxRateRepositoryV1SavePost) | **POST** /V1/taxRates | taxRates
[**taxTaxRateRepositoryV1SavePut**](TaxRatesApi.md#taxTaxRateRepositoryV1SavePut) | **PUT** /V1/taxRates | taxRates



## taxTaxRateRepositoryV1SavePost

> TaxDataTaxRateInterface taxTaxRateRepositoryV1SavePost(opts)

taxRates

Create or update tax rate

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRatesApi();
let opts = {
  'taxTaxRateRepositoryV1SavePutRequest': new MagentoB2B.TaxTaxRateRepositoryV1SavePutRequest() // TaxTaxRateRepositoryV1SavePutRequest | 
};
apiInstance.taxTaxRateRepositoryV1SavePost(opts, (error, data, response) => {
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
 **taxTaxRateRepositoryV1SavePutRequest** | [**TaxTaxRateRepositoryV1SavePutRequest**](TaxTaxRateRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**TaxDataTaxRateInterface**](TaxDataTaxRateInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## taxTaxRateRepositoryV1SavePut

> TaxDataTaxRateInterface taxTaxRateRepositoryV1SavePut(opts)

taxRates

Create or update tax rate

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRatesApi();
let opts = {
  'taxTaxRateRepositoryV1SavePutRequest': new MagentoB2B.TaxTaxRateRepositoryV1SavePutRequest() // TaxTaxRateRepositoryV1SavePutRequest | 
};
apiInstance.taxTaxRateRepositoryV1SavePut(opts, (error, data, response) => {
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
 **taxTaxRateRepositoryV1SavePutRequest** | [**TaxTaxRateRepositoryV1SavePutRequest**](TaxTaxRateRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**TaxDataTaxRateInterface**](TaxDataTaxRateInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

