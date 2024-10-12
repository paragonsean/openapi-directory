# PayRunIo.DpsMessageApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDpsMessage**](DpsMessageApi.md#deleteDpsMessage) | **DELETE** /Employer/{EmployerId}/DpsMessage/{DpsMessageId} | Deletes the DPS message
[**getDpsMessageFromEmployer**](DpsMessageApi.md#getDpsMessageFromEmployer) | **GET** /Employer/{EmployerId}/DpsMessage/{DpsMessageId} | Gets the DPS message
[**getDpsMessagesFromEmployer**](DpsMessageApi.md#getDpsMessagesFromEmployer) | **GET** /Employer/{EmployerId}/DpsMessages | Gets the DPS messages
[**patchDpsMessage**](DpsMessageApi.md#patchDpsMessage) | **PATCH** /Employer/{EmployerId}/DpsMessage/{DpsMessageId} | Patches the DPS message
[**postDpsMessage**](DpsMessageApi.md#postDpsMessage) | **POST** /Employer/{EmployerId}/DpsMessages | Posta the DPS message
[**putDpsMessage**](DpsMessageApi.md#putDpsMessage) | **PUT** /Employer/{EmployerId}/DpsMessage/{DpsMessageId} | Puts the DPS message



## deleteDpsMessage

> deleteDpsMessage(employerId, dpsMessageId, authorization, apiVersion)

Deletes the DPS message

Deletes the DPS message

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.DpsMessageApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let dpsMessageId = "dpsMessageId_example"; // String | The DPS message unique identifier. E.g. DPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteDpsMessage(employerId, dpsMessageId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **dpsMessageId** | **String**| The DPS message unique identifier. E.g. DPS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDpsMessageFromEmployer

> DpsMessage getDpsMessageFromEmployer(employerId, dpsMessageId, authorization, apiVersion)

Gets the DPS message

Gets the DPS message

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.DpsMessageApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let dpsMessageId = "dpsMessageId_example"; // String | The DPS message unique identifier. E.g. DPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getDpsMessageFromEmployer(employerId, dpsMessageId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **dpsMessageId** | **String**| The DPS message unique identifier. E.g. DPS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**DpsMessage**](DpsMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDpsMessagesFromEmployer

> LinkCollection getDpsMessagesFromEmployer(employerId, authorization, apiVersion)

Gets the DPS messages

Gets the DPS message links

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.DpsMessageApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getDpsMessagesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchDpsMessage

> DpsMessage patchDpsMessage(employerId, dpsMessageId, authorization, apiVersion)

Patches the DPS message

Patches the specified DPS message with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.DpsMessageApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let dpsMessageId = "dpsMessageId_example"; // String | The DPS message unique identifier. E.g. DPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.patchDpsMessage(employerId, dpsMessageId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **dpsMessageId** | **String**| The DPS message unique identifier. E.g. DPS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**DpsMessage**](DpsMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDpsMessage

> Link postDpsMessage(employerId, authorization, apiVersion)

Posta the DPS message

Insert new DPS message

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.DpsMessageApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.postDpsMessage(employerId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putDpsMessage

> DpsMessage putDpsMessage(employerId, dpsMessageId, authorization, apiVersion)

Puts the DPS message

Puts the DPS message

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.DpsMessageApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let dpsMessageId = "dpsMessageId_example"; // String | The DPS message unique identifier. E.g. DPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putDpsMessage(employerId, dpsMessageId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **dpsMessageId** | **String**| The DPS message unique identifier. E.g. DPS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**DpsMessage**](DpsMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

