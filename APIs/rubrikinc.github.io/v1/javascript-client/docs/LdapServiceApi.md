# RubrikRestApi.LdapServiceApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLdapService**](LdapServiceApi.md#createLdapService) | **POST** /ldap_service | Add a new authentication domain
[**deleteLdapService**](LdapServiceApi.md#deleteLdapService) | **DELETE** /ldap_service/{id} | Delete an authentication domain for the given ID
[**getLdapService**](LdapServiceApi.md#getLdapService) | **GET** /ldap_service/{id} | Get a LDAP service for the given ID
[**patchLdapService**](LdapServiceApi.md#patchLdapService) | **PATCH** /ldap_service/{id} | Update an existing authentication domain
[**putLdapService**](LdapServiceApi.md#putLdapService) | **PUT** /ldap_service/{id} | Replace the values of an authentication domain
[**queryLdapService**](LdapServiceApi.md#queryLdapService) | **GET** /ldap_service | Get a list of LDAP services



## createLdapService

> LdapServiceSummary createLdapService(ldapServiceInfo)

Add a new authentication domain

Add a new authentication domain.

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

let apiInstance = new RubrikRestApi.LdapServiceApi();
let ldapServiceInfo = new RubrikRestApi.LdapServiceInfo(); // LdapServiceInfo | Information for joining an authentication domain.
apiInstance.createLdapService(ldapServiceInfo, (error, data, response) => {
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
 **ldapServiceInfo** | [**LdapServiceInfo**](LdapServiceInfo.md)| Information for joining an authentication domain. | 

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLdapService

> deleteLdapService(id)

Delete an authentication domain for the given ID

Delete an authentication domain for the given ID.

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

let apiInstance = new RubrikRestApi.LdapServiceApi();
let id = "id_example"; // String | ID of the authentication domain to be deleted.
apiInstance.deleteLdapService(id, (error, data, response) => {
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
 **id** | **String**| ID of the authentication domain to be deleted. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLdapService

> LdapServiceSummary getLdapService(id)

Get a LDAP service for the given ID

Get a LDAP service for the given ID.

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

let apiInstance = new RubrikRestApi.LdapServiceApi();
let id = "id_example"; // String | ID of the authentication domain to be retrieved.
apiInstance.getLdapService(id, (error, data, response) => {
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
 **id** | **String**| ID of the authentication domain to be retrieved. | 

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchLdapService

> LdapServiceSummary patchLdapService(id, ldapServiceInfoUpdate)

Update an existing authentication domain

Modify the values of a specified authentication domain object.

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

let apiInstance = new RubrikRestApi.LdapServiceApi();
let id = "id_example"; // String | ID of the authentication domain to be updated.
let ldapServiceInfoUpdate = new RubrikRestApi.LdapServiceInfoUpdate(); // LdapServiceInfoUpdate | Information for updating an authentication domain.
apiInstance.patchLdapService(id, ldapServiceInfoUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the authentication domain to be updated. | 
 **ldapServiceInfoUpdate** | [**LdapServiceInfoUpdate**](LdapServiceInfoUpdate.md)| Information for updating an authentication domain. | 

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putLdapService

> LdapServiceSummary putLdapService(id, ldapServiceInfoUpdate)

Replace the values of an authentication domain

Replace the values of a specified authentication domain object.

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

let apiInstance = new RubrikRestApi.LdapServiceApi();
let id = "id_example"; // String | ID of the authentication domain to be updated.
let ldapServiceInfoUpdate = new RubrikRestApi.LdapServiceInfoUpdate(); // LdapServiceInfoUpdate | Information for updating an authentication domain.
apiInstance.putLdapService(id, ldapServiceInfoUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the authentication domain to be updated. | 
 **ldapServiceInfoUpdate** | [**LdapServiceInfoUpdate**](LdapServiceInfoUpdate.md)| Information for updating an authentication domain. | 

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryLdapService

> LdapServiceSummaryListResponse queryLdapService()

Get a list of LDAP services

Get a list of LDAP services.

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

let apiInstance = new RubrikRestApi.LdapServiceApi();
apiInstance.queryLdapService((error, data, response) => {
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

[**LdapServiceSummaryListResponse**](LdapServiceSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

