# RubrikRestApi.IdpAuthDomainApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIdProviderAuthDomain**](IdpAuthDomainApi.md#createIdProviderAuthDomain) | **POST** /idp_auth_domain | Add a new IdP authentication domain
[**deleteIdProviderAuthDomain**](IdpAuthDomainApi.md#deleteIdProviderAuthDomain) | **DELETE** /idp_auth_domain/{id} | Delete an IdP authentication domain for the given ID
[**getIdProviderAuthDomain**](IdpAuthDomainApi.md#getIdProviderAuthDomain) | **GET** /idp_auth_domain/{id} | Get an IdP authentication domain for the given id
[**queryIdProviderAuthDomain**](IdpAuthDomainApi.md#queryIdProviderAuthDomain) | **GET** /idp_auth_domain | Get a list of IdP authentication domains
[**updateIdProviderAuthDomain**](IdpAuthDomainApi.md#updateIdProviderAuthDomain) | **PATCH** /idp_auth_domain/{id} | Update an existing IdP authentication domain



## createIdProviderAuthDomain

> IdProviderAuthDomainSummary createIdProviderAuthDomain(idProviderAuthDomainInfo)

Add a new IdP authentication domain

Add a new IdP authentication domain.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.IdpAuthDomainApi();
let idProviderAuthDomainInfo = new RubrikRestApi.IdProviderAuthDomainInfo(); // IdProviderAuthDomainInfo | Information for joining an IdP authentication domain.
apiInstance.createIdProviderAuthDomain(idProviderAuthDomainInfo, (error, data, response) => {
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
 **idProviderAuthDomainInfo** | [**IdProviderAuthDomainInfo**](IdProviderAuthDomainInfo.md)| Information for joining an IdP authentication domain. | 

### Return type

[**IdProviderAuthDomainSummary**](IdProviderAuthDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteIdProviderAuthDomain

> deleteIdProviderAuthDomain(id)

Delete an IdP authentication domain for the given ID

Delete an IdP authentication domain for the given ID.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.IdpAuthDomainApi();
let id = "id_example"; // String | ID of the IdP authentication domain to be deleted.
apiInstance.deleteIdProviderAuthDomain(id, (error, data, response) => {
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
 **id** | **String**| ID of the IdP authentication domain to be deleted. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getIdProviderAuthDomain

> IdProviderAuthDomainSummary getIdProviderAuthDomain(id)

Get an IdP authentication domain for the given id

Get an IdP authentication domain for the given id.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.IdpAuthDomainApi();
let id = "id_example"; // String | ID of the IdP Authentication Domain to be retrieved.
apiInstance.getIdProviderAuthDomain(id, (error, data, response) => {
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
 **id** | **String**| ID of the IdP Authentication Domain to be retrieved. | 

### Return type

[**IdProviderAuthDomainSummary**](IdProviderAuthDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryIdProviderAuthDomain

> IdProviderAuthDomainSummaryListResponse queryIdProviderAuthDomain()

Get a list of IdP authentication domains

Get a list of IdP authentication domains.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.IdpAuthDomainApi();
apiInstance.queryIdProviderAuthDomain((error, data, response) => {
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

[**IdProviderAuthDomainSummaryListResponse**](IdProviderAuthDomainSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateIdProviderAuthDomain

> IdProviderAuthDomainSummary updateIdProviderAuthDomain(id, idProviderAuthDomainInfoUpdate)

Update an existing IdP authentication domain

Update an existing IdP authentication domain.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.IdpAuthDomainApi();
let id = "id_example"; // String | ID of the IdP authentication domain to be updated.
let idProviderAuthDomainInfoUpdate = new RubrikRestApi.IdProviderAuthDomainInfoUpdate(); // IdProviderAuthDomainInfoUpdate | Information for updating an IdP authentication domain.
apiInstance.updateIdProviderAuthDomain(id, idProviderAuthDomainInfoUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the IdP authentication domain to be updated. | 
 **idProviderAuthDomainInfoUpdate** | [**IdProviderAuthDomainInfoUpdate**](IdProviderAuthDomainInfoUpdate.md)| Information for updating an IdP authentication domain. | 

### Return type

[**IdProviderAuthDomainSummary**](IdProviderAuthDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

