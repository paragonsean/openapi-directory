# ZipCodeDataApi.DefaultApi

All URIs are relative to *https://global.metadapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistance**](DefaultApi.md#getDistance) | **GET** /zipc/v1/distance | Distance Between 2 Zip Codes
[**getMsagroups**](DefaultApi.md#getMsagroups) | **GET** /zipc/v1/msagroups | List All MSA Groups
[**getMsagroupsMsacode**](DefaultApi.md#getMsagroupsMsacode) | **GET** /zipc/v1/msagroups/{msaCode} | Metro/Micro Statistical Area Details
[**getRadius**](DefaultApi.md#getRadius) | **GET** /zipc/v1/radius | Zip Code Radius
[**getZipcV1**](DefaultApi.md#getZipcV1) | **GET** /zipc/v1 | Validate License Key
[**getZipcode**](DefaultApi.md#getZipcode) | **GET** /zipc/v1/zipcodes/{zipcode} | Zip Code Details
[**getZipcodes**](DefaultApi.md#getZipcodes) | **GET** /zipc/v1/zipcodes | List all Zip Codes



## getDistance

> GetDistance200Response getDistance(zipCode1, zipCode2)

Distance Between 2 Zip Codes

Gets the distance (in miles and kilometers) between 2 zip codes passed as parameters. There are 2 mandatory query parameters (zipCode1 and zipCode2). 

### Example

```javascript
import ZipCodeDataApi from 'zip_code_data_api';
let defaultClient = ZipCodeDataApi.ApiClient.instance;
// Configure API key authorization: subscription-key
let subscription-key = defaultClient.authentications['subscription-key'];
subscription-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//subscription-key.apiKeyPrefix = 'Token';

let apiInstance = new ZipCodeDataApi.DefaultApi();
let zipCode1 = "90210"; // String | Zip Code 1
let zipCode2 = "33162"; // String | Zip Code 2
apiInstance.getDistance(zipCode1, zipCode2, (error, data, response) => {
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
 **zipCode1** | **String**| Zip Code 1 | 
 **zipCode2** | **String**| Zip Code 2 | 

### Return type

[**GetDistance200Response**](GetDistance200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMsagroups

> GetMsagroups200Response getMsagroups(limit, offset, opts)

List All MSA Groups

This end point lists all the Metropolitan and Micropolitan Statistical Areas in the United States with the corresponding states and counties that make up the group. 

### Example

```javascript
import ZipCodeDataApi from 'zip_code_data_api';
let defaultClient = ZipCodeDataApi.ApiClient.instance;
// Configure API key authorization: subscription-key
let subscription-key = defaultClient.authentications['subscription-key'];
subscription-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//subscription-key.apiKeyPrefix = 'Token';

let apiInstance = new ZipCodeDataApi.DefaultApi();
let limit = 56; // Number | Number of records to return in each page. Max value: 50.
let offset = 56; // Number | Offset is the position in the dataset to start retrieval of records.
let opts = {
  'stateCode': "CA" // String | Parameter for state code.
};
apiInstance.getMsagroups(limit, offset, opts, (error, data, response) => {
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
 **limit** | **Number**| Number of records to return in each page. Max value: 50. | 
 **offset** | **Number**| Offset is the position in the dataset to start retrieval of records. | 
 **stateCode** | **String**| Parameter for state code. | [optional] 

### Return type

[**GetMsagroups200Response**](GetMsagroups200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMsagroupsMsacode

> GetMsagroupsMsacode200Response getMsagroupsMsacode(msaCode)

Metro/Micro Statistical Area Details

Gets the details of a single Metropolitan Statistical Area code passed as a path parameter.

### Example

```javascript
import ZipCodeDataApi from 'zip_code_data_api';
let defaultClient = ZipCodeDataApi.ApiClient.instance;
// Configure API key authorization: subscription-key
let subscription-key = defaultClient.authentications['subscription-key'];
subscription-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//subscription-key.apiKeyPrefix = 'Token';

let apiInstance = new ZipCodeDataApi.DefaultApi();
let msaCode = "11580"; // String | 5 digit MSA (Metropolitan Statistical Area) code.
apiInstance.getMsagroupsMsacode(msaCode, (error, data, response) => {
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
 **msaCode** | **String**| 5 digit MSA (Metropolitan Statistical Area) code. | 

### Return type

[**GetMsagroupsMsacode200Response**](GetMsagroupsMsacode200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRadius

> GetRadius200Response getRadius(zipCode, radius, uom)

Zip Code Radius

Endpoint that returns the zip codes that fall within the specified radius of another zip code. The returned zip codes are sorted by distance.

### Example

```javascript
import ZipCodeDataApi from 'zip_code_data_api';
let defaultClient = ZipCodeDataApi.ApiClient.instance;
// Configure API key authorization: subscription-key
let subscription-key = defaultClient.authentications['subscription-key'];
subscription-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//subscription-key.apiKeyPrefix = 'Token';

let apiInstance = new ZipCodeDataApi.DefaultApi();
let zipCode = "zipCode_example"; // String | 5 Digit US Zip Code
let radius = 56; // Number | Radius distance.  Max 322 km or 200 mi
let uom = "mi"; // String | Unit of Measure
apiInstance.getRadius(zipCode, radius, uom, (error, data, response) => {
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
 **zipCode** | **String**| 5 Digit US Zip Code | 
 **radius** | **Number**| Radius distance.  Max 322 km or 200 mi | 
 **uom** | **String**| Unit of Measure | 

### Return type

[**GetRadius200Response**](GetRadius200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getZipcV1

> getZipcV1()

Validate License Key

Endpoint used to validate license key only. Returns 204 on Success

### Example

```javascript
import ZipCodeDataApi from 'zip_code_data_api';
let defaultClient = ZipCodeDataApi.ApiClient.instance;
// Configure API key authorization: subscription-key
let subscription-key = defaultClient.authentications['subscription-key'];
subscription-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//subscription-key.apiKeyPrefix = 'Token';

let apiInstance = new ZipCodeDataApi.DefaultApi();
apiInstance.getZipcV1((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getZipcode

> GetZipcode200Response getZipcode(zipcode)

Zip Code Details

Gets the details of a single Zip code. 

### Example

```javascript
import ZipCodeDataApi from 'zip_code_data_api';
let defaultClient = ZipCodeDataApi.ApiClient.instance;
// Configure API key authorization: subscription-key
let subscription-key = defaultClient.authentications['subscription-key'];
subscription-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//subscription-key.apiKeyPrefix = 'Token';

let apiInstance = new ZipCodeDataApi.DefaultApi();
let zipcode = "zipcode_example"; // String | 5 Digit US Zip Code
apiInstance.getZipcode(zipcode, (error, data, response) => {
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
 **zipcode** | **String**| 5 Digit US Zip Code | 

### Return type

[**GetZipcode200Response**](GetZipcode200Response.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getZipcodes

> ZipCodeResponse getZipcodes(opts)

List all Zip Codes

Returns a list of zip codes. Results are always paginated. Visit the [Zip Code Data API](https://www.metadapi.com/API-Products/API-Product-Details/zip-code-api) product page for information on how to get an API key.

### Example

```javascript
import ZipCodeDataApi from 'zip_code_data_api';
let defaultClient = ZipCodeDataApi.ApiClient.instance;
// Configure API key authorization: subscription-key
let subscription-key = defaultClient.authentications['subscription-key'];
subscription-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//subscription-key.apiKeyPrefix = 'Token';

let apiInstance = new ZipCodeDataApi.DefaultApi();
let opts = {
  'offset': 10, // Number | Offset is the position in the dataset to start retrieval of records.
  'limit': 10, // Number | Number of records to return in each page.
  'zipcode': "90210,33162", // String | 5 Digit Zip Code query parameter. Can have multiple values (separated by comma).
  'uspsMainCityKey': "Z20259", // String | Parameter for USPS City / Town key identifier for the main city of the zip code.
  'zipClassificationCode': "P", // String | Parameter for zipClassificationCode
  'uspsFacilityCode': "B", // String | Parameter for facility code.
  'uspsDeliveryCode': "uspsDeliveryCode_example", // String | Parameter for delivery code.
  'uspsCarrierRouteSortCode': "uspsCarrierRouteSortCode_example", // String | Parameter for carrier route sort code.
  'uniqueZipNameInd': true, // Boolean | Parameter for unique zip name indicator.
  'uspsFinanceNumber': "uspsFinanceNumber_example", // String | Parameter for finance number.
  'stateCode': "CA", // String | Parameter for state code.
  'stateFipsCode': "06", // String | Parameter for State FIPS code.
  'countyFipsCode': "037", // String | Parameter for county FIPS code.
  'divisionCode': "9", // String | Parameter for division code. 
  'regionCode': "4", // String | Parameter for region code. 
  'msaCode': "31080" // String | Parameter for msaCode.
};
apiInstance.getZipcodes(opts, (error, data, response) => {
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
 **offset** | **Number**| Offset is the position in the dataset to start retrieval of records. | [optional] 
 **limit** | **Number**| Number of records to return in each page. | [optional] 
 **zipcode** | **String**| 5 Digit Zip Code query parameter. Can have multiple values (separated by comma). | [optional] 
 **uspsMainCityKey** | **String**| Parameter for USPS City / Town key identifier for the main city of the zip code. | [optional] 
 **zipClassificationCode** | **String**| Parameter for zipClassificationCode | [optional] 
 **uspsFacilityCode** | **String**| Parameter for facility code. | [optional] 
 **uspsDeliveryCode** | **String**| Parameter for delivery code. | [optional] 
 **uspsCarrierRouteSortCode** | **String**| Parameter for carrier route sort code. | [optional] 
 **uniqueZipNameInd** | **Boolean**| Parameter for unique zip name indicator. | [optional] 
 **uspsFinanceNumber** | **String**| Parameter for finance number. | [optional] 
 **stateCode** | **String**| Parameter for state code. | [optional] 
 **stateFipsCode** | **String**| Parameter for State FIPS code. | [optional] 
 **countyFipsCode** | **String**| Parameter for county FIPS code. | [optional] 
 **divisionCode** | **String**| Parameter for division code.  | [optional] 
 **regionCode** | **String**| Parameter for region code.  | [optional] 
 **msaCode** | **String**| Parameter for msaCode. | [optional] 

### Return type

[**ZipCodeResponse**](ZipCodeResponse.md)

### Authorization

[subscription-key](../README.md#subscription-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

