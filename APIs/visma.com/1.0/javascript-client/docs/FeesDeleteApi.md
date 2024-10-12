# SeveraPublicRestApiDocumentation.FeesDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flatRatesDeleteFlatRate**](FeesDeleteApi.md#flatRatesDeleteFlatRate) | **DELETE** /v1/flatrates/{guid} | Delete a flat rate of a phase.
[**projectFeesDeleteProjectFree**](FeesDeleteApi.md#projectFeesDeleteProjectFree) | **DELETE** /v1/projectfees/{guid} | Deletes a project fee.
[**projectRecurringFeeRulesDeleteProjectRecurringFeeRule**](FeesDeleteApi.md#projectRecurringFeeRulesDeleteProjectRecurringFeeRule) | **DELETE** /v1/projectrecurringfeerules/{guid} | Deletes a projectRecurringFeeRule.



## flatRatesDeleteFlatRate

> flatRatesDeleteFlatRate(guid)

Delete a flat rate of a phase.

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesDeleteApi();
let guid = "guid_example"; // String | ID of flat rate.
apiInstance.flatRatesDeleteFlatRate(guid, (error, data, response) => {
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
 **guid** | **String**| ID of flat rate. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesDeleteProjectFree

> projectFeesDeleteProjectFree(guid)

Deletes a project fee.

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the project fee.
apiInstance.projectFeesDeleteProjectFree(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the project fee. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectRecurringFeeRulesDeleteProjectRecurringFeeRule

> projectRecurringFeeRulesDeleteProjectRecurringFeeRule(guid)

Deletes a projectRecurringFeeRule.

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FeesDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the project recurring fee rule.
apiInstance.projectRecurringFeeRulesDeleteProjectRecurringFeeRule(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the project recurring fee rule. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

