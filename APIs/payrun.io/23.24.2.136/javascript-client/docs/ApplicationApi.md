# PayRunIo.ApplicationApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteApplicationSecret**](ApplicationApi.md#deleteApplicationSecret) | **DELETE** /Secret/{SecretId} | Deletes Application secret
[**getApplicationSecret**](ApplicationApi.md#getApplicationSecret) | **GET** /Secret/{SecretId} | Get Application secret
[**getApplicationSecrets**](ApplicationApi.md#getApplicationSecrets) | **GET** /Secrets | Get all Application secret links
[**postApplicationSecret**](ApplicationApi.md#postApplicationSecret) | **POST** /Secrets | Create a new Application secret
[**putApplicationSecret**](ApplicationApi.md#putApplicationSecret) | **PUT** /Secret/{SecretId} | Create a new Application secret



## deleteApplicationSecret

> deleteApplicationSecret(secretId, authorization, apiVersion)

Deletes Application secret

Deletes an Application secret from the given resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ApplicationApi();
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteApplicationSecret(secretId, authorization, apiVersion, (error, data, response) => {
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
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationSecret

> ApplicationSecret getApplicationSecret(secretId, authorization, apiVersion)

Get Application secret

Get the public visible Application secret object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ApplicationApi();
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getApplicationSecret(secretId, authorization, apiVersion, (error, data, response) => {
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
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**ApplicationSecret**](ApplicationSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationSecrets

> LinkCollection getApplicationSecrets(authorization, apiVersion)

Get all Application secret links

Get all the Application secret links

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ApplicationApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getApplicationSecrets(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postApplicationSecret

> Link postApplicationSecret(authorization, apiVersion)

Create a new Application secret

Create new Application secret using auto generated resource location key

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ApplicationApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.postApplicationSecret(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putApplicationSecret

> ApplicationSecret putApplicationSecret(secretId, authorization, apiVersion)

Create a new Application secret

Create / update an Application secret at the given resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ApplicationApi();
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putApplicationSecret(secretId, authorization, apiVersion, (error, data, response) => {
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
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**ApplicationSecret**](ApplicationSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

