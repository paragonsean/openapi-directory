# GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi

All URIs are relative to *https://apps.nrs.gov.bc.ca/gwells/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aquiferCodesDemandList**](AquiferCodesApi.md#aquiferCodesDemandList) | **GET** /aquifer-codes/demand/ | 
[**aquiferCodesMaterialsList**](AquiferCodesApi.md#aquiferCodesMaterialsList) | **GET** /aquifer-codes/materials/ | 
[**aquiferCodesProductivityList**](AquiferCodesApi.md#aquiferCodesProductivityList) | **GET** /aquifer-codes/productivity/ | 
[**aquiferCodesQualityConcernsList**](AquiferCodesApi.md#aquiferCodesQualityConcernsList) | **GET** /aquifer-codes/quality-concerns/ | 
[**aquiferCodesSubtypesList**](AquiferCodesApi.md#aquiferCodesSubtypesList) | **GET** /aquifer-codes/subtypes/ | 
[**aquiferCodesVulnerabilityList**](AquiferCodesApi.md#aquiferCodesVulnerabilityList) | **GET** /aquifer-codes/vulnerability/ | 
[**aquiferCodesWaterUseList**](AquiferCodesApi.md#aquiferCodesWaterUseList) | **GET** /aquifer-codes/water-use/ | 



## aquiferCodesDemandList

> AquiferCodesDemandList200Response aquiferCodesDemandList(opts)



return a list of aquifer demand codes

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.aquiferCodesDemandList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**AquiferCodesDemandList200Response**](AquiferCodesDemandList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aquiferCodesMaterialsList

> AquiferCodesMaterialsList200Response aquiferCodesMaterialsList(opts)



return a list of aquifer material codes

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.aquiferCodesMaterialsList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**AquiferCodesMaterialsList200Response**](AquiferCodesMaterialsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aquiferCodesProductivityList

> AquiferCodesProductivityList200Response aquiferCodesProductivityList(opts)



return a list of aquifer productivity codes

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.aquiferCodesProductivityList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**AquiferCodesProductivityList200Response**](AquiferCodesProductivityList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aquiferCodesQualityConcernsList

> AquiferCodesQualityConcernsList200Response aquiferCodesQualityConcernsList(opts)



return a list of quality concern codes

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.aquiferCodesQualityConcernsList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**AquiferCodesQualityConcernsList200Response**](AquiferCodesQualityConcernsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aquiferCodesSubtypesList

> AquiferCodesSubtypesList200Response aquiferCodesSubtypesList(opts)



return a list of aquifer subtype codes

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.aquiferCodesSubtypesList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**AquiferCodesSubtypesList200Response**](AquiferCodesSubtypesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aquiferCodesVulnerabilityList

> AquiferCodesVulnerabilityList200Response aquiferCodesVulnerabilityList(opts)



return a list of aquifer vulnerability codes

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.aquiferCodesVulnerabilityList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**AquiferCodesVulnerabilityList200Response**](AquiferCodesVulnerabilityList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aquiferCodesWaterUseList

> AquiferCodesWaterUseList200Response aquiferCodesWaterUseList(opts)



return a list of water use codes

### Example

```javascript
import GroundwaterWellsAquifersAndRegistryApi from 'groundwater_wells_aquifers_and_registry_api';
let defaultClient = GroundwaterWellsAquifersAndRegistryApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new GroundwaterWellsAquifersAndRegistryApi.AquiferCodesApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.aquiferCodesWaterUseList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**AquiferCodesWaterUseList200Response**](AquiferCodesWaterUseList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

