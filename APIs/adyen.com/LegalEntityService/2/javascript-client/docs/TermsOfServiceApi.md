# LegalEntityManagementApi.TermsOfServiceApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLegalEntitiesIdTermsOfServiceAcceptanceInfos**](TermsOfServiceApi.md#getLegalEntitiesIdTermsOfServiceAcceptanceInfos) | **GET** /legalEntities/{id}/termsOfServiceAcceptanceInfos | Get Terms of Service information for a legal entity
[**getLegalEntitiesIdTermsOfServiceStatus**](TermsOfServiceApi.md#getLegalEntitiesIdTermsOfServiceStatus) | **GET** /legalEntities/{id}/termsOfServiceStatus | Get Terms of Service status
[**patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid**](TermsOfServiceApi.md#patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid) | **PATCH** /legalEntities/{id}/termsOfService/{termsofservicedocumentid} | Accept Terms of Service
[**postLegalEntitiesIdTermsOfService**](TermsOfServiceApi.md#postLegalEntitiesIdTermsOfService) | **POST** /legalEntities/{id}/termsOfService | Get Terms of Service document



## getLegalEntitiesIdTermsOfServiceAcceptanceInfos

> GetTermsOfServiceAcceptanceInfosResponse getLegalEntitiesIdTermsOfServiceAcceptanceInfos(id)

Get Terms of Service information for a legal entity

Returns Terms of Service information for a legal entity.

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

let apiInstance = new LegalEntityManagementApi.TermsOfServiceApi();
let id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
apiInstance.getLegalEntitiesIdTermsOfServiceAcceptanceInfos(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | 

### Return type

[**GetTermsOfServiceAcceptanceInfosResponse**](GetTermsOfServiceAcceptanceInfosResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLegalEntitiesIdTermsOfServiceStatus

> CalculateTermsOfServiceStatusResponse getLegalEntitiesIdTermsOfServiceStatus(id)

Get Terms of Service status

Returns the required types of Terms of Service that need to be accepted by a legal entity.

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

let apiInstance = new LegalEntityManagementApi.TermsOfServiceApi();
let id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
apiInstance.getLegalEntitiesIdTermsOfServiceStatus(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | 

### Return type

[**CalculateTermsOfServiceStatusResponse**](CalculateTermsOfServiceStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid

> AcceptTermsOfServiceResponse patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid(id, termsofservicedocumentid, opts)

Accept Terms of Service

Accepts Terms of Service.

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

let apiInstance = new LegalEntityManagementApi.TermsOfServiceApi();
let id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
let termsofservicedocumentid = "termsofservicedocumentid_example"; // String | The unique identifier of the Terms of Service document.
let opts = {
  'acceptTermsOfServiceRequest': new LegalEntityManagementApi.AcceptTermsOfServiceRequest() // AcceptTermsOfServiceRequest | 
};
apiInstance.patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid(id, termsofservicedocumentid, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | 
 **termsofservicedocumentid** | **String**| The unique identifier of the Terms of Service document. | 
 **acceptTermsOfServiceRequest** | [**AcceptTermsOfServiceRequest**](AcceptTermsOfServiceRequest.md)|  | [optional] 

### Return type

[**AcceptTermsOfServiceResponse**](AcceptTermsOfServiceResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postLegalEntitiesIdTermsOfService

> GetTermsOfServiceDocumentResponse postLegalEntitiesIdTermsOfService(id, opts)

Get Terms of Service document

Returns the Terms of Service document for a legal entity.

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

let apiInstance = new LegalEntityManagementApi.TermsOfServiceApi();
let id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
let opts = {
  'getTermsOfServiceDocumentRequest': new LegalEntityManagementApi.GetTermsOfServiceDocumentRequest() // GetTermsOfServiceDocumentRequest | 
};
apiInstance.postLegalEntitiesIdTermsOfService(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | 
 **getTermsOfServiceDocumentRequest** | [**GetTermsOfServiceDocumentRequest**](GetTermsOfServiceDocumentRequest.md)|  | [optional] 

### Return type

[**GetTermsOfServiceDocumentResponse**](GetTermsOfServiceDocumentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

