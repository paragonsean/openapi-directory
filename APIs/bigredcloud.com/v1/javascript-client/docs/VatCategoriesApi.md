# BigRedCloudApi.VatCategoriesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vatCategoriesGet**](VatCategoriesApi.md#vatCategoriesGet) | **GET** /v1/vatCategories | Returns a list of global Vat Categories. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.
[**vatCategoriesProcessVatRates**](VatCategoriesApi.md#vatCategoriesProcessVatRates) | **POST** /v1/vatCategories/vatRates | Process Vat Rates



## vatCategoriesGet

> PageResultVatCategoryDto vatCategoriesGet()

Returns a list of global Vat Categories. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.VatCategoriesApi();
apiInstance.vatCategoriesGet((error, data, response) => {
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

[**PageResultVatCategoryDto**](PageResultVatCategoryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vatCategoriesProcessVatRates

> Object vatCategoriesProcessVatRates(vatRatesByVatCategoryDto)

Process Vat Rates

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.VatCategoriesApi();
let vatRatesByVatCategoryDto = [new BigRedCloudApi.VatRatesByVatCategoryDto()]; // [VatRatesByVatCategoryDto] | Array of Vat Rates.
apiInstance.vatCategoriesProcessVatRates(vatRatesByVatCategoryDto, (error, data, response) => {
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
 **vatRatesByVatCategoryDto** | [**[VatRatesByVatCategoryDto]**](VatRatesByVatCategoryDto.md)| Array of Vat Rates. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

