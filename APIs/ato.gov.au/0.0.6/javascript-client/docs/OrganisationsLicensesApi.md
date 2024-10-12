# BusinessRegistries.OrganisationsLicensesApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organisationsPartyIdLicensesGet**](OrganisationsLicensesApi.md#organisationsPartyIdLicensesGet) | **GET** /organisations/{partyId}/licenses | Retrieve a list of licenses
[**organisationsPartyIdLicensesPost**](OrganisationsLicensesApi.md#organisationsPartyIdLicensesPost) | **POST** /organisations/{partyId}/licenses | Create a license
[**organisationsPartyIdLicensesProductIdDelete**](OrganisationsLicensesApi.md#organisationsPartyIdLicensesProductIdDelete) | **DELETE** /organisations/{partyId}/licenses/{productId} | Delete a license
[**organisationsPartyIdLicensesProductIdGet**](OrganisationsLicensesApi.md#organisationsPartyIdLicensesProductIdGet) | **GET** /organisations/{partyId}/licenses/{productId} | Retrieve a license
[**organisationsPartyIdLicensesProductIdPut**](OrganisationsLicensesApi.md#organisationsPartyIdLicensesProductIdPut) | **PUT** /organisations/{partyId}/licenses/{productId} | Update a license



## organisationsPartyIdLicensesGet

> [License] organisationsPartyIdLicensesGet(apiKey, partyId)

Retrieve a list of licenses

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.organisationsPartyIdLicensesGet(apiKey, partyId, (error, data, response) => {
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


## organisationsPartyIdLicensesPost

> License organisationsPartyIdLicensesPost(apiKey, partyId, license)

Create a license

Create a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let license = new BusinessRegistries.License(); // License | License resource
apiInstance.organisationsPartyIdLicensesPost(apiKey, partyId, license, (error, data, response) => {
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


## organisationsPartyIdLicensesProductIdDelete

> organisationsPartyIdLicensesProductIdDelete(apiKey, partyId, productId)

Delete a license

Delete a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.organisationsPartyIdLicensesProductIdDelete(apiKey, partyId, productId, (error, data, response) => {
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


## organisationsPartyIdLicensesProductIdGet

> License organisationsPartyIdLicensesProductIdGet(apiKey, partyId, productId)

Retrieve a license

Retrieve a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
apiInstance.organisationsPartyIdLicensesProductIdGet(apiKey, partyId, productId, (error, data, response) => {
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


## organisationsPartyIdLicensesProductIdPut

> License organisationsPartyIdLicensesProductIdPut(apiKey, partyId, productId, license)

Update a license

Update a license 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.OrganisationsLicensesApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let productId = "productId_example"; // String | The product identifier.
let license = new BusinessRegistries.License(); // License | License resource
apiInstance.organisationsPartyIdLicensesProductIdPut(apiKey, partyId, productId, license, (error, data, response) => {
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

