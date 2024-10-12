# NordigenAccountInformationServicesApi.InstitutionsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveAllSupportedInstitutionsInAGivenCountry**](InstitutionsApi.md#retrieveAllSupportedInstitutionsInAGivenCountry) | **GET** /api/v2/institutions/ | 
[**retrieveInstitution**](InstitutionsApi.md#retrieveInstitution) | **GET** /api/v2/institutions/{id}/ | 



## retrieveAllSupportedInstitutionsInAGivenCountry

> [Integration] retrieveAllSupportedInstitutionsInAGivenCountry(opts)



List all available institutions

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.InstitutionsApi();
let opts = {
  'country': "AT", // String | ISO 3166 two-character country code
  'paymentsEnabled': "false" // String | Boolean value, indicating if payments are enabled
};
apiInstance.retrieveAllSupportedInstitutionsInAGivenCountry(opts, (error, data, response) => {
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
 **country** | **String**| ISO 3166 two-character country code | [optional] 
 **paymentsEnabled** | **String**| Boolean value, indicating if payments are enabled | [optional] 

### Return type

[**[Integration]**](Integration.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveInstitution

> IntegrationRetrieve retrieveInstitution(id)



Get details about a specific Institution

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.InstitutionsApi();
let id = "N26_NTSBDEB1"; // String | 
apiInstance.retrieveInstitution(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**IntegrationRetrieve**](IntegrationRetrieve.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

