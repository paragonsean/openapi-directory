# BusinessRegistries.IndividualsLicensesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**individualsPartyIdLicensesGet**](IndividualsLicensesApi.md#individualsPartyIdLicensesGet) | **GET** /individuals/{partyId}/licenses | Retrieve a list of licenses
[**individualsPartyIdLicensesPost**](IndividualsLicensesApi.md#individualsPartyIdLicensesPost) | **POST** /individuals/{partyId}/licenses | Create a license
[**individualsPartyIdLicensesProductIdDelete**](IndividualsLicensesApi.md#individualsPartyIdLicensesProductIdDelete) | **DELETE** /individuals/{partyId}/licenses/{productId} | Delete a license
[**individualsPartyIdLicensesProductIdGet**](IndividualsLicensesApi.md#individualsPartyIdLicensesProductIdGet) | **GET** /individuals/{partyId}/licenses/{productId} | Retrieve a license
[**individualsPartyIdLicensesProductIdPut**](IndividualsLicensesApi.md#individualsPartyIdLicensesProductIdPut) | **PUT** /individuals/{partyId}/licenses/{productId} | Update a license



## individualsPartyIdLicensesGet

> [License] individualsPartyIdLicensesGet(apiKey, partyId)

Retrieve a list of licenses

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.individualsPartyIdLicensesGet(apiKey, partyId, (error, data, response) => {
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

[**[License]**](License.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## individualsPartyIdLicensesPost

> License individualsPartyIdLicensesPost(apiKey, partyId, license)

Create a license

Create a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let license = new BusinessRegistries.License(); // License | License resource
apiInstance.individualsPartyIdLicensesPost(apiKey, partyId, license, (error, data, response) => {
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
 **license** | [**License**](License.md)| License resource | 

### Return type

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## individualsPartyIdLicensesProductIdDelete

> individualsPartyIdLicensesProductIdDelete(apiKey, partyId, productId)

Delete a license

Delete a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.individualsPartyIdLicensesProductIdDelete(apiKey, partyId, productId, (error, data, response) => {
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


## individualsPartyIdLicensesProductIdGet

> License individualsPartyIdLicensesProductIdGet(apiKey, partyId, productId)

Retrieve a license

Retrieve a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.individualsPartyIdLicensesProductIdGet(apiKey, partyId, productId, (error, data, response) => {
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

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## individualsPartyIdLicensesProductIdPut

> License individualsPartyIdLicensesProductIdPut(apiKey, partyId, productId, license)

Update a license

Update a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
let license = new BusinessRegistries.License(); // License | License resource
apiInstance.individualsPartyIdLicensesProductIdPut(apiKey, partyId, productId, license, (error, data, response) => {
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
 **license** | [**License**](License.md)| License resource | 

### Return type

[**License**](License.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

