# BusinessRegistries.OrganisationsApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisationsGet**](OrganisationsApi.md#organisationsGet) | **GET** /organisations | Retrieve a list of organisations
[**organisationsPartyIdDelete**](OrganisationsApi.md#organisationsPartyIdDelete) | **DELETE** /organisations/{partyId} | Delete an organisation
[**organisationsPartyIdGet**](OrganisationsApi.md#organisationsPartyIdGet) | **GET** /organisations/{partyId} | Retrieve an organisation
[**organisationsPartyIdPut**](OrganisationsApi.md#organisationsPartyIdPut) | **PUT** /organisations/{partyId} | Update an organisation
[**organisationsPost**](OrganisationsApi.md#organisationsPost) | **POST** /organisations | Create an organisation



## organisationsGet

> [Organisation] organisationsGet(apiKey, opts)

Retrieve a list of organisations

Retrieve a list of organisations 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsApi();
let apiKey = "apiKey_example"; // String | The API key.
let opts = {
  'registeredIdentifier': "registeredIdentifier_example", // String | The registered identifier, for example, `ACN` or `ABN`.
  'identifier': "identifier_example" // String | The identifier, for example, `123456789`.
};
apiInstance.organisationsGet(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **registeredIdentifier** | **String**| The registered identifier, for example, &#x60;ACN&#x60; or &#x60;ABN&#x60;. | [optional] 
 **identifier** | **String**| The identifier, for example, &#x60;123456789&#x60;. | [optional] 

### Return type

[**[Organisation]**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdDelete

> organisationsPartyIdDelete(apiKey, partyId)

Delete an organisation

Delete an organisation with the specified identifier 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.organisationsPartyIdDelete(apiKey, partyId, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdGet

> Organisation organisationsPartyIdGet(apiKey, partyId)

Retrieve an organisation

Retrieve an organisation with the specified identifier 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.organisationsPartyIdGet(apiKey, partyId, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdPut

> Organisation organisationsPartyIdPut(apiKey, partyId, organisation)

Update an organisation

Update an organisation 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let organisation = new BusinessRegistries.Organisation(); // Organisation | Organisation resource
apiInstance.organisationsPartyIdPut(apiKey, partyId, organisation, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **partyId** | **String**| The party identifier. | 
 **organisation** | [**Organisation**](Organisation.md)| Organisation resource | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organisationsPost

> Organisation organisationsPost(apiKey, organisation)

Create an organisation

Create an organisation 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsApi();
let apiKey = "apiKey_example"; // String | The API key.
let organisation = new BusinessRegistries.Organisation(); // Organisation | Organisation resource
apiInstance.organisationsPost(apiKey, organisation, (error, data, response) => {
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
 **apiKey** | **String**| The API key. | 
 **organisation** | [**Organisation**](Organisation.md)| Organisation resource | 

### Return type

[**Organisation**](Organisation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

