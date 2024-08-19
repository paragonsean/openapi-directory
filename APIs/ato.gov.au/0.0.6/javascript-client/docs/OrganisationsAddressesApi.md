# BusinessRegistries.OrganisationsAddressesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisationsPartyIdAddressesAddressIdDelete**](OrganisationsAddressesApi.md#organisationsPartyIdAddressesAddressIdDelete) | **DELETE** /organisations/{partyId}/addresses/{addressId} | Delete an address
[**organisationsPartyIdAddressesAddressIdGet**](OrganisationsAddressesApi.md#organisationsPartyIdAddressesAddressIdGet) | **GET** /organisations/{partyId}/addresses/{addressId} | Retrieve an address
[**organisationsPartyIdAddressesAddressIdPut**](OrganisationsAddressesApi.md#organisationsPartyIdAddressesAddressIdPut) | **PUT** /organisations/{partyId}/addresses/{addressId} | Update an address
[**organisationsPartyIdAddressesGet**](OrganisationsAddressesApi.md#organisationsPartyIdAddressesGet) | **GET** /organisations/{partyId}/addresses | Retrieve a list of addresses
[**organisationsPartyIdAddressesPost**](OrganisationsAddressesApi.md#organisationsPartyIdAddressesPost) | **POST** /organisations/{partyId}/addresses | Create an address



## organisationsPartyIdAddressesAddressIdDelete

> organisationsPartyIdAddressesAddressIdDelete(apiKey, partyId, addressId)

Delete an address

Delete an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.organisationsPartyIdAddressesAddressIdDelete(apiKey, partyId, addressId, (error, data, response) => {
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
 **addressId** | **String**| The address identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdAddressesAddressIdGet

> Address organisationsPartyIdAddressesAddressIdGet(apiKey, partyId, addressId)

Retrieve an address

Retrieve an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.organisationsPartyIdAddressesAddressIdGet(apiKey, partyId, addressId, (error, data, response) => {
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
 **addressId** | **String**| The address identifier. | 

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdAddressesAddressIdPut

> Address organisationsPartyIdAddressesAddressIdPut(apiKey, partyId, addressId, address)

Update an address

Update an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
let address = new BusinessRegistries.Address(); // Address | Address resource
apiInstance.organisationsPartyIdAddressesAddressIdPut(apiKey, partyId, addressId, address, (error, data, response) => {
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
 **addressId** | **String**| The address identifier. | 
 **address** | [**Address**](Address.md)| Address resource | 

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organisationsPartyIdAddressesGet

> [Address] organisationsPartyIdAddressesGet(apiKey, partyId)

Retrieve a list of addresses

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.organisationsPartyIdAddressesGet(apiKey, partyId, (error, data, response) => {
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

[**[Address]**](Address.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdAddressesPost

> Address organisationsPartyIdAddressesPost(apiKey, partyId, address)

Create an address

Create an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let address = new BusinessRegistries.Address(); // Address | Address resource
apiInstance.organisationsPartyIdAddressesPost(apiKey, partyId, address, (error, data, response) => {
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
 **address** | [**Address**](Address.md)| Address resource | 

### Return type

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

