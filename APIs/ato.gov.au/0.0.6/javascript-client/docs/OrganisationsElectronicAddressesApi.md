# BusinessRegistries.OrganisationsElectronicAddressesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisationsPartyIdElectronicAddressesAddressIdDelete**](OrganisationsElectronicAddressesApi.md#organisationsPartyIdElectronicAddressesAddressIdDelete) | **DELETE** /organisations/{partyId}/electronic-addresses/{addressId} | Delete an electronic address
[**organisationsPartyIdElectronicAddressesAddressIdGet**](OrganisationsElectronicAddressesApi.md#organisationsPartyIdElectronicAddressesAddressIdGet) | **GET** /organisations/{partyId}/electronic-addresses/{addressId} | Retrieve an electronic address
[**organisationsPartyIdElectronicAddressesAddressIdPut**](OrganisationsElectronicAddressesApi.md#organisationsPartyIdElectronicAddressesAddressIdPut) | **PUT** /organisations/{partyId}/electronic-addresses/{addressId} | Update an electronic address
[**organisationsPartyIdElectronicAddressesGet**](OrganisationsElectronicAddressesApi.md#organisationsPartyIdElectronicAddressesGet) | **GET** /organisations/{partyId}/electronic-addresses | Retrieve a list of electronic addresses
[**organisationsPartyIdElectronicAddressesPost**](OrganisationsElectronicAddressesApi.md#organisationsPartyIdElectronicAddressesPost) | **POST** /organisations/{partyId}/electronic-addresses | Create an electronic address



## organisationsPartyIdElectronicAddressesAddressIdDelete

> organisationsPartyIdElectronicAddressesAddressIdDelete(apiKey, partyId, addressId)

Delete an electronic address

Delete an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.organisationsPartyIdElectronicAddressesAddressIdDelete(apiKey, partyId, addressId, (error, data, response) => {
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


## organisationsPartyIdElectronicAddressesAddressIdGet

> ElectronicAddress organisationsPartyIdElectronicAddressesAddressIdGet(apiKey, partyId, addressId)

Retrieve an electronic address

Retrieve an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.organisationsPartyIdElectronicAddressesAddressIdGet(apiKey, partyId, addressId, (error, data, response) => {
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

[**ElectronicAddress**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdElectronicAddressesAddressIdPut

> ElectronicAddress organisationsPartyIdElectronicAddressesAddressIdPut(apiKey, partyId, addressId, electronicAddress)

Update an electronic address

Update an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
let electronicAddress = new BusinessRegistries.ElectronicAddress(); // ElectronicAddress | Electronic Address resource
apiInstance.organisationsPartyIdElectronicAddressesAddressIdPut(apiKey, partyId, addressId, electronicAddress, (error, data, response) => {
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
 **electronicAddress** | [**ElectronicAddress**](ElectronicAddress.md)| Electronic Address resource | 

### Return type

[**ElectronicAddress**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## organisationsPartyIdElectronicAddressesGet

> [ElectronicAddress] organisationsPartyIdElectronicAddressesGet(apiKey, partyId)

Retrieve a list of electronic addresses

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.organisationsPartyIdElectronicAddressesGet(apiKey, partyId, (error, data, response) => {
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

[**[ElectronicAddress]**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organisationsPartyIdElectronicAddressesPost

> ElectronicAddress organisationsPartyIdElectronicAddressesPost(apiKey, partyId, electronicAddress)

Create an electronic address

Create an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let electronicAddress = new BusinessRegistries.ElectronicAddress(); // ElectronicAddress | Electronic Address resource
apiInstance.organisationsPartyIdElectronicAddressesPost(apiKey, partyId, electronicAddress, (error, data, response) => {
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
 **electronicAddress** | [**ElectronicAddress**](ElectronicAddress.md)| Electronic Address resource | 

### Return type

[**ElectronicAddress**](ElectronicAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

