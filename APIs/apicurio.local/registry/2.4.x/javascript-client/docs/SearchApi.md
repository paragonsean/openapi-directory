# ApicurioRegistryApiV2.SearchApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchArtifacts**](SearchApi.md#searchArtifacts) | **GET** /search/artifacts | Search for artifacts
[**searchArtifactsByContent**](SearchApi.md#searchArtifactsByContent) | **POST** /search/artifacts | Search for artifacts by content



## searchArtifacts

> ArtifactSearchResults searchArtifacts(opts)

Search for artifacts

Returns a paginated list of all artifacts that match the provided filter criteria. 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.SearchApi();
let opts = {
  'name': "name_example", // String | Filter by artifact name.
  'offset': 0, // Number | The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
  'limit': 20, // Number | The number of artifacts to return.  Defaults to 20.
  'order': new ApicurioRegistryApiV2.SortOrder(), // SortOrder | Sort order, ascending (`asc`) or descending (`desc`).
  'orderby': new ApicurioRegistryApiV2.SortBy(), // SortBy | The field to sort by.  Can be one of:  * `name` * `createdOn` 
  'labels': ["null"], // [String] | Filter by label.  Include one or more label to only return artifacts containing all of the specified labels.
  'properties': ["null"], // [String] | Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example `properties=foo:bar` will return only artifacts with a custom property named `foo` and value `bar`.
  'description': "description_example", // String | Filter by description.
  'group': "group_example", // String | Filter by artifact group.
  'globalId': 789, // Number | Filter by globalId.
  'contentId': 789 // Number | Filter by contentId.
};
apiInstance.searchArtifacts(opts, (error, data, response) => {
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
 **name** | **String**| Filter by artifact name. | [optional] 
 **offset** | **Number**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] [default to 0]
 **limit** | **Number**| The number of artifacts to return.  Defaults to 20. | [optional] [default to 20]
 **order** | [**SortOrder**](.md)| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] 
 **orderby** | [**SortBy**](.md)| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] 
 **labels** | [**[String]**](String.md)| Filter by label.  Include one or more label to only return artifacts containing all of the specified labels. | [optional] 
 **properties** | [**[String]**](String.md)| Filter by one or more name/value property.  Separate each name/value pair using a colon.  For example &#x60;properties&#x3D;foo:bar&#x60; will return only artifacts with a custom property named &#x60;foo&#x60; and value &#x60;bar&#x60;. | [optional] 
 **description** | **String**| Filter by description. | [optional] 
 **group** | **String**| Filter by artifact group. | [optional] 
 **globalId** | **Number**| Filter by globalId. | [optional] 
 **contentId** | **Number**| Filter by contentId. | [optional] 

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchArtifactsByContent

> ArtifactSearchResults searchArtifactsByContent(body, opts)

Search for artifacts by content

Returns a paginated list of all artifacts with at least one version that matches the posted content. 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.SearchApi();
let body = "/path/to/file"; // File | The content to search for.
let opts = {
  'canonical': true, // Boolean | Parameter that can be set to `true` to indicate that the server should \"canonicalize\" the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the `artifactType` query parameter.
  'artifactType': "artifactType_example", // String | Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the `canonical` query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts.
  'offset': 0, // Number | The number of artifacts to skip before starting to collect the result set.  Defaults to 0.
  'limit': 20, // Number | The number of artifacts to return.  Defaults to 20.
  'order': "order_example", // String | Sort order, ascending (`asc`) or descending (`desc`).
  'orderby': "orderby_example" // String | The field to sort by.  Can be one of:  * `name` * `createdOn` 
};
apiInstance.searchArtifactsByContent(body, opts, (error, data, response) => {
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
 **body** | **File**| The content to search for. | 
 **canonical** | **Boolean**| Parameter that can be set to &#x60;true&#x60; to indicate that the server should \&quot;canonicalize\&quot; the content when searching for matching artifacts.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.  Must be used along with the &#x60;artifactType&#x60; query parameter. | [optional] 
 **artifactType** | **String**| Indicates the type of artifact represented by the content being used for the search.  This is only needed when using the &#x60;canonical&#x60; query parameter, so that the server knows how to canonicalize the content prior to searching for matching artifacts. | [optional] 
 **offset** | **Number**| The number of artifacts to skip before starting to collect the result set.  Defaults to 0. | [optional] [default to 0]
 **limit** | **Number**| The number of artifacts to return.  Defaults to 20. | [optional] [default to 20]
 **order** | **String**| Sort order, ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] 
 **orderby** | **String**| The field to sort by.  Can be one of:  * &#x60;name&#x60; * &#x60;createdOn&#x60;  | [optional] 

### Return type

[**ArtifactSearchResults**](ArtifactSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

