# OsfApiv2Documentation.SchemaResponseActionsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schemaResponseActionRead**](SchemaResponseActionsApi.md#schemaResponseActionRead) | **GET** /schema_responses/{schema_response_id}/actions/ | Retrieve a list of Schema Response Actions for a Schema Response
[**schemaResponsesSchemaResponseIdActionsPost**](SchemaResponseActionsApi.md#schemaResponsesSchemaResponseIdActionsPost) | **POST** /schema_responses/{schema_response_id}/actions/ | Create a new Schema Response Action
[**schemaResponsesSchemaResponseIdActionsSchemaResponseActionIdGet**](SchemaResponseActionsApi.md#schemaResponsesSchemaResponseIdActionsSchemaResponseActionIdGet) | **GET** /schema_responses/{schema_response_id}/actions/{schema_response_action_id} | A Schema Response Action from a Schema Response



## schemaResponseActionRead

> SchemaResponseActions schemaResponseActionRead(schemaResponseId)

Retrieve a list of Schema Response Actions for a Schema Response

This retrieves a paginated list of all Schema Response Actions created for a Schema Response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponseActionsApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
apiInstance.schemaResponseActionRead(schemaResponseId, (error, data, response) => {
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

[**SchemaResponseActions**](SchemaResponseActions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## schemaResponsesSchemaResponseIdActionsPost

> schemaResponsesSchemaResponseIdActionsPost(schemaResponseId)

Create a new Schema Response Action

This creates a new Schema Response Action in order to trigger a state transition for a Schema Response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponseActionsApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
apiInstance.schemaResponsesSchemaResponseIdActionsPost(schemaResponseId, (error, data, response) => {
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


## schemaResponsesSchemaResponseIdActionsSchemaResponseActionIdGet

> SchemaResponseActions schemaResponsesSchemaResponseIdActionsSchemaResponseActionIdGet(schemaResponseId, schemaResponseActionId)

A Schema Response Action from a Schema Response

Retrieves a Schema Response Action by it&#39;s ID. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.SchemaResponseActionsApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Schema Response example `61b9cd62eb66180215222669`.
let schemaResponseActionId = "schemaResponseActionId_example"; // String | The unique identifier of the Schema Response Action example `61b9eae1a7d8ac025c4c46d3`.
apiInstance.schemaResponsesSchemaResponseIdActionsSchemaResponseActionIdGet(schemaResponseId, schemaResponseActionId, (error, data, response) => {
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
 **schemaResponseId** | **String**| The unique identifier of the Schema Response example &#x60;61b9cd62eb66180215222669&#x60;. | 
 **schemaResponseActionId** | **String**| The unique identifier of the Schema Response Action example &#x60;61b9eae1a7d8ac025c4c46d3&#x60;. | 

### Return type

[**SchemaResponseActions**](SchemaResponseActions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

