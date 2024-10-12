# OsfApiv2Documentation.RegistrationSchemaBlocksApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schemaResponseBlocksRead**](RegistrationSchemaBlocksApi.md#schemaResponseBlocksRead) | **GET** /schema_responses/{schema_response_id}/schema_blocks/ | Retrieve a list of Registration Schema Blocks for a Schema Response
[**schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet**](RegistrationSchemaBlocksApi.md#schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet) | **GET** /schema_responses/{schema_response_id}/schema_blocks/{schema_response_block_id} | Retrieve a Registration Schema Block



## schemaResponseBlocksRead

> RegistrationSchemaBlock schemaResponseBlocksRead(schemaResponseId)

Retrieve a list of Registration Schema Blocks for a Schema Response

This returns a list of all the Registration Schema Blocks are contained in Registration Schema. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.RegistrationSchemaBlocksApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
apiInstance.schemaResponseBlocksRead(schemaResponseId, (error, data, response) => {
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

[**RegistrationSchemaBlock**](RegistrationSchemaBlock.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet

> RegistrationSchemaBlock schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet(schemaResponseId, schemaResponseBlockId)

Retrieve a Registration Schema Block

This returns a Registration Schema Block by it&#39;s ID. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.RegistrationSchemaBlocksApi();
let schemaResponseId = "schemaResponseId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
let schemaResponseBlockId = "schemaResponseBlockId_example"; // String | The unique identifier of the Schema Response Block example `61b79f9eadbb5701424a2d5e`.
apiInstance.schemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdGet(schemaResponseId, schemaResponseBlockId, (error, data, response) => {
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
 **schemaResponseBlockId** | **String**| The unique identifier of the Schema Response Block example &#x60;61b79f9eadbb5701424a2d5e&#x60;. | 

### Return type

[**RegistrationSchemaBlock**](RegistrationSchemaBlock.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

