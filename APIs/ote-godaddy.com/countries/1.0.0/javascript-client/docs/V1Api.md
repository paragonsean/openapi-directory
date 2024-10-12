# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCountries**](V1Api.md#getCountries) | **GET** /v1/countries | Retrieves summary country information for the provided marketId and filters
[**getCountry**](V1Api.md#getCountry) | **GET** /v1/countries/{countryKey} | Retrieves country and summary state information for provided countryKey



## getCountries

> [CountrySummary] getCountries(marketId, opts)

Retrieves summary country information for the provided marketId and filters

Authorization is not required

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let marketId = "marketId_example"; // String | MarketId in which the request is being made, and for which responses should be localized
let opts = {
  'regionTypeId': 56, // Number | Restrict countries to this region type; required if regionName is supplied
  'regionName': "regionName_example", // String | Restrict countries to this region name; required if regionTypeId is supplied
  'sort': "'key'", // String | The term to sort the result countries by.
  'order': "'ascending'" // String | The direction to sort the result countries by.
};
apiInstance.getCountries(marketId, opts, (error, data, response) => {
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
 **marketId** | **String**| MarketId in which the request is being made, and for which responses should be localized | 
 **regionTypeId** | **Number**| Restrict countries to this region type; required if regionName is supplied | [optional] 
 **regionName** | **String**| Restrict countries to this region name; required if regionTypeId is supplied | [optional] 
 **sort** | **String**| The term to sort the result countries by. | [optional] [default to &#39;key&#39;]
 **order** | **String**| The direction to sort the result countries by. | [optional] [default to &#39;ascending&#39;]

### Return type

[**[CountrySummary]**](CountrySummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCountry

> [Country] getCountry(countryKey, marketId, opts)

Retrieves country and summary state information for provided countryKey

Authorization is not required

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let countryKey = "countryKey_example"; // String | The country key
let marketId = "marketId_example"; // String | MarketId in which the request is being made, and for which responses should be localized
let opts = {
  'sort': "'key'", // String | The term to sort the result country states by.
  'order': "'ascending'" // String | The direction to sort the result country states by.
};
apiInstance.getCountry(countryKey, marketId, opts, (error, data, response) => {
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
 **countryKey** | **String**| The country key | 
 **marketId** | **String**| MarketId in which the request is being made, and for which responses should be localized | 
 **sort** | **String**| The term to sort the result country states by. | [optional] [default to &#39;key&#39;]
 **order** | **String**| The direction to sort the result country states by. | [optional] [default to &#39;ascending&#39;]

### Return type

[**[Country]**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

