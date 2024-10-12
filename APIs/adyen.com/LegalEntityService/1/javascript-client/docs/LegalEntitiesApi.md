# LegalEntityManagementApi.LegalEntitiesApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLegalEntitiesId**](LegalEntitiesApi.md#getLegalEntitiesId) | **GET** /legalEntities/{id} | Get a legal entity
[**getLegalEntitiesIdBusinessLines**](LegalEntitiesApi.md#getLegalEntitiesIdBusinessLines) | **GET** /legalEntities/{id}/businessLines | Get all business lines under a legal entity
[**patchLegalEntitiesId**](LegalEntitiesApi.md#patchLegalEntitiesId) | **PATCH** /legalEntities/{id} | Update a legal entity
[**postLegalEntities**](LegalEntitiesApi.md#postLegalEntities) | **POST** /legalEntities | Create a legal entity



## getLegalEntitiesId

> LegalEntity getLegalEntitiesId(id)

Get a legal entity

Returns a legal entity.

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

let apiInstance = new LegalEntityManagementApi.LegalEntitiesApi();
let id = "id_example"; // String | The unique identifier of the legal entity.
apiInstance.getLegalEntitiesId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity. | 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLegalEntitiesIdBusinessLines

> BusinessLines getLegalEntitiesIdBusinessLines(id)

Get all business lines under a legal entity

Returns the business lines owned by a legal entity.

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

let apiInstance = new LegalEntityManagementApi.LegalEntitiesApi();
let id = "id_example"; // String | The unique identifier of the legal entity.
apiInstance.getLegalEntitiesIdBusinessLines(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity. | 

### Return type

[**BusinessLines**](BusinessLines.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchLegalEntitiesId

> LegalEntity patchLegalEntitiesId(id, opts)

Update a legal entity

Updates a legal entity.   &gt;To change the legal entity type, include only the new &#x60;type&#x60; in your request. To update the &#x60;entityAssociations&#x60; array, you need to replace the entire array. For example, if the array has 3 entries and you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

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

let apiInstance = new LegalEntityManagementApi.LegalEntitiesApi();
let id = "id_example"; // String | The unique identifier of the legal entity.
let opts = {
  'xRequestedVerificationCode': "1", // String | Use the requested verification code 0_0001 to resolve any suberrors associated with the legal entity. Requested verification codes can only be used in your test environment.
  'legalEntityInfo': new LegalEntityManagementApi.LegalEntityInfo() // LegalEntityInfo | 
};
apiInstance.patchLegalEntitiesId(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity. | 
 **xRequestedVerificationCode** | **String**| Use the requested verification code 0_0001 to resolve any suberrors associated with the legal entity. Requested verification codes can only be used in your test environment. | [optional] 
 **legalEntityInfo** | [**LegalEntityInfo**](LegalEntityInfo.md)|  | [optional] 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postLegalEntities

> LegalEntity postLegalEntities(opts)

Create a legal entity

Creates a legal entity.   This resource contains information about the user that will be onboarded in your platform. Adyen uses this information to perform verification checks as required by payment industry regulations. Adyen informs you of the verification results through webhooks or API responses.   &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

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

let apiInstance = new LegalEntityManagementApi.LegalEntitiesApi();
let opts = {
  'xRequestedVerificationCode': "13004", // String | Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment.
  'legalEntityInfoRequiredType': new LegalEntityManagementApi.LegalEntityInfoRequiredType() // LegalEntityInfoRequiredType | 
};
apiInstance.postLegalEntities(opts, (error, data, response) => {
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
 **xRequestedVerificationCode** | **String**| Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment. | [optional] 
 **legalEntityInfoRequiredType** | [**LegalEntityInfoRequiredType**](LegalEntityInfoRequiredType.md)|  | [optional] 

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

