# BusinessRegistries.IndividualsBusinessNamesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**individualsPartyIdBusinessNamesGet**](IndividualsBusinessNamesApi.md#individualsPartyIdBusinessNamesGet) | **GET** /individuals/{partyId}/business-names | Retrieve a list of business names
[**individualsPartyIdBusinessNamesPost**](IndividualsBusinessNamesApi.md#individualsPartyIdBusinessNamesPost) | **POST** /individuals/{partyId}/business-names | Create a business name
[**individualsPartyIdBusinessNamesProductIdDelete**](IndividualsBusinessNamesApi.md#individualsPartyIdBusinessNamesProductIdDelete) | **DELETE** /individuals/{partyId}/business-names/{productId} | Delete a business name
[**individualsPartyIdBusinessNamesProductIdGet**](IndividualsBusinessNamesApi.md#individualsPartyIdBusinessNamesProductIdGet) | **GET** /individuals/{partyId}/business-names/{productId} | Retrieve a business name
[**individualsPartyIdBusinessNamesProductIdPut**](IndividualsBusinessNamesApi.md#individualsPartyIdBusinessNamesProductIdPut) | **PUT** /individuals/{partyId}/business-names/{productId} | Update a business name



## individualsPartyIdBusinessNamesGet

> [BusinessName] individualsPartyIdBusinessNamesGet(apiKey, partyId)

Retrieve a list of business names

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.individualsPartyIdBusinessNamesGet(apiKey, partyId, (error, data, response) => {
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


## individualsPartyIdBusinessNamesPost

> BusinessName individualsPartyIdBusinessNamesPost(apiKey, partyId, businessName)

Create a business name

Create a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let businessName = new BusinessRegistries.BusinessName(); // BusinessName | Business Name resource
apiInstance.individualsPartyIdBusinessNamesPost(apiKey, partyId, businessName, (error, data, response) => {
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


## individualsPartyIdBusinessNamesProductIdDelete

> individualsPartyIdBusinessNamesProductIdDelete(apiKey, partyId, productId)

Delete a business name

Delete a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.individualsPartyIdBusinessNamesProductIdDelete(apiKey, partyId, productId, (error, data, response) => {
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


## individualsPartyIdBusinessNamesProductIdGet

> BusinessName individualsPartyIdBusinessNamesProductIdGet(apiKey, partyId, productId)

Retrieve a business name

Retrieve a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.individualsPartyIdBusinessNamesProductIdGet(apiKey, partyId, productId, (error, data, response) => {
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


## individualsPartyIdBusinessNamesProductIdPut

> BusinessName individualsPartyIdBusinessNamesProductIdPut(apiKey, partyId, productId, businessName)

Update a business name

Update a business name 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsBusinessNamesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
let businessName = new BusinessRegistries.BusinessName(); // BusinessName | Business Name resource
apiInstance.individualsPartyIdBusinessNamesProductIdPut(apiKey, partyId, productId, businessName, (error, data, response) => {
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

