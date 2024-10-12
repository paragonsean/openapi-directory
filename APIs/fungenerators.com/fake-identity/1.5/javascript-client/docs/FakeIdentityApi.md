# FakeIdentityGenerationApi.FakeIdentityApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identityCompanyAddressGet**](FakeIdentityApi.md#identityCompanyAddressGet) | **GET** /identity/company/address | 
[**identityCompanyGet**](FakeIdentityApi.md#identityCompanyGet) | **GET** /identity/company | 
[**identityCompanyNameGet**](FakeIdentityApi.md#identityCompanyNameGet) | **GET** /identity/company/name | 
[**identityCompanyPhonenumberGet**](FakeIdentityApi.md#identityCompanyPhonenumberGet) | **GET** /identity/company/phonenumber | 
[**identityPersonAddressGet**](FakeIdentityApi.md#identityPersonAddressGet) | **GET** /identity/person/address | 
[**identityPersonCreditcardGet**](FakeIdentityApi.md#identityPersonCreditcardGet) | **GET** /identity/person/creditcard | 
[**identityPersonEmailGet**](FakeIdentityApi.md#identityPersonEmailGet) | **GET** /identity/person/email | 
[**identityPersonGet**](FakeIdentityApi.md#identityPersonGet) | **GET** /identity/person | 
[**identityPersonNameFirstGet**](FakeIdentityApi.md#identityPersonNameFirstGet) | **GET** /identity/person/name/first | 
[**identityPersonNameGet**](FakeIdentityApi.md#identityPersonNameGet) | **GET** /identity/person/name | 
[**identityPersonNameLastGet**](FakeIdentityApi.md#identityPersonNameLastGet) | **GET** /identity/person/name/last | 
[**identityPersonPhonenumberGet**](FakeIdentityApi.md#identityPersonPhonenumberGet) | **GET** /identity/person/phonenumber | 



## identityCompanyAddressGet

> identityCompanyAddressGet(opts)



Generate postal addresses

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of addresses to return. Defaults to 1.
};
apiInstance.identityCompanyAddressGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of addresses to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityCompanyGet

> identityCompanyGet()



Generate full company identity

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
apiInstance.identityCompanyGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityCompanyNameGet

> identityCompanyNameGet(opts)



Generate company name(s)

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of names to return. Defaults to 1.
};
apiInstance.identityCompanyNameGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of names to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityCompanyPhonenumberGet

> identityCompanyPhonenumberGet(opts)



Generate random company phone number(s)

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of phone numbers to return. Defaults to 1.
};
apiInstance.identityCompanyPhonenumberGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of phone numbers to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonAddressGet

> identityPersonAddressGet(opts)



Generate postal addresses

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of addresses to return. Defaults to 1.
};
apiInstance.identityPersonAddressGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of addresses to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonCreditcardGet

> identityPersonCreditcardGet(opts)



Generate credit card details (number, type, expiration date, name on the card etc).

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of credit card details to return. Defaults to 1.
};
apiInstance.identityPersonCreditcardGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of credit card details to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonEmailGet

> identityPersonEmailGet(opts)



Generate random email ids

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of email ids to return. Defaults to 1.
};
apiInstance.identityPersonEmailGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of email ids to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonGet

> identityPersonGet()



Generate full identity name, phone, email, address, credit card etc.

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
apiInstance.identityPersonGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonNameFirstGet

> identityPersonNameFirstGet(opts)



Generate first name (in a given gender)

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'gender': "gender_example", // String | Gender of the names. If not specified both gender names will be returned.
  'limit': 56 // Number | No of names to return. Defaults to 1.
};
apiInstance.identityPersonNameFirstGet(opts, (error, data, response) => {
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
 **gender** | **String**| Gender of the names. If not specified both gender names will be returned. | [optional] 
 **limit** | **Number**| No of names to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonNameGet

> identityPersonNameGet(opts)



Generate full name(s)

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'gender': "gender_example", // String | Gender of the names. If not specified both gender names will be returned.
  'limit': 56 // Number | No of names to return. Defaults to 1.
};
apiInstance.identityPersonNameGet(opts, (error, data, response) => {
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
 **gender** | **String**| Gender of the names. If not specified both gender names will be returned. | [optional] 
 **limit** | **Number**| No of names to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonNameLastGet

> identityPersonNameLastGet(opts)



Generate last name(s)

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of names to return. Defaults to 1.
};
apiInstance.identityPersonNameLastGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of names to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## identityPersonPhonenumberGet

> identityPersonPhonenumberGet(opts)



Generate random phone number(s)

### Example

```javascript
import FakeIdentityGenerationApi from 'fake_identity_generation_api';
let defaultClient = FakeIdentityGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FakeIdentityGenerationApi.FakeIdentityApi();
let opts = {
  'limit': 56 // Number | No of phone numbers to return. Defaults to 1.
};
apiInstance.identityPersonPhonenumberGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of phone numbers to return. Defaults to 1. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

