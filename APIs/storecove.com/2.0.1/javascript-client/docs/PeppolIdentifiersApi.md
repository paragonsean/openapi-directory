# StorecoveApi.PeppolIdentifiersApi

All URIs are relative to *https://api.storecove.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPeppolIdentifier**](PeppolIdentifiersApi.md#createPeppolIdentifier) | **POST** /legal_entities/{legal_entity_id}/peppol_identifiers | Create a new PeppolIdentifier
[**deletePeppolIdentifier**](PeppolIdentifiersApi.md#deletePeppolIdentifier) | **DELETE** /legal_entities/{legal_entity_id}/peppol_identifiers/{superscheme}/{scheme}/{identifier} | Delete PeppolIdentifier



## createPeppolIdentifier

> PeppolIdentifier createPeppolIdentifier(legalEntityId, peppolIdentifierCreate)

Create a new PeppolIdentifier

Create a brand new new PeppolIdentifier. For &lt;&lt;_sg_singapore&gt;&gt;, special rules apply.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.PeppolIdentifiersApi();
let legalEntityId = 789; // Number | The id of the LegalEntity for which to create the PeppolIdentifier
let peppolIdentifierCreate = new StorecoveApi.PeppolIdentifierCreate(); // PeppolIdentifierCreate | PeppolIdentifier to create
apiInstance.createPeppolIdentifier(legalEntityId, peppolIdentifierCreate, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity for which to create the PeppolIdentifier | 
 **peppolIdentifierCreate** | [**PeppolIdentifierCreate**](PeppolIdentifierCreate.md)| PeppolIdentifier to create | 

### Return type

[**PeppolIdentifier**](PeppolIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletePeppolIdentifier

> deletePeppolIdentifier(legalEntityId, superscheme, scheme, identifier)

Delete PeppolIdentifier

Delete a PeppolIdentifier.

### Example

```javascript
import StorecoveApi from 'storecove_api';
let defaultClient = StorecoveApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new StorecoveApi.PeppolIdentifiersApi();
let legalEntityId = 789; // Number | The id of the LegalEntity this PeppolIdentifier belongs to
let superscheme = "superscheme_example"; // String | The superscheme of the identifier. Should always be \"iso6523-actorid-upis\".
let scheme = "scheme_example"; // String | PEPPOL identifier scheme id, e.g. \"DE:VAT\". For a full list see <<_receiver_identifiers_list>>.
let identifier = "identifier_example"; // String | PEPPOL identifier
apiInstance.deletePeppolIdentifier(legalEntityId, superscheme, scheme, identifier, (error, data, response) => {
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
 **legalEntityId** | **Number**| The id of the LegalEntity this PeppolIdentifier belongs to | 
 **superscheme** | **String**| The superscheme of the identifier. Should always be \&quot;iso6523-actorid-upis\&quot;. | 
 **scheme** | **String**| PEPPOL identifier scheme id, e.g. \&quot;DE:VAT\&quot;. For a full list see &lt;&lt;_receiver_identifiers_list&gt;&gt;. | 
 **identifier** | **String**| PEPPOL identifier | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

