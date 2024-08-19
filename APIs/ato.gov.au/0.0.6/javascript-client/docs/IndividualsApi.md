# BusinessRegistries.IndividualsApi

All URIs are relative to *http://api.abr.ato.gov.au*

Method | HTTP request | Description
------------- | ------------- | -------------
[**individualsGet**](IndividualsApi.md#individualsGet) | **GET** /individuals | Retrieve a list of individuals
[**individualsPartyIdDelete**](IndividualsApi.md#individualsPartyIdDelete) | **DELETE** /individuals/{partyId} | Delete an individual
[**individualsPartyIdGet**](IndividualsApi.md#individualsPartyIdGet) | **GET** /individuals/{partyId} | Retrieve an individual
[**individualsPartyIdPut**](IndividualsApi.md#individualsPartyIdPut) | **PUT** /individuals/{partyId} | Update an individual
[**individualsPost**](IndividualsApi.md#individualsPost) | **POST** /individuals | Create an individual



## individualsGet

> [Individual] individualsGet(apiKey, opts)

Retrieve a list of individuals

Retrieve a list of individuals 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsApi();
let apiKey = "apiKey_example"; // String | The API key.
let opts = {
  'dateOfBirth': "dateOfBirth_example", // String | The individual's date of birth, for example, `1979-01-13` (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format).
  'placeOfBirth': "placeOfBirth_example" // String | The individual's place of birth, for example, `Tamworth`.
};
apiInstance.individualsGet(apiKey, opts, (error, data, response) => {
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
 **dateOfBirth** | **String**| The individual&#39;s date of birth, for example, &#x60;1979-01-13&#x60; (in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format). | [optional] 
 **placeOfBirth** | **String**| The individual&#39;s place of birth, for example, &#x60;Tamworth&#x60;. | [optional] 

### Return type

[**[Individual]**](Individual.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## individualsPartyIdDelete

> individualsPartyIdDelete(apiKey, partyId)

Delete an individual

Delete an individual with the specified identifier 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.individualsPartyIdDelete(apiKey, partyId, (error, data, response) => {
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


## individualsPartyIdGet

> Individual individualsPartyIdGet(apiKey, partyId)

Retrieve an individual

Retrieve an individual with the specified identifier 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
apiInstance.individualsPartyIdGet(apiKey, partyId, (error, data, response) => {
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

[**Individual**](Individual.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## individualsPartyIdPut

> Individual individualsPartyIdPut(apiKey, partyId, individual)

Update an individual

Update an individual 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsApi();
let apiKey = "apiKey_example"; // String | The API key.
let partyId = "partyId_example"; // String | The party identifier.
let individual = new BusinessRegistries.Individual(); // Individual | Individual resource
apiInstance.individualsPartyIdPut(apiKey, partyId, individual, (error, data, response) => {
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
 **individual** | [**Individual**](Individual.md)| Individual resource | 

### Return type

[**Individual**](Individual.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## individualsPost

> Individual individualsPost(apiKey, individual)

Create an individual

Create an individual 

### Example

```javascript
import BusinessRegistries from 'business_registries';

let apiInstance = new BusinessRegistries.IndividualsApi();
let apiKey = "apiKey_example"; // String | The API key.
let individual = new BusinessRegistries.Individual(); // Individual | Individual resource
apiInstance.individualsPost(apiKey, individual, (error, data, response) => {
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
 **individual** | [**Individual**](Individual.md)| Individual resource | 

### Return type

[**Individual**](Individual.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

