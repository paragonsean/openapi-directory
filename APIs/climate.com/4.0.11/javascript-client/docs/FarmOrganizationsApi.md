# ClimateFieldViewPlatformApis.FarmOrganizationsApi

All URIs are relative to *https://platform.climate.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchFarmOrganizationByTypeAndId**](FarmOrganizationsApi.md#fetchFarmOrganizationByTypeAndId) | **GET** /v4/farmOrganizations/{farmOrganizationType}/{farmOrganizationId} | Retrieve a specific farm organization by organization type and ID



## fetchFarmOrganizationByTypeAndId

> FarmOrganization fetchFarmOrganizationByTypeAndId(farmOrganizationType, farmOrganizationId)

Retrieve a specific farm organization by organization type and ID

Retrieve a given **farm organization** by organization type and ID.

### Example

```javascript
import ClimateFieldViewPlatformApis from 'climate_field_view_platform_apis';
let defaultClient = ClimateFieldViewPlatformApis.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2_authorization_code
let oauth2_authorization_code = defaultClient.authentications['oauth2_authorization_code'];
oauth2_authorization_code.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ClimateFieldViewPlatformApis.FarmOrganizationsApi();
let farmOrganizationType = "farmOrganizationType_example"; // String | Type of the farm organization.
let farmOrganizationId = "farmOrganizationId_example"; // String | Unique identifier of the farm organization.
apiInstance.fetchFarmOrganizationByTypeAndId(farmOrganizationType, farmOrganizationId, (error, data, response) => {
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
 **farmOrganizationType** | **String**| Type of the farm organization. | 
 **farmOrganizationId** | **String**| Unique identifier of the farm organization. | 

### Return type

[**FarmOrganization**](FarmOrganization.md)

### Authorization

[api_key](../README.md#api_key), [oauth2_authorization_code](../README.md#oauth2_authorization_code)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

