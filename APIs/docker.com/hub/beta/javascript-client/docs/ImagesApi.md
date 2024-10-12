# DockerHubApi.ImagesApi

All URIs are relative to *https://hub.docker.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNamespacesRepositoriesImages**](ImagesApi.md#getNamespacesRepositoriesImages) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/images | Get details of repository&#39;s images
[**getNamespacesRepositoriesImagesSummary**](ImagesApi.md#getNamespacesRepositoriesImagesSummary) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/images-summary | Get summary of repository&#39;s images
[**getNamespacesRepositoriesImagesTags**](ImagesApi.md#getNamespacesRepositoriesImagesTags) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/images/{digest}/tags | Get image&#39;s tags
[**postNamespacesDeleteImages**](ImagesApi.md#postNamespacesDeleteImages) | **POST** /v2/namespaces/{namespace}/delete-images | Delete images



## getNamespacesRepositoriesImages

> GetNamespaceRepositoryImagesResponse getNamespacesRepositoriesImages(namespace, repository, opts)

Get details of repository&#39;s images

Gets details on the images in a repository.

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ImagesApi();
let namespace = "namespace_example"; // String | Namespace of the repository.
let repository = "repository_example"; // String | Name of the repository.
let opts = {
  'status': "status_example", // String | Filters to only show images of this status.
  'currentlyTagged': true, // Boolean | Filters to only show images with: - `true`: at least 1 current tag. - `false`: no current tags. 
  'ordering': "ordering_example", // String | Orders the results by this property.  Prefixing with `-` sorts by descending order. 
  'activeFrom': "activeFrom_example", // String | Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time. 
  'page': 56, // Number | Page number to get. Defaults to 1.
  'pageSize': 56 // Number | Number of images to get per page. Defaults to 10. Max of 100.
};
apiInstance.getNamespacesRepositoriesImages(namespace, repository, opts, (error, data, response) => {
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
 **namespace** | **String**| Namespace of the repository. | 
 **repository** | **String**| Name of the repository. | 
 **status** | **String**| Filters to only show images of this status. | [optional] 
 **currentlyTagged** | **Boolean**| Filters to only show images with: - &#x60;true&#x60;: at least 1 current tag. - &#x60;false&#x60;: no current tags.  | [optional] 
 **ordering** | **String**| Orders the results by this property.  Prefixing with &#x60;-&#x60; sorts by descending order.  | [optional] 
 **activeFrom** | **String**| Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time.  | [optional] 
 **page** | **Number**| Page number to get. Defaults to 1. | [optional] 
 **pageSize** | **Number**| Number of images to get per page. Defaults to 10. Max of 100. | [optional] 

### Return type

[**GetNamespaceRepositoryImagesResponse**](GetNamespaceRepositoryImagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNamespacesRepositoriesImagesSummary

> GetNamespaceRepositoryImagesSummaryResponse getNamespacesRepositoriesImagesSummary(namespace, repository, opts)

Get summary of repository&#39;s images

Gets the number of images in a repository and the number of images counted as active and inactive. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ImagesApi();
let namespace = "namespace_example"; // String | Namespace of the repository.
let repository = "repository_example"; // String | Name of the repository.
let opts = {
  'activeFrom': "activeFrom_example" // String | Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time. 
};
apiInstance.getNamespacesRepositoriesImagesSummary(namespace, repository, opts, (error, data, response) => {
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
 **namespace** | **String**| Namespace of the repository. | 
 **repository** | **String**| Name of the repository. | 
 **activeFrom** | **String**| Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time.  | [optional] 

### Return type

[**GetNamespaceRepositoryImagesSummaryResponse**](GetNamespaceRepositoryImagesSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNamespacesRepositoriesImagesTags

> GetNamespaceRepositoryImagesTagsResponse getNamespacesRepositoriesImagesTags(namespace, repository, digest, opts)

Get image&#39;s tags

Gets current and historical tags for an image.

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ImagesApi();
let namespace = "namespace_example"; // String | Namespace of the repository.
let repository = "repository_example"; // String | Name of the repository.
let digest = "digest_example"; // String | Digest of the image.
let opts = {
  'page': 56, // Number | Page number to get. Defaults to 1.
  'pageSize': 56 // Number | Number of images to get per page. Defaults to 10. Max of 100.
};
apiInstance.getNamespacesRepositoriesImagesTags(namespace, repository, digest, opts, (error, data, response) => {
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
 **namespace** | **String**| Namespace of the repository. | 
 **repository** | **String**| Name of the repository. | 
 **digest** | **String**| Digest of the image. | 
 **page** | **Number**| Page number to get. Defaults to 1. | [optional] 
 **pageSize** | **Number**| Number of images to get per page. Defaults to 10. Max of 100. | [optional] 

### Return type

[**GetNamespaceRepositoryImagesTagsResponse**](GetNamespaceRepositoryImagesTagsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postNamespacesDeleteImages

> PostNamespacesDeleteImagesResponseSuccess postNamespacesDeleteImages(namespace, postNamespacesDeleteImagesRequest)

Delete images

Deletes one or more images within a namespace. This is currently limited to a single  repository.  If you attempt to delete images that are marked as active or are currently tagged, the deletion does not happen and it displays the warnings. To continue with the deletion, you must ignore these warnings by putting them in the &#x60;ignore_warnings&#x60; property.  Deleting a currently tagged image deletes the tag from the repository.  You cannot ignore errors. It is not possible to directly delete children of multi-arch images. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ImagesApi();
let namespace = "namespace_example"; // String | Namespace of the repository.
let postNamespacesDeleteImagesRequest = new DockerHubApi.PostNamespacesDeleteImagesRequest(); // PostNamespacesDeleteImagesRequest | Delete request.
apiInstance.postNamespacesDeleteImages(namespace, postNamespacesDeleteImagesRequest, (error, data, response) => {
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
 **namespace** | **String**| Namespace of the repository. | 
 **postNamespacesDeleteImagesRequest** | [**PostNamespacesDeleteImagesRequest**](PostNamespacesDeleteImagesRequest.md)| Delete request. | 

### Return type

[**PostNamespacesDeleteImagesResponseSuccess**](PostNamespacesDeleteImagesResponseSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

