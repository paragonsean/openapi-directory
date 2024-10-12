# HubhopperPartnerIntegrationApiSProduction.UtilApi

All URIs are relative to *https://apis.hubhopper.com/partner*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utilLanguagesGet**](UtilApi.md#utilLanguagesGet) | **GET** /util/languages | 



## utilLanguagesGet

> LanguageList utilLanguagesGet(opts)



### Example

```javascript
import HubhopperPartnerIntegrationApiSProduction from 'hubhopper_partner_integration_api_s_production';
let defaultClient = HubhopperPartnerIntegrationApiSProduction.ApiClient.instance;
// Configure API key authorization: partner_id
let partner_id = defaultClient.authentications['partner_id'];
partner_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//partner_id.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new HubhopperPartnerIntegrationApiSProduction.UtilApi();
let opts = {
  'pageSize': "pageSize_example", // String | Provide the size of the page to fetch.
  'page': "page_example" // String | Provide the page number to fetch.
};
apiInstance.utilLanguagesGet(opts, (error, data, response) => {
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
 **pageSize** | **String**| Provide the size of the page to fetch. | [optional] 
 **page** | **String**| Provide the page number to fetch. | [optional] 

### Return type

[**LanguageList**](LanguageList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

