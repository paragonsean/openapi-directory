# StorecoveApi.AdditionalTaxIdentifiersApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#createAdditionalTaxIdentifier) | **POST** /legal_entities/{legal_entity_id}/additional_tax_identifiers | Create a new AdditionalTaxIdentifier
[**deleteAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#deleteAdditionalTaxIdentifier) | **DELETE** /legal_entities/{legal_entity_id}/additional_tax_identifiers/{id} | Delete AdditionalTaxIdentifier
[**getAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#getAdditionalTaxIdentifier) | **GET** /legal_entities/{legal_entity_id}/additional_tax_identifiers/{id} | Get AdditionalTaxIdentifier
[**updateAdditionalTaxIdentifier**](AdditionalTaxIdentifiersApi.md#updateAdditionalTaxIdentifier) | **PATCH** /legal_entities/{legal_entity_id}/additional_tax_identifiers/{id} | Update AdditionalTaxIdentifier



## createAdditionalTaxIdentifier

> AdditionalTaxIdentifier createAdditionalTaxIdentifier(legalEntityId, additionalTaxIdentifierCreate)

Create a new AdditionalTaxIdentifier

Create a new AdditionalTaxIdentifier. An AdditionalTaxIdentifier is a seconday tax identifier that is used inside the EU when sending invoices to consumers. In that case, the VAT of the receiving country is used and if the sender has a local VAT identifier, that is used to identifiy the sender, instead of the sender&#39;s origin country VAT number. To use these identifiers, use the invoice.consumerTaxMode &#x3D; true property.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdditionalTaxIdentifiersApi();
let legalEntityId = 789; // Number | The id of the LegalEntity for which to create the AdditionalTaxIdentifier
let additionalTaxIdentifierCreate = new StorecoveApi.AdditionalTaxIdentifierCreate(); // AdditionalTaxIdentifierCreate | AdditionalTaxIdentifier to create
apiInstance.createAdditionalTaxIdentifier(legalEntityId, additionalTaxIdentifierCreate, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity for which to create the AdditionalTaxIdentifier | 
 **additionalTaxIdentifierCreate** | [**AdditionalTaxIdentifierCreate**](AdditionalTaxIdentifierCreate.md)| AdditionalTaxIdentifier to create | 

### Return type

[**AdditionalTaxIdentifier**](AdditionalTaxIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAdditionalTaxIdentifier

> deleteAdditionalTaxIdentifier(legalEntityId, id)

Delete AdditionalTaxIdentifier

Delete an AdditionalTaxIdentifier

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdditionalTaxIdentifiersApi();
let legalEntityId = 789; // Number | The id of the LegalEntity the AdditionalTaxIdentifier belongs to
let id = 789; // Number | The id of the AdditionalTaxIdentifier
apiInstance.deleteAdditionalTaxIdentifier(legalEntityId, id, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity the AdditionalTaxIdentifier belongs to | 
 **id** | **Number**| The id of the AdditionalTaxIdentifier | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAdditionalTaxIdentifier

> AdditionalTaxIdentifier getAdditionalTaxIdentifier(legalEntityId, id)

Get AdditionalTaxIdentifier

Get an AdditionalTaxIdentifier

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdditionalTaxIdentifiersApi();
let legalEntityId = 789; // Number | The id of the LegalEntity the AdditionalTaxIdentifier belongs to
let id = 789; // Number | The id of the AdditionalTaxIdentifier
apiInstance.getAdditionalTaxIdentifier(legalEntityId, id, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity the AdditionalTaxIdentifier belongs to | 
 **id** | **Number**| The id of the AdditionalTaxIdentifier | 

### Return type

[**AdditionalTaxIdentifier**](AdditionalTaxIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAdditionalTaxIdentifier

> AdditionalTaxIdentifier updateAdditionalTaxIdentifier(legalEntityId, id, additionalTaxIdentifierUpdate)

Update AdditionalTaxIdentifier

Update an AdditionalTaxIdentifier

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.AdditionalTaxIdentifiersApi();
let legalEntityId = 789; // Number | The id of the LegalEntity the AdditionalTaxIdentifier belongs to
let id = 789; // Number | The id of the AdditionalTaxIdentifier to be updated
let additionalTaxIdentifierUpdate = new StorecoveApi.AdditionalTaxIdentifierUpdate(); // AdditionalTaxIdentifierUpdate | AdditionalTaxIdentifier to update
apiInstance.updateAdditionalTaxIdentifier(legalEntityId, id, additionalTaxIdentifierUpdate, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity the AdditionalTaxIdentifier belongs to | 
 **id** | **Number**| The id of the AdditionalTaxIdentifier to be updated | 
 **additionalTaxIdentifierUpdate** | [**AdditionalTaxIdentifierUpdate**](AdditionalTaxIdentifierUpdate.md)| AdditionalTaxIdentifier to update | 

### Return type

[**AdditionalTaxIdentifier**](AdditionalTaxIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

