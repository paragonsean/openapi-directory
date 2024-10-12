# StorecoveApi.LegalEntitiesApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLegalEntity**](LegalEntitiesApi.md#createLegalEntity) | **POST** /legal_entities | Create a new LegalEntity
[**deleteLegalEntity**](LegalEntitiesApi.md#deleteLegalEntity) | **DELETE** /legal_entities/{id} | Delete LegalEntity
[**getLegalEntity**](LegalEntitiesApi.md#getLegalEntity) | **GET** /legal_entities/{id} | Get LegalEntity
[**updateLegalEntity**](LegalEntitiesApi.md#updateLegalEntity) | **PATCH** /legal_entities/{id} | Update LegalEntity



## createLegalEntity

> LegalEntity createLegalEntity(legalEntityCreate)

Create a new LegalEntity

Create a new LegalEntity.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.LegalEntitiesApi();
let legalEntityCreate = new StorecoveApi.LegalEntityCreate(); // LegalEntityCreate | LegalEntity to create
apiInstance.createLegalEntity(legalEntityCreate, (error, data, response) => {
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
 **legalEntityCreate** | [**LegalEntityCreate**](LegalEntityCreate.md)| LegalEntity to create | 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLegalEntity

> deleteLegalEntity(id)

Delete LegalEntity

Delete a specific LegalEntity.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.LegalEntitiesApi();
let id = 789; // Number | legal_entity id
apiInstance.deleteLegalEntity(id, (error, data, response) => {
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
 **id** | **Number**| legal_entity id | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getLegalEntity

> LegalEntity getLegalEntity(id)

Get LegalEntity

Get a specific LegalEntity.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.LegalEntitiesApi();
let id = 789; // Number | legal_entity id
apiInstance.getLegalEntity(id, (error, data, response) => {
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
 **id** | **Number**| legal_entity id | 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLegalEntity

> LegalEntity updateLegalEntity(id, legalEntityUpdate)

Update LegalEntity

Update a specific LegalEntity.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.LegalEntitiesApi();
let id = 789; // Number | legal_entity id
let legalEntityUpdate = new StorecoveApi.LegalEntityUpdate(); // LegalEntityUpdate | LegalEntity updates
apiInstance.updateLegalEntity(id, legalEntityUpdate, (error, data, response) => {
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
 **id** | **Number**| legal_entity id | 
 **legalEntityUpdate** | [**LegalEntityUpdate**](LegalEntityUpdate.md)| LegalEntity updates | 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

