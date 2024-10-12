# BusinessRegistries.IndividualsElectronicAddressesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**individualsPartyIdElectronicAddressesAddressIdDelete**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesAddressIdDelete) | **DELETE** /individuals/{partyId}/electronic-addresses/{addressId} | Delete an electronic address
[**individualsPartyIdElectronicAddressesAddressIdGet**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesAddressIdGet) | **GET** /individuals/{partyId}/electronic-addresses/{addressId} | Retrieve an electronic address
[**individualsPartyIdElectronicAddressesAddressIdPut**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesAddressIdPut) | **PUT** /individuals/{partyId}/electronic-addresses/{addressId} | Update an electronic address
[**individualsPartyIdElectronicAddressesGet**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesGet) | **GET** /individuals/{partyId}/electronic-addresses | Retrieve a list of electronic addresses
[**individualsPartyIdElectronicAddressesPost**](IndividualsElectronicAddressesApi.md#individualsPartyIdElectronicAddressesPost) | **POST** /individuals/{partyId}/electronic-addresses | Create an electronic address



## individualsPartyIdElectronicAddressesAddressIdDelete

> individualsPartyIdElectronicAddressesAddressIdDelete(apiKey, partyId, addressId)

Delete an electronic address

Delete an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.individualsPartyIdElectronicAddressesAddressIdDelete(apiKey, partyId, addressId, (error, data, response) => {
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


## individualsPartyIdElectronicAddressesAddressIdGet

> ElectronicAddress individualsPartyIdElectronicAddressesAddressIdGet(apiKey, partyId, addressId)

Retrieve an electronic address

Retrieve an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.individualsPartyIdElectronicAddressesAddressIdGet(apiKey, partyId, addressId, (error, data, response) => {
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


## individualsPartyIdElectronicAddressesAddressIdPut

> ElectronicAddress individualsPartyIdElectronicAddressesAddressIdPut(apiKey, partyId, addressId, electronicAddress)

Update an electronic address

Update an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
let electronicAddress = new BusinessRegistries.ElectronicAddress(); // ElectronicAddress | Electronic Address resource
apiInstance.individualsPartyIdElectronicAddressesAddressIdPut(apiKey, partyId, addressId, electronicAddress, (error, data, response) => {
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


## individualsPartyIdElectronicAddressesGet

> [ElectronicAddress] individualsPartyIdElectronicAddressesGet(apiKey, partyId)

Retrieve a list of electronic addresses

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.individualsPartyIdElectronicAddressesGet(apiKey, partyId, (error, data, response) => {
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


## individualsPartyIdElectronicAddressesPost

> ElectronicAddress individualsPartyIdElectronicAddressesPost(apiKey, partyId, electronicAddress)

Create an electronic address

Create an electronic address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsElectronicAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let electronicAddress = new BusinessRegistries.ElectronicAddress(); // ElectronicAddress | Electronic Address resource
apiInstance.individualsPartyIdElectronicAddressesPost(apiKey, partyId, electronicAddress, (error, data, response) => {
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

