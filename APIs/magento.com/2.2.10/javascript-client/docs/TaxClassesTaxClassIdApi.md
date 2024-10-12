# MagentoB2B.TaxClassesTaxClassIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxTaxClassRepositoryV1DeleteByIdDelete**](TaxClassesTaxClassIdApi.md#taxTaxClassRepositoryV1DeleteByIdDelete) | **DELETE** /V1/taxClasses/{taxClassId} | taxClasses/{taxClassId}
[**taxTaxClassRepositoryV1GetGet**](TaxClassesTaxClassIdApi.md#taxTaxClassRepositoryV1GetGet) | **GET** /V1/taxClasses/{taxClassId} | taxClasses/{taxClassId}



## taxTaxClassRepositoryV1DeleteByIdDelete

> Boolean taxTaxClassRepositoryV1DeleteByIdDelete(taxClassId)

taxClasses/{taxClassId}

Delete a tax class with the given tax class id.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxClassesTaxClassIdApi();
let taxClassId = 56; // Number | 
apiInstance.taxTaxClassRepositoryV1DeleteByIdDelete(taxClassId, (error, data, response) => {
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
 **taxClassId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## taxTaxClassRepositoryV1GetGet

> TaxDataTaxClassInterface taxTaxClassRepositoryV1GetGet(taxClassId)

taxClasses/{taxClassId}

Get a tax class with the given tax class id.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TaxClassesTaxClassIdApi();
let taxClassId = 56; // Number | 
apiInstance.taxTaxClassRepositoryV1GetGet(taxClassId, (error, data, response) => {
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
 **taxClassId** | **Number**|  | 

### Return type

[**TaxDataTaxClassInterface**](TaxDataTaxClassInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

