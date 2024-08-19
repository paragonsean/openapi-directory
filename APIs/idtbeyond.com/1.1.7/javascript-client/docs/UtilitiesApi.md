# ActiveDocumentationForV1.UtilitiesApi

All URIs are relative to *https://api.idtbeyond.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iatuNumberValidatorGet**](UtilitiesApi.md#iatuNumberValidatorGet) | **GET** /iatu/number-validator | Mobile number validation
[**iatuProductsPromotionsGet**](UtilitiesApi.md#iatuProductsPromotionsGet) | **GET** /iatu/products/promotions | Current promotions
[**statusGet**](UtilitiesApi.md#statusGet) | **GET** /status | Status check



## iatuNumberValidatorGet

> iatuNumberValidatorGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, mobileNumber)

Mobile number validation

Checks to verify if the phone number is valid for the country supplied.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.UtilitiesApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
let countryCode = "'BR'"; // String | 2-digit code of the country in ISO 3166 format. 'BR'
let mobileNumber = "'5521983115555'"; // String | The mobile number you would like to validate. '5521983115555'
apiInstance.iatuNumberValidatorGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, mobileNumber, (error, data, response) => {
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
 **countryCode** | **String**| 2-digit code of the country in ISO 3166 format. &#39;BR&#39; | [default to &#39;BR&#39;]
 **mobileNumber** | **String**| The mobile number you would like to validate. &#39;5521983115555&#39; | [default to &#39;5521983115555&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## iatuProductsPromotionsGet

> iatuProductsPromotionsGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Current promotions

Returns a JSON of the current promotions.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.UtilitiesApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
apiInstance.iatuProductsPromotionsGet(xIdtBeyondAppId, xIdtBeyondAppKey, (error, data, response) => {
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


## statusGet

> statusGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Status check

Returns a JSON of the API status.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.UtilitiesApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
apiInstance.statusGet(xIdtBeyondAppId, xIdtBeyondAppKey, (error, data, response) => {
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

