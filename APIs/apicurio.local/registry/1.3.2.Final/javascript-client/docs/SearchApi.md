# ApicurioRegistryApi.SearchApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchArtifacts**](SearchApi.md#searchArtifacts) | **GET** /search/artifacts | Search for artifacts
[**searchVersions**](SearchApi.md#searchVersions) | **GET** /search/artifacts/{artifactId}/versions | Search artifact versions



## searchArtifacts

> ArtifactSearchResults searchArtifacts(offset, limit, opts)

Search for artifacts

Returns a paginated list of all artifacts that match the provided search criteria. 

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.SearchApi();
let offset = 0; // Number | The number of artifacts to skip before starting to collect the result set.
let limit = 20; // Number | The number of artifacts to return.
let opts = {
  'search': "search_example", // String | The text to search.
  'over': "over_example", // String | What fields to search.
  'order': "order_example" // String | Sort order, ascending or descending.
};
apiInstance.searchArtifacts(offset, limit, opts, (error, data, response) => {
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
 **offset** | **Number**| The number of artifacts to skip before starting to collect the result set. | [default to 0]
 **limit** | **Number**| The number of artifacts to return. | [default to 20]
 **search** | **String**| The text to search. | [optional] 
 **over** | **String**| What fields to search. | [optional] 
 **order** | **String**| Sort order, ascending or descending. | [optional] 

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchVersions

> VersionSearchResults searchVersions(artifactId, offset, limit)

Search artifact versions

Searches for versions of a specific artifact.  This is typically used to get a listing of all versions of an artifact (for example, in a user interface).

### Example

```javascript
import ApicurioRegistryApi from 'apicurio_registry_api';

let apiInstance = new ApicurioRegistryApi.SearchApi();
let artifactId = "artifactId_example"; // String | The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier.
let offset = 56; // Number | The number of versions to skip before starting to collect the result set.
let limit = 56; // Number | The number of versions to return.
apiInstance.searchVersions(artifactId, offset, limit, (error, data, response) => {
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
 **artifactId** | **String**| The artifact ID.  Can be a string (client-provided) or integer (server-generated) representing the unique artifact identifier. | 
 **offset** | **Number**| The number of versions to skip before starting to collect the result set. | 
 **limit** | **Number**| The number of versions to return. | 

### Return type

[**VersionSearchResults**](VersionSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

