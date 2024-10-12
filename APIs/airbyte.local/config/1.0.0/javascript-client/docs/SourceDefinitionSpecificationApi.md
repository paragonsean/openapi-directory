# AirbyteConfigurationApi.SourceDefinitionSpecificationApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSourceDefinitionSpecification**](SourceDefinitionSpecificationApi.md#getSourceDefinitionSpecification) | **POST** /v1/source_definition_specifications/get | Get specification for a SourceDefinition.



## getSourceDefinitionSpecification

> SourceDefinitionSpecificationRead getSourceDefinitionSpecification(sourceDefinitionIdWithWorkspaceId)

Get specification for a SourceDefinition.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionSpecificationApi();
let sourceDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
apiInstance.getSourceDefinitionSpecification(sourceDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | 

### Return type

[**SourceDefinitionSpecificationRead**](SourceDefinitionSpecificationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

