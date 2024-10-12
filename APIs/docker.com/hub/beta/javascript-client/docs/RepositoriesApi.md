# DockerHubApi.RepositoriesApi

All URIs are relative to *https://hub.docker.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2NamespacesNamespaceRepositoriesRepositoryTagsGet**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsGet) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/tags | List repository tags
[**v2NamespacesNamespaceRepositoriesRepositoryTagsHead**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsHead) | **HEAD** /v2/namespaces/{namespace}/repositories/{repository}/tags | Check repository tags
[**v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag} | Read repository tag
[**v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead) | **HEAD** /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag} | Check repository tag



## v2NamespacesNamespaceRepositoriesRepositoryTagsGet

> PaginatedTags v2NamespacesNamespaceRepositoriesRepositoryTagsGet(namespace, repository, opts)

List repository tags

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.RepositoriesApi();
let namespace = "namespace_example"; // String | 
let repository = "repository_example"; // String | 
let opts = {
  'page': 56, // Number | Page number to get. Defaults to 1.
  'pageSize': 56 // Number | Number of items to get per page. Defaults to 10. Max of 100.
};
apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsGet(namespace, repository, opts, (error, data, response) => {
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
 **namespace** | **String**|  | 
 **repository** | **String**|  | 
 **page** | **Number**| Page number to get. Defaults to 1. | [optional] 
 **pageSize** | **Number**| Number of items to get per page. Defaults to 10. Max of 100. | [optional] 

### Return type

[**PaginatedTags**](PaginatedTags.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2NamespacesNamespaceRepositoriesRepositoryTagsHead

> v2NamespacesNamespaceRepositoriesRepositoryTagsHead(namespace, repository)

Check repository tags

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.RepositoriesApi();
let namespace = "namespace_example"; // String | 
let repository = "repository_example"; // String | 
apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsHead(namespace, repository, (error, data, response) => {
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
 **namespace** | **String**|  | 
 **repository** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet

> Tag v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet(namespace, repository, tag)

Read repository tag

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.RepositoriesApi();
let namespace = "namespace_example"; // String | 
let repository = "repository_example"; // String | 
let tag = "tag_example"; // String | 
apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet(namespace, repository, tag, (error, data, response) => {
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
 **namespace** | **String**|  | 
 **repository** | **String**|  | 
 **tag** | **String**|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead

> v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead(namespace, repository, tag)

Check repository tag

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.RepositoriesApi();
let namespace = "namespace_example"; // String | 
let repository = "repository_example"; // String | 
let tag = "tag_example"; // String | 
apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead(namespace, repository, tag, (error, data, response) => {
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
 **namespace** | **String**|  | 
 **repository** | **String**|  | 
 **tag** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

