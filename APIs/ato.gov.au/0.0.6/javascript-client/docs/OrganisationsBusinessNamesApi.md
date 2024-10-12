# BusinessRegistries.OrganisationsBusinessNamesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisationsPartyIdBusinessNamesGet**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesGet) | **GET** /organisations/{partyId}/business-names | Retrieve a list of business names
[**organisationsPartyIdBusinessNamesPost**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesPost) | **POST** /organisations/{partyId}/business-names | Create a business name
[**organisationsPartyIdBusinessNamesProductIdDelete**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesProductIdDelete) | **DELETE** /organisations/{partyId}/business-names/{productId} | Delete a business name
[**organisationsPartyIdBusinessNamesProductIdGet**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesProductIdGet) | **GET** /organisations/{partyId}/business-names/{productId} | Retrieve a business name
[**organisationsPartyIdBusinessNamesProductIdPut**](OrganisationsBusinessNamesApi.md#organisationsPartyIdBusinessNamesProductIdPut) | **PUT** /organisations/{partyId}/business-names/{productId} | Update a business name



## organisationsPartyIdBusinessNamesGet

> [BusinessName] organisationsPartyIdBusinessNamesGet(apiKey, partyId)

Retrieve a list of business names

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.organisationsPartyIdBusinessNamesGet(apiKey, partyId, (error, data, response) => {
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

[**[BusinessName]**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdBusinessNamesPost

> BusinessName organisationsPartyIdBusinessNamesPost(apiKey, partyId, businessName)

Create a business name

Create a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let businessName = new BusinessRegistries.BusinessName(); // BusinessName | Business Name resource
apiInstance.organisationsPartyIdBusinessNamesPost(apiKey, partyId, businessName, (error, data, response) => {
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
 **businessName** | [**BusinessName**](BusinessName.md)| Business Name resource | 

### Return type

[**BusinessName**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organisationsPartyIdBusinessNamesProductIdDelete

> organisationsPartyIdBusinessNamesProductIdDelete(apiKey, partyId, productId)

Delete a business name

Delete a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.organisationsPartyIdBusinessNamesProductIdDelete(apiKey, partyId, productId, (error, data, response) => {
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
 **productId** | **String**| The product identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdBusinessNamesProductIdGet

> BusinessName organisationsPartyIdBusinessNamesProductIdGet(apiKey, partyId, productId)

Retrieve a business name

Retrieve a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.organisationsPartyIdBusinessNamesProductIdGet(apiKey, partyId, productId, (error, data, response) => {
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
 **productId** | **String**| The product identifier. | 

### Return type

[**BusinessName**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdBusinessNamesProductIdPut

> BusinessName organisationsPartyIdBusinessNamesProductIdPut(apiKey, partyId, productId, businessName)

Update a business name

Update a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
let businessName = new BusinessRegistries.BusinessName(); // BusinessName | Business Name resource
apiInstance.organisationsPartyIdBusinessNamesProductIdPut(apiKey, partyId, productId, businessName, (error, data, response) => {
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
 **productId** | **String**| The product identifier. | 
 **businessName** | [**BusinessName**](BusinessName.md)| Business Name resource | 

### Return type

[**BusinessName**](BusinessName.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

