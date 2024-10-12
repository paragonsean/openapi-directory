# BusinessRegistries.IndividualsAddressesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**individualsPartyIdAddressesAddressIdDelete**](IndividualsAddressesApi.md#individualsPartyIdAddressesAddressIdDelete) | **DELETE** /individuals/{partyId}/addresses/{addressId} | Delete an address
[**individualsPartyIdAddressesAddressIdGet**](IndividualsAddressesApi.md#individualsPartyIdAddressesAddressIdGet) | **GET** /individuals/{partyId}/addresses/{addressId} | Retrieve an address
[**individualsPartyIdAddressesAddressIdPut**](IndividualsAddressesApi.md#individualsPartyIdAddressesAddressIdPut) | **PUT** /individuals/{partyId}/addresses/{addressId} | Update an address
[**individualsPartyIdAddressesGet**](IndividualsAddressesApi.md#individualsPartyIdAddressesGet) | **GET** /individuals/{partyId}/addresses | Retrieve a list of addresses
[**individualsPartyIdAddressesPost**](IndividualsAddressesApi.md#individualsPartyIdAddressesPost) | **POST** /individuals/{partyId}/addresses | Create an address



## individualsPartyIdAddressesAddressIdDelete

> individualsPartyIdAddressesAddressIdDelete(apiKey, partyId, addressId)

Delete an address

Delete an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.individualsPartyIdAddressesAddressIdDelete(apiKey, partyId, addressId, (error, data, response) => {
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


## individualsPartyIdAddressesAddressIdGet

> Address individualsPartyIdAddressesAddressIdGet(apiKey, partyId, addressId)

Retrieve an address

Retrieve an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
apiInstance.individualsPartyIdAddressesAddressIdGet(apiKey, partyId, addressId, (error, data, response) => {
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


## individualsPartyIdAddressesAddressIdPut

> Address individualsPartyIdAddressesAddressIdPut(apiKey, partyId, addressId, address)

Update an address

Update an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let addressId = "addressId_example"; // String | The address identifier.
let address = new BusinessRegistries.Address(); // Address | Address resource
apiInstance.individualsPartyIdAddressesAddressIdPut(apiKey, partyId, addressId, address, (error, data, response) => {
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


## individualsPartyIdAddressesGet

> [Address] individualsPartyIdAddressesGet(apiKey, partyId)

Retrieve a list of addresses

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.individualsPartyIdAddressesGet(apiKey, partyId, (error, data, response) => {
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


## individualsPartyIdAddressesPost

> Address individualsPartyIdAddressesPost(apiKey, partyId, address)

Create an address

Create an address 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsAddressesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let address = new BusinessRegistries.Address(); // Address | Address resource
apiInstance.individualsPartyIdAddressesPost(apiKey, partyId, address, (error, data, response) => {
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

