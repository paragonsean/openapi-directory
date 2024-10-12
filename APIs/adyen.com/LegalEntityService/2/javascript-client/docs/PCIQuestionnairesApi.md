# LegalEntityManagementApi.PCIQuestionnairesApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLegalEntitiesIdPciQuestionnaires**](PCIQuestionnairesApi.md#getLegalEntitiesIdPciQuestionnaires) | **GET** /legalEntities/{id}/pciQuestionnaires | Get PCI questionnaire details
[**getLegalEntitiesIdPciQuestionnairesPciid**](PCIQuestionnairesApi.md#getLegalEntitiesIdPciQuestionnairesPciid) | **GET** /legalEntities/{id}/pciQuestionnaires/{pciid} | Get PCI questionnaire
[**postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates**](PCIQuestionnairesApi.md#postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates) | **POST** /legalEntities/{id}/pciQuestionnaires/generatePciTemplates | Generate PCI questionnaire
[**postLegalEntitiesIdPciQuestionnairesSignPciTemplates**](PCIQuestionnairesApi.md#postLegalEntitiesIdPciQuestionnairesSignPciTemplates) | **POST** /legalEntities/{id}/pciQuestionnaires/signPciTemplates | Sign PCI questionnaire



## getLegalEntitiesIdPciQuestionnaires

> GetPciQuestionnaireInfosResponse getLegalEntitiesIdPciQuestionnaires(id)

Get PCI questionnaire details

Get a list of signed PCI questionnaires.

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

let apiInstance = new LegalEntityManagementApi.PCIQuestionnairesApi();
let id = "id_example"; // String | The unique identifier of the legal entity to get PCI questionnaire information.
apiInstance.getLegalEntitiesIdPciQuestionnaires(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity to get PCI questionnaire information. | 

### Return type

[**GetPciQuestionnaireInfosResponse**](GetPciQuestionnaireInfosResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLegalEntitiesIdPciQuestionnairesPciid

> GetPciQuestionnaireResponse getLegalEntitiesIdPciQuestionnairesPciid(id, pciid)

Get PCI questionnaire

Returns the signed PCI questionnaire.

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

let apiInstance = new LegalEntityManagementApi.PCIQuestionnairesApi();
let id = "id_example"; // String | The legal entity ID of the individual who signed the PCI questionnaire.
let pciid = "pciid_example"; // String | The unique identifier of the signed PCI questionnaire.
apiInstance.getLegalEntitiesIdPciQuestionnairesPciid(id, pciid, (error, data, response) => {
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
 **id** | **String**| The legal entity ID of the individual who signed the PCI questionnaire. | 
 **pciid** | **String**| The unique identifier of the signed PCI questionnaire. | 

### Return type

[**GetPciQuestionnaireResponse**](GetPciQuestionnaireResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates

> GeneratePciDescriptionResponse postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates(id, opts)

Generate PCI questionnaire

Generates the required PCI questionnaires based on the user&#39;s [salesChannel](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__reqParam_salesChannels).

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

let apiInstance = new LegalEntityManagementApi.PCIQuestionnairesApi();
let id = "id_example"; // String | The unique identifier of the legal entity to get PCI questionnaire information.
let opts = {
  'generatePciDescriptionRequest': new LegalEntityManagementApi.GeneratePciDescriptionRequest() // GeneratePciDescriptionRequest | 
};
apiInstance.postLegalEntitiesIdPciQuestionnairesGeneratePciTemplates(id, opts, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the legal entity to get PCI questionnaire information. | 
 **generatePciDescriptionRequest** | [**GeneratePciDescriptionRequest**](GeneratePciDescriptionRequest.md)|  | [optional] 

### Return type

[**GeneratePciDescriptionResponse**](GeneratePciDescriptionResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postLegalEntitiesIdPciQuestionnairesSignPciTemplates

> PciSigningResponse postLegalEntitiesIdPciQuestionnairesSignPciTemplates(id, opts)

Sign PCI questionnaire

Signs the required PCI questionnaire.

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

let apiInstance = new LegalEntityManagementApi.PCIQuestionnairesApi();
let id = "id_example"; // String | The legal entity ID of the user that has a contractual relationship with your platform.
let opts = {
  'pciSigningRequest': new LegalEntityManagementApi.PciSigningRequest() // PciSigningRequest | 
};
apiInstance.postLegalEntitiesIdPciQuestionnairesSignPciTemplates(id, opts, (error, data, response) => {
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
 **id** | **String**| The legal entity ID of the user that has a contractual relationship with your platform. | 
 **pciSigningRequest** | [**PciSigningRequest**](PciSigningRequest.md)|  | [optional] 

### Return type

[**PciSigningResponse**](PciSigningResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

