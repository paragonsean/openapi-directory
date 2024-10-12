# PayRunIo.NominalCodeApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteNominalCode**](NominalCodeApi.md#deleteNominalCode) | **DELETE** /Employer/{EmployerId}/NominalCode/{NominalCodeId} | Deletes the nominal codes
[**getNominalCodeFromEmployer**](NominalCodeApi.md#getNominalCodeFromEmployer) | **GET** /Employer/{EmployerId}/NominalCode/{NominalCodeId} | Gets the nominal code
[**getNominalCodesFromEmployer**](NominalCodeApi.md#getNominalCodesFromEmployer) | **GET** /Employer/{EmployerId}/NominalCodes | Gets the nominal codes
[**postNominalCode**](NominalCodeApi.md#postNominalCode) | **POST** /Employer/{EmployerId}/NominalCodes | Insert nominal code
[**putNominalCode**](NominalCodeApi.md#putNominalCode) | **PUT** /Employer/{EmployerId}/NominalCode/{NominalCodeId} | Insert nominal code



## deleteNominalCode

> deleteNominalCode(employerId, nominalCodeId, authorization, apiVersion)

Deletes the nominal codes

Deletes the nominal code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.NominalCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let nominalCodeId = "nominalCodeId_example"; // String | The nominal code unique identifier. E.g. NOM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteNominalCode(employerId, nominalCodeId, authorization, apiVersion, (error, data, response) => {
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
 **nominalCodeId** | **String**| The nominal code unique identifier. E.g. NOM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNominalCodeFromEmployer

> NominalCode getNominalCodeFromEmployer(employerId, nominalCodeId, authorization, apiVersion)

Gets the nominal code

Gets the nominal code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.NominalCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let nominalCodeId = "nominalCodeId_example"; // String | The nominal code unique identifier. E.g. NOM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getNominalCodeFromEmployer(employerId, nominalCodeId, authorization, apiVersion, (error, data, response) => {
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
 **nominalCodeId** | **String**| The nominal code unique identifier. E.g. NOM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**NominalCode**](NominalCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNominalCodesFromEmployer

> LinkCollection getNominalCodesFromEmployer(employerId, authorization, apiVersion)

Gets the nominal codes

Gets the nominal code links

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.NominalCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getNominalCodesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## postNominalCode

> Link postNominalCode(employerId, authorization, apiVersion, nominalCode)

Insert nominal code

Inserts a new nominal code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.NominalCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let nominalCode = new PayRunIo.NominalCode(); // NominalCode | The nominal code object.
apiInstance.postNominalCode(employerId, authorization, apiVersion, nominalCode, (error, data, response) => {
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
 **nominalCode** | [**NominalCode**](NominalCode.md)| The nominal code object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putNominalCode

> NominalCode putNominalCode(employerId, nominalCodeId, authorization, apiVersion, nominalCode)

Insert nominal code

Inserts a new nominal code at the specified resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.NominalCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let nominalCodeId = "nominalCodeId_example"; // String | The nominal code unique identifier. E.g. NOM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let nominalCode = new PayRunIo.NominalCode(); // NominalCode | The nominal code object.
apiInstance.putNominalCode(employerId, nominalCodeId, authorization, apiVersion, nominalCode, (error, data, response) => {
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
 **nominalCodeId** | **String**| The nominal code unique identifier. E.g. NOM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **nominalCode** | [**NominalCode**](NominalCode.md)| The nominal code object. | 

### Return type

[**NominalCode**](NominalCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

