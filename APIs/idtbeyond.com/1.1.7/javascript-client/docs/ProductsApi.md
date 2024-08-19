# ActiveDocumentationForV1.ProductsApi

All URIs are relative to *https://api.idtbeyond.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iatuProductsReportsAllCsvGet**](ProductsApi.md#iatuProductsReportsAllCsvGet) | **GET** /iatu/products/reports/all.csv | Get a list of products in CSV format
[**iatuProductsReportsAllGet**](ProductsApi.md#iatuProductsReportsAllGet) | **GET** /iatu/products/reports/all | Get a list of products in JSON format
[**iatuProductsReportsLocalValueGet**](ProductsApi.md#iatuProductsReportsLocalValueGet) | **GET** /iatu/products/reports/local-value | Get the estimated Local Value of a product



## iatuProductsReportsAllCsvGet

> iatuProductsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Get a list of products in CSV format

Returns a CSV of products, ranges, and their commissions percentages.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.ProductsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
apiInstance.iatuProductsReportsAllCsvGet(xIdtBeyondAppId, xIdtBeyondAppKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## iatuProductsReportsAllGet

> iatuProductsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Get a list of products in JSON format

Returns a JSON list of products, ranges, and their commissions percentages.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.ProductsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
apiInstance.iatuProductsReportsAllGet(xIdtBeyondAppId, xIdtBeyondAppKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## iatuProductsReportsLocalValueGet

> iatuProductsReportsLocalValueGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, carrierCode, amount, currencyCode)

Get the estimated Local Value of a product

Returns a CSV of products, ranges, and their commissions percentages.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.ProductsApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let countryCode = "'GT'"; // String | 2-digit code of the country in ISO 3166 format. 'GT'
let carrierCode = "'Claro'"; // String | Name of the mobile carrier. 'Claro'
let amount = 500; // Number | This is the amount, in cents, of the product you are purchasing. '500' = $5.00
let currencyCode = "'USD'"; // String | The currency code (ISO 4217) on the product you are querying. 'USD'
apiInstance.iatuProductsReportsLocalValueGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, carrierCode, amount, currencyCode, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]
 **countryCode** | **String**| 2-digit code of the country in ISO 3166 format. &#39;GT&#39; | [default to &#39;GT&#39;]
 **carrierCode** | **String**| Name of the mobile carrier. &#39;Claro&#39; | [default to &#39;Claro&#39;]
 **amount** | **Number**| This is the amount, in cents, of the product you are purchasing. &#39;500&#39; &#x3D; $5.00 | [default to 500]
 **currencyCode** | **String**| The currency code (ISO 4217) on the product you are querying. &#39;USD&#39; | [default to &#39;USD&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

