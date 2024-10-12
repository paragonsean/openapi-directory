# Apacta.MaterialRentalsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**materialsMaterialIdRentalsCheckoutPost**](MaterialRentalsApi.md#materialsMaterialIdRentalsCheckoutPost) | **POST** /materials/{material_id}/rentals/checkout/ | Checkout material rental
[**materialsMaterialIdRentalsGet**](MaterialRentalsApi.md#materialsMaterialIdRentalsGet) | **GET** /materials/{material_id}/rentals/ | Show list of rentals for specific material
[**materialsMaterialIdRentalsMaterialRentalIdDelete**](MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdDelete) | **DELETE** /materials/{material_id}/rentals/{material_rental_id}/ | Delete material rental
[**materialsMaterialIdRentalsMaterialRentalIdGet**](MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdGet) | **GET** /materials/{material_id}/rentals/{material_rental_id}/ | Show rental foor materi
[**materialsMaterialIdRentalsMaterialRentalIdPut**](MaterialRentalsApi.md#materialsMaterialIdRentalsMaterialRentalIdPut) | **PUT** /materials/{material_id}/rentals/{material_rental_id}/ | Edit material rental
[**materialsMaterialIdRentalsPost**](MaterialRentalsApi.md#materialsMaterialIdRentalsPost) | **POST** /materials/{material_id}/rentals/ | Add material rental



## materialsMaterialIdRentalsCheckoutPost

> ClockingRecordsPost201Response materialsMaterialIdRentalsCheckoutPost(materialId, opts)

Checkout material rental

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MaterialRentalsApi();
let materialId = "materialId_example"; // String | 
let opts = {
  'materialsMaterialIdRentalsCheckoutPostRequest': new Apacta.MaterialsMaterialIdRentalsCheckoutPostRequest() // MaterialsMaterialIdRentalsCheckoutPostRequest | 
};
apiInstance.materialsMaterialIdRentalsCheckoutPost(materialId, opts, (error, data, response) => {
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
 **materialId** | **String**|  | 
 **materialsMaterialIdRentalsCheckoutPostRequest** | [**MaterialsMaterialIdRentalsCheckoutPostRequest**](MaterialsMaterialIdRentalsCheckoutPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## materialsMaterialIdRentalsGet

> MaterialsMaterialIdRentalsGet200Response materialsMaterialIdRentalsGet(materialId)

Show list of rentals for specific material

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MaterialRentalsApi();
let materialId = "materialId_example"; // String | 
apiInstance.materialsMaterialIdRentalsGet(materialId, (error, data, response) => {
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
 **materialId** | **String**|  | 

### Return type

[**MaterialsMaterialIdRentalsGet200Response**](MaterialsMaterialIdRentalsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## materialsMaterialIdRentalsMaterialRentalIdDelete

> ExpenseFilesExpenseFileIdPut200Response materialsMaterialIdRentalsMaterialRentalIdDelete(materialId, materialRentalId)

Delete material rental

Delete rental for material

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MaterialRentalsApi();
let materialId = "materialId_example"; // String | 
let materialRentalId = "materialRentalId_example"; // String | 
apiInstance.materialsMaterialIdRentalsMaterialRentalIdDelete(materialId, materialRentalId, (error, data, response) => {
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
 **materialId** | **String**|  | 
 **materialRentalId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## materialsMaterialIdRentalsMaterialRentalIdGet

> MaterialsMaterialIdRentalsMaterialRentalIdGet200Response materialsMaterialIdRentalsMaterialRentalIdGet(materialId, materialRentalId)

Show rental foor materi

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MaterialRentalsApi();
let materialId = "materialId_example"; // String | 
let materialRentalId = "materialRentalId_example"; // String | 
apiInstance.materialsMaterialIdRentalsMaterialRentalIdGet(materialId, materialRentalId, (error, data, response) => {
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
 **materialId** | **String**|  | 
 **materialRentalId** | **String**|  | 

### Return type

[**MaterialsMaterialIdRentalsMaterialRentalIdGet200Response**](MaterialsMaterialIdRentalsMaterialRentalIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## materialsMaterialIdRentalsMaterialRentalIdPut

> ExpenseFilesExpenseFileIdPut200Response materialsMaterialIdRentalsMaterialRentalIdPut(materialId, materialRentalId)

Edit material rental

Edit material rental

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MaterialRentalsApi();
let materialId = "materialId_example"; // String | 
let materialRentalId = "materialRentalId_example"; // String | 
apiInstance.materialsMaterialIdRentalsMaterialRentalIdPut(materialId, materialRentalId, (error, data, response) => {
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
 **materialId** | **String**|  | 
 **materialRentalId** | **String**|  | 

### Return type

[**ExpenseFilesExpenseFileIdPut200Response**](ExpenseFilesExpenseFileIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## materialsMaterialIdRentalsPost

> ClockingRecordsPost201Response materialsMaterialIdRentalsPost(materialId, opts)

Add material rental

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.MaterialRentalsApi();
let materialId = "materialId_example"; // String | 
let opts = {
  'materialsMaterialIdRentalsPostRequest': new Apacta.MaterialsMaterialIdRentalsPostRequest() // MaterialsMaterialIdRentalsPostRequest | 
};
apiInstance.materialsMaterialIdRentalsPost(materialId, opts, (error, data, response) => {
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
 **materialId** | **String**|  | 
 **materialsMaterialIdRentalsPostRequest** | [**MaterialsMaterialIdRentalsPostRequest**](MaterialsMaterialIdRentalsPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

