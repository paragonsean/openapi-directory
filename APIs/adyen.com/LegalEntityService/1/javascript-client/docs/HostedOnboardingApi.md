# LegalEntityManagementApi.HostedOnboardingApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getThemes**](HostedOnboardingApi.md#getThemes) | **GET** /themes | Get a list of hosted onboarding page themes
[**getThemesId**](HostedOnboardingApi.md#getThemesId) | **GET** /themes/{id} | Get an onboarding link theme
[**postLegalEntitiesIdOnboardingLinks**](HostedOnboardingApi.md#postLegalEntitiesIdOnboardingLinks) | **POST** /legalEntities/{id}/onboardingLinks | Get a link to an Adyen-hosted onboarding page



## getThemes

> OnboardingThemes getThemes()

Get a list of hosted onboarding page themes

Returns a list of hosted onboarding page themes.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.HostedOnboardingApi();
apiInstance.getThemes((error, data, response) => {
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

[**OnboardingThemes**](OnboardingThemes.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThemesId

> OnboardingTheme getThemesId(id)

Get an onboarding link theme

Returns the details of the theme identified in the path.&gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.HostedOnboardingApi();
let id = "id_example"; // String | The unique identifier of the theme
apiInstance.getThemesId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the theme | 

### Return type

[**OnboardingTheme**](OnboardingTheme.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postLegalEntitiesIdOnboardingLinks

> OnboardingLink postLegalEntitiesIdOnboardingLinks(id, opts)

Get a link to an Adyen-hosted onboarding page

Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example

```javascript
import LegalEntityManagementApi from 'legal_entity_management_api';
let defaultClient = LegalEntityManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new LegalEntityManagementApi.HostedOnboardingApi();
let id = "id_example"; // String | The unique identifier of the legal entity
let opts = {
  'onboardingLinkInfo': new LegalEntityManagementApi.OnboardingLinkInfo() // OnboardingLinkInfo | 
};
apiInstance.postLegalEntitiesIdOnboardingLinks(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity | 
 **onboardingLinkInfo** | [**OnboardingLinkInfo**](OnboardingLinkInfo.md)|  | [optional] 

### Return type

[**OnboardingLink**](OnboardingLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

