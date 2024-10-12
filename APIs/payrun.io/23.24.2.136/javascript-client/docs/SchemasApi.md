# PayRunIo.SchemasApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSchema**](SchemasApi.md#getSchema) | **GET** /Schemas/{DtoDataType} | Get XSD schema
[**getSchemas**](SchemasApi.md#getSchemas) | **GET** /Schemas | Get a list of all available schemas



## getSchema

> File getSchema(dtoDataType, authorization, apiVersion)

Get XSD schema

Returns the XSD schema for the specified data type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SchemasApi();
let dtoDataType = "dtoDataType_example"; // String | The data transfer object type name. E.g PensionPayInstruction
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSchema(dtoDataType, authorization, apiVersion, (error, data, response) => {
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
 **dtoDataType** | **String**| The data transfer object type name. E.g PensionPayInstruction | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSchemas

> LinkCollection getSchemas(authorization, apiVersion)

Get a list of all available schemas

Returns a collection of links to all the available data object schemas

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SchemasApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSchemas(authorization, apiVersion, (error, data, response) => {
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

