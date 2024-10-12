# MarketcheckApis.VINDecoderAPIApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decode**](VINDecoderAPIApi.md#decode) | **GET** /decode/car/{vin}/specs | VIN Decoder
[**decodeViaEPI**](VINDecoderAPIApi.md#decodeViaEPI) | **GET** /decode/car/epi/{vin}/specs | EPI VIN Decoder
[**decodeViaNeoVIN**](VINDecoderAPIApi.md#decodeViaNeoVIN) | **GET** /decode/car/neovin/{vin}/specs | NeoVIN Decoder
[**getTaxonomyTerms**](VINDecoderAPIApi.md#getTaxonomyTerms) | **GET** /specs/car/terms | API for getting terms from taxonomy
[**specsCarAutoCompleteGet**](VINDecoderAPIApi.md#specsCarAutoCompleteGet) | **GET** /specs/car/auto-complete | API for auto-completion of inputs based on taxonomy



## decode

> Build decode(vin, opts)

VIN Decoder

Get the basic information on specifications for a car identified by a valid VIN

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.VINDecoderAPIApi();
let vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.decode(vin, opts, (error, data, response) => {
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
 **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## decodeViaEPI

> Build decodeViaEPI(vin, opts)

EPI VIN Decoder

Get the basic information on specifications for a car identified by a valid VIN from EPI&#39;s decoder

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.VINDecoderAPIApi();
let vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.decodeViaEPI(vin, opts, (error, data, response) => {
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
 **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**Build**](Build.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## decodeViaNeoVIN

> NeoVIN decodeViaNeoVIN(vin, opts)

NeoVIN Decoder

Get the basic information on specifications for a car identified by a valid VIN from NeoVIN decoder

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.VINDecoderAPIApi();
let vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'includeGeneric': false, // Boolean | Boolean variable to indicate wheather to include generic data as well in response
  'forceDecode': false // Boolean | Decode VIN on the fly instead of cached response
};
apiInstance.decodeViaNeoVIN(vin, opts, (error, data, response) => {
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
 **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **includeGeneric** | **Boolean**| Boolean variable to indicate wheather to include generic data as well in response | [optional] [default to false]
 **forceDecode** | **Boolean**| Decode VIN on the fly instead of cached response | [optional] [default to false]

### Return type

[**NeoVIN**](NeoVIN.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTaxonomyTerms

> SpecsAutoCompleteResponse getTaxonomyTerms(field, opts)

API for getting terms from taxonomy

Facets on taxonomy

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.VINDecoderAPIApi();
let field = "field_example"; // String | Comma separated list of fields to get terms for
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineBlock': "engineBlock_example" // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
};
apiInstance.getTaxonomyTerms(field, opts, (error, data, response) => {
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
 **field** | **String**| Comma separated list of fields to get terms for | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 

### Return type

[**SpecsAutoCompleteResponse**](SpecsAutoCompleteResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## specsCarAutoCompleteGet

> SpecsAutoCompleteResponse specsCarAutoCompleteGet(field, input, opts)

API for auto-completion of inputs based on taxonomy

Auto-complete the inputs of your end users, not from active set but from taxonomy (decoder database)

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.VINDecoderAPIApi();
let field = "field_example"; // String | Field name for which you want auto-completion
let input = "input_example"; // String | Input entered so far
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'ignoreCase': true, // Boolean | Boolean variable to indicate ignore case of current input
  'facetMinCount': 1 // Number | Provide minimum count value for facets
};
apiInstance.specsCarAutoCompleteGet(field, input, opts, (error, data, response) => {
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
 **field** | **String**| Field name for which you want auto-completion | 
 **input** | **String**| Input entered so far | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **ignoreCase** | **Boolean**| Boolean variable to indicate ignore case of current input | [optional] [default to true]
 **facetMinCount** | **Number**| Provide minimum count value for facets | [optional] [default to 1]

### Return type

[**SpecsAutoCompleteResponse**](SpecsAutoCompleteResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

