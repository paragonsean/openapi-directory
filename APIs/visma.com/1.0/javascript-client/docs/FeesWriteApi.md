# SeveraPublicRestApiDocumentation.FeesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flatRatesPatchFlatRate**](FeesWriteApi.md#flatRatesPatchFlatRate) | **PATCH** /v1/flatrates/{guid} | Update (Patch) a flat rate or a part of it.
[**flatRatesPostFlatRate**](FeesWriteApi.md#flatRatesPostFlatRate) | **POST** /v1/flatrates | Insert a flat rate.
[**projectFeesPatchProjectFee**](FeesWriteApi.md#projectFeesPatchProjectFee) | **PATCH** /v1/projectfees/{guid} | Update (Patch) a projectFee or a part of it.
[**projectFeesPostProjectFee**](FeesWriteApi.md#projectFeesPostProjectFee) | **POST** /v1/projectfees | Insert a project fee.
[**projectRecurringFeeRulesPatchProjectRecurringFeeRule**](FeesWriteApi.md#projectRecurringFeeRulesPatchProjectRecurringFeeRule) | **PATCH** /v1/projectrecurringfeerules/{guid} | Update (Patch) a projectRecurringFeeRule or a part of it.
[**projectRecurringFeeRulesPostProjectRecurringFeeRule**](FeesWriteApi.md#projectRecurringFeeRulesPostProjectRecurringFeeRule) | **POST** /v1/projectrecurringfeerules | Insert a projectRecurringFeeRule.



## flatRatesPatchFlatRate

> [FlatRateOutputModel] flatRatesPatchFlatRate(guid, opts)

Update (Patch) a flat rate or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.FeesWriteApi();
let guid = "guid_example"; // String | ID of the flat rate.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of FlatRateModel.
};
apiInstance.flatRatesPatchFlatRate(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the flat rate. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of FlatRateModel. | [optional] 

### Return type

[**[FlatRateOutputModel]**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## flatRatesPostFlatRate

> FlatRateOutputModel flatRatesPostFlatRate(opts)

Insert a flat rate.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.FeesWriteApi();
let opts = {
  'flatRateInputModel': new SeveraPublicRestApiDocumentation.FlatRateInputModel() // FlatRateInputModel | FlatRateModel.
};
apiInstance.flatRatesPostFlatRate(opts, (error, data, response) => {
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
 **flatRateInputModel** | [**FlatRateInputModel**](FlatRateInputModel.md)| FlatRateModel. | [optional] 

### Return type

[**FlatRateOutputModel**](FlatRateOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectFeesPatchProjectFee

> [ProjectFeeOutputModel] projectFeesPatchProjectFee(guid, opts)

Update (Patch) a projectFee or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.FeesWriteApi();
let guid = "guid_example"; // String | ID of the project fee Can also be comma separate list of IDs to patch multiple project fees with one call. When multiple IDs are given, returns model which has list of succeeded project fees and list of errors.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ProjectFeeInputModel.
};
apiInstance.projectFeesPatchProjectFee(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the project fee Can also be comma separate list of IDs to patch multiple project fees with one call. When multiple IDs are given, returns model which has list of succeeded project fees and list of errors. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ProjectFeeInputModel. | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectFeesPostProjectFee

> [ProjectFeeOutputModel] projectFeesPostProjectFee(opts)

Insert a project fee.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.FeesWriteApi();
let opts = {
  'projectFeeInputModel': new SeveraPublicRestApiDocumentation.ProjectFeeInputModel() // ProjectFeeInputModel | ProjectFeeInputModel.
};
apiInstance.projectFeesPostProjectFee(opts, (error, data, response) => {
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
 **projectFeeInputModel** | [**ProjectFeeInputModel**](ProjectFeeInputModel.md)| ProjectFeeInputModel. | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectRecurringFeeRulesPatchProjectRecurringFeeRule

> [ProjectRecurringFeeRuleOutputModel] projectRecurringFeeRulesPatchProjectRecurringFeeRule(guid, opts)

Update (Patch) a projectRecurringFeeRule or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.FeesWriteApi();
let guid = "guid_example"; // String | ID of the projectRecurringFeeRule.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ProjectRecurringFeeRuleModel.
};
apiInstance.projectRecurringFeeRulesPatchProjectRecurringFeeRule(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the projectRecurringFeeRule. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ProjectRecurringFeeRuleModel. | [optional] 

### Return type

[**[ProjectRecurringFeeRuleOutputModel]**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectRecurringFeeRulesPostProjectRecurringFeeRule

> [ProjectRecurringFeeRuleOutputModel] projectRecurringFeeRulesPostProjectRecurringFeeRule(opts)

Insert a projectRecurringFeeRule.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.FeesWriteApi();
let opts = {
  'projectRecurringFeeRuleInputModel': new SeveraPublicRestApiDocumentation.ProjectRecurringFeeRuleInputModel() // ProjectRecurringFeeRuleInputModel | ProjectRecurringFeeRuleModel.
};
apiInstance.projectRecurringFeeRulesPostProjectRecurringFeeRule(opts, (error, data, response) => {
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
 **projectRecurringFeeRuleInputModel** | [**ProjectRecurringFeeRuleInputModel**](ProjectRecurringFeeRuleInputModel.md)| ProjectRecurringFeeRuleModel. | [optional] 

### Return type

[**[ProjectRecurringFeeRuleOutputModel]**](ProjectRecurringFeeRuleOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

