# InfermedicaApi.RiskFactorsApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllRiskFactors**](RiskFactorsApi.md#getAllRiskFactors) | **GET** /risk_factors | List all risk factors
[**getRiskFactor**](RiskFactorsApi.md#getRiskFactor) | **GET** /risk_factors/{id} | Get risk factor by id



## getAllRiskFactors

> [RiskFactorPublic] getAllRiskFactors(opts)

List all risk factors

Returns a list of all available risk factors.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.RiskFactorsApi();
let opts = {
  'ageValue': 18, // Number | age value
  'ageUnit': "year", // String | unit in which age value was provided
  'enableTriage5': true // Boolean | enable 5-level triage values
};
apiInstance.getAllRiskFactors(opts, (error, data, response) => {
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
 **ageValue** | **Number**| age value | [optional] 
 **ageUnit** | **String**| unit in which age value was provided | [optional] [default to &#39;year&#39;]
 **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] 

### Return type

[**[RiskFactorPublic]**](RiskFactorPublic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRiskFactor

> RiskFactorDetails getRiskFactor(id, opts)

Get risk factor by id

Returns details of a single risk factor specified by id parameter.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.RiskFactorsApi();
let id = "id_example"; // String | risk factor id
let opts = {
  'ageValue': 18, // Number | age value
  'ageUnit': "year", // String | unit in which age value was provided
  'enableTriage5': true // Boolean | enable 5-level triage values
};
apiInstance.getRiskFactor(id, opts, (error, data, response) => {
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
 **id** | **String**| risk factor id | 
 **ageValue** | **Number**| age value | [optional] 
 **ageUnit** | **String**| unit in which age value was provided | [optional] [default to &#39;year&#39;]
 **enableTriage5** | **Boolean**| enable 5-level triage values | [optional] 

### Return type

[**RiskFactorDetails**](RiskFactorDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

