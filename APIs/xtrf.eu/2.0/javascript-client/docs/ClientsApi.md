# XtrfHomePortalApi.ClientsApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create2**](ClientsApi.md#create2) | **POST** /customers/persons | Creates a new person.
[**create3**](ClientsApi.md#create3) | **POST** /customers | Creates a new client.
[**delete3**](ClientsApi.md#delete3) | **DELETE** /customers/persons/{personId} | Removes a person.
[**delete4**](ClientsApi.md#delete4) | **DELETE** /customers/priceLists/{priceListId} | Removes a customer price list.
[**delete5**](ClientsApi.md#delete5) | **DELETE** /customers/{customerId} | Removes a client.
[**generateSingleUseSignInToken**](ClientsApi.md#generateSingleUseSignInToken) | **POST** /customers/persons/accessToken | Generates a single use sign-in token.
[**getAddress**](ClientsApi.md#getAddress) | **GET** /customers/{customerId}/address | Returns address of a given client.
[**getAllIds1**](ClientsApi.md#getAllIds1) | **GET** /customers/persons/ids | Returns persons&#39; internal identifiers.
[**getAllIds2**](ClientsApi.md#getAllIds2) | **GET** /customers/ids | Returns clients&#39; internal identifiers.
[**getAllNamesWithIds**](ClientsApi.md#getAllNamesWithIds) | **GET** /customers | Returns list of simple clients representations
[**getById1**](ClientsApi.md#getById1) | **GET** /customers/persons/{personId} | Returns person details.
[**getById2**](ClientsApi.md#getById2) | **GET** /customers/{customerId} | Returns client details.
[**getCategories**](ClientsApi.md#getCategories) | **GET** /customers/{customerId}/categories | Returns categories of a given client.
[**getContact**](ClientsApi.md#getContact) | **GET** /customers/persons/{personId}/contact | Returns contact of a given person.
[**getContact1**](ClientsApi.md#getContact1) | **GET** /customers/{customerId}/contact | Returns contact of a given client.
[**getCorrespondenceAddress**](ClientsApi.md#getCorrespondenceAddress) | **GET** /customers/{customerId}/correspondenceAddress | Returns correspondence address of a given client.
[**getCustomField**](ClientsApi.md#getCustomField) | **GET** /customers/{customerId}/customFields/{customFieldKey} | Returns custom field of a given client.
[**getCustomFields**](ClientsApi.md#getCustomFields) | **GET** /customers/persons/{personId}/customFields | Returns custom fields of a given person.
[**getCustomFields1**](ClientsApi.md#getCustomFields1) | **GET** /customers/{customerId}/customFields | Returns custom fields of a given client.
[**getIndustries**](ClientsApi.md#getIndustries) | **GET** /customers/{customerId}/industries | Returns industries of a given client.
[**update1**](ClientsApi.md#update1) | **PUT** /customers/persons/{personId} | Updates an existing person.
[**update2**](ClientsApi.md#update2) | **PUT** /customers/{customerId} | Updates an existing client.
[**updateAddress**](ClientsApi.md#updateAddress) | **PUT** /customers/{customerId}/address | Updates address of a given client.
[**updateCategories**](ClientsApi.md#updateCategories) | **PUT** /customers/{customerId}/categories | Updates categories of a given client.
[**updateContact**](ClientsApi.md#updateContact) | **PUT** /customers/persons/{personId}/contact | Updates contact of a given person.
[**updateContact1**](ClientsApi.md#updateContact1) | **PUT** /customers/{customerId}/contact | Updates contact of a given client.
[**updateCorrespondenceAddress**](ClientsApi.md#updateCorrespondenceAddress) | **PUT** /customers/{customerId}/correspondenceAddress | Updates correspondence address of a given client.
[**updateCustomField**](ClientsApi.md#updateCustomField) | **PUT** /customers/{customerId}/customFields/{customFieldKey} | Updates given custom field of a given client.
[**updateCustomFields**](ClientsApi.md#updateCustomFields) | **PUT** /customers/persons/{personId}/customFields | Updates custom fields of a given person.
[**updateCustomFields1**](ClientsApi.md#updateCustomFields1) | **PUT** /customers/{customerId}/customFields | Updates custom fields of a given client.
[**updateIndustries**](ClientsApi.md#updateIndustries) | **PUT** /customers/{customerId}/industries | Updates industries of a given client.



## create2

> CustomerPersonDTO create2(customerPersonDTO)

Creates a new person.

Creates a new person. Required fields are presented in the example. Other fields (from PUT) may also be specified here.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerPersonDTO = /home-api/assets/examples/customers/persons/create.json#requestBody; // CustomerPersonDTO | Brand new person.
apiInstance.create2(customerPersonDTO, (error, data, response) => {
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
 **customerPersonDTO** | [**CustomerPersonDTO**](CustomerPersonDTO.md)| Brand new person. | 

### Return type

[**CustomerPersonDTO**](CustomerPersonDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## create3

> CustomerDTO create3(customerDTO)

Creates a new client.

Creates a new client. All available fields are presented in PUT request.&lt;p&gt;   Required fields:   &lt;ul&gt;     &lt;li&gt;name&lt;/li&gt;     &lt;li&gt;fullName&lt;/li&gt;     &lt;li&gt;contact -&gt; emails -&gt; primary&lt;/li&gt;   &lt;/ul&gt; &lt;/p&gt; 

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerDTO = /home-api/assets/examples/customers/create.json#requestBody; // CustomerDTO | Created user object
apiInstance.create3(customerDTO, (error, data, response) => {
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
 **customerDTO** | [**CustomerDTO**](CustomerDTO.md)| Created user object | 

### Return type

[**CustomerDTO**](CustomerDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## delete3

> delete3(personId)

Removes a person.

Removes a person.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let personId = 789; // Number | person's internal identifier
apiInstance.delete3(personId, (error, data, response) => {
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
 **personId** | **Number**| person&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delete4

> delete4(priceListId)

Removes a customer price list.

Removes a customer price list.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let priceListId = 789; // Number | customer price list's internal identifier
apiInstance.delete4(priceListId, (error, data, response) => {
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
 **priceListId** | **Number**| customer price list&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delete5

> delete5(customerId)

Removes a client.

Removes a client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
apiInstance.delete5(customerId, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## generateSingleUseSignInToken

> AccessTokenDTO generateSingleUseSignInToken(accessTokenRequestDTO)

Generates a single use sign-in token.

Generates a single use sign-in token for the customer person found for given login or e-mail. Returns &#39;url&#39; and &#39;token&#39; which allows to sign-in to customer portal as this person. Token is valid for two minutes and can be used only once. To sign-in to customer portal you should post &#39;token&#39; provided as the &#39;accessToken&#39; form param to the &#39;url&#39; using POST method.Detailed description is available in the Customer API &lt;a href&#x3D;\&quot;/api-doc/customer-api/authentication\&quot;&gt;authentication&lt;/a&gt;.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let accessTokenRequestDTO = /home-api/assets/examples/customers/persons/generateSingleUseSignInToken.json#requestBody; // AccessTokenRequestDTO | Generated sign-in token.
apiInstance.generateSingleUseSignInToken(accessTokenRequestDTO, (error, data, response) => {
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
 **accessTokenRequestDTO** | [**AccessTokenRequestDTO**](AccessTokenRequestDTO.md)| Generated sign-in token. | 

### Return type

[**AccessTokenDTO**](AccessTokenDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getAddress

> AddressDTO getAddress(customerId)

Returns address of a given client.

Returns address of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
apiInstance.getAddress(customerId, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 

### Return type

[**AddressDTO**](AddressDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getAllIds1

> [Number] getAllIds1(opts)

Returns persons&#39; internal identifiers.

Returns persons&#39; internal identifiers.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let opts = {
  'updatedSince': 789 // Number | only persons modified since this timestamp
};
apiInstance.getAllIds1(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only persons modified since this timestamp | [optional] 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getAllIds2

> [Number] getAllIds2(opts)

Returns clients&#39; internal identifiers.

Returns clients&#39; internal identifiers.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let opts = {
  'updatedSince': 789, // Number | only clients modified since this timestamp
  'nameEquals': "nameEquals_example", // String | exact name of client
  'emailEquals': "emailEquals_example" // String | exact email of client
};
apiInstance.getAllIds2(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only clients modified since this timestamp | [optional] 
 **nameEquals** | **String**| exact name of client | [optional] 
 **emailEquals** | **String**| exact email of client | [optional] 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getAllNamesWithIds

> [EntityWithNameDTO] getAllNamesWithIds(opts)

Returns list of simple clients representations

Returns list of simple clients representations

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let opts = {
  'updatedSince': 789 // Number | only clients modified since this timestamp
};
apiInstance.getAllNamesWithIds(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only clients modified since this timestamp | [optional] 

### Return type

[**[EntityWithNameDTO]**](EntityWithNameDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getById1

> CustomerPersonDTO getById1(personId)

Returns person details.

Returns person details.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let personId = 789; // Number | person's internal identifier
apiInstance.getById1(personId, (error, data, response) => {
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
 **personId** | **Number**| person&#39;s internal identifier | 

### Return type

[**CustomerPersonDTO**](CustomerPersonDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getById2

> CustomerDTO getById2(customerId, opts)

Returns client details.

Returns client details.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let opts = {
  'embed': "embed_example" // String | list of additional fields which should be embedded in the response (available options: persons)
};
apiInstance.getById2(customerId, opts, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **embed** | **String**| list of additional fields which should be embedded in the response (available options: persons) | [optional] 

### Return type

[**CustomerDTO**](CustomerDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCategories

> [Number] getCategories(customerId)

Returns categories of a given client.

Returns categories of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
apiInstance.getCategories(customerId, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getContact

> PersonContactDTO getContact(personId)

Returns contact of a given person.

Returns contact of a given person.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let personId = 789; // Number | person's internal identifier
apiInstance.getContact(personId, (error, data, response) => {
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
 **personId** | **Number**| person&#39;s internal identifier | 

### Return type

[**PersonContactDTO**](PersonContactDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getContact1

> ContactDTO getContact1(customerId)

Returns contact of a given client.

Returns contact of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
apiInstance.getContact1(customerId, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 

### Return type

[**ContactDTO**](ContactDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCorrespondenceAddress

> AddressDTO getCorrespondenceAddress(customerId)

Returns correspondence address of a given client.

Returns correspondence address of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
apiInstance.getCorrespondenceAddress(customerId, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 

### Return type

[**AddressDTO**](AddressDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomField

> CustomFieldDTO getCustomField(customerId, customFieldKey)

Returns custom field of a given client.

Returns custom field of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let customFieldKey = "customFieldKey_example"; // String | custom field's key
apiInstance.getCustomField(customerId, customFieldKey, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **customFieldKey** | **String**| custom field&#39;s key | 

### Return type

[**CustomFieldDTO**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomFields

> [CustomFieldDTO] getCustomFields(personId)

Returns custom fields of a given person.

Returns custom fields of a given person.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let personId = 789; // Number | person's internal identifier
apiInstance.getCustomFields(personId, (error, data, response) => {
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
 **personId** | **Number**| person&#39;s internal identifier | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomFields1

> [CustomFieldDTO] getCustomFields1(customerId)

Returns custom fields of a given client.

Returns custom fields of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
apiInstance.getCustomFields1(customerId, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getIndustries

> [Number] getIndustries(customerId)

Returns industries of a given client.

Returns industries of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
apiInstance.getIndustries(customerId, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## update1

> CustomerPersonDTO update1(personId, customerPersonDTO)

Updates an existing person.

Only specified fields will be changed. One may not specify embeddable fields here - use separate API calls for updating them.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let personId = 789; // Number | person's internal identifier
let customerPersonDTO = /home-api/assets/examples/customers/persons/update.json#requestBody; // CustomerPersonDTO | Updated existing person.
apiInstance.update1(personId, customerPersonDTO, (error, data, response) => {
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
 **personId** | **Number**| person&#39;s internal identifier | 
 **customerPersonDTO** | [**CustomerPersonDTO**](CustomerPersonDTO.md)| Updated existing person. | 

### Return type

[**CustomerPersonDTO**](CustomerPersonDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## update2

> CustomerDTO update2(customerId, customerDTO)

Updates an existing client.

Only specified fields will be changed (id is required). One may not specify embeddable fields here - use separate API calls for updating them.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let customerDTO = /home-api/assets/examples/customers/update.json#requestBody; // CustomerDTO | Updated client
apiInstance.update2(customerId, customerDTO, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **customerDTO** | [**CustomerDTO**](CustomerDTO.md)| Updated client | 

### Return type

[**CustomerDTO**](CustomerDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateAddress

> AddressDTO updateAddress(customerId, addressDTO)

Updates address of a given client.

Updates address of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let addressDTO = /home-api/assets/examples/customers/address/updateAddress.json#requestBody; // AddressDTO | Updated address of a given client.
apiInstance.updateAddress(customerId, addressDTO, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **addressDTO** | [**AddressDTO**](AddressDTO.md)| Updated address of a given client. | 

### Return type

[**AddressDTO**](AddressDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCategories

> [Number] updateCategories(customerId, requestBody)

Updates categories of a given client.

Updates categories of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let requestBody = /home-api/assets/examples/customers/updateCategories.json#requestBody; // [Number] | Updated categories of a given client.
apiInstance.updateCategories(customerId, requestBody, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **requestBody** | [**[Number]**](Number.md)| Updated categories of a given client. | 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateContact

> PersonContactDTO updateContact(personId, personContactDTO)

Updates contact of a given person.

Updates contact of a given person. Sets that this person uses specific address and contact (not the one from customer).

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let personId = 789; // Number | person's internal identifier
let personContactDTO = /home-api/assets/examples/customers/persons/updateContact.json#requestBody; // PersonContactDTO | Updated contact of a given person.
apiInstance.updateContact(personId, personContactDTO, (error, data, response) => {
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
 **personId** | **Number**| person&#39;s internal identifier | 
 **personContactDTO** | [**PersonContactDTO**](PersonContactDTO.md)| Updated contact of a given person. | 

### Return type

[**PersonContactDTO**](PersonContactDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateContact1

> ContactDTO updateContact1(customerId, contactDTO)

Updates contact of a given client.

Updates contact of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let contactDTO = /home-api/assets/examples/customers/updateContact.json#requestBody; // ContactDTO | Updated contact of a given client.
apiInstance.updateContact1(customerId, contactDTO, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **contactDTO** | [**ContactDTO**](ContactDTO.md)| Updated contact of a given client. | 

### Return type

[**ContactDTO**](ContactDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCorrespondenceAddress

> AddressDTO updateCorrespondenceAddress(customerId, addressDTO)

Updates correspondence address of a given client.

Updates correspondence address of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let addressDTO = /home-api/assets/examples/customers/address/updateCorrespondenceAddress.json#requestBody; // AddressDTO | Updated address of a given client.
apiInstance.updateCorrespondenceAddress(customerId, addressDTO, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **addressDTO** | [**AddressDTO**](AddressDTO.md)| Updated address of a given client. | 

### Return type

[**AddressDTO**](AddressDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCustomField

> CustomFieldDTO updateCustomField(customerId, customFieldKey, customFieldDTO)

Updates given custom field of a given client.

Updates given custom field of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let customFieldKey = "customFieldKey_example"; // String | custom field's key
let customFieldDTO = /home-api/assets/examples/customers/updateCustomField.json#requestBody; // CustomFieldDTO | Updated custom field of a given client.
apiInstance.updateCustomField(customerId, customFieldKey, customFieldDTO, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **customFieldKey** | **String**| custom field&#39;s key | 
 **customFieldDTO** | [**CustomFieldDTO**](CustomFieldDTO.md)| Updated custom field of a given client. | 

### Return type

[**CustomFieldDTO**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCustomFields

> [CustomFieldDTO] updateCustomFields(personId, customFieldDTO)

Updates custom fields of a given person.

Updates custom fields of a given person.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let personId = 789; // Number | person's internal identifier
let customFieldDTO = /home-api/assets/examples/customers/persons/updateCustomFields.json#requestBody; // [CustomFieldDTO] | Updated custom fields of a given person.
apiInstance.updateCustomFields(personId, customFieldDTO, (error, data, response) => {
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
 **personId** | **Number**| person&#39;s internal identifier | 
 **customFieldDTO** | [**[CustomFieldDTO]**](CustomFieldDTO.md)| Updated custom fields of a given person. | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json;charset=UTF-8
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateCustomFields1

> [CustomFieldDTO] updateCustomFields1(customerId, customFieldDTO)

Updates custom fields of a given client.

Updates custom fields of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let customFieldDTO = /home-api/assets/examples/customers/updateCustomFields.json#requestBody; // [CustomFieldDTO] | Updated custom fields of a given client.
apiInstance.updateCustomFields1(customerId, customFieldDTO, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **customFieldDTO** | [**[CustomFieldDTO]**](CustomFieldDTO.md)| Updated custom fields of a given client. | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateIndustries

> [Number] updateIndustries(customerId, requestBody)

Updates industries of a given client.

Updates industries of a given client.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.ClientsApi();
let customerId = 789; // Number | client's internal identifier
let requestBody = /home-api/assets/examples/customers/updateIndustries.json#requestBody; // [Number] | Updated industries of a given client.
apiInstance.updateIndustries(customerId, requestBody, (error, data, response) => {
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
 **customerId** | **Number**| client&#39;s internal identifier | 
 **requestBody** | [**[Number]**](Number.md)| Updated industries of a given client. | 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

