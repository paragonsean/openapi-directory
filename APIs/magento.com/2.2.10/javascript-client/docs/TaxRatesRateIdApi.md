# MagentoB2B.TaxRatesRateIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxTaxRateRepositoryV1DeleteByIdDelete**](TaxRatesRateIdApi.md#taxTaxRateRepositoryV1DeleteByIdDelete) | **DELETE** /V1/taxRates/{rateId} | taxRates/{rateId}
[**taxTaxRateRepositoryV1GetGet**](TaxRatesRateIdApi.md#taxTaxRateRepositoryV1GetGet) | **GET** /V1/taxRates/{rateId} | taxRates/{rateId}



## taxTaxRateRepositoryV1DeleteByIdDelete

> Boolean taxTaxRateRepositoryV1DeleteByIdDelete(rateId)

taxRates/{rateId}

Delete tax rate

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRatesRateIdApi();
let rateId = 56; // Number | 
apiInstance.taxTaxRateRepositoryV1DeleteByIdDelete(rateId, (error, data, response) => {
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
 **rateId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## taxTaxRateRepositoryV1GetGet

> TaxDataTaxRateInterface taxTaxRateRepositoryV1GetGet(rateId)

taxRates/{rateId}

Get tax rate

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxRatesRateIdApi();
let rateId = 56; // Number | 
apiInstance.taxTaxRateRepositoryV1GetGet(rateId, (error, data, response) => {
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
 **rateId** | **Number**|  | 

### Return type

[**TaxDataTaxRateInterface**](TaxDataTaxRateInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

