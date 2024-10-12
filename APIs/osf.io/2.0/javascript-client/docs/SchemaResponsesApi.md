# OsfApiv2Documentation.SchemaResponsesApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schemaResponseDelete**](SchemaResponsesApi.md#schemaResponseDelete) | **DELETE** /schema_responses/{schema_response_id} | Delete a Incomplete Schema Response
[**schemaResponsePatch**](SchemaResponsesApi.md#schemaResponsePatch) | **PATCH** /schema_responses/{schema_response_id} | Update a Registration&#39;s Schema Response
[**schemaResponsePpost**](SchemaResponsesApi.md#schemaResponsePpost) | **POST** /schema_responses/ | Create a new Schema Response
[**schemaResponsesList**](SchemaResponsesApi.md#schemaResponsesList) | **GET** /schema_responses/ | List all Schema Responses
[**schemaResponsesRead**](SchemaResponsesApi.md#schemaResponsesRead) | **GET** /schema_responses/{schema_response_id} | Retrieve a Schema Response



## schemaResponseDelete

> schemaResponseDelete(schemaResponseId)

Delete a Incomplete Schema Response

This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the &#x60;in_progress&#x60; state. Once a Schema Response is transitioned to an &#x60;approved&#x60; it is immutable and another Schema Response must be created to update the Schema Response for that registration. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponsesApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
apiInstance.schemaResponseDelete(schemaResponseId, (error, data, response) => {
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
 **schemaResponseId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## schemaResponsePatch

> SchemaResponses schemaResponsePatch(schemaResponseId, schemaResponses)

Update a Registration&#39;s Schema Response

Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an &#x60;in_progress&#x60; state. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponsesApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
let schemaResponses = new OsfApiv2Documentation.SchemaResponses(); // SchemaResponses | 
apiInstance.schemaResponsePatch(schemaResponseId, schemaResponses, (error, data, response) => {
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
 **schemaResponseId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | 
 **schemaResponses** | [**SchemaResponses**](SchemaResponses.md)|  | 

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*, application/json


## schemaResponsePpost

> SchemaResponses schemaResponsePpost(schemaResponses)

Create a new Schema Response

This endpoint creates a new Schema Response with an &#x60;in_progress&#x60; state. A new response can only be created if the current schema response is in an &#x60;approved&#x60; state. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing an updated representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponsesApi();
let schemaResponses = new OsfApiv2Documentation.SchemaResponses(); // SchemaResponses | 
apiInstance.schemaResponsePpost(schemaResponses, (error, data, response) => {
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
 **schemaResponses** | [**SchemaResponses**](SchemaResponses.md)|  | 

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*, application/json


## schemaResponsesList

> SchemaResponses schemaResponsesList()

List all Schema Responses

This retrieves a paginated list of all active Schema Responses that are public. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponsesApi();
apiInstance.schemaResponsesList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## schemaResponsesRead

> SchemaResponses schemaResponsesRead(schemaResponseId)

Retrieve a Schema Response

This retrieves a single Schema response using it&#39;s id. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponsesApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
apiInstance.schemaResponsesRead(schemaResponseId, (error, data, response) => {
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
 **schemaResponseId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | 

### Return type

[**SchemaResponses**](SchemaResponses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

