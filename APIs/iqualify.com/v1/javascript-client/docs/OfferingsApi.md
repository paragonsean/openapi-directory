# IQualifyManagementApi.OfferingsApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsCurrentGet**](OfferingsApi.md#offeringsCurrentGet) | **GET** /offerings/current | Find active offerings
[**offeringsFutureGet**](OfferingsApi.md#offeringsFutureGet) | **GET** /offerings/future | Find scheduled offerings
[**offeringsGet**](OfferingsApi.md#offeringsGet) | **GET** /offerings | Find current, past and future offerings
[**offeringsInfoTextPatternGet**](OfferingsApi.md#offeringsInfoTextPatternGet) | **GET** /offerings/info/{textPattern} | Find offerings where info field matches the specified textPattern
[**offeringsOfferingIdGet**](OfferingsApi.md#offeringsOfferingIdGet) | **GET** /offerings/{offeringId} | Find offering by ID
[**offeringsOfferingIdPatch**](OfferingsApi.md#offeringsOfferingIdPatch) | **PATCH** /offerings/{offeringId} | Update offering
[**offeringsPastGet**](OfferingsApi.md#offeringsPastGet) | **GET** /offerings/past | Find past offerings
[**offeringsPost**](OfferingsApi.md#offeringsPost) | **POST** /offerings | Create offering
[**offeringsSummaryGet**](OfferingsApi.md#offeringsSummaryGet) | **GET** /offerings/summary | Offerings summary



## offeringsCurrentGet

> [OfferingMetadataResponse] offeringsCurrentGet()

Find active offerings

Responds with active offerings for your organisation.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
apiInstance.offeringsCurrentGet((error, data, response) => {
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

[**[OfferingMetadataResponse]**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsFutureGet

> [OfferingMetadataResponse] offeringsFutureGet()

Find scheduled offerings

Responds with scheduled offerings for your organisation. Scheduled offerings have a start date after today&#39;s date (inclusive).

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
apiInstance.offeringsFutureGet((error, data, response) => {
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

[**[OfferingMetadataResponse]**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsGet

> [OfferingMetadataResponse] offeringsGet()

Find current, past and future offerings

Responds with all offerings for your organisation.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
apiInstance.offeringsGet((error, data, response) => {
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

[**[OfferingMetadataResponse]**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsInfoTextPatternGet

> [PortfolioActivations] offeringsInfoTextPatternGet(textPattern)

Find offerings where info field matches the specified textPattern

Find offerings where info field matches the specified text pattern.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
let textPattern = "textPattern_example"; // String | Text pattern to search for (minimum of 3 characters length).
apiInstance.offeringsInfoTextPatternGet(textPattern, (error, data, response) => {
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
 **textPattern** | **String**| Text pattern to search for (minimum of 3 characters length). | 

### Return type

[**[PortfolioActivations]**](PortfolioActivations.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdGet

> OfferingMetadataResponse offeringsOfferingIdGet(offeringId)

Find offering by ID

Responds with an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdGet(offeringId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdPatch

> OfferingMetadataResponse offeringsOfferingIdPatch(offeringId, offering)

Update offering

Updates the offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
let offeringId = "offeringId_example"; // String | offering's id
let offering = new IQualifyManagementApi.Offering(); // Offering | 
apiInstance.offeringsOfferingIdPatch(offeringId, offering, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **offering** | [**Offering**](Offering.md)|  | 

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsPastGet

> [OfferingMetadataResponse] offeringsPastGet()

Find past offerings

Responds with past offerings for your organisation.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
apiInstance.offeringsPastGet((error, data, response) => {
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

[**[OfferingMetadataResponse]**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsPost

> OfferingMetadataResponse offeringsPost(offeringRequired)

Create offering

Creates a new offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
let offeringRequired = new IQualifyManagementApi.OfferingRequired(); // OfferingRequired | 
apiInstance.offeringsPost(offeringRequired, (error, data, response) => {
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
 **offeringRequired** | [**OfferingRequired**](OfferingRequired.md)|  | 

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsSummaryGet

> [PortfolioActivations] offeringsSummaryGet(opts)

Offerings summary

Responds with a summary of all offerings for your organisation.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingsApi();
let opts = {
  'top': "'50'", // String | Returns only the first n results.
  'orderby': "orderby_example", // String | Sorts the results.
  'filter': "filter_example" // String | Filters the results, based on a Boolean condition.
};
apiInstance.offeringsSummaryGet(opts, (error, data, response) => {
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
 **top** | **String**| Returns only the first n results. | [optional] [default to &#39;50&#39;]
 **orderby** | **String**| Sorts the results. | [optional] 
 **filter** | **String**| Filters the results, based on a Boolean condition. | [optional] 

### Return type

[**[PortfolioActivations]**](PortfolioActivations.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

