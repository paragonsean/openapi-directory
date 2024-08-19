# XtrfHomePortalApi.QuotesClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLanguageCombination1**](QuotesClassicApi.md#createLanguageCombination1) | **POST** /quotes/{quoteId}/languageCombinations | Creates a new language combination for a given quote without creating a task.
[**createPayable1**](QuotesClassicApi.md#createPayable1) | **POST** /quotes/{quoteId}/finance/payables | Adds a payable.
[**createReceivable1**](QuotesClassicApi.md#createReceivable1) | **POST** /quotes/{quoteId}/finance/receivables | Adds a receivable.
[**createTask1**](QuotesClassicApi.md#createTask1) | **POST** /quotes/{quoteId}/tasks | Creates a new task for a given quote.
[**delete13**](QuotesClassicApi.md#delete13) | **DELETE** /quotes/{quoteId} | Removes a quote.
[**deletePayable1**](QuotesClassicApi.md#deletePayable1) | **DELETE** /quotes/{quoteId}/finance/payables/{payableId} | Deletes a payable.
[**deleteReceivable1**](QuotesClassicApi.md#deleteReceivable1) | **DELETE** /quotes/{quoteId}/finance/receivables/{receivableId} | Deletes a receivable.
[**getAllIds7**](QuotesClassicApi.md#getAllIds7) | **GET** /quotes/ids | Returns quotes&#39; internal identifiers.
[**getById8**](QuotesClassicApi.md#getById8) | **GET** /quotes/{quoteId} | Returns quote details.
[**getCustomFields6**](QuotesClassicApi.md#getCustomFields6) | **GET** /quotes/{quoteId}/customFields | Returns custom fields of a given quote.
[**getDates2**](QuotesClassicApi.md#getDates2) | **GET** /quotes/{quoteId}/dates | Returns dates of a given quote.
[**getFinance1**](QuotesClassicApi.md#getFinance1) | **GET** /quotes/{quoteId}/finance | Returns finance of a given quote.
[**getInstructions1**](QuotesClassicApi.md#getInstructions1) | **GET** /quotes/{quoteId}/instructions | Returns instructions of a given quote.
[**send1**](QuotesClassicApi.md#send1) | **POST** /quotes/{quoteId}/confirmation/send | Sends a quote for customer confirmation.
[**start**](QuotesClassicApi.md#start) | **POST** /quotes/{quoteId}/start | Starts a quote.
[**updateCustomFields4**](QuotesClassicApi.md#updateCustomFields4) | **PUT** /quotes/{quoteId}/customFields | Updates custom fields of a given quote.
[**updateInstructions2**](QuotesClassicApi.md#updateInstructions2) | **PUT** /quotes/{quoteId}/instructions | Updates instructions of a given quote.
[**updatePayable1**](QuotesClassicApi.md#updatePayable1) | **PUT** /quotes/{quoteId}/finance/payables/{payableId} | Updates a payable.
[**updateReceivable1**](QuotesClassicApi.md#updateReceivable1) | **PUT** /quotes/{quoteId}/finance/receivables/{receivableId} | Updates a receivable.



## createLanguageCombination1

> CommonLanguageCombinationDTO createLanguageCombination1(quoteId, commonLanguageCombinationDTO)

Creates a new language combination for a given quote without creating a task.

Creates a new language combination for a given quote without creating a task.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let commonLanguageCombinationDTO = /home-api/assets/examples/v1/quotes/createLanguageCombination.json#requestBody; // CommonLanguageCombinationDTO | Created a new language combination for a given quote without creating a task.
apiInstance.createLanguageCombination1(quoteId, commonLanguageCombinationDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **commonLanguageCombinationDTO** | [**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)| Created a new language combination for a given quote without creating a task. | 

### Return type

[**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## createPayable1

> PayableDTO createPayable1(quoteId, payableCreateDTO)

Adds a payable.

Adds a payable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let payableCreateDTO = /home-api/assets/examples/v1/quotes/createCATPayable.json#requestBody; // PayableCreateDTO | Adds a payable.
apiInstance.createPayable1(quoteId, payableCreateDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **payableCreateDTO** | [**PayableCreateDTO**](PayableCreateDTO.md)| Adds a payable. | 

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReceivable1

> ReceivableDTO createReceivable1(quoteId, receivableCreateDTO)

Adds a receivable.

Adds a receivable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let receivableCreateDTO = /home-api/assets/examples/v1/quotes/createReceivable.json#requestBody; // ReceivableCreateDTO | Adds a receivable.
apiInstance.createReceivable1(quoteId, receivableCreateDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **receivableCreateDTO** | [**ReceivableCreateDTO**](ReceivableCreateDTO.md)| Adds a receivable. | 

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTask1

> TaskDTO createTask1(quoteId, taskDTO)

Creates a new task for a given quote.

Creates a new task for a given quote. Required fields are presented in the example.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let taskDTO = /home-api/assets/examples/v1/quotes/createTask.json#requestBody; // TaskDTO | Updated custom fields of a given quote.
apiInstance.createTask1(quoteId, taskDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **taskDTO** | [**TaskDTO**](TaskDTO.md)| Updated custom fields of a given quote. | 

### Return type

[**TaskDTO**](TaskDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## delete13

> delete13(quoteId)

Removes a quote.

Removes a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.delete13(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePayable1

> deletePayable1(quoteId, payableId)

Deletes a payable.

Deletes a payable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quoteId's internal identifier
let payableId = 789; // Number | payable's internal identifier
apiInstance.deletePayable1(quoteId, payableId, (error, data, response) => {
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
 **quoteId** | **String**| quoteId&#39;s internal identifier | 
 **payableId** | **Number**| payable&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteReceivable1

> deleteReceivable1(quoteId, receivableId)

Deletes a receivable.

Deletes a receivable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quoteId's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
apiInstance.deleteReceivable1(quoteId, receivableId, (error, data, response) => {
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
 **quoteId** | **String**| quoteId&#39;s internal identifier | 
 **receivableId** | **Number**| receivable&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllIds7

> [Number] getAllIds7(opts)

Returns quotes&#39; internal identifiers.

Returns quotes&#39; internal identifiers.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let opts = {
  'updatedSince': 789 // Number | only quotes modified since this timestamp
};
apiInstance.getAllIds7(opts, (error, data, response) => {
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
 **updatedSince** | **Number**| only quotes modified since this timestamp | [optional] 

### Return type

**[Number]**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getById8

> QuoteDTOv1 getById8(quoteId, opts)

Returns quote details.

Returns quote details. If the specified quote ID refers to Smart Quote, 400 Bad Request is returned instead.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let opts = {
  'embed': "embed_example" // String | list of adittional fields which should be embedded in the response (ie. tasks)
};
apiInstance.getById8(quoteId, opts, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **embed** | **String**| list of adittional fields which should be embedded in the response (ie. tasks) | [optional] 

### Return type

[**QuoteDTOv1**](QuoteDTOv1.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getCustomFields6

> [CustomFieldDTO] getCustomFields6(quoteId)

Returns custom fields of a given quote.

Returns custom fields of a given quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getCustomFields6(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getDates2

> QuoteDatesDTO getDates2(quoteId)

Returns dates of a given quote.

Returns dates of a given quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getDates2(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**QuoteDatesDTO**](QuoteDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getFinance1

> FinanceDTO getFinance1(quoteId)

Returns finance of a given quote.

Returns finance of a given quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getFinance1(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**FinanceDTO**](FinanceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## getInstructions1

> InstructionsDTO getInstructions1(quoteId)

Returns instructions of a given quote.

Returns instructions of a given quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.getInstructions1(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## send1

> send1(quoteId)

Sends a quote for customer confirmation.

Sends a quote for customer confirmation. Quote status is changed to SENT and a document is sent to the customer.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.send1(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## start

> start(quoteId)

Starts a quote.

Starts a quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
apiInstance.start(quoteId, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateCustomFields4

> [CustomFieldDTO] updateCustomFields4(quoteId, customFieldDTO)

Updates custom fields of a given quote.

Updates custom fields of a given quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let customFieldDTO = /home-api/assets/examples/v1/quotes/updateCustomFields.json#requestBody; // [CustomFieldDTO] | Updated custom fields of a given quote.
apiInstance.updateCustomFields4(quoteId, customFieldDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **customFieldDTO** | [**[CustomFieldDTO]**](CustomFieldDTO.md)| Updated custom fields of a given quote. | 

### Return type

[**[CustomFieldDTO]**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updateInstructions2

> InstructionsDTO updateInstructions2(quoteId, instructionsDTO)

Updates instructions of a given quote.

Updates instructions of a given quote.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let instructionsDTO = /home-api/assets/examples/v1/quotes/updateInstructions.json#requestBody; // InstructionsDTO | Updated instructions of a given project.
apiInstance.updateInstructions2(quoteId, instructionsDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions of a given project. | 

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8


## updatePayable1

> PayableDTO updatePayable1(quoteId, payableId, payableDTO)

Updates a payable.

Updates a payable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let payableId = 789; // Number | payable's internal identifier
let payableDTO = /home-api/assets/examples/v1/quotes/updatePayable.json#requestBody; // PayableDTO | Updates a payable.
apiInstance.updatePayable1(quoteId, payableId, payableDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **payableId** | **Number**| payable&#39;s internal identifier | 
 **payableDTO** | [**PayableDTO**](PayableDTO.md)| Updates a payable. | 

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateReceivable1

> ReceivableDTO updateReceivable1(quoteId, receivableId, receivableDTO)

Updates a receivable.

Updates a receivable.

### Example

```javascript
import XtrfHomePortalApi from 'xtrf_home_portal_api';
let defaultClient = XtrfHomePortalApi.ApiClient.instance;
// Configure API key authorization: X-AUTH-ACCESS-TOKEN
let X-AUTH-ACCESS-TOKEN = defaultClient.authentications['X-AUTH-ACCESS-TOKEN'];
X-AUTH-ACCESS-TOKEN.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AUTH-ACCESS-TOKEN.apiKeyPrefix = 'Token';

let apiInstance = new XtrfHomePortalApi.QuotesClassicApi();
let quoteId = "quoteId_example"; // String | quote's internal identifier
let receivableId = 789; // Number | receivable's internal identifier
let receivableDTO = /home-api/assets/examples/v1/quotes/updateReceivable.json#requestBody; // ReceivableDTO | Updates a receivable.
apiInstance.updateReceivable1(quoteId, receivableId, receivableDTO, (error, data, response) => {
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
 **quoteId** | **String**| quote&#39;s internal identifier | 
 **receivableId** | **Number**| receivable&#39;s internal identifier | 
 **receivableDTO** | [**ReceivableDTO**](ReceivableDTO.md)| Updates a receivable. | 

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

