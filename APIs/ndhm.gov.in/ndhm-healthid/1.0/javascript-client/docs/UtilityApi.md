# HealthIdService.UtilityApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistrictsInStateUsingGET**](UtilityApi.md#getDistrictsInStateUsingGET) | **GET** /v1/ha/lgd/districts | Get a list of districts in a given  State as per LGD.
[**getStatesUsingGET**](UtilityApi.md#getStatesUsingGET) | **GET** /v1/ha/lgd/states | Get a list of states as per LGD.



## getDistrictsInStateUsingGET

> [DistrictDTO] getDistrictsInStateUsingGET(stateCode, opts)

Get a list of districts in a given  State as per LGD.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.UtilityApi();
let stateCode = "stateCode_example"; // String | stateCode
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.getDistrictsInStateUsingGET(stateCode, opts, (error, data, response) => {
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
 **stateCode** | **String**| stateCode | 
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**[DistrictDTO]**](DistrictDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStatesUsingGET

> [StatesDTO] getStatesUsingGET(opts)

Get a list of states as per LGD.

### Example

```javascript
import HealthIdService from 'health_id_service';
let defaultClient = HealthIdService.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';
// Configure API key authorization: X-HIP-ID
let X-HIP-ID = defaultClient.authentications['X-HIP-ID'];
X-HIP-ID.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-HIP-ID.apiKeyPrefix = 'Token';

let apiInstance = new HealthIdService.UtilityApi();
let opts = {
  'acceptLanguage': "'en-US'" // String | 
};
apiInstance.getStatesUsingGET(opts, (error, data, response) => {
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
 **acceptLanguage** | **String**|  | [optional] [default to &#39;en-US&#39;]

### Return type

[**[StatesDTO]**](StatesDTO.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

