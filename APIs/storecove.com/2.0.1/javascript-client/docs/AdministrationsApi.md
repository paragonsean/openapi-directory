# StorecoveApi.AdministrationsApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAdministration**](AdministrationsApi.md#createAdministration) | **POST** /legal_entities/{legal_entity_id}/administrations | Create a new Administration
[**deleteAdministration**](AdministrationsApi.md#deleteAdministration) | **DELETE** /legal_entities/{legal_entity_id}/administrations/{id} | Delete Administration
[**getAdministration**](AdministrationsApi.md#getAdministration) | **GET** /legal_entities/{legal_entity_id}/administrations/{id} | Get Administration
[**updateAdministration**](AdministrationsApi.md#updateAdministration) | **PATCH** /legal_entities/{legal_entity_id}/administrations/{id} | Update Administration



## createAdministration

> Administration createAdministration(legalEntityId, administrationCreate)

Create a new Administration

Deprecated. Create a new Administration. An Administration is an email destination for purchase invoices.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdministrationsApi();
let legalEntityId = 789; // Number | The id of the LegalEntity for which to create the Administration
let administrationCreate = new StorecoveApi.AdministrationCreate(); // AdministrationCreate | Administration to create
apiInstance.createAdministration(legalEntityId, administrationCreate, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity for which to create the Administration | 
 **administrationCreate** | [**AdministrationCreate**](AdministrationCreate.md)| Administration to create | 

### Return type

[**Administration**](Administration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAdministration

> deleteAdministration(legalEntityId, id)

Delete Administration

Deprecated. Delete an Administration

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdministrationsApi();
let legalEntityId = 789; // Number | The id of the LegalEntity the Administration belongs to
let id = 789; // Number | The id of the Administration
apiInstance.deleteAdministration(legalEntityId, id, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity the Administration belongs to | 
 **id** | **Number**| The id of the Administration | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAdministration

> Administration getAdministration(legalEntityId, id)

Get Administration

Deprecated. Get an Administration

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdministrationsApi();
let legalEntityId = 789; // Number | The id of the LegalEntity the Administration belongs to
let id = 789; // Number | The id of the Administration
apiInstance.getAdministration(legalEntityId, id, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity the Administration belongs to | 
 **id** | **Number**| The id of the Administration | 

### Return type

[**Administration**](Administration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAdministration

> Administration updateAdministration(legalEntityId, id, administrationUpdate)

Update Administration

Deprecated. Update an Administration

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdministrationsApi();
let legalEntityId = 789; // Number | The id of the LegalEntity the Administration belongs to
let id = 789; // Number | The id of the Administration to be updated
let administrationUpdate = new StorecoveApi.AdministrationUpdate(); // AdministrationUpdate | Administration to update
apiInstance.updateAdministration(legalEntityId, id, administrationUpdate, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity the Administration belongs to | 
 **id** | **Number**| The id of the Administration to be updated | 
 **administrationUpdate** | [**AdministrationUpdate**](AdministrationUpdate.md)| Administration to update | 

### Return type

[**Administration**](Administration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

