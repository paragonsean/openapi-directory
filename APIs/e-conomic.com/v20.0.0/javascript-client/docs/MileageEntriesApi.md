# VismaEConomicOpenApi.MileageEntriesApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approveMileageEntries_0**](MileageEntriesApi.md#approveMileageEntries_0) | **POST** /mileages/approve | Approve a list of Mileage entries
[**createMileage**](MileageEntriesApi.md#createMileage) | **POST** /mileages | Create a single Mileage entry
[**deleteMileageById**](MileageEntriesApi.md#deleteMileageById) | **DELETE** /mileages/{number} | Delete single Mileage entry
[**getAllMileageEntries**](MileageEntriesApi.md#getAllMileageEntries) | **GET** /mileages | Retrieve all Mileage entries
[**getMileageById**](MileageEntriesApi.md#getMileageById) | **GET** /mileages/{number} | Retrieve single Mileage entry
[**getNumberOfMileageEntries**](MileageEntriesApi.md#getNumberOfMileageEntries) | **GET** /mileages/count | Retrieve the number of Mileage entries
[**getPageOfMileageEntries**](MileageEntriesApi.md#getPageOfMileageEntries) | **GET** /mileages/paged | Retrieve a page of Mileage entries
[**updateMileage**](MileageEntriesApi.md#updateMileage) | **PUT** /mileages | Update a single Mileage entry



## approveMileageEntries_0

> approveMileageEntries_0(opts)

Approve a list of Mileage entries

Use this endpoint to approve a list of Mileage entries.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let opts = {
  'mileageNumbersCollection': new VismaEConomicOpenApi.MileageNumbersCollection() // MileageNumbersCollection | 
};
apiInstance.approveMileageEntries_0(opts, (error, data, response) => {
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
 **mileageNumbersCollection** | [**MileageNumbersCollection**](MileageNumbersCollection.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## createMileage

> CreatedResult createMileage(opts)

Create a single Mileage entry

Use this endpoint to create a single Mileage entry.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let opts = {
  'mileage': new VismaEConomicOpenApi.Mileage() // Mileage | 
};
apiInstance.createMileage(opts, (error, data, response) => {
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
 **mileage** | [**Mileage**](Mileage.md)|  | [optional] 

### Return type

[**CreatedResult**](CreatedResult.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## deleteMileageById

> deleteMileageById(number)

Delete single Mileage entry

Use this endpoint to delete a single Mileage entry by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let number = 56; // Number | 
apiInstance.deleteMileageById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllMileageEntries

> MileageCursorResults getAllMileageEntries(opts)

Retrieve all Mileage entries

Use this endpoint to retrieve all Mileage entries in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'filter': "filter_example" // String | 
};
apiInstance.getAllMileageEntries(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **filter** | **String**|  | [optional] 

### Return type

[**MileageCursorResults**](MileageCursorResults.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMileageById

> Mileage getMileageById(number)

Retrieve single Mileage entry

Use this endpoint to load a single Mileage entry by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let number = 56; // Number | 
apiInstance.getMileageById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

[**Mileage**](Mileage.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumberOfMileageEntries

> Number getNumberOfMileageEntries(opts)

Retrieve the number of Mileage entries

Call this endpoint to get the number of Mileage entries. You can use a filtering as well.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let opts = {
  'filter': "filter_example" // String | 
};
apiInstance.getNumberOfMileageEntries(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 

### Return type

**Number**

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPageOfMileageEntries

> [Mileage] getPageOfMileageEntries(opts)

Retrieve a page of Mileage entries

Use this endpoint to load a page of Mileage entries.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let opts = {
  'filter': "filter_example", // String | 
  'sort': "sort_example", // String | 
  'pageSize': 20, // Number | 
  'skipPages': 0 // Number | 
};
apiInstance.getPageOfMileageEntries(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] [default to 20]
 **skipPages** | **Number**|  | [optional] [default to 0]

### Return type

[**[Mileage]**](Mileage.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMileage

> updateMileage(opts)

Update a single Mileage entry

Use this endpoint to update a single Mileage entry.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileageEntriesApi();
let opts = {
  'mileage': new VismaEConomicOpenApi.Mileage() // Mileage | 
};
apiInstance.updateMileage(opts, (error, data, response) => {
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
 **mileage** | [**Mileage**](Mileage.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

