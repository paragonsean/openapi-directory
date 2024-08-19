# IbmContainersApi.ImagesApi

All URIs are relative to *https://containers-api.ng.bluemix.net/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buildPost**](ImagesApi.md#buildPost) | **POST** /build | Build a Docker image from a Dockerfile
[**imagesIdDelete**](ImagesApi.md#imagesIdDelete) | **DELETE** /images/{id} | Remove a Docker image.
[**imagesJsonGet**](ImagesApi.md#imagesJsonGet) | **GET** /images/json | List all Docker images that are available in your private Bluemix registry.
[**imagesNameOrIdJsonGet**](ImagesApi.md#imagesNameOrIdJsonGet) | **GET** /images/{name_or_id}/json | Inspect a Docker image in private Bluemix registry



## buildPost

> buildPost(xAuthToken, xAuthProjectId, t, body, opts)

Build a Docker image from a Dockerfile

This API builds a new container image from a Dockerfile that is stored on your local machine and pushes the image to the private Bluemix registry (corresponding IBM Containers command: &#x60;cf ic build&#x60;).   To push an image to your Bluemix registry, a namespace must be set for the organization. Run &#x60;cf ic namespace get&#x60; or call the &#x60;GET /registry/namespaces&#x60; API to check if a namespace is already set. If not, run &#x60;cf ic namespace set NAMESPACE&#x60; or call the &#x60;PUT /registry/namespaces/{namespace}&#x60; API to set a namespace for your organization.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.ImagesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let t = "t_example"; // String | Tag the image with the full path to your private Bluemix registry in the following format: `t=registry.ng.bluemix.net/<namespace>/<image_name>:<tag>`. This path is used to push the image to the private Bluemix registry after it is built.
let body = "/path/to/file"; // File | Must be the content of a tar archive compressed with gzip. The archive must include a file called 'Dockerfile' at its root. It may include any number of other files which will be accessible in the build context.
let opts = {
  'q': true, // Boolean | You can choose whether or not to show the verbose build output to review every step during the container image build. If you set the query parameter to `q=false`, `q=False`, or `q=0`, the verbose build output is suppressed. To show the verbose build output, enter `q=true`, `q=True`, or `q=1`.
  'nocache': true, // Boolean | If you set the query parameter to `nocache=true`, `nocache=True`, or `nocache=1`, the cache will not be used to build your image. To use the cache, enter `nocache=false`, `nocache=False`, or `nocache=0`.
  'pull': true // Boolean | If set to pull=true, pull=True, or pull=1, then a newer version of the image is always attempted to be pulled even though an older version of the image exists locally. If set to pull=false, pull=False, or pull=0, then the local image will be used if one exists.
};
apiInstance.buildPost(xAuthToken, xAuthProjectId, t, body, opts, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **t** | **String**| Tag the image with the full path to your private Bluemix registry in the following format: &#x60;t&#x3D;registry.ng.bluemix.net/&lt;namespace&gt;/&lt;image_name&gt;:&lt;tag&gt;&#x60;. This path is used to push the image to the private Bluemix registry after it is built. | 
 **body** | **File**| Must be the content of a tar archive compressed with gzip. The archive must include a file called &#39;Dockerfile&#39; at its root. It may include any number of other files which will be accessible in the build context. | 
 **q** | **Boolean**| You can choose whether or not to show the verbose build output to review every step during the container image build. If you set the query parameter to &#x60;q&#x3D;false&#x60;, &#x60;q&#x3D;False&#x60;, or &#x60;q&#x3D;0&#x60;, the verbose build output is suppressed. To show the verbose build output, enter &#x60;q&#x3D;true&#x60;, &#x60;q&#x3D;True&#x60;, or &#x60;q&#x3D;1&#x60;. | [optional] 
 **nocache** | **Boolean**| If you set the query parameter to &#x60;nocache&#x3D;true&#x60;, &#x60;nocache&#x3D;True&#x60;, or &#x60;nocache&#x3D;1&#x60;, the cache will not be used to build your image. To use the cache, enter &#x60;nocache&#x3D;false&#x60;, &#x60;nocache&#x3D;False&#x60;, or &#x60;nocache&#x3D;0&#x60;. | [optional] 
 **pull** | **Boolean**| If set to pull&#x3D;true, pull&#x3D;True, or pull&#x3D;1, then a newer version of the image is always attempted to be pulled even though an older version of the image exists locally. If set to pull&#x3D;false, pull&#x3D;False, or pull&#x3D;0, then the local image will be used if one exists. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/tar
- **Accept**: Not defined


## imagesIdDelete

> imagesIdDelete(xAuthToken, xAuthProjectId, id)

Remove a Docker image.

Remove a Docker image from the private Bluemix registry that is identified by the image ID (corresponding IBM Containers command: &#x60;cf ic rmi &lt;image&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.ImagesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let id = "id_example"; // String | The unique identifier representing a Docker image. Run `cf ic images`, or call the `GET /images/json` endpoint to review the Docker images that are available in your private Bluemix registry.
apiInstance.imagesIdDelete(xAuthToken, xAuthProjectId, id, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **id** | **String**| The unique identifier representing a Docker image. Run &#x60;cf ic images&#x60;, or call the &#x60;GET /images/json&#x60; endpoint to review the Docker images that are available in your private Bluemix registry. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## imagesJsonGet

> ImageInfo imagesJsonGet(xAuthToken, xAuthProjectId)

List all Docker images that are available in your private Bluemix registry.

This endpoint returns a list of all available Docker images in a private Bluemix registry (corresponding IBM Containers command: &#x60;cf ic images&#x60;.

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.ImagesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
apiInstance.imagesJsonGet(xAuthToken, xAuthProjectId, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 

### Return type

[**ImageInfo**](ImageInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## imagesNameOrIdJsonGet

> ImageDetail imagesNameOrIdJsonGet(xAuthToken, xAuthProjectId, nameOrId)

Inspect a Docker image in private Bluemix registry

This endpoint returns detailed information about a Docker image that is stored in the private Bluemix registry of an organization (corresponding IBM Containers command: &#x60;cf ic inspect &lt;image_name_or_id&gt;&#x60;).

### Example

```javascript
import IbmContainersApi from 'ibm_containers_api';

let apiInstance = new IbmContainersApi.ImagesApi();
let xAuthToken = "xAuthToken_example"; // String | The Bluemix JSON web token that you receive when logging into Bluemix. Run `cf oauth-token` to retrieve your access token.
let xAuthProjectId = "xAuthProjectId_example"; // String | The unique ID of your organization space where you want to create or work with your containers. Run `cf space <space_name> --guid`, where `<space_name>` is the name of your space, to retrieve your space ID.
let nameOrId = "nameOrId_example"; // String | The full private Bluemix registry path to your image or the unique ID of the image that you want to inspect. Run `cf ic images` or call the `GET /images/json` endpoint to review the images in your private Bluemix registry. 
apiInstance.imagesNameOrIdJsonGet(xAuthToken, xAuthProjectId, nameOrId, (error, data, response) => {
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
 **xAuthToken** | **String**| The Bluemix JSON web token that you receive when logging into Bluemix. Run &#x60;cf oauth-token&#x60; to retrieve your access token. | 
 **xAuthProjectId** | **String**| The unique ID of your organization space where you want to create or work with your containers. Run &#x60;cf space &lt;space_name&gt; --guid&#x60;, where &#x60;&lt;space_name&gt;&#x60; is the name of your space, to retrieve your space ID. | 
 **nameOrId** | **String**| The full private Bluemix registry path to your image or the unique ID of the image that you want to inspect. Run &#x60;cf ic images&#x60; or call the &#x60;GET /images/json&#x60; endpoint to review the images in your private Bluemix registry.  | 

### Return type

[**ImageDetail**](ImageDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

