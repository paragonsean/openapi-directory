# ApicurioRegistryApiV2.ArtifactTypeApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listArtifactTypes**](ArtifactTypeApi.md#listArtifactTypes) | **GET** /admin/artifactTypes | List artifact types



## listArtifactTypes

> [ArtifactTypeInfo] listArtifactTypes()

List artifact types

Gets a list of all the configured artifact types.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.ArtifactTypeApi();
apiInstance.listArtifactTypes((error, data, response) => {
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

[**[ArtifactTypeInfo]**](ArtifactTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

