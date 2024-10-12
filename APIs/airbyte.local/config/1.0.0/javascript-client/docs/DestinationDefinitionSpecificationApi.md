# AirbyteConfigurationApi.DestinationDefinitionSpecificationApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDestinationDefinitionSpecification**](DestinationDefinitionSpecificationApi.md#getDestinationDefinitionSpecification) | **POST** /v1/destination_definition_specifications/get | Get specification for a destinationDefinition



## getDestinationDefinitionSpecification

> DestinationDefinitionSpecificationRead getDestinationDefinitionSpecification(destinationDefinitionIdWithWorkspaceId)

Get specification for a destinationDefinition

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionSpecificationApi();
let destinationDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
apiInstance.getDestinationDefinitionSpecification(destinationDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | 

### Return type

[**DestinationDefinitionSpecificationRead**](DestinationDefinitionSpecificationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

